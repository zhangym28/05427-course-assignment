# 05427-course-assignment

# 轴承故障诊断的域泛化代码

<!-- ABOUT THE PROJECT -->
## 关于项目

采用深度学习的算法实现了对轴承域泛化的故障诊断。项目的代码在master分支里面，tif图片和excel文件展示了实验的具体结果。

## 代码的运行环境

- Python 3.9.19
-  Pytorch 2.3.0
-  Numpy 1.24.3
-  Pandas 2.2.1
-  ipykernel 6.28.0
-  scipy 1.10.1
-  tqdm 4.66.4

## 数据集来源  
本项目采用了以下两个公开轴承故障诊断数据集:
- **[CWRU](https://engineering.case.edu/bearingdatacenter)** - 凯斯西储大学轴承数据集
- **[MFPT](https://www.mfpt.org/fault-data-sets)** - 美国机械故障预防技术学会轴承数据集


### 领域泛化数据集的建立
- 建立一个根文件夹"datasets" 
- 将CWRU和MFTP数据集文件放在"datasets"文件夹中, 对数据集的处理步骤如下:

#### 跨工况故障诊断
按照设备不同工况进行数据集的处理:
1. 在对应的数据集中按照设备的不同工况分别建立 "condition_0", "condition_1","condition_2" 等文件夹。
2. 在每个工况的文件夹中分别建立不同轴承故障类型的子文件夹，将子文件夹命名为轴承的故障类型。


#### 跨设备故障诊断
按照不同设备对应的数据集进行处理:
1.在"datasets"文件夹中建立CWRU和MFTP两个子文件夹。
2.只选取两个轴承数据集中都存在的故障类型“inner”、“normal”、“outer”，分别建立相对应故障类型的子文件夹，将其他故障类型的数据舍弃。


#### （处理完后的数据集在master分支datasets文件夹中）


## 训练过程
### 跨工况故障诊断
选择一个工况数据为测试集，其他工况的数据集为训练集，但来自于同一数据集。

例如:选择CWRU数据集，采用ADACL算法，训练集为CWRU_0,CWRU_1,CWRU_2，测试集为CWRU_3对模型进行训练。（采用命令行在pycharm终端里运行）

python train.py --model_name ADACL --source CWRU_0,CWRU_1,CWRU_2  --target CWRU_3 --train_mode multi_source --cuda_device 0 


### 跨设备故障诊断
训练集和测试集来自于不同的数据集。

例如: 采用DANN算法，训练集为CWRU，测试集为MFPT对模型进行训练。（采用命令行在pycharm终端里运行）

python train.py --model_name DANN --source CWRU --target MFPT --train_mode single_source --cuda_device 0

（采用命令行在pycharm终端里进行跨设备模型训练之前，需将CWRU文件名修改成CWRU-within，CWRU-cross文件名修改成CWRU）  
## 参考代码  
https://github.com/CHAOZHAO-1/DG-PHM  

https://github.com/Feaxure-fresh/TL-Bearing-Fault-Diagnosis



