# Audio-Visual Grounding, Synchronization & Video Understanding

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Oral
- Area：10
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕语音驱动开放集检测、声音相关目标定位、视听时序对齐、视频 LLM 是否需要听力、多语视听仇恨言论，以及时序/语义解耦的同步评测。核心问题是：多模态系统常“看起来懂”，但未必真正用地点、声音与时间对齐。

定位类工作规避文本中介误差传播，或用热图引导无框标注下的声音区域。理解类工作强调跨帧差分注意力与时序对齐交叉注意力。审计发现多项视频基准单帧即可答约 76% AVQA，说明听力能力被低估；接入语音/音频编码器后，需听的任务才见收益。应用侧用双曲空间融合副语言与行为线索做仇恨检测；评测侧 AV-SyncBench 首次把时序与语义一致性完全拆开。

## 论文技术总结

# Speech-to-See: End-to-End Speech-Driven Open-Set Object Detection

- 论文编号：2183
- 报告人：Xinyue Song
- 程序：Monday 28 September 2026 / Audio-Visual Grounding, Synchronization & Video Understanding
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/lu26d_interspeech.pdf

## 问题
语音驱动开放集目标检测（audio grounding）数据稀缺；先前 YOSS 等两阶段、经文本/CLIP 中介的管线易误差累积且难端到端优化，也难直接利用韵律等声学线索。

## 方法
Speech2See：在 Grounding DINO + HuBERT 上渐进训练。(1) 预训练：冻结视觉/语音骨干与检测解码器，用 Query-Guided Semantic Aggregation（可学习 query 对 HuBERT 序列交叉注意）压成紧凑语义 token，再经特征增强与 speech-guided query 选择做语音–视觉对齐；(2) 微调：仅训解码器 FFN 中的 Mixture-of-LoRA-Experts（Top-1 路由，K=2），加负载均衡损失。总损失为检测损失（L1、GIoU、对比对齐）+ λ·L_lb。训练语料由 COCO/Objects365/Flickr30k/LVIS 文本标注经 edge-TTS 多说话人合成语音。

## 实验与结果
COCO 闭集：相对 YOSS-large +17.0 AP（56.2 vs 39.2）。零样本 COCO：Obj365+Flickr+GQA 上 42.7 AP，超过 YOSS 闭集。LVIS 零样本：19.9 vs YOSS-large 16.3。相对 Whisper+G-DINO 级联：参数更少（197.8M vs 266.7M）、RTF 更低、AP 更高。消融：QSA 换 MLP 掉约 15.5 AP；K=2 优于 K=1，K=3 无额外收益。相对纯文本 Grounding DINO 仍有差距。

## 结论
作者认为端到端迁移文本–图像先验 + QSA/MoLE 可在合成语音设定下实现直接“听声定位”，并在效率与精度上优于级联与两阶段基线；未来需真实语音与噪声/长尾验证。

## 点评
抓住数据稀缺下“借文本–图像检测器先验、再适配语音”的务实路线；QSA 针对语音时序冗余是合理设计。主要边界是合成 TTS 语音与真实语音分布差，作者已承认；与文本驱动上界的差距也提示声学纠缠（说话人/韵律）仍是对齐难点。


# EchoLoc: Audio-Aware Object Grounding via Joint Heatmap and Box-Level Localization

- 论文编号：2320
- 报告人：Junghwa Shin
- 程序：Monday 28 September 2026 / Audio-Visual Grounding, Synchronization & Video Understanding
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/shin26b_interspeech.pdf

## 问题
音视频定位常只有模糊的相似度热图，难得到清晰目标框；带声源框标注的数据稀缺，而文本–图像 grounding 又对不完整/噪声文本敏感。需要在无显式框标注下，把音频线索接到目标级框预测并端到端训练。

## 方法
EchoLoc 基于 MDETR 式 query 检测器：ResNet-101 视觉 + 冻结 PANNs CNN14 音频。并行两支：(1) 热图支：像素级音视相似度，用空间/全局双向对比学习；(2) 框支：早期融合 Transformer 编解码器输出候选框。用热图 top-α 概率质量区域生成伪框，Hungarian 匹配后做音频条件分类 + L1/GIoU；总损失 L_spa+L_glob+L_box。不以伪框作硬唯一目标，而用多候选 + 最高音视相似度选择，缓解自举不稳定。

## 实验与结果
VGGSound→VGG-SS：cIoU 36.36、AUC 38.28。Flickr-SoundNet-144K→Test：固定阈值 cIoU 84.34；自适应指标 cIoU(adap) 88.22、AUC(adap) 79.99，相对 SOTA 相对提升约 +2.58% / +17.08%。消融：仅热图 cIoU 31.73，加框支升至 36.36。在多实例/模糊对应的 Flickr 上自适应收益更明显。

## 结论
作者认为热图软线索与 query 框预测联合训练，可在无框标注下实现更精细的声源目标定位，尤其利于模糊多目标场景。

## 点评
设计上正面处理“伪框自举悖论”：多候选 + 相似度选择而非硬回归伪框。固定阈值 AUC 不一定全面领先，说明标定敏感；强项在自适应评测与模糊场景。依赖热图质量与 α 阈值，音频编码器冻结也限制声学自适应上限。


# Consistent and Coherent Audio-Visual Understanding with Cross-Frame Patch Differential Attention and Cross-Modal Temporal Alignment

- 论文编号：619
- 报告人：Lecheng Yan
- 程序：Monday 28 September 2026 / Audio-Visual Grounding, Synchronization & Video Understanding
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/yan26b_interspeech.pdf

## 问题
现有 MLLM 常把音视频分路处理，跨模态交互弱，难保证时间同步与语义一致；仅“能接音频”而不做对齐，收益极小（如 MiniCPM-v 与 o 变体差距约 0.04%）。

## 方法
在视觉–语言骨干 + Whisper 音频编码器上，引入：(1) 帧级 RoPE 与模态频率注入（视觉升序、音频降序）建立跨模态时间坐标系；(2) Cross-Frame Patch Differential Attention（CFPDA）对相邻帧 patch 差分做注意力，跟踪与音频相关的视觉变化；(3) Temporal Aligned Attention：按音视频长度比硬/软对齐掩码限制交叉注意，并用自适应质量分平衡模态内特征与跨模态上下文。训练为自回归 CE，参数高效微调（新模块可训、解冻末 4 层解码器等）。模型称 C2AVLM。

## 实验与结果
AVSD：ACC 50.30%、BERT-F1 89.87，全面优于含 Qwen-2.5-Omni（46.95 ACC）等基线。消融显示去音频、去 RoPE/频率、去 CFPDA 或仅交叉注意均掉点。域外：AVHBench 音频驱动幻觉 F1 80.2 领先；Video-MME 长视频无字幕 50.7% 强于 InternVL-3；LongVALE 描述类指标相对弱、但多超基座 Qwen-2.5-VL。

## 结论
作者认为成功的音视频理解依赖精确时间与语义对齐，而非仅多模态接入；所提编码与注意力机制在对话、幻觉检测与长视频时间推理上有效。

## 点评
问题诊断与消融一致：对齐机制比“加个音频塔”更关键。AVSD 与幻觉检测亮眼；长视频 caption 指标偏弱、且多数对比用 8 帧而 Omni 用全帧，作者已说明仍可赢，但跨设定解释需谨慎。依赖 LLM 评判准确率，主观偏置仍在。


# Do Modern Video-LLMs Need to Listen? A Benchmark Audit and Scalable Remedy

- 论文编号：2532
- 报告人：Geewook Kim
- 程序：Monday 28 September 2026 / Audio-Visual Grounding, Synchronization & Video Understanding
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/kim26s_interspeech.pdf

## 问题
Video-LLM 常丢弃音轨，因主流基准多可用纯视觉作答；即便标榜音视频的套件也存在视觉捷径。同时原始音频 token（约 25 Hz）对长视频上下文不可承受。

## 方法
(1) 基准审计：仅用时间中心单帧、无音频喂 GPT-4o 两次，双对即剔除，得到过滤子集（如 AVQA 约 76% 可单帧解）。(2) 在 LLaVA-OneVision 上接 Qwen2-Audio 的 Whisper 编码器；比较仅视觉、非交错、时间对齐交错输入。(3) 周期 query 将音频压缩 25×（25→1 Hz）；比较 Avg Pool、Resampler、Uni/BiMamba、UniMambaMia（因果 Mamba + 门控注意，可流式）。

## 实验与结果
10 个基准上，交错+压缩在需听懂/跨模态题上明显增益；过滤后 AVSpeakerBench +3.0、WorldSense +2.7、VideoMME +2.4 等仍成立，长视频增益更大。压缩器中 UniMambaMia 最稳。最终模型在 Qwen2-7B 系统一评测中多项最优；相对未压缩 Qwen2.5-Omni 时延/显存更低（约 1.6 s vs 4.1 s）。视觉中心套件加音频收益小或略干扰。

## 结论
作者认为 Video-LLM 需要听，但前提是基准真正要求听；控制视觉捷径后音频价值清晰。时间对齐交错 + 因果轻量压缩是可扩展接音频的实用配方。

## 点评
贡献一半是评测诊断（捷径审计与过滤集），一半是工程配方（因果 25× 压缩）。用 GPT-4o 定义“可单帧解”可能过严/过松，但作为下界审计仍有说服力。与 Omni 等不同骨干/数据规模对比不宜过度解读为纯音频通路优劣。


# VINAYAKA: Multilingual Audio-Visual Hate Speech Detection via Cross-Modal Fusion in Hyperbolic Space

- 论文编号：2262
- 报告人：Orchid Chetia Phukan
- 程序：Monday 28 September 2026 / Audio-Visual Grounding, Synchronization & Video Understanding
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/kuwar26_interspeech.pdf

## 问题
多语言/码混视频仇恨检测若依赖 ASR 文本，易受识别错误与跨语域漂移影响；仇恨意图也常在韵律、表情、场景等非词汇音视频线索中。需验证仅用 AV 线索能否在跨语/跨集设定下更稳健。

## 方法
VINAYAKA：冻结 WavLM（音频）与 ImageBind 视觉编码器抽特征，经 1D-CNN 后投影到 Poincaré 球；用双曲距离做双向交叉注意（音频引导视觉/视觉引导音频），Möbius 加和与标量乘聚合，再对数映射回欧氏空间分类。对比拼接、欧氏交叉注意、仅 Möbius 加以及文本依赖的 MM-HSD、ToxVidLM、MultiHateClip 复现。数据：HateMM、ToxCMM（Hi-En 码混）、MultiHateClip 英/中，五折交叉验证与跨集零微调迁移。

## 实验与结果
域内：VINAYAKA 全面最优（如 HateMM Acc/F1 0.914/0.901，ToxCMM 0.892/0.885）。曲率消融：双曲 c=−1 优于欧氏与球面。跨集迁移普遍优于文本依赖基线；跨语/跨文化仍有掉点但相对更稳，作者归因于避开 ASR 误差传播。

## 结论
作者认为仅靠副语言/行为 AV 线索 + 双曲跨模态融合，可比文本中心方法在多语言与分布外设定更稳健，并报告 M-AVHSD 上 SOTA。

## 点评
问题设定清楚：把“文本不可靠”当作一等公民约束。双曲几何假设行为线索有层级结构，曲率消融支持该选择。数据集规模中等、标签二值化（Offensive 并入 Hate）会简化任务；ImageBind/WavLM 语义层与“仇恨”标签的因果仍偏黑盒。


# AV-SyncBench: Decoupled Benchmarking of Temporal and Semantic Audio-Visual Synchronization

- 论文编号：2177
- 报告人：Yuxuan Jiang
- 程序：Monday 28 September 2026 / Audio-Visual Grounding, Synchronization & Video Understanding
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/zhou26g_interspeech.pdf

## 问题
音视频特征评测常把语义匹配（检索）与时间偏移检测混为一谈或偏重其一，数据构造也耦合，难以独立诊断时间一致性与语义一致性。

## 方法
提出 AV-SyncBench：从野外视频筛选声源在画面内的片段（Gemini 初筛 + 人工复核），得 3,269 视频、38,390 样本，覆盖 Voice/Music/Sound、10 场景。解耦两类挑战——时间：全局偏移（50–500 ms）、局部抖动、全局变速（0.8×–1.25×），语义不变；语义：OpenVoice/DDSP 改音色/乐器但保持节奏时序。切 0.64 s chunk，用对角余弦相似（或零偏移概率）做成对比较，报告二分类准确率。评测 Synchformer、SparseSync、ImageBind、CAV-MAE、CAV-MAE-Sync。

## 实验与结果
大扰动更易检出；全局偏移上 Synchformer/SparseSync 较强，CAV-MAE 近随机。局部抖动与变速上模型表现分化。语义音色任务：ImageBind 整体最高（约 0.859），SparseSync 近随机，CAV-MAE 系在乐器上更强。类别上单源清晰场景优于多源复杂场景。结论显示时间与语义能力明显解耦、训练目标偏科。

## 结论
作者认为解耦基准可诊断特征提取器的时间/语义短板，并呼吁未来模型同时建模细粒度时间结构与语义对齐。

## 点评
贡献是评测协议与变量隔离的数据构造，而非新对齐模型。生成式音色编辑可能引入非纯语义伪迹（作者已写局限）；片段偏短（≤13 s）、物体声可控替换仍弱。对下游同步生成/筛选数据仍有直接工具价值。

