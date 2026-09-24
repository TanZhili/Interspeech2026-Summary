# FoleyImmersive: Decoupling What and Where for Video-to-First-Order Ambisonics

- 论文编号：531
- 报告人：Liming Liang
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liang26b_interspeech.pdf

## 问题
从静音 FoV 视频生成 FOA 时，公开视频–FOA 语料语义稀疏，端到端模型易纠缠“内容”与“几何”，两阶段管线又常在语义保真与空间一致性间折损。

## 方法
FoleyImmersive 解耦 what/where：在 YT-Ambigen 上用 Qwen2.5-VL-7B 增补结构化描述得到 YT-AmbiSem。Stage 1 以语义优先扩散生成单声道 W（MR-CFA 融合 4 fps/1 fps CLIP，并行文本交叉注意力，PTM 用时间检测概率门控残差）。Stage 2 用 complex-STFT U-Net 从 W 预测 XYZ，瓶颈处 Directional Residual Mixer 按视觉与相机方向做通道门控残差，并加能量预算正则；推理时不改动 W。

## 实验与结果
相对 ViSAGe 等：KLDdec 1.532、FADdec 4.253、FADavg 4.126；空间 CC(all)=0.741、AUC(all)=0.851。去 MR-CFA / 去 DRM 均明显掉点。主观 MOS（30 人、50 条）Semantics/Spatiality/Overall 为 4.01/4.16/4.08，优于 ViSAGe。

## 结论
语义增强数据 + 两阶段解耦与轻量方向残差可同时提升视频到 FOA 的语义与空间指标；未来需加强未见复杂场景泛化。

## 点评
把 W 钉死、只在 XYZ 做残差空间化，直接针对“空间化改写内容”的常见病。指标与消融一致支持设计；依赖 VL 自动标注与 FoV→FOA 设定，跨域与全景输入仍需另验证。
