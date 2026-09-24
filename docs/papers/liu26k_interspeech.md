# HWB-plus: A Lightweight Speech Bandwidth Extension Method with Separate Modeling for Consonants and Vowels

- 论文编号：1498
- 报告人：Xueliang Zhang
- 程序：Wednesday 30 September 2026 / Dereverberation, Bandwidth Extension and Restoration
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liu26k_interspeech.pdf

## 问题
轻量 BWE（如 HWB-Net）参数少，但高频辅音重建弱：输入增强与辅音需求不匹配，单 WGMM 谱建模初始化不够感知化。

## 方法
HWB-plus：在 HWB-Net 上保持约 194K 参数、12.39M MACs/s；用 DualWGMM 分建模辅音/元音相关谱，配合带引导掩码与改进初始化。HR 采样率改为 22050 Hz 以覆盖辅音频段；VCTK 说话人无关划分，LR 由 2–3 kHz 低通产生。

## 实验与结果
相对 HWB：LSD 1.11→0.94，DNSMOS P.808 3.31→3.55，PESQ 3.35→3.83，VISQOL/NISQA 同步升。优于 BAE-Lite 等轻量对比，接近更大 BAE 的部分感知分而算力远低。

## 结论
分辅音/元音谱建模在不增复杂度下显著提升轻量 BWE，尤其听感与辅音相关质量。

## 点评
“同预算换结构”对照干净，适合端侧。DualWGMM 依赖辅音/元音路径分工正确；极端窄带或噪声 LR 未充分展开。指标全面（LSD+多听感）利于部署选型。
