# Foundational speech models evaluation on multilingual dementia prediction

- 论文编号：2587
- 报告人：Bartłomiej Eljasiak
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 1
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/eljasiak26_interspeech.pdf

## 问题
痴呆早期筛查需要可扩展语音生物标志；主流基础语音编码器在多语、跨语与零样本认知障碍检测上的系统比较不足，且临床标签数据稀疏。

## 方法
SUPERB 式管线：冻结或微调编码器 → 可学习层加权 → 下游头（轻量 ECAPA-TDNN 或前馈/注意力池化）→ 段级概率平均到被试。语料：DementiaBank 系 ADReSS/ADReSSo/ADReSSM/TAUKADIAL/Dem@Care/Ivanova，加波兰 DiagNeuro；统一痴呆 vs 健康（非健康一律映射为痴呆）。说话人分离用时间戳或 pyannote；段长约 ≥6 s 参与者语音，训练随机 30 s。比较 Wav2Vec2、HuBERT、WavLM、Whisper 等；单语、多语预训练再微调、及未见语迁移。

## 实验与结果
多语设定 WavLM-Base+ 整体 F1 0.761；WavLM-Large 英语子集 F1 0.854。单库上冻结编码器 ADReSSo F1 0.916、DiagNeuro 0.943 等，部分可比或超公开 SOTA。跨语：如 EN+SP 训测 PL 可达 F1 0.929；向 PL 逐步加语种可抬 F1（0.692→0.840）。Whisper-tiny：非目标语预训练再微调普遍优于纯单语基线；西语上仅跨语 transfer 即可 F1 0.678 超单语 0.648。作者因官方 TAUKADIAL 测分不具代表性而自建分层划分，并剔除重复文件以防泄漏。

## 结论
在多语料统一管线下，基础语音模型可做稳健多语痴呆检测；增加训练语种常提升单语表现，并存在一定零样本迁移。注意切分与去重对可比性至关重要。

## 点评
贡献偏“大规模对照与数据卫生”而非新架构，对领域很实用。强在多编码器×多语设定与“加语种反而帮单语”的经验；弱在病因标签被压成二类、任务与录音时长异质、以及自建 TAUKADIAL 划分使与挑战榜直接对比需谨慎。
