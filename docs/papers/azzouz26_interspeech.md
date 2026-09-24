# Acoustic-to-Articulatory Inversion of Clean Speech Using an MRI-Trained Model

- 论文编号：734
- 报告人：Sofiane Azzouz
- 程序：Thursday 1 October 2026 / Speech Production and Perception 2
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/azzouz26_interspeech.pdf

## 问题
rt-MRI 可同时获得声学与完整声道形状，但机内录音噪声大，即使去噪也与安静环境语音差异明显；实际应用需要能对干净语音做 acoustic-to-articulatory inversion，而不能假定始终有 MRI 噪声条件下的音频。

## 方法
同一法语女说话人分别采集约 2.5 小时 rt-MRI（136×136，20 fps）去噪语音与对应干净录音；用专家校正的音素切分做层级对齐（句→词→音素内时间归一化）。输入用 HuBERT-Base 嵌入，经两层全连接 + 两层 Bi-LSTM 回归 8 个调音器轮廓（各 50 点，MSE）。对比三设定：M2M（去噪训测）、M2C（去噪训/干净测）、C2C（干净训测）；并与 DTW 对齐对照。

## 实验与结果
平均 RMSE：M2M 1.51 mm、C2C 1.56 mm、M2C 1.64 mm；C2C 接近 M2M，明显优于跨域 M2C。音素对齐优于 DTW（M2C-DTW 1.71 mm、C2C-DTW 1.68 mm）。舌等调音器误差相对较大，咽壁等较小。

## 结论
在 MRI 轮廓监督下，用干净语音训练/测试可将平均误差做到约 1.56 mm（接近像素尺度 1.62 mm），说明声学–调音反演可用于真实安静场景，而不仅限于机内去噪语音。

## 点评
核心贡献是把“MRI 监督–干净声学输入”的域落差用音素级对齐桥起来，而不是只做更强去噪。C2C 接近 M2M、又显著好于 M2C，说明训练域匹配比硬跨域推理更关键。未建模 Lombard/仰卧姿势效应、且为单说话人，是走向多说话人实用系统时的主要边界。
