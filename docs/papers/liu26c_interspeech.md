# StyleStream: Real-Time Zero-Shot Voice Style Conversion

- 论文编号：404
- 报告人：Yisi Liu
- 程序：Monday 28 September 2026 / Text-to-Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liu26c_interspeech.pdf

## 问题
零样本语音风格转换需要把源句改成未见目标说话人的音色、口音与情感，同时保留语言内容。现有方法内容–风格解耦不干净：大码本语义 token（如 CosyVoice 2，6561）仍泄漏口音/情感；Vevo 等纯自监督量化又易损伤可懂度。实时语音转换多只做音色，尚无端到端流式的整体风格转换。

## 方法
StyleStream 分 Destylizer 与 Stylizer。Destylizer：冻结 HuBERT-Large（训练流式时解冻并改因果）+ Conformer，FSQ 码本 `[5,3,3]`（45 码）与 ASR 解码器联合做 seq2seq ASR；推理用 FSQ 前的连续表示作内容特征（50 Hz），而非离散码。Stylizer：WavLM-TDNN2 风格编码器 + 16 层 DiT，以频谱 inpainting + OT 路径 conditional flow matching 训练，CFG=2、NFE=16。声码器为因果 Vocos（16 kHz）。流式用 chunked-causal attention，默认 600 ms chunk，端到端延迟约 1 s（`L = t_chunksize + t_proc`）。

## 实验与结果
Destylizer 在约 1300 h LMG（LibriTTS+MSP-Podcast+GLOBE）训练；Stylizer 在 Emilia 英语音约 50k h。评测 StyleStream-Test：300×10=3000 源–目标对。离线 StyleStream：WER 9.2%，S/A/E-SIM 0.852/0.640/0.827，主观 A/E/S-SMOS 最高（约 4.32/4.42/4.36）；流式 WER 15.3%，风格相似度仍领先 Vevo 等。chunk 增大（200→1000 ms）降低 WER、提高相似度与 UTMOS。RTX A6000 上 600 ms chunk 处理约 0.429 s，可流式。全文抽取在 baselines/消融中段截断，后续分析数字不全。

## 结论
作者认为以 ASR 监督 + 紧凑 FSQ + 连续软单元，可更干净地解耦内容与风格，并首次实现约 1 s 延迟的实时零样本风格转换，口音/情感相似度明显优于先前系统。流式相对离线牺牲可懂度。

## 点评
核心抓的是“内容提取瓶颈过宽导致风格泄漏”与“非自回归等长建模便于流式”两点；相对 CosyVoice 2/Vevo，把监督 ASR 与极窄码本压在一起、却用预量化连续特征喂 DiT，是合理折中。PDF 抽取在实验后半截断，消融与延迟表不完整，流式 WER 仍偏高，口音/情感泛化边界需对照完整原文。
