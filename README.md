# CelebA+masks and CASIA-WebFace+masks data sets from "A realistic approach to generate masked faces applied on two novel masked face recognition data sets" (NeurIPS 2021) - Official Repository

## 1. License Agreement

**Copyright (C) 2021 - SecurifAI**

This package contains free data and software: you can use, redistribute and/or modify it under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license.

This data set and software is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

The complete license agreement can be consulted at:
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).


## 2. Citation

Please cite the corresponding work (see citation.bib file to obtain the citation in BibTex format) if you use this data set and software (or a modified version of it) in any scientific work:

**[1] Tudor Mare, Georgian Duță, Mariana-Iuliana Georgescu, Adrian Șandru, Bogdan Alexe, Marius Popescu, Radu Tudor Ionescu. A realistic approach to generate masked faces applied on two novel masked face recognition data sets. In Proceedings of NeurIPS, 2021 [(link to ArXiv version)](http://arxiv.org/abs/2109.01745).**

## 3. Description

The COVID-19 pandemic raises the problem of adapting face recognition systems to the new reality, where people may wear surgical masks to cover their noses and mouths. Traditional data sets (e.g., CelebA, CASIA-WebFace) used for training these systems were released before the pandemic, so they now seem unsuited due to the lack of examples of people wearing masks. We propose a method for enhancing data sets containing faces without masks by creating synthetic masks and overlaying them on faces in the original images. Our method relies on Spark AR Studio, a developer program made by Facebook that is used to create Instagram face filters. In our approach, we use 9 masks of different colors, shapes and fabrics. We employ our method to generate a number of 445,446 (90%) samples of masks for the CASIA-WebFace data set and 196,254 (96.8%) masks for the CelebA data set. 

Our repository contains:
  - Images of masks with transparent background.
  - Code to overlay the masks on the corresponding CelebA and CASIA-WebFace images.

#### Important note: This repo does not include the original CelebA or CAISA-WebFace images. The original images should be downloaded from the original repositories.

## 4. Data Sets

The masks for the CelebA data set are available for download at:

# [CelebA+masks](https://fmiunibuc-my.sharepoint.com/:u:/g/personal/radu_ionescu_fmi_unibuc_ro/EQdIsLQB9jdOkaOHV0T_wMQBSz8qQkxRm7w8Nuo_qZOoFA?e=1eekcq)

The masks for the CASIA-WebFace data set are available for download at:

# [CASIA-WebFace+masks](https://fmiunibuc-my.sharepoint.com/:u:/g/personal/radu_ionescu_fmi_unibuc_ro/ETWFdcY8sAhCpbxrSiytXzUBK3PHaAxMbARlarBY-tNK3g?e=31YZOw)

## 5. Software Usage

For convenience, we provide Python scripts to apply the masks on the original CelebA and CASIA-WebFace images.

To run the script on the CelebA / CASIA-WebFace data set, extract the respective archive in the same folder as the CelebA / CASIA-WebFace main data set folder. Inside each script there is a celeba_folder / casia_folder parameter and a masks_folder parameter which have to be set accordingly. The output of the script will be located in the masked_celeba or masked_casia folder, respectively.

Make sure to install the packages listed in requirements.txt before running the scripts.

#### For CelebA

Make sure you have the following folder structure on your machine:
```
main directory
│   apply_masks_celeba.py
└───celeba_masks - masks folder (from this repo)
│   │   ...
└───celeba - data set folder (original images)
│   │   ...
└───masked_celeba - output folder (images with overlaid masks)
    │   ...    
```

Then use the following command:
```
>> python apply_masks_celeba.py
```

#### For CASIA-WebFace

Make sure you have the following folder structure on your machine:
```
main directory
│   apply_masks_casia.py
└───casia_masks - masks folder (from this repo)
│   │   ...
└───casia - data set folder (original images)
│   │   ...
└───masked_casia - output folder (images with overlaid masks)
    │   ...    
```

Then use the following command:
```
>> python apply_masks_casia.py
```

## 6. Feedback

We are happy to hear your feedback and suggestions at: tudor[dot]mare{at}securif(dot)ai
