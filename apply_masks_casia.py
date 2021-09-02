# This script applies masks over Casia-WebFace dataset. casia_folder, masks_folder, output folder should be set
# SecurifAI - 2021


import os
import glob
import cv2
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




# casia images main folder
casia_folder = 'CASIA-WebFace'

# masks main folder
masks_folder = 'CASIA-WebFace_masks'

# masks img list
mask_list = glob.glob(masks_folder + '/*/*.png')

# output folder
output_folder = 'masked_CASIA-WebFace'

if not os.path.isdir(output_folder):
    os.mkdir(output_folder)


for mask in tqdm(mask_list):    
    
    # get the basename of the mask to find original Casia image
    mask_basename = os.path.basename(mask)
    
    parent_folder = os.path.basename(os.path.dirname(mask))
    if not os.path.isdir(os.path.join(output_folder,parent_folder)):
        os.mkdir(os.path.join(output_folder,parent_folder))

    # create path for original mask
    img_path = os.path.join(casia_folder, parent_folder, mask_basename.replace('png','jpg')) 

    # check that original image exists, if it exists load it
    if os.path.isfile(img_path):
        casia_image = cv2.imread(img_path)
    else:
        continue
        
    # load the mask
    mask_image = cv2.imread(mask,cv2.IMREAD_UNCHANGED)
    
    # apply mask over image
    overlay_image_alpha(casia_image,
        mask_image[:, :, 0:3],
        (0, 0),
        mask_image[:, :, 3] / 255.0)

    # save new overlayed image
    cv2.imwrite(os.path.join(output_folder,parent_folder, mask_basename.replace('png','jpg')),casia_image)