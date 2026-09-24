# Audio-visual Contrastive Alignment for Diffusion-based Visual-conditioned Speech Enhancement

- 论文编号：766
- 报告人：Colombe Mboungou
- 程序：Wednesday 30 September 2026 / Audio-Visual and Generative Target Speaker Extraction
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mboungou26_interspeech.pdf

## 问题
无监督扩散 AVSE（如 AV-UDiffSE+）靠交叉注意力视觉条件，但未显式对齐音视频表征，视觉利用可能不足，低 SNR 与跨域时尤甚。

## 方法
在条件扩散分数模型训练中加入对比音视频损失，强化跨模态对齐；推理仍用原后验采样（NMF 观测模型）不变。在匹配（TCD+DEMAND）与失配（LRS3+NTCD）及多 SNR 上对比 AO/AV DiffUSEEN 与监督 FlowAVSE。

## 实验与结果
匹配集相对 AV-DiffUSEEN：SI-SDR 13.6→16.0、SI-SIR 24.3→29.5；−5 dB 时增益更明显（SI-SDR +3.2、SI-SIR +6.6）。失配集仍有 SI-SIR/SI-SDR 提升。线性投影消融显示对齐头有贡献。监督 FlowAVSE 匹配更强但跨域崩塌。

## 结论
训练期对比对齐可加强视觉条件、改善干扰抑制与低 SNR 稳健性，且不改推理流程。

## 点评
改动集中在先验训练目标，部署友好。增益以干扰抑制为主；极干净高 SNR 时感知收益有限，符合“声学已够好时视觉边际变小”。
