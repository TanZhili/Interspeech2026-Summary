# DASR-CPO: Reference-Free Contrastive Preference Optimization for Correcting Mandarin Semantic Drift in Low-Resource Chinese Dialect ASR

- 论文编号：1228
- 报告人：Tao Zhang
- 程序：Tuesday 29 September 2026 / Language and Dialect Recognition
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26s_interspeech.pdf

## 问题
Whisper 等预训练 ASR 在低资源中文方言上常出现 Mandarin Semantic Drift：把方言词解成音近但义错的高频普通话同音词（如“阆中→郎中”）；LoRA SFT 降 CER，却不显式压制这些竞争假设。

## 方法
提出 DASR-CPO：离线从基线假设挖掘混淆（去调拼音编辑距离≤2 的高频替换）构成硬负例；用全序列动态匹配在 BPE 下定位方言跨度；在 teacher-forcing 参考上对跨度打分，取最强负例做 reference-free CPO，并与 SFT CE 混合 \(L_{SFT}+\lambda L_{CPO}\)。骨干 Whisper-Large-v3 + LoRA（q/v，r=32）；Stage1 SFT 3 epoch，Stage2 CPO 2 epoch（β=0.5，λ=1.0，冻结编码器）。

## 实验与结果
MagicData 四川话 ASR-CSICHDIACSC（4.53 h，24 说话人，8:1:1）。相对 Pure LoRA：CER 24.85%→22.58%，方言实体 F1 72.82→74.15，Recall +1.55，假正例 39→32；优于 Context Bias 重加权。推理无额外开销。局限：划分非说话人无关、依赖词表与挖掘质量。

## 结论
把方言适应写成对漂移跨度的偏好排序，可在极低资源下同时改善 CER 与实体语义，且零推理开销；未来拟扩到更多方言与语码转换。

## 点评
针对“音近义错”这一解码先验问题，跨度级硬负对比比纯似然或 token 重加权更贴病灶。非 speaker-disjoint 与小词表可能夸大泛化；CER 绝对值改善有限，但实体指标更能说明语义收益。
