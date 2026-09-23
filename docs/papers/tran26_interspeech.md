# Deepfake Word Detection by Next-token Prediction using Fine-tuned Whisper

- 论文编号：628
- 报告人：Xin Wang
- 程序：Monday 28 September 2026 / Speech Deepfake Detection: Robustness, Generalization, Attribution
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/tran26_interspeech.pdf

## 问题
部分篡改（用合成词替换真实词）需定位哪一段是假的；专用序列检测器开发与部署成本高。能否只微调预训练 Whisper，在转写同时标记假词？

## 方法
在训练转写中于假词两侧插入复用词表已有标记（如 `!!!!!!` / `~~~~` 作 TOF/EOF），仍用标准 next-token 训练，推理时夹在标记间的 token 判为合成。数据可用声码器对 1–5 个词做 copy-synthesis（Ft.Voc）或真实 TTS 部分伪造（Ft.TTS / 混合），降低造数成本。

## 实验与结果
域内 E.Voc/E.TTS：微调 Whisper 检测 FAR/FRR 与专用 ResNet 接近（如 E.Voc FAR 7.22%、FRR 0.52%），且转写 WER 相对预训练显著下降。域外 AV-Deepfake1M、PartialEdit（如 VoiceCraft）上检测与转写均程度不一地退化，与 ResNet 相当量级但整体需更好泛化。

## 结论
最小改动即可把 Whisper 变成“转写+假词定位”一体模型；声码器模拟可降低训练成本，但跨生成器泛化仍是瓶颈。

## 点评
工程价值高：不改结构、不加重头，就把反欺骗嵌进 ASR 流水线。标记复用词表 token 可能与真实文本冲突；域外退化说明 vocoder 伪迹与现代 LLM 编辑伪迹仍有鸿沟。
