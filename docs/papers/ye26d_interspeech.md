# ZipCodec: Simple and Pretrained-Model-Free Speech Tokenizer via Flow-Matching

- 论文编号：2941
- 报告人：Lingxuan Ye
- 程序：Monday 28 September 2026 / From Self-Supervised Pre-training to Phonetic Analysis of Speech Models
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/ye26d_interspeech.pdf

## 问题
现有语音 tokenizer 多为语义蒸馏/侧载预训练模型（HuBERT、Whisper 等）或复杂多阶段管线，编码器臃肿；能否在无外部教师、无标注的单阶段训练下，用极轻量编码器得到声学与语义都够用的离散 token？

## 方法
**ZipCodec**：mel → 卷积 4× 下采样 → 轻量 Zipformer 编码器（4.4M）→ FSQ 量化 → Zipformer flow-matching 解码器重建 mel（Vocos 转波形）。训练用条件 flow-matching（CFG），并加 **Encoder Consistency Regularization (ECR)**：干净与加噪视图的编码器输出双向 stop-grad 余弦一致性，逼编码器抓语义稳定结构。另有 ZipCodec-distill：教师两步 ODE+CFG 蒸馏，学生将 γ 作为条件、冻结编码器，把 NFE 降到 3。数据以 Emilia 中英约 96.7k 小时为主，另用 LibriTTS 开发。

## 实验与结果
重建上相对 EnCodec、SpeechTokenizer、XCodec/2.0、XY-Tokenizer、BiCodec，ZipCodec 在 Librispeech PC / SeedTTS en/zh 多项 WER、SIM-o、PESQ、ViSQOL 最优或前列（如 LS WER 2.21、SIM-o 0.884），编码器远小于多数基线。ECR（λ=0.25）相对无 ECR 使 LS WER 降约 5.4%。下游同骨干 NAR 零样本 TTS：ZipCodec WER 2.16、SIM-o 0.597、UTMOS 4.08，优于 XCodec 2.0 与 XY-Tokenizer。

## 结论
强 FM 解码器可把语义/声学负担从巨大编码器卸下；ECR 在无教师条件下提升语义；蒸馏版在少 NFE 下保持接近质量。

## 点评
设计哲学是“重解码、轻编码 + 自监督一致性”，直接挑战“语义 token 必须挂大预训练编码器”的主流路线。强在参数与管线极简、下游 TTS 仍占优。边界在于 Vocos 天花板、总参仍含较大解码器，以及语义评估主要靠 ASR WER/下游 TTS，未必覆盖全部语义任务。
