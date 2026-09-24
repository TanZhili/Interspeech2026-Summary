# TAP-ETS: Time Aligned Phoneme Guiding for EMG-to-Speech Synthesis

- 论文编号：3485
- 报告人：Dongyub Han
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/han26f_interspeech.pdf

## 问题
EMG 到语音（ETS）常把音素分类仅作辅助损失，语言信息未显式条件化生成，外部文本/音素纠错也难回注到帧级声学合成。

## 方法
TAP-ETS：训练时以帧级音素嵌入经交叉注意力注入 mel 解码器（EMG 特征为 Q，音素为 K/V），并保留辅助音素分类。推理时用 TAP 精炼：把合并音素/文本纠错（如 MONA-LISA+GPT）经 Levenshtein 时长重分配与掩码 Transformer 再对齐到 EMG 帧，无需改合成骨干。在 Gaddy silent EMG 基准评测。

## 实验与结果
相对 Gaddy/Scheck，Acc 73.03%、PER 15.59%、CER 11.15%、WER 19.77%（基线 WER 约 25–26%），达文中所称 SOTA。消融：Lev 与掩码精炼互补；帧级音素条件优于文本或合并序列条件。

## 结论
帧对齐音素条件 + 可插拔精炼管线可显著提升静默 EMG 可懂度，并使任意音素/文本纠错模块无缝接入。

## 点评
把“音素从监督变成可控条件”是对 ETS 控制力的关键升级。精炼依赖外部强纠错（识别 WER 12.70%）与 DTW/MFA 对齐质量；测试集仅 98 句静默样本，规模有限。
