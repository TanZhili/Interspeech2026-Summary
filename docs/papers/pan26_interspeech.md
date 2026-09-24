# Supervised Post-training of Speech Foundation Models for Robust Adaptation in Speech Deepfake Detection

- 论文编号：908
- 报告人：Zihan Pan
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pan26_interspeech.pdf

## 问题
SSL 语音基础模型（如 WavLM）预训练目标偏音素/长程内容，对深度伪造中局部频谱–时间不连续不敏感；直接端到端微调在低资源与域外条件下易过拟合已知攻击。

## 方法
提出 Mix-Frames Post-Training（MFPT）三阶段：① 从相反类别抽取 injector，固定长度裁剪/填充后按比例 r_mix 做句内 cut-and-paste，并按帧中心是否落在注入段赋帧级标签；② 在混合波形上用线性帧分类头 + BCE 监督，经 LoRA（QKV+FFN）更新 SSL；③ 丢弃帧头，保留适配编码器，再用 Attentive Merging + 话语级分类头（LSTM / ECAPA-TDNN / Nes2Net）做 CE 微调。骨干为 WavLM Large，默认 r_mix 10–30%。

## 实验与结果
ASVspoof5 上无数据增强的单模型 EER 4.50%（ECAPA，QKV+FFN LoRA），优于文中所列多数单模型/部分融合系统。r_mix 过大（50–70%）恶化至 7.31%。低资源：在 ASV5 后训练后再用不同比例 ASV19LA 微调，相对无后训练在 ASV21DF 等域外增益明显（如 20% 数据时 DF EER 9.32%→4.34%）。ASVspoof2021 LA/DF：EER 3.88%/4.04%，绝对差距仅 0.16，最差情形与跨条件稳定性优于多篇对比系统。

## 结论
作者认为监督式后训练能把表示偏向局部伪造线索，再做话语级微调，可提升低资源与跨失真鲁棒性，并在 ASV5 取得无增强单模型 SOTA 级结果。

## 点评
核心是“先用伪造式局部拼接学帧级不一致，再做任务微调”，比直接微调更贴伪迹形态。强项是低资源与 LA–DF 平衡；弱项是混合比例与分类头需调，且 cut-and-paste 伪迹是否覆盖真实 VC/TTS 全谱仍依赖实验外推。
