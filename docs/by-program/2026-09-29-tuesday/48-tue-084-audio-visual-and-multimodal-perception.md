# Audio-Visual and Multimodal Perception

- 日期：Tuesday 29 September 2026
- 时间：16:30-18:30
- 形式：Long Oral
- Area：
- 论文数：5

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场从“多模态是否有效”转向“多模态如何贡献、是否真正泛化、是否像人一样感知”。音视频语音识别侧用 Shapley 归因拆解模态贡献，并在严格匹配分布的未见集上检验 LRS3 近乎完美分数是否反映真实泛化；视觉语音识别则对比模型与人类唇读在词/视位层的成功失败模式。

情感分析侧批评优化式模态平衡方法混淆拟合速度与判别贡献，主张用留出判别效用重新定义模态价值。听觉注意解码则发布面向移动对话场景的大规模多模态数据集，把生态效度与多生理通道纳入注意力与聆听努力研究。

共同主题是：诊断与评测协议优先于再堆叠架构；泛化、类人感知与模态效用估计成为下一阶段瓶颈。

## 论文技术总结

# Dr. SHAP-AV: Decoding Relative Modality Contributions via Shapley Attribution in Audio-Visual Speech Recognition

- 论文编号：417
- 报告人：Umberto Cappellazzo
- 程序：Tuesday 29 September 2026 / Audio-Visual and Multimodal Perception
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/cappellazzo26_interspeech.pdf

## 问题
AVSR 在噪声下靠唇动补声学，但干净条件下 ASR 与 AVSR 差距很小，模态消融显示去视频几乎不伤、去音频则崩溃——模型如何平衡音视频、受何因素驱动，缺少跨架构的形式化分析。

## 方法
Dr. SHAP-AV：用 Shapley 值做性能无关的模态归因。三项分析——Global SHAP（整体 A/V 贡献比）、Generative SHAP（解码窗口轨迹）、Temporal Alignment SHAP（输入时段与输出 token 对应）。覆盖六模型（AV-HuBERT、Auto-AVSR、Whisper-Flamingo；Llama-AVSR、Llama-SMoP、Omni-AVSR）与 LRS2/LRS3，扫描干净到 −10 dB 等多 SNR 与噪声类型。

## 实验与结果
主要发现（正文摘要）：噪声下会转向视觉，但 −10 dB 时音频贡献仍达 38–46%；生成过程中部分模型音频依赖上升，AV-HuBERT 更稳；时序对齐在噪声下仍保持；噪声类型影响视觉依赖幅度；句长效应因架构而异；SNR 是主导因素，同 SNR 内识别难度影响小。干净条件模态消融：去视频 WER 接近全 AVSR，去音频则升一至两个数量级；含显式 VSR 多任务训练的模型视觉单模态相对更强。

## 结论
存在持续音频偏置，作者主张把 Shapley 式归因作为 AVSR 诊断常态，并启发显式模态加权机制。

## 点评
把「模型到底听还是看」从消融轶事提升为可公理化的贡献分解，并扩展到 cross-attention 与 LLM 两系。强在多粒度与 SNR 扫描；脆弱点在 Shapley 计算成本与特征联盟定义敏感。全文后半模型细节处有截断，但不影响核心发现复述。


# Assessing True Generalisability of Audio-Visual Speech Recognisers

- 论文编号：2583
- 报告人：Zhaofeng Lin
- 程序：Tuesday 29 September 2026 / Audio-Visual and Multimodal Perception
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/lin26m_interspeech.pdf

## 问题
AVSR 在 LRS3 上已近饱和（干净 WER <1%），但测试集仅约 0.9h，疑似对 LRS3 分布过拟合。WildVSR 等未见集缺音频，无法评 AVSR。需要严格匹配分布的未见评测来检验真泛化。

## 方法
从 MultiVSR 子采样构建 MV2LRS3：在声学、视觉与人口统计七因子（时长、年龄、性别、肤色、头姿、SNR、语速）上对齐 LRS3 test。评五个 SoTA（含 AV-HuBERT、Auto-AVSR、Llama-AVSR 等）；做属性分析、词表内外对比、A/V/AV 三设定与错误类型分析；发布数据与元数据。

## 实验与结果
五模型在 LRS3 上 WER 约 0.77–1.50%，在 MV2LRS3 上崩至约 14.0–23.5%（如 Llama-AVSR 0.77→16.5，Auto-AVSR 0.95→14.0）。扩大匹配集仍稳健。存在词表偏置：限制到 LRS3 共享词汇可相对改善（如 Whisper-Flamingo 至 9.9%，约 47% 相对提升）。多数模型 AV 甚至差于 audio-only；替换/删除/插入模式因模型而异。

## 结论
对齐分布仍崩溃→近完美 LRS3 分数不等于真泛化；词表与模态融合是关键短板。作者释放 MV2LRS3 作未来基准。

## 点评
用「匹配分布的未见集」区分分布漂移与记忆过拟合，比随意 OOD 更有说服力。强在七因子与词表隔离；脆弱点在 Whisper 生成转写可能引入标签噪声，以及 MultiVSR 来源与 TED 风格差异仍可能残留。


# The Lipreading Gap: Do VSR Models Perceive Visual Speech Like Human Lipreaders?

- 论文编号：2498
- 报告人：Rishabh Jain
- 程序：Tuesday 29 September 2026 / Audio-Visual and Multimodal Perception
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/jain26_interspeech.pdf

## 问题
VSR 在 LRS3 等基准上已很强，但高准确率未必等于类人视觉语音感知；模型可能依赖训练语言模式而非构音视觉线索。缺公开人类唇读数据时难以对齐比较。

## 方法
在 MaFI 词级唇读集上对比 Auto-AVSR（S/L）、AV-HuBERT、VSP-LLM 与人类基线；报告词/字/音素/视素指标；用仅给前若干音素的文本 n-gram 作无视觉基线；分析训练词频 vs 视觉信息量（MaFI informativeness）对错误的解释力；视素混淆与清晰度相关。

## 实验与结果
摘要与方法段：模型整体准确率更高，但成功/失败词与人类不同；文本 n-gram 可媲美人类唇读；词级错误更由训练词频解释而非视觉难度；模型在人类最难视素上增益最大，对视觉清晰度依赖远弱于人类。LRS3 上模型 WER 约 20.3–28.6%（Table 1 报告值）。具体 MaFI 表数值以可读段落定性结论为主。

## 结论
当代 VSR 主要靠语言先验，未能把视觉特征稳固绑定为有意义的词；基准高分不等于类人感知。

## 点评
把「像不像人类唇读」操作化为多粒度对齐与无视觉基线，打中过拟合语言模式的痛点。强在 MaFI 视觉信息量维度；脆弱点在词级孤立评测与连续语音训练设定的鸿沟，以及模型未为词级唇读特训。


# The Illusion of Balanced Multimodal Sentiment Analysis: Beyond the Limits of Optimization-Based Methods

- 论文编号：2556
- 报告人：Alexandros Potamianos
- 程序：Tuesday 29 September 2026 / Audio-Visual and Multimodal Perception
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/kaffeza26_interspeech.pdf

## 问题
多模态情感分析常因模态失衡（文本主导）而弱于单模态；社区依赖梯度/损失再加权（OGM、AGM、PMR、ReconBoost 等）试图「平衡」，但可能混淆拟合速度与判别贡献。

## 方法
统一评测框架：在 CMU-MOSI/MOSEI 上用简单 LSTM 晚融合隔离单模态优化动态；对比梯度类与损失类平衡法；诊断「loss≠utility、gradient≠importance」；探索优化器、batch、调制时长与专用校准集。主张转向留出集上的判别式模态效用估计。

## 实验与结果
Late Concatenation 在多数设定不可被可靠超越（如 MOSI A-V 54.93，T-V 74.35；各平衡法常小幅波动或更差）。结果对超参敏感；比例校准亦无稳定增益。训练曲线显示文本损失迅速下降并牵引多模态曲线，音视频损失近乎平坦。

## 结论
优化期再加权测错了信号，无法真正解决模态失衡；应改用基于留出性能的模态效用估计。

## 点评
批判性工作：用受控简单架构暴露「平衡算法」的幻觉，理论类比 1990s AVSR 似然比失败史很有力。强在统一对比；脆弱点在简化融合可能低估复杂注意力融合中再加权的作用，外推需谨慎。


# MOV-AAD: A Large-Scale Multimodal Dataset for Auditory Attention Decoding During Moving Conversations

- 论文编号：3556
- 报告人：Nima Mesgarani
- 程序：Tuesday 29 September 2026 / Audio-Visual and Multimodal Perception
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/he26g_interspeech.pdf

## 问题
多数听觉注意解码（AAD）公开数据偏静态双讲者、缺同步自主神经与行为指标，生态效度不足，难研究动态空间场景下皮层–外周协同。

## 方法
发布 MOV-AAD：50 名正常听力被试；64 导 EEG（1200 Hz）同步眼动、呼吸、GSR、心率、SpO2、体温、加速度、PPG 等。单会话（40 trial）与多会话竞争（56 trial，声源在 ±90° 动态移动、轮流）；HRTF 空间化，背景噪声相对语音 −9/−12 dB RMS；重复词检测作注意行为；另有方位定位任务与预处理（坏导插值等）流程。数据开源。

## 实验与结果
正文给出定位任务：9 方位 −90°–+90°，报告准确率与 MAE（机遇 MAE 约 66.7°）；重复词检测在 SC/MC 上报告准确率/F1，并用 Wilcoxon 等检验。数据集相对 KULeuven、DTU、PhyAAt 等的独特组合见表 1。具体群体数值因篇幅以协议描述为主。

## 结论
MOV-AAD 为真实空间动态下的稳健 AAD、多模态注意与听努力、被试间神经相关提供基准资源。

## 点评
贡献是生态化多模态基础设施，而非新解码算法。强在移动交谈 + 外周生理齐全；脆弱点在实验室 HRTF/固定噪声级与真实鸡尾酒会仍有差距，以及 N=50 对个体差异建模的上限。

