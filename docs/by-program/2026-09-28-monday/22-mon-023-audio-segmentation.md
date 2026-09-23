# Audio segmentation

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Oral（Area 5）
- 论文数：6
- 材料：官方程序中该场全部论文摘要（[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA 列表](https://www.isca-archive.org/interspeech_2026/index.html)）。摘要写明问题、方法与主要结论；未出现的数字与细节不写入。

## 技术趋势

本场名义为音频分割，实际覆盖多任务门控理解、关键词测试时适应、流式端点检测、超小 VAD、语音编解码器探测，以及文本–音频对比学习的模态内相似监督。共同点是在端侧/流式约束下决定“何时听、听什么、表示里有什么”。

门控多任务把 ASR、情感与场景分类统一在 Whisper-small 上，按干净/噪声/非语音条件激活头，并发布 ESAS-32K。KWS 的测试时适应直面关键词稀有与背景主导导致的熵最小化偏差。端点检测用“到下一语音 onset 的时间”作可从时间戳衍生的监督，缓解犹豫停顿。极简因果 VAD 强调标准 Mel、纯 CNN、结构化剪枝与角距 QAT。

另一侧是表示诊断与学习：主流 speech tokenizer 经探测更偏语音而非词义语义；对比学习则把文本–文本、音频–音频相似转为跨模态软目标。整体从“切段”扩展到“条件激活、在线适应与表示内容核对”。

## 技术内容

### 多任务门控、测试时适应与流式端点

**A Gated Multi-Task Whisper Framework for Speech, Emotion, and Scene Understanding**（论文 135；Manjiri Bhat）
在 Whisper-small 编码器上联合 ASR、SER 与声学场景分类，门控将输入判为干净语音、噪声语音或非语音以条件激活下游头；并引入情感语音与场景混合的 ESAS-32K。实验称优于无门控与单任务基线，并减轻语音到文本幻觉。

**ImKWS: Test-Time Adaptation for Keyword Spotting with Class Imbalance**（论文 258；Ting Dang）
标准 TTA 熵最小化在关键词稀有、背景频繁时过信背景类。ImKWS 将熵拆为奖励/惩罚支并分设更新强度，并跨多种音频变换强制一致性。Google Speech Commands 实验称在真实不平衡场景下适应可靠。

**Next-Turn: Duration-Aware Streaming Endpoint Detection via Time-to-Next-Speech-Onset Prediction**（论文 1053；Tao Zhong）
以到下一语音 onset 的时间作训练目标，标签直接来自语音时间戳、无需额外人工标注。相对最强基线，320 ms 内端点准确率绝对提升 25.9%；与标准二分类 EPD 联合训练时，停顿越长收益越大。

### 端侧 VAD、编解码探测与对比监督

**VAD to the Bone: Ultra-Tiny Speech Activity Detection for Edge Deployment**（论文 2523；Shanza Iftikhar）
提出 kiloVAD：标准 Mel、纯 CNN、可调上下文/频谱参数；逐层结构化剪枝+自蒸馏，以及优于标准 QAT 约 1–4% 的角距 QAT。因果逐帧评估下，2.1k 参数、200 ms 上下文在 AVA-Speech 达 0.850 AUC。

**Speech Codec Probing from Semantic and Phonetic Perspectives**（论文 3135；Xuan Shi）
对多种常用 speech tokenizer 做词义语义与语音内容三任务评估。结果表明当前分词器主要捕获语音而非词汇语义结构，并对下一代 tokenization 设计给出实践含义。

**Leveraging Mutual Intra-Modal Similarity Supervision for Text and Audio**（论文 3300；Julian Miguel von Aspern）
将批次内文本–文本相似作文本–音频软目标，并推广到音频–音频相似；再用不确定性估计得到相似目标，并考察模态分类分支与 MSE 引导估计。在指定训练体制下称下游任务可与 SOTA 竞争，但训练数据与 batch 更小。

## 本场要点

- 门控多任务可按输入类型条件激活 ASR/情感/场景模块并抑制幻觉。
- 不平衡 KWS 的 TTA 需拆分熵奖励/惩罚，避免背景类主导。
- 时长感知的“下一 onset 时间”目标改善流式端点对犹豫停顿的稳健性。
- 千参数级因果 VAD 可通过剪枝与角距 QAT 达到可部署精度。
- 现有 speech tokenizer 探测结果偏语音、弱词义，制约多模态对齐叙事。
- 模态内相似可作跨模态软监督，降低对比学习数据规模需求。

## 覆盖核对

- 135 | A Gated Multi-Task Whisper Framework for Speech, Emotion, and Scene Understanding
- 258 | ImKWS: Test-Time Adaptation for Keyword Spotting with Class Imbalance
- 1053 | Next-Turn: Duration-Aware Streaming Endpoint Detection via Time-to-Next-Speech-Onset Prediction
- 2523 | VAD to the Bone: Ultra-Tiny Speech Activity Detection for Edge Deployment
- 3135 | Speech Codec Probing from Semantic and Phonetic Perspectives
- 3300 | Leveraging Mutual Intra-Modal Similarity Supervision for Text and Audio
