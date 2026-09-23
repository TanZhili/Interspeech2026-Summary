# Audio-Visual Grounding, Synchronization & Video Understanding

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Oral（Area 10）
- 论文数：6
- 材料：官方程序中该场全部论文摘要（[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA 列表](https://www.isca-archive.org/interspeech_2026/index.html)）。摘要写明问题、方法与主要结论；未出现的数字与细节不写入。

## 技术趋势

本场围绕语音驱动开放集检测、声音相关目标定位、视听时序对齐、视频 LLM 是否需要听力、多语视听仇恨言论，以及时序/语义解耦的同步评测。核心问题是：多模态系统常“看起来懂”，但未必真正用地点、声音与时间对齐。

定位类工作规避文本中介误差传播，或用热图引导无框标注下的声音区域。理解类工作强调跨帧差分注意力与时序对齐交叉注意力。审计发现多项视频基准单帧即可答约 76% AVQA，说明听力能力被低估；接入语音/音频编码器后，需听的任务才见收益。应用侧用双曲空间融合副语言与行为线索做仇恨检测；评测侧 AV-SyncBench 首次把时序与语义一致性完全拆开。

## 技术内容

### 语音/音频驱动定位

**Speech-to-See: End-to-End Speech-Driven Open-Set Object Detection**（论文 2183；Xinyue Song）
Speech2See 以渐进预训练与微调利用语义先验，Query-Guided Semantic Aggregation 压缩时序冗余，微调用 Mixture-of-LoRA-Experts 做细粒度跨模态对齐。实验称无需中间文本即可听音定位，多基准达领先水平。

**EchoLoc: Audio-Aware Object Grounding via Joint Heatmap and Box-Level Localization**（论文 2320；Junghwa Shin）
基于 MDETR 查询式检测器引入音频，经视听对齐学习空间热图并引导 ROI 级框预测，即使无显式框标注也能定位声音相关区域。Flickr-SoundNet-Test 上相对 SOTA，cIoU(adap)/AUC(adap) 相对提升 +2.58%/+17.08%。

### 时序对齐、基准审计与应用/评测

**Consistent and Coherent Audio-Visual Understanding with Cross-Frame Patch Differential Attention and Cross-Modal Temporal Alignment**（论文 619；Lecheng Yan）
框架含频率注入旋转位置编码、跨帧 patch 差分注意力，以及自适应加权的时序对齐跨模态注意力。AVSD 准确率 50.30%，相对基线 +11.59%；域外测试在音频驱动幻觉检测与长视频理解上泛化强。

**Do Modern Video-LLMs Need to Listen? A Benchmark Audit and Scalable Remedy**（论文 2532；Geewook Kim）
审计 10 个视频基准，发现多题仅靠视觉可解：单帧探针无音频即可答约 76% AVQA。在 LLaVA-OneVision 上接入语音/音频编码器并比较五种 25× 压缩器（25 Hz→1 Hz）。需语音理解或跨模态对齐的任务有明确增益，视觉中心套件基本不受影响。

**VINAYAKA: Multilingual Audio-Visual Hate Speech Detection via Cross-Modal Fusion in Hyperbolic Space**（论文 2262；Orchid Chetia Phukan）
仅用 AV 线索，结合 WavLM、ImageBind 与双曲空间跨模态融合（CFHS）对齐副语言与行为线索。跨语言/跨数据集的分布内与分布外均称 SOTA，并对 ASR 误差传播稳健。

**AV-SyncBench: Decoupled Benchmarking of Temporal and Semantic Audio-Visual Synchronization**（论文 2177；Yuxuan Jiang）
首个完全分离时序与语义评估的视听同步基准，覆盖 Voice/Music/Sound、10 场景与 5 挑战任务；3,269 视频、38,390 样本，并评估五种代表模型。代码与数据公开。

## 本场要点

- 端到端语音定位避免文本管道误差；热图可在无框标注下引导声音区域。
- 视听理解依赖精确时序与语义对齐，而非简单拼接模态流。
- 现有视频基准大量可不听作答，低估语音编码器价值。
- 双曲融合有助于多语视听仇恨检测并对 ASR 噪声稳健。
- AV-SyncBench 把时序偏移与语义匹配评测解耦。

## 覆盖核对

- 2183 | Speech-to-See: End-to-End Speech-Driven Open-Set Object Detection
- 2320 | EchoLoc: Audio-Aware Object Grounding via Joint Heatmap and Box-Level Localization
- 619 | Consistent and Coherent Audio-Visual Understanding with Cross-Frame Patch Differential Attention and Cross-Modal Temporal Alignment
- 2532 | Do Modern Video-LLMs Need to Listen? A Benchmark Audit and Scalable Remedy
- 2262 | VINAYAKA: Multilingual Audio-Visual Hate Speech Detection via Cross-Modal Fusion in Hyperbolic Space
- 2177 | AV-SyncBench: Decoupled Benchmarking of Temporal and Semantic Audio-Visual Synchronization
