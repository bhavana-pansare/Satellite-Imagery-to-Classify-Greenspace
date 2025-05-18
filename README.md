# Greenspace Classification in Belfast

## Overview

This repository addresses the Deloitte Analytathon 2 Challenge, aimed at classifying greenspaces within the Belfast area using high-resolution satellite imagery from Sentinel-2 L2A. The primary goal was to accurately label green vegetation areas (parks, forests, street trees) using advanced machine learning and deep learning techniques.

## Project Objectives

* Classify greenspaces using Sentinel-2 satellite images.
* Develop machine learning models for precise image segmentation.
* Evaluate and compare various model architectures.

## Data Exploration and Preprocessing

* Analysed satellite images (True Colour, False Colour, and Scene Mask images).
* Preprocessed data by applying scene masking to filter out non-relevant features (clouds, water, snow).
* Image splitting into manageable segments for efficient processing.

## Dataset Generation and Augmentation

* Removed images with cloud coverage exceeding 75%.
* Resized images to 256x256 pixels to streamline computational processes.
* Performed data augmentation techniques including rotations and mirroring, generating six variations per image.
* Implemented Normalized Difference Vegetation Index (NDVI) calculations for enhanced vegetation analysis.
* Split data into training (70%), testing (25%), and validation (5%) datasets.

## Models Used

* **Bhavana\_DeepLabV3**: Utilized ResNet50 backbone and Atrous Spatial Pyramid Pooling (ASPP) for enhanced segmentation accuracy.
* **Maria\_ResNet34**: Adapted pre-trained ResNet34 for precise pixel-wise predictions.
* **U-Net**: Leveraged downsampling and upsampling operations for detailed segmentation.
* **U-Net+ (Recommended)**: Enhanced U-Net with additional layers for improved feature extraction and segmentation accuracy.

## Model Evaluation

* Conducted comparative analysis among different models.
* U-Net+ achieved the highest accuracy (99.82%) and the best overall performance.
* Performance evaluated using precision (99.8%), recall (99.5%), ROC Curve, AUC (100%), and confusion matrix (99.54% accuracy).

## Results

* Achieved superior results with U-Net+, demonstrating clear identification and delineation of greenspaces in Belfast.
* Produced detailed visualizations combining True Colour, False Colour, and NDVI images, displaying model accuracy against ground truth.

## Recommendations for Future Work

* Expand dataset with more diverse images from various seasons and conditions.
* Automate data processing and model training pipelines.
* Consider multi-class segmentation for detailed vegetation and urban classification.

## Technologies and Tools

* Python
* PyTorch
* Adam Optimizer
* Deep Learning Models (DeepLabV3, ResNet34, U-Net, U-Net+)
* NDVI Analysis

## References

* Ismayilova & Timpf (2022). *AGILE: GIScience Series*.
* Ludwig et al. (2021). *ISPRS International Journal of Geo-Information*.
* Schetke et al. (2016). *Urban Forestry & Urban Greening*.
* Zeiler & Fergus (2013). Visualizing Convolutional Networks, arXiv.

---

Detailed implementation steps and model training processes are available in the associated notebooks and scripts within this repository.
