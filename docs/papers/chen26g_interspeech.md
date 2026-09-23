# Using Phonological-Level Wav2Vec2 for Mandarin Automatic Mispronunciation Detection and Diagnosis

- 论文编号：869
- 报告人：Jinghao Chen
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26g_interspeech.pdf

## 问题
普通话 MDD 中，端到端音素检测准确率提升后，诊断反馈仍常停在音素对错，未显式拆分音段与声调属性，难解释错误如何产生。

## 方法
用 Dragonmapper 等将转写转为 IPA（Pinyin 仅作中间层）；把每个音素映射为发音方式/部位、元音高度/前后/圆唇、双元音、声调等二值属性。在 Wav2Vec2-XLSR-53-CTC 上做多标签属性序列预测。对比 IPA-S/IPA-D（双元音是否拆分）与 Tone-Cat/Tone-PT（类别声调 vs 音高目标描述）。推理时属性比对得属性级反馈，再经 attributes-to-phoneme 转写得音素级诊断。母语 CV13-CN 训练，AISHELL-1 做跨库识别，LATIC L2 做 MDD。

## 实验与结果
AISHELL-1 上 IPA-D 显著降 AER（如 IPA-D×Tone-CAT 平均 AER 0.0183 vs IPA-S 约 0.033）。LATIC 音素 MDD：相对 Wav2Vec2 音素基线，IPA-D×Tone-CAT 的 FAR 9.97%→8.15%、DER 34.03%→27.86%；IPA-D×Tone-PT DER 最低 26.05%。Tone-PT 在属性级可降 tone FRR/DER，但 FAR 上升。混淆对上，只评区分性属性可进一步降 FAR（声调对平均约降 72%）。

## 结论
统一建模音段与声调语音学属性，可降低 FAR/DER 并提供更细诊断；双元音分解是主要增益来源，音高目标表示利于声调诊断但更敏感。

## 点评
把“错在哪”细化到 articulatory/tonal 属性，比单纯音素替换列表更符合 CAPT 反馈需求。LATIC 说话人少、错误稀疏，单对混淆统计波动大；Tone-PT 的 FAR–诊断分辨率权衡说明属性粒度需按应用选。
