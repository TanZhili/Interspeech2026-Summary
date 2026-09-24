# Joint Learning Global-Local Speaker Classification to Enhance End-to-End Speaker Diarization and Recognition

- 论文编号：774
- 报告人：Yuhang Dai
- 程序：Wednesday 30 September 2026 / Speaker Diarization 1
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/dai26b_interspeech.pdf

## 问题
LALM 端到端说话人日志化与识别（SDR）在语义转写上强，但说话人可分性弱：对话数据少、缺少显式说话人表征优化，声学相近说话人易混淆。

## 方法
GLSC-SDR：在 Qwen2.5-Omni-7B 上用 LoRA 联合训练 SDR 与说话人分类。GLSC：对高质量单说话人段提 ERes2Net 嵌入，HDBSCAN 聚类得全局标签；簇内说话人再局部重编码得局部标签，拼接为层次监督。数据经 ASR 质量过滤（WER>30% 或插入错误>2 丢弃）。无需改 LLM 骨干结构。

## 实验与结果
AliMeeting / AISHELL-4 / AMI-SDM：GLSC-SDR 的 cpWER 分别为 25.43 / 23.49 / 23.32，优于同骨干 SFT（26.77 / 26.34 / 27.16）及若干相关工作；SCA 与 Δcp 同步改善。消融显示仅全局或仅局部分类弱于 GLSC。簇数过少/过多损害 cpWER。

## 结论
层次全局–局部说话人分类可增强 LALM 的说话人判别而不牺牲转写，在会议基准上达到有竞争力或更优表现，且不依赖大规模真实对话仿真。

## 点评
把 SV 式度量学习思想接到 LALM 多任务，而不堆额外说话人编码器，工程上干净。层次标签依赖嵌入聚类质量；过滤规则可能丢掉难例。相对 TagSpeech 等，优势在联合优化而非架构增补。
