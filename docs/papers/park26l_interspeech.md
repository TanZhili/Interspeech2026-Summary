# Prosody-Aware Speech Representations for Emotion Recognition under Pragmatic Ambiguity

- 论文编号：3486
- 报告人：Yeonwoo Park
- 程序：Wednesday 30 September 2026 / Self-supervised Speech Representation Learning
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/park26l_interspeech.pdf

## 问题
SER 常用 STT 取向编码器（如 Whisper）学语义/频谱表示，却未显式保留韵律；在语用歧义（如同句“Geurae”可因语调表同意/讽刺等）下，Hamming 等粗指标会掩盖模型真实差距。

## 方法
冻结 whisper-large-v3-turbo，提取帧级隐表示；用 Parselmouth/Librosa 得到阈值化 F0 与能量，时间对齐后与编码器输出拼接并投影，再经两层 Transformer + 线性头做 59 类多标签情感分类。另建未见过的 Pragmatic Ambiguity Resolution（PAR）评测：从韩语对话视频中筛出多模态标签与文本单模态不一致、且与音频一致的 1000 句。对比文本/SSL/融合模型及同骨干有无韵律、有无上下文（±5 句）。

## 实验与结果
AI-Hub 韩语情感风格数据（约 457h）训练验证。Hamming 各模型都约 96–98，差距被压缩；注入 F0+能量后 Subset 准确率 12.46→26.39（+13.93%p），PAR 21.00→32.60（+11.6%p），超过多数基线并略优于 GPT-4o mini（31.10）。同骨干下上下文增益小于韵律（Subset +4.83%p、PAR +1.6%p）。较小 Whisper-base 上韵律收益有限。

## 结论
语用歧义下瓶颈在表示是否保留韵律，而非单纯模型规模；显式注入 F0/能量可显著缓解 STT 编码器的韵律抑制，且粗粒度指标不足以诊断该问题。

## 点评
贡献主要在诊断设定（PAR）与同骨干对照，方法本身是冻结编码器后的韵律拼接，简单但能直接暴露 STT 表示缺口。结论依赖韩语数据与特定歧义定义；韵律只进分类头、不改 Whisper 内部注意力，上限仍受冻结骨干约束。
