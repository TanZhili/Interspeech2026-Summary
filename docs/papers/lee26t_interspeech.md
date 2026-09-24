# Progressive Alignment Objectives for Aligner-Encoder based ASR

- 论文编号：2132
- 报告人：Jaeyoung Lee
- 程序：Thursday 1 October 2026 / New Training Methods for ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/lee26t_interspeech.pdf

## 问题
Aligner-Encoder 用编码器第 u 个位置直接预测第 u 个 token，无 cross-attention / Transducer 格点；对齐多在深层突然出现，长句上训练脆、性能差。

## 方法
提出 InterAligner：在中间层 ℓ_int（主实验第 15 层）对更长、更细粒度 BPE 序列加中间 Aligner 损失（独立 predictor/joiner）；在更早层 ℓ_ctc=12 加 InterCTC；顶层仍对较粗短序列做最终 Aligner。总损失加权 λ_final L_final + λ_int L_int + λ_ctc L_ctc，形成由早到晚、由细到粗的对齐课程。

## 实验与结果
17 层 Conformer-L（~118M），LibriSpeech 960h：Final-only 5.0/7.8 → +InterCTC 3.4/6.0 → +InterAligner 3.1/5.6（test-clean/other）。Common Voice EN：12.4→11.2→10.9。按时长分层，>21 s 句 clean/other 从 InterCTC 的 17.0/18.0 再到 InterAligner 的 11.6/13.5。消融：中间与 CTC 目标同用较小词表（如 256）优于不匹配；λ_final/λ_int=0.5/1.0 优于 1.0/0.5；InterAligner 挂在第 15 层优于第 16/13；仅缩小最终词表不够，需要层级监督。注意力可视化显示层 14 出现细粒度对角、层 16 再到粗粒度。

## 结论
中间 CTC + 中间细粒度 Aligner 可让对齐在深度上渐进形成，稳定 Aligner-Encoder 训练，并在长句上带来最大收益。

## 点评
针对“对齐瓶颈挤在顶层”的结构问题，用多粒度中间监督做课程，比单纯加深或换解码器更对症。挂层位置与词表粒度敏感（需留出至少约两层做细→粗转换）。收益主要在长句；短句上相对 InterCTC 提升有限。
