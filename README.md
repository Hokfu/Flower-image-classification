## Table of Contents
1. [Introduction](#flower-image-classification)
2. [Dataset](#dataset)
3. [Problem Description](#problem-description)
4. [Model Training](#model-training)
5. [Dependency and Environment Management](#dependency-and-environment-management)
6. [Containerization](#containerization)
7. [Usage](#usage)

# Flower-image-classification
Classification model for the flowers 'daisy' and 'dandelion'. This dataset is from Kaggle. <br><br>
https://www.kaggle.com/datasets/alsaniipe/flowers-dataset
<br><br>
The notebook was run in Kaggle. You can install the necessary libraries from requirements.txt, or you can run it in Kaggle.
<br><br>
This is my first project on image classification. 
<br><br>
The trained model is converted to Tensorflow lite for light usages.
# Dataset
Train dataset has 529 daisy images and 1275 dandelion images.<br>
Validation dataset has 1620 daisy images and 1821 dandelion images.<br>
Test dataset has 1352 daisy images and 1457 dandelion images.<br><br>
# Problem Description
This model intends to identify and differentiate between daisy and dandelion.
<br><br>
Example use cases: image detection IoT devices, gardening, environmental monitoring, mobile app for nature enthusiasts
<br><br>
# Model Training
Model is trained with sequential model with CNN, and pre-trained models- 'VGG16' and 'Xception'.
<br><br>
VGG16 model is used as the final model.
<br><br>
# Dependency and Environment Management
Dependencies are in 'pipfile'. To install dependencies, you need to create pipenv virtual environment.
<br><br>
```$pip install pipenv```

```$pipenv --python 3.9```

```$pipenv install```
<br><br>
# Containerization
<br><br>
Docker file is provided to 
```$Docker build -t 'container_name' .```
<br><br>
After containerization, the model can be used to deploy in cloud services like AWS. 
<br><br>
# Usage
<br><br>
Clone the model in your device and can be used. If your device is not compatible with Tensorflow lite, you can run the repository in cloud services like saturncloud.

