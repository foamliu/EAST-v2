# EAST: An Efficient and Accurate Scene Text Detector

## Introduction

This is a PyTorch re-implementation of EAST: An Efficient and Accurate Scene Text Detector ([paper](https://arxiv.org/abs/1704.03155)). 

The features are summarized blow:
- Only RBOX part is implemented.
- A fast Locality-Aware NMS in C++ provided by the paper's author.
- The pre-trained model provided achieves 80.83 F1-score on ICDAR 2015 Incidental Scene Text Detection Challenge using only training images from ICDAR 2015 and 2013. see here for the detailed results.
- Differences from original paper
    - Use ResNet-50 rather than PVANET
    - Use dice loss (optimize IoU of segmentation) rather than balanced cross entropy
    - Use linear learning rate decay rather than staged learning rate decay

## Performance

### ICDAR 2015 

|Model|Recall|Precision|Hmean|Download|
|---|---|---|---|---|
|PyTorch re-implementation of EAST|74.48%|90.26%|81.61%|[Link](https://github.com/foamliu/EAST/releases/download/v1.0/BEST_checkpoint.tar)

![image](https://github.com/foamliu/EAST/raw/master/images/Results_IoU.png)

[Link](https://rrc.cvc.uab.es/?ch=4&com=evaluation&view=method_info&task=1&m=61493)

### Offline evaluation

```bash
$ python eval.py
$ ./eval.sh

```

## Credit
Most codes are ported from [argman/EAST](https://github.com/argman/EAST) (the Tensorflow re-implementation).

## DataSet

Model is trained on COCO-Text & tested on ICDAR 2015. 

### COCO-Text
63,686 images, 145,859 text instances (training: 43,686/118,309 training, validation: 10,000/27,550 validation, test: 10,000/no public annotations)

Go to [COCO-Text](https://vision.cornell.edu/se3/coco-text-2/) to download:
- [COCO-Text annotations 2017 v1.4](https://vision.cornell.edu/se3/wp-content/uploads/2019/05/COCO_Text.zip)

Go to [MSCOCO](http://cocodataset.org/#download) to download:
- [2014 Train images](http://images.cocodataset.org/zips/train2014.zip)

### ICDAR 2015
Go to [ICDAR 2015](http://rrc.cvc.uab.es/?ch=4&com=downloads) to download:
- ch4_test_images.zip
- Challenge4_Test_Task1_GT.zip


## Dependency

- PyTorch 1.1.0

## Usage
### Data Pre-processing
Extract training & test images:
```bash
$ python extract.py
```

### Train
```bash
$ python train.py
```

If you want to visualize during training, run in your terminal:
```bash
$ tensorboard --logdir runs
```

### Demo
Pick 10 random test examples from ICDAR-2015:
```bash
$ python demo.py
```

Examples|
|----|
|![image](https://github.com/foamliu/EAST/raw/master/images/out_0.jpg)
|![image](https://github.com/foamliu/EAST/raw/master/images/out_1.jpg)
|![image](https://github.com/foamliu/EAST/raw/master/images/out_2.jpg)
|![image](https://github.com/foamliu/EAST/raw/master/images/out_3.jpg)
|![image](https://github.com/foamliu/EAST/raw/master/images/out_4.jpg)
|![image](https://github.com/foamliu/EAST/raw/master/images/out_5.jpg)
|![image](https://github.com/foamliu/EAST/raw/master/images/out_6.jpg)
|![image](https://github.com/foamliu/EAST/raw/master/images/out_7.jpg)
|![image](https://github.com/foamliu/EAST/raw/master/images/out_8.jpg)
|![image](https://github.com/foamliu/EAST/raw/master/images/out_9.jpg)
