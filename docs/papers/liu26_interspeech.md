# CoSTA: Cognitive-State-Conditioned TTS Data Augmentation Using ASR Transcripts for Alzheimer’s Disease Detection

- 论文编号：88
- 报告人：Yin-Long Liu
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/liu26_interspeech.pdf

## 问题
基于语音的阿尔茨海默病（AD）检测受病理语音稀缺制约；传统信号扰动难以引入新语义或 AD 特异不流畅，标准 TTS 又追求自然度会抹平病理声学线索。

## 方法
提出 CoSTA：分别适配 CosyVoice2（指令微调得 AD/HC 两变体）与 F5-TTS（认知标签嵌入+流匹配）做认知状态条件（CS-Cond）合成。构建含人工转写（MT）与 36 路 ASR（18 预训练+18 在 DementiaBank 子集微调）的转写池驱动 TTS。训练增强含自参考 2× 与类内交叉参考更高倍数；测试时用无认知条件的零样本 CosyVoice2 做 TTA 并概率平均。检测器用 WavLM 加权层融合 + 注意力池化 + MLP。

## 实验与结果
ADReSS（Cookie Theft）：基线准确率 81.67%。CS-Cond 相对预训练 TTS 更常超过基线（CosyVoice2 28/37 vs 7/37）。多数情况下 ASR 驱动增强优于 MT。增强倍数呈倒 U，约 2× 最优。摘要报告 CoSTA 相对基线提升 4.16%，测试集纯音频准确率 85.83%，优于既往方法。

## 结论
认知条件 TTS 可提升合成数据效用；ASR 转写的非随机错误可增加诊断相关多样性。过量合成易使检测器过拟合 TTS 伪迹。

## 点评
把「故意合成病理说话风格」与「用 ASR 错误当语义扰动」绑在一起，比纯声学扰动更贴近 AD 线索。依赖类标签条件合成，测试阶段只能退回零样本 TTA；增强倍数敏感也说明合成分布与真病理分布仍有隙。
