# Context Projector: Complementary Keyword and Dialogue Context Embeddings for LLM-based ASR

- 论文编号：3326
- 报告人：Sergio Burdisso
- 程序：Tuesday 29 September 2026 / Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/villatorotello26_interspeech.pdf

## 问题
联络中心 ASR 既要整体 WER，也要业务实体（BWER）。把原始多轮上下文塞进 LLM-ASR 提示易变差且昂贵；需参数高效地注入压缩对话上下文与关键词。

## 方法
在冻结 SLAM-ASR（WavLM-Large + Llama 3.2 3B）上增加 context projector：Dialog2Flow 句嵌入经与 speech projector 同构的 MLP 变成紧凑上下文 token；Gemma3-27B 从历史抽关键词。只训 projector。DefinedAI 多域联络数据约 246h、约 3.8 万实体。

## 实验与结果
原始长上下文常抬高 WER；关键词 alone 改善 BWER 但可能伤 WER。keywords + context projector 改善 WER–BWER 权衡：相对基线平均相对降 WER 最高约 2.5%、BWER 约 7.2%，并提升实体 F1。近期短窗上下文通常足够。

## 结论
压缩动作感知上下文 + 关键词互补，是 LLM-ASR 在联络中心场景下实用的上下文增强，避免原始长提示退化。

## 点评
把“实体敏感”明确成 BWER，比只报 WER 更贴业务。冻结骨干只训投影器工程友好；关键词依赖大模型抽取，部署成本与错误会传导到 ASR。
