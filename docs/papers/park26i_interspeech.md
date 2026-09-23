# Word-level Emotional Intensity Control in TTS via Emotion Residual Vectors

- 论文编号：3079
- 报告人：Ji-Hyun Park
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/park26i_interspeech.pdf

## 问题
情感 TTS 多采用句级情绪条件，难以在词级分配韵律突显，易把强度加错词。已有词级强度控制（EmoQ-TTS、HED-TTS、EME-TTS 等）虽可控，却常带来突变基频、不自然时长或过突显目标词，自然度下降。

## 方法
提出 **情绪残差向量（ERV）** 作为无标注的词级控制信号：
1. 在 ESD 平行中性–情绪同文对上，用 MFA 对齐 + WavLM-Base（层 7–12 聚合）得到词级嵌入，定义 \(r_w=u_w^{\mathrm{emo}}-u_w^{\mathrm{neu}}\)。
2. 三阶段训练：先训带说话人/句级情绪的 FastSpeech2；冻结骨干、全局情绪固定为中性，只训残差注入模块（RIM）：瓶颈投影 \(B\in\mathbb{R}^{a\times D}\)（默认 \(a=32\)）再映射到编码器隐空间，加 LayerNorm，按词级权重 \(\alpha\) 注入；再用学到的 \(B\) 生成投影目标，微调 RoBERTa 预测器从文本+情绪提示预测投影 ERV。
3. 推理：预测器输出 \(\hat z_w\)，经冻结 RIM 注入中性条件骨干，用 \(\alpha\) 连续调节词级强度。

## 实验与结果
ESD 英语子集（10 说话人，五情绪；14,900/950/1,550）；抽取约 88,400 词级 ERV。主观 NMOS/EMOS 与客观 UTMOS、Emotion2vec 情绪准确率：Proposed（\(\alpha_w=1\)）与 FS2+emo 接近（NMOS 3.83、Emo.Acc. 0.71），明显优于 HED-TTS。词级 A/B：相对 EME-TTS 赢 55.3%，相对 HED-TTS 赢 87.1%。增大 \(\alpha\) 时平均音高按情绪方向变化。消融：无瓶颈时 Emo.Acc. 偏低；\(a=32\) 附近情绪准确较好；带预测器后 Emo.Acc. 达 0.71。

## 结论
作者认为 ERV + 瓶颈注入可实现词级情绪强度控制并更好保持自然度；瓶颈使高维 S3L 残差变得可预测、可缩放。局限：依赖平行、词对齐的中性–情绪对，扩展到非约束数据仍是开放问题。

## 点评
关键洞察是「控制信号应是中性→情绪的局部残差，而不是另造一套强度标签」。把残差压进低维瓶颈再让 RoBERTa 预测，既稳定了 \(\alpha\) 缩放，又把监督从声学残差转到文本条件——这是相对直接注入高维 ERV 更工程化的一步。相对 HED/EME 类显式强度/分布控制，主观词级自然度优势明显。脆弱点紧扣作者自己指出的平行对齐依赖；且全局情绪固定为中性、情绪主要靠残差表达，对「非平行」或跨语料泛化可能变脆。
