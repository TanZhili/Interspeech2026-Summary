# Efficient Inference for ASR and Speech LMs

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：9
- 论文数：10
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program ；https://www.isca-archive.org/interspeech_2026/index.html）。不补写摘要未给出的数字与细节。

## 技术趋势

本场关注 ASR 与语音语言模型的高效推理：无资源音节令牌化、无数据无训练压缩、端侧关键词检出的结构剪枝与短时记忆卷积、统一音频理解与生成的高吞吐管线、半自回归并行生成、流式发射策略、自适应令牌采样、LLM 知识合并，以及千类少样本持续学习。核心是在延迟、算力、内存与质量之间取得可部署折中。

离散令牌序列过长推动音节级与自适应合并；基础模型压缩探索通道聚类剪枝；始终在线 KWS 同时做权重与通道剪枝或把 CNN 改为 LSTM 式在线推理。生成侧 vLLM 扩展延迟模式多流采样与 CFG 共调度，Audio-NSP 仅靠数据重构激活并行解码。流式 ASR 用训练无关发射策略包装时间戳基础模型；AdaTS 动态合并低信息令牌降推理成本；LoRA 算术合并把外部 LM 知识并入 ASR 参数而不增推理开销。

## 技术内容

### 令牌化、压缩与端侧 KWS

**ZeroSyl: Simple Zero-Resource Syllable Tokenization for Spoken Language Modeling**（论文 315；Nicol Visser）  
训练无关方法：从冻结 WavLM 中间层 L2 范数提取音节边界与嵌入，均值池化后 K-means 离散化再训 LM。摘要称音节分割有竞争力，跨词法/句法/叙事基准优于既有音节分词器；细粒度单位利于词法，发现的音节单位在句法建模上扩展行为更好。

**Towards Data-free and Training-free Compression for Speech Foundation Models Using Parameter Clustering**（论文 1010；Haoning Xu）  
通道维 k-means 聚类压缩，并探索按层变化簇数的混合稀疏剪枝。LibriSpeech 上 HuBERT-large 50% 稀疏相对幅度剪枝微调前/后均有 WER 下降；Whisper-large-v3 10% 稀疏相对幅度剪枝亦有显著相对 WER 下降，且相对未压缩基线无明显恶化。

**OnDA: On-device Channel Pruning for Efficient Personalized Keyword Spotting**（论文 1253；Alessio Burello）  
首次把在线结构化通道剪枝与端侧权重适配耦合于个性化 KWS。HeySnips/HeySnapdragon 上相对未剪枝基线最高约 9.63× 模型体积压缩且任务性能持平；Jetson Orin Nano 上相对仅权重适配，在线训练/推理延迟与能耗最高分别约 1.52×/1.57× 与 1.64×/1.77× 改善。

**Sub-Model Short-Term Memory Convolutions for Keyword Spotting Systems on Device**（论文 1343；Szymon Klimaszewski）  
将 STMC 用于模块化 CNN 的在线类 LSTM 推理，降低功耗与冗余计算。相对等效频繁标准 CNN 与原版 STMC，MCPS 最高分别降约 82% 与 46%；最佳配置 Google Speech Commands 11 类准确率 93.8%，零填充同任务 97.1%。

### 高吞吐生成、流式 ASR 与模型合并

**An Efficient vLLM-Based Inference Pipeline for Unified Audio Understanding and Generation**（论文 1244；Haoran Wang）  
扩展自回归解码以原生执行延迟模式解交织与协调多流采样，并集成 GPU 上声学解码器做端到端波形合成；将条件/无条件请求共调度于连续批处理，CFG 吞吐维持非 CFG 的约 80%。框架开源。

**Audio-NSP: Data-Centric Semi-Autoregressive Generation for Large Audio-Language Models**（论文 1737；Liang Cao）  
仅通过数据中心 SFT 与块注意力重构序列，在预训练 LALM 上激活半自回归并行生成；模态感知动态截断对文本严格、对音频宽松，避免退化为单步解码。摘要称加速最高约 3.42×，质量保持显著优于 MTP 基线。

**Improving streaming ASR with foundation models using emission policies**（论文 3358；Gerard Mas Mollà）  
训练无关流式管线：滑窗缓冲、令牌级时间戳管理与纯文本发射策略。三套英语数据上评估多种发射策略；摘要称使 Parakeet、Canary 等可出时间戳的 SFM 在实时环境接近离线转写质量，无需访问内部张量。

**AdaTS: Adaptive Token Sampling for Efficient Speech Language Models**（论文 2753；Sonal Sannigrahi）  
动态合并低信息区域令牌，使 LLM 所见语音长度降 2× 或更多；ASR、SQA、ST 上常优于标准下采样，推理成本约降 40%。

**Merging the Knowledge of LLMs for Automatic Speech Recognition**（论文 2561；Hayato Futami）  
通过 LoRA 参数算术运算把外部 LM 直接并入基于 LLM 的 ASR，推理无额外开销。CSJ 与 LibriSpeech 训练模型的域扩展/迁移实验摘要称目标域 ASR 持续改善且不损速度与显存。

**Scaling few-shot spoken word classification with generative meta-continual learning**（论文 408；Batsirayi Mupamhi Ziki）  
用 GeMCL 顺序学习区分 1,000 类、每类仅五样本。摘要称性能异常稳定；虽不总优于反复全微调或冻结 HuBERT+反复训练头，但与后者可比且适配快约 2,000 倍，数据不到一半、训练时间低两个数量级。

## 本场要点

- ZeroSyl 以冻结 WavLM 提供简单无资源音节令牌化。
- 无数据聚类剪枝可在高稀疏下相对幅度剪枝显著降 WER。
- 端侧 KWS 把通道剪枝与 STMC 在线推理推向可穿戴约束。
- vLLM 多流 + CFG 共调度与 Audio-NSP 半自回归提升生成吞吐。
- 发射策略包装使流式基础模型接近离线质量。
- AdaTS、LM 合并与 GeMCL 分别削减令牌冗余、融合开销与少样本扩展成本。

## 覆盖核对

| id | title |
|---|---|
| 315 | ZeroSyl: Simple Zero-Resource Syllable Tokenization for Spoken Language Modeling |
| 1010 | Towards Data-free and Training-free Compression for Speech Foundation Models Using Parameter Clustering |
| 1253 | OnDA: On-device Channel Pruning for Efficient Personalized Keyword Spotting |
| 1343 | Sub-Model Short-Term Memory Convolutions for Keyword Spotting Systems on Device |
| 1244 | An Efficient vLLM-Based Inference Pipeline for Unified Audio Understanding and Generation |
| 1737 | Audio-NSP: Data-Centric Semi-Autoregressive Generation for Large Audio-Language Models |
| 3358 | Improving streaming ASR with foundation models using emission policies |
| 2753 | AdaTS: Adaptive Token Sampling for Efficient Speech Language Models |
| 2561 | Merging the Knowledge of LLMs for Automatic Speech Recognition |
| 408 | Scaling few-shot spoken word classification with generative meta-continual learning |
