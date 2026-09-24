# CoSTA: Cognitive-State-Conditioned TTS Data Augmentation Using ASR Transcripts for Alzheimer’s Disease Detection

- 论文编号：88
- 报告人：Yin-Long Liu
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/liu26_interspeech.pdf

## 问题
语音 AD 检测受病理数据稀缺制约；传统扰动难引入新语义或 AD 特异不流畅，而标准 TTS 常抹平病理韵律；用手工转写还是 ASR 转写驱动合成亦未系统比较。

## 方法
提出 CoSTA：用认知状态指令微调 CosyVoice2（AD/HC 两套）并在 F5-TTS 中加入 cognition embedding，使合成可控为 AD-like 或 HC-like。构建含 MT 与 36 路 ASR（18 预训练+18 微调，跨 Wav2Vec2/HuBERT/WavLM/Whisper）的转写池驱动合成；训练增强含自参考 2× 与类内交叉参考更高倍数；测试时用无指令零样本 CosyVoice2 做 TTA 概率平均。检测器为 WavLM 加权层融合+注意力池化+MLP。

## 实验与结果
ADReSS：基线准确率 81.67%。CS-Cond 相对预训练 TTS 更常超过基线（CosyVoice2 28/37 vs 7/37）。多数情况下 ASR 驱动优于 MT。增强倍数呈倒 U，约 2× 最优。摘要报告 CoSTA 相对基线提升 4.16%，测试集仅音频准确率 85.83%。CS-Cond 在 MCD/FAD 等客观指标上亦更接近真值。

## 结论
认知状态条件 TTS 提升合成样本对 AD 检测的效用；ASR 错误可增加诊断相关多样性；适度增强优于过度合成。

## 点评
把「病理说话风格」显式条件化，比无差别扰动更贴诊断目标；ASR 驱动有效说明识别错误可能编码病理声学线索。过度增强易过拟合 TTS 伪迹，部署需控制合成占比；TTA 在无类标时退回无条件合成，与训练时 CS-Cond 不完全对称。
