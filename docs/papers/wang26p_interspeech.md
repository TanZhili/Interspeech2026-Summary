# SAGE: Switch-Aware EEG-Guided Soft Gating for Target Speaker Extraction with In-Trial Switching

- 论文编号：864
- 报告人：Xuefei Wang
- 程序：Monday 28 September 2026 / Brain Studies and Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26p_interspeech.pdf

## 问题
EEG 引导目标说话人提取多假设注意在试次内固定；自发切换时 EEG 噪声与神经延迟会造成硬切换断续与错误说话人泄漏。

## 方法
SAGE：Conv-TasNet 式前端分离出两路候选；EEG 模块预测注意偏置 α(t) 与切换概率 p_sw(t)，温度 τ(t)=τ0+λ p_sw 软门控并局部平滑得 g(t)，输出 g·s1+(1−g)·s2。可微分局部时移补偿延迟；dropout 方差估计不确定性并加权平滑正则。损失 −SI-SDR + 切换感知 TV + 不确定性平滑；三阶段训分离器再联合微调。

## 实验与结果
自建 18 人普通话自发注意切换数据（64 导 EEG，±90° 男女混合）。SAGE：SI-SDR 8.67 dB、STOI 88.24%、平均切换延迟 2.04 s，优于 BASEN/NeuroHeed/NeuroSpex+/M3ANet。消融去掉软门控、延迟对齐或不确定性策略均降 SI-SDR/STOI/ACC；去掉对齐延迟升至约 2.58 s。

## 结论
把试次内切换当作动态软选择，并显式处理延迟与不可靠 EEG，可同时提升提取质量与切换时延。未来关注跨被试与更复杂声学。

## 点评
相对“先 AAD 再硬选音轨”，SAGE 在波形融合层做切换感知平滑，对准听感断续这一痛点。自建数据与按钮标注延迟、双说话人设定，跨被试泛化与多说话人仍待验证。
