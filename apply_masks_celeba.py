# This script applies the celeba_masks over the celeba_images. celeba_folder, output_folder must be set.
# SecurifAI - 2021

import glob
import cv2
import os
from tqdm import tqdm

def overlay_image_alpha(img, img_overlay, pos, alpha_mask):
    x, y = pos

    y1, y2 = max(0, y), min(img.shape[0], y + img_overlay.shape[0])
    x1, x2 = max(0, x), min(img.shape[1], x + img_overlay.shape[1])

    y1o, y2o = max(0, -y), min(img_overlay.shape[0], img.shape[0] - y)
    x1o, x2o = max(0, -x), min(img_overlay.shape[1], img.shape[1] - x)

    if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
        return

    channels = img.shape[2]

    alpha = alpha_mask[y1o:y2o, x1o:x2o]
    alpha_inv = 1.0 - alpha

    for c in range(channels):
        img[y1:y2, x1:x2, c] = (alpha * img_overlay[y1o:y2o, x1o:x2o, c] +
                                alpha_inv * img[y1:y2, x1:x2, c])


# folder where celeba images are stored
celeba_folder = 'img_celeba'
img_list = glob.glob(celeba_folder + '/*.png')

# folder where the masks are stored
mask_folder = 'celeba_masks'
mask_list = glob.glob(mask_folder + '/*.png')

# output folder
output_folder = 'masked_celeba'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    

for mask in tqdm(mask_list):
    # get basename and remove '_mask' string, change png to jpg
    mask_basename = os.path.basename(mask).replace('_mask','').replace('png','jpg')
    
    # get celeba path from mask path
    img_path = celeba_folder + '/' + mask_basename
    
    # check if we have an image for mask
    if os.path.exists(img_path):
        generated_mask = cv2.imread(mask,cv2.IMREAD_UNCHANGED)
        celeba_img = cv2.imread(img_path)
        
        # apply mask over celeba_image
        overlay_image_alpha(celeba_img,
                    generated_mask[:, :, 0:3],
                    (0, 0),
                    generated_mask[:, :, 3] / 255.0)
                    
        # write new image in output_folder
        cv2.imwrite(output_folder + '/' + mask_basename, celeba_img)
        