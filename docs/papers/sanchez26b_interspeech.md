# From Lab to Laptop: Validating 3D Speech Kinematics with MediaPipe Face Mesh

- 论文编号：3022
- 报告人：Victoria Sanchez
- 程序：Tuesday 29 September 2026 / Multimodal and Non-Speech Healthcare Applications
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sanchez26b_interspeech.pdf

## 问题
发音运动测量依赖 EMA/光学动作捕捉，成本高难临床扩展；已有摄像头方法常缺毫米级、深度可解释的完整轨迹验证。

## 方法
单路笔记本 RGB + MediaPipe Face Mesh；以外眦距做被试校准到毫米，稳定面标做头动刚体校正；与同步 Cortex 光学捕捉对比。任务：DDK、句子重复、最大幅度运动（4 成人，116 段）。评 30/15 fps（匹配滤波带宽）下 3D uRMSE、相对 ROM 的位移误差、速度保真与互相关。

## 实验与结果
3D 位置 uRMSE 均值 2.03±0.59 mm（30 fps），15 fps 相当；归一化位移误差 6.63±1.28%；深度轴可恢复；15 fps 在语音相关频带无明显效用损失。误差沿各标记主运动轴最大。

## 结论
单相机 MediaPipe 流程可达毫米级、深度可解释的发音轨迹，15 fps 仍可用，利于规模化与远程采集。

## 点评
把“是否够临床用”落到轨迹级、毫米单位的金标准对比，比只比摘要特征更硬。样本量小且健康受试者；真实疾病与光照/摄像头变异仍需外推验证。
