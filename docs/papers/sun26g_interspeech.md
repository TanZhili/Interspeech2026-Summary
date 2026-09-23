# ADD-DINO: A Two-Stage Self-Distillation Framework for Audio Deepfake Detection

- 论文编号：1847
- 报告人：Zhaorui Sun
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sun26g_interspeech.pdf

## 问题
SSL+后端的 ADD 依赖大量标注，且易过拟合特定伪造类型，跨域与未见合成器时稳健性差。掩码式 SSL 侧重局部预测，未必最适合捕获真伪一致性线索。

## 方法
ADD-DINO 两阶段：Stage1 在约 100 万无标注音频上做非对比 teacher–student 自蒸馏——teacher 吃全局长段、student 吃噪声增强的局部短段，对齐预测分布，teacher 用 EMA 更新；骨干为 XLS-R/WavLM 等 + AASIST 图模块。Stage2 给预训练 teacher 换新分类头，在少量有标数据上微调。评测 ASVspoof 2019/2021、In-the-Wild、DFADD 等，以及 CosyVoice、F5-TTS 等未见合成器。

## 实验与结果
少标微调时，如 XLS-R 骨干 20% 标签：19LA EER 0.55（全监督基线同比例 1.19），接近更高标注比例表现。跨域与未见合成器上相对基线：摘要称 EER 相对降 19.99%、准确率升 22.7%。多骨干对比表显示低标注比例下 ADD-DINO 普遍优于同骨干全监督微调。

## 结论
作者认为全局–局部一致性自蒸馏可在标签稀缺下逼近全监督，并提升跨域与未见伪造的泛化。

## 点评
把 DINO 式非对比蒸馏接到 ADD，用“长全局 vs 短局部”对齐伪造痕迹，比单纯掩码重建更贴检测目标。未见合成器测试用 ACC（全假样本）与标准 EER 混用，跨表比较时需注意协议差异。
