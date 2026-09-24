# Through-Wall Radar Speech Acquisition via Cascaded Attention Fusion

- 论文编号：1034
- 报告人：Ruotong Ding
- 程序：Thursday 1 October 2026 / Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ding26c_interspeech.pdf

## 问题
穿墙 FMCW 雷达语音严重带限、杂波与高频衰减，常规卷积难抓长程依赖，标准 MHSA 在低 SNR 高频易碎片化、跨频交互不足。

## 方法
CAF-Former：从可靠低频（约前 50 bin）经 K=10 层渐进扩到全带。每层 Temporal Multi-Query Attention（共享 K/V、多独立 Q）再经 Frequency Attention Fusion 沿频轴融合；保留输入噪声相位、优化 log-spectral 幅度距离。5.31 GHz、15 cm 混凝土墙采集；仿真约 312 h 训练。

## 实验与结果
相对 RANet、Wave-Voice、TF-Locoformer、EBENet：仿真/实录上 STOI、DNSMOS、CS-MFCC 最优（如实录 STOI 0.617、DNSMOS 2.423），PESQ 略低于个别强基线但更均衡。消融显示 TMQA+FAF 优于 MHSA、仅 LP 融合或单 query。

## 结论
级联时频注意力与渐进扩带利于穿障雷达语音的高频谐波恢复；未来将评真人发声场景。

## 点评
针对雷达“低频可靠、高频噪声主导”的传感退化设计渐进与共享 KV 多 query，问题匹配度高。PESQ 非全面第一但可懂度/感知更稳；仍用激励器隔墙而非真人，迁移需再验。
