# AudioGround: Fine-Grained Temporal Grounding in Audio via Deterministic Boundary Supervision

- 论文编号：3467
- 报告人：Mingi Kim
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/kim26z_interspeech.pdf

## 问题
LALM 能描述有什么声，却难以精确定位何时发生；既有监督多为粗多选或 LLM 推断时间戳，边界不可验证，限制细粒度时序定位。

## 方法
构建 **AudioGround-IT**（49.9K 指令、835 小时）：拼接 AudioCaps 片段与静音间隙，边界由构造过程确定；四任务（定位、时长、频次、排序）统一要求输出起止时间戳，并控制位置/长度偏置。模型 **AudioGround** 基于 SALMONN：帧级插值对齐 Whisper/BEATs → 滑窗 Q-Former（文本时间戳条件）→ 混合绝对时间嵌入（正弦 + 可学习残差）→ LoRA 适配 LLM。

## 实验与结果
零样本时刻检索相对多种 LALM，在 Clotho-Moment、UnAV-100、TUT-SE2017 的 Original 设定上整体最优（如 Clotho R1@0.5 27.47）；SALMONN 等基线近零。仍低于监督 AM-DETR，但显著缩小差距。消融显示绝对时间嵌入尤其 hybrid 优于仅时间戳条件。

## 结论
可验证的边界监督是 LALM 时序定位的关键瓶颈；少量确定性标注即可大幅提升零样本 grounding。

## 点评
把问题从“多加点时序数据”纠偏为“监督是否可验证”，合成拼接保证 GT，配套滑窗与时间嵌入合理。脆弱处：训练分布仍是拼接短 clip，与真实长音频重叠事件不同；评测依赖自由文本时间戳解析启发式。
