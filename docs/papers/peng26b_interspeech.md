# TASU2: Controllable CTC Simulation for Alignment and Low-Resource Adaptation of Speech LLMs

- 论文编号：866
- 报告人：Jing Peng
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/peng26b_interspeech.pdf

## 问题
Speech LLM 后训练缺大规模音文对成本高；TASU 用文本随机模拟 CTC 后验可做纯文本对齐，但对不确定性与错误率可控性弱，课程设计偏启发式，低资源适配时易伤源域。

## 方法
提出 TASU2：学习 WER 条件文本→CTC 后验模拟器（6+6 层 Transformer，隐维 512）。用 LibriSpeech 约 1/7 加噪/混响，教师 ASR 产出真实 CTC 后验与假设，按 WER 分三档（0–6%、10–40%、50–150%）作控制码，以分布级 CE 匹配后验。推理时指定档位自回归生成伪后验，经投影送冻结 SenseVoice-Small + Qwen2.5-1.5B。两阶段后训练可做源→目标（如 Medical）文本 Sim-CTC 适配（LoRA）。

## 实验与结果
后验相似度优于 TASU-style（CE 2.51→1.23，KL 2.34→1.05）。WER 分档可分离实现错误率。Libri 训练下 TASU2 分档：clean/other 3.41/8.15，Slide/TED 优于原 TASU。Medical 两阶段：目标 WER 12.12，优于 raw text 13.62、TTS 12.79、raw audio 12.35，且源域相对 Stage1 几乎不变（约 +0.02/+0.07）。多任务下 Libri 大升、CoVoST2 BLEU 与 TASU 接近。

## 结论
作者认为可控 CTC 模拟能更好贴合声学解码接口，强化纯文本对齐与低资源迁移并保留源域；可作缺配对音频时的 TTS 替代。

## 点评
相对 TASU，关键是把“随机扰动”换成“教师后验 + WER 旋钮”，让课程与域适配可调度。强项是保真度指标与 Medical 迁移对照完整；脆弱处在于模拟器依赖教师 ASR 与 Libri 增强分布，极端域的音素混淆是否可迁移仍存疑。
