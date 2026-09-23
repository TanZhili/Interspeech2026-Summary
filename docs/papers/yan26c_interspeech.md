# Probing and Mitigating Hallucinations in Speech-augmented Language Models for Automatic Speech Recognition via Small Language Models

- 论文编号：1278
- 报告人：Bi-Cheng Yan
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yan26c_interspeech.pdf

## 问题
Speech-augmented Language Models（SLM）做 ASR 时仍易幻觉：生成与语音不对齐的额外内容。文中将幻觉词定义为对齐后的一类特殊插入错误。相对视觉–语言与纯文本场景，SLM 的幻觉机制与缓解仍不足。

## 方法
先用因果中介（对 MHA/MLP 做零消融）与注意力行为分析定位幻觉来源。再提出 AudioSLM：在 connector 上建 CTC 模块得到对齐 logits，经 CTC-Gated（深度卷积 + SwiGLU 门控） refinement 音频 token；在 Transformer 块的 MHA 与 MLP 之间插入 cross-attention（query 来自 MHA，key/value 为音频 token），训练时主要更新该层。骨干为 SmolLM2，音频编码器取自 Whisper-large-v2，connector 为 3 层 CNN（下采样 4），LLM 侧用 LoRA。

## 实验与结果
LibriSpeech train-clean-100，评估 clean/other。Dev-clean 上 Vanilla-SLM 的 HER 52.01%、INS 3.69%，AudioSLM 降至 HER 8.69%、INS 0.74%；去掉 CA 或 CTC-Gate 后 HER 升至 11.96%/14.67%。WER：AudioSLM（135M）test-clean/other 为 7.11/11.92，优于 Vanilla-SLM 与 CTC/RNN-T/CTC-Atten，并在 other 上优于 LLM-Guided Decoder（LLaMA-7B）；放大到 1.7B 后 test-clean/other 为 4.71/10.21，但 Dev-clean HER 随规模从 8.69 升到 10.64、12.76。分析显示幻觉词注意力几乎全偏文本 token。

## 结论
幻觉主要来自过度偏向文本先验的自注意力；CTC 对齐门控与跨模态交叉注意力可显著降低 HER，并保持有竞争力的 WER。作者计划后续研究无训练的解码抑制策略。

## 点评
把幻觉形式化为对齐后的插入并做组件级因果分析，使缓解方向有据可依。训练数据仅 clean-100、骨干偏小，规模越大 HER 反升，提示“更强语言先验”与幻觉风险同向；方法强在对齐与跨模态约束，对极嘈杂或开放域场景的外推仍待验证。
