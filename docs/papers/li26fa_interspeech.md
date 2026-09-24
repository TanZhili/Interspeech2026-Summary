# Language-Invariant Multilingual Speaker Verification for the TidyVoice 2026 Challenge

- 论文编号：2437
- 报告人：Xiaoxiao Miao
- 程序：Thursday 1 October 2026 / TidyVoice2026 Challenge: Cross-Lingual Speaker Verification
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/li26fa_interspeech.pdf

## 问题
多语说话人确认受跨语数据不足与嵌入中语言相关信息拖累。官方 TidyVoiceX 虽多语，但每说话人通常只有两三种语言，语言多样性不够，易学到身份–语言纠缠的表示，削弱跨语泛化。

## 方法
骨干为 w2v-BERT 2.0：各 Conformer 层经 Layer Adapter 降维适配，拼接后 ASP + 线性得到说话人嵌入，LoRA 高效微调。语言不变学习：在嵌入上接语言分类器，经 GRL 做对抗（λ_GRL=λ_lang=0.1），先单独训语言头再联合对抗。合成增广：用 Qwen3-TTS 零样本多语克隆，对最多约 3495 条 >3s 参考音各合成 10 语种×10 句，共约 34.95 万条；文本来自 LibriTTS 经 M2M100 翻译，参考转写用 Whisper-large-v3。训练两阶段：先在 VoxCeleb2/VoxBlink2/3D-Speaker/KeSpeech/CN-Celeb 上大规模说话人预训练（冻→解冻）；再在 TidyVoiceX 上域适应并开 GRL。比较 ArcFace 与 SphereFace2-A/C；推理用 QMF（时长、嵌入范数、SNR、原分等）逻辑回归校准。

## 实验与结果
官方基线 Dev 3.07%、eval-A 9.06%、eval-U 11.59%。仅预训练数据微调已 Dev 2.74%。SphereFace2-C 明显优于 ArcFace；仅 TidyVoiceX 微调的 SF2-C：Dev 0.95%，+GRL 0.937，++QMF 达 Dev 0.893、eval-A 2.458、eval-U 4.451。混入大规模预训练数据对未见语种 eval-U 更有利，对见语种子集更偏域特化。合成数据：t-SNE 显示同说话人合成与真实嵌入接近；但在本设置下加合成未再提升，仅用合成约 1.022% Dev EER，接近真实数据 0.95%，作者认为数据充足时合成–真实域差可能伤性能，低资源时更有价值。

## 结论
作者认为微调大规模 SSL、用 SphereFace2、语言对抗与（低资源下）ZS-TTS 增广可提升多语 SV；GRL 带来适度去语言收益，合成增广在数据受限时更有意义。

## 点评
三条线并列：强 PTM+MFA、GRL 去语言、TTS 扩语种。GRL 与 QMF 的增益清晰但幅度不大；SphereFace2 相对 ArcFace 的提升更醒目。脆弱点在于合成增广在充足真实数据下未兑现收益，说明“更多语种”不等于更好——域匹配与标签噪声同样关键；eval-U 仍明显高于 eval-A，未见语种泛化仍未彻底解决。
