# Unsupervised Speech in the Wild Challenge: Learning Robust Multilingual Representations

- 论文编号：3113
- 报告人：Rafael Mosquera Gómez
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gomez26_interspeech.pdf

## 问题
现有 SSL 多在 LibriSpeech、CommonVoice 等较干净语料上预训练，对网络爬取语音中的自发对话、噪声、长尾语种覆盖不足。需要在仅允许使用 Unsupervised People’s Speech（UPS）的约束下，公平评估多语表示质量。

## 方法
组织 UPS 2026 Challenge：训练数据为 UPS（约 80 万小时公开许可网络音频，Silero VAD 检出约 52.2 万小时语音，Whisper 编码器检出约 89 种语言）。提交须暴露冻结编码器的帧级嵌入接口；下游探针由官方固定：(1) FLEURS 子集 73 语种 LID，线性分类器，macro-F1；(2) 同子集 few-shot CTC ASR，逐语种字符表，macro CER；(3) VoxTube 派生 70 语种/398 说话人聚类，按语种 oracle 说话人数算 ARI 再宏平均。总分按三任务排名均值。经 Dynabench 统一评测。

## 实验与结果
14 队共 80 次有效计分：Macro-F1 均值 0.362（最大约 0.949），CER 均值 0.787（最低约 0.538），ARI 均值 0.457（最大约 0.947）。单模型不统治全任务：LID 最强多为 whisper-baseline / Nx；CER 最强为 WavLM-large 变体；ARI 最强为 qwen3-encoder-baseline。日文等非拉丁脚本 CER 系统性更高；瑞典语/丹麦语等 ARI 更难，且与子集说话人数与性别失衡有关。

## 结论
挑战表明在异构“野外”网络音频上可推动多语 SSL，但三任务探测互补性质，无单一系统全面最优；评估还受正字法与聚类子集构成影响。作者希望推动更稳健、语言无关且说话人感知的表示学习。

## 点评
这是赛道说明书式论文：价值在统一数据约束、冻结编码器与多任务探针设计，而不是提出新架构。对参赛与后续复现最有用的是任务定义、数据集构造与“无模型通吃”的实证；诊断部分也提醒 CER/ARI 解读需结合脚本与子集组成，不能只看排行榜总分。
