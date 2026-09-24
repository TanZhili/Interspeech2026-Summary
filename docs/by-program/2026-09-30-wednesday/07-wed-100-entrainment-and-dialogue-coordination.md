# Entrainment and Dialogue Coordination

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：11
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场研究对话中的协同与同步：发音协同（articulatory entrainment）、韵律–语义多粒度适配、多方场景下的话轮决策，以及多模态反馈信号。研究从双人自发对话扩展到议会半自发多语、人–数字代理多方互动，以及面对面多模态收敛。

方法上，声学–发音倒置与协调复杂度指标用于自闭与非自闭对话比较；议会语料引入跨语与首因/近因效应分析；多方 AI 助手场景把“每个停顿都开口”重新表述为上下文感知的说/沉默决策，并表明零样本 LLM 不足、需显式监督微调。多模态侧则把收敛视为跨声学、发音与共言语运动的多维现象，并用分类任务区分“表面理解”与真实理解不一致的 backchannel。

共同主题是：协同既是自动过程也受社会动机调节，代理参与会改变全局同步模式，而可靠对话 AI 需要超越简单停顿启发式。

## 论文技术总结

# Articulatory Entrainment and Coordination Complexity in Spontaneous Autistic and Non-autistic Dialogue

- 论文编号：2855
- 报告人：Thanushi Withanage
- 程序：Wednesday 30 September 2026 / Entrainment and Dialogue Coordination
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/withanage26_interspeech.pdf

## 问题
自发对话中发音器官协同的 entrainment 研究不足，自闭与混合神经类型互动尤然；既往多依赖侵入式测量或任务型/音素级范式，难反映自然对话。

## 方法
用声学–发音反演得到六维声道变量（唇开度/前伸、舌尖/舌体收缩度与位置），建 ACF 矩阵并取 90 维特征谱；以几何衰减加权和 ω 刻画协同复杂度。将对话分半，用带符号的距离变化度量双向 entrainment `e`。数据：CANDOR 中 1381 对非自闭–非自闭 Zoom 对话；UTD 子集含 AT–AT、AT–NA、NA–NA 面对面短对话。

## 实验与结果
CANDOR 上 NA–NA 的 ω 随时间显著下降（半程、四分程 ANOVA），显示协同复杂度上升，且早期变化最大；正向 entrainment（e>0）与更高自我报告会话成功相关。UTD：NA–NA entrainment 最强，混合 dyad 最低，AT–AT 介于其间；混合组后期更趋简单协同，作者解释为澄清努力。

## 结论
声道变量特征谱可无创、说话人无关地量化自发对话中的发音 entrainment；同神经类型 dyad 更易协同变复杂并对齐，混合类型对齐最弱。

## 点评
把 Lindblom 式“舒适→协同更复杂”与双共情框架接到可复现的特征谱距离上，解释性强。脆弱点在 UTD 样本量与时长有限、CANDOR 排除高 AQ 特质后难直接推广到临床自闭群体，且依赖反演与 diarization 质量。


# On Entrainment in Semi-Spontaneous Multilingual Parliamentary Speech

- 论文编号：2492
- 报告人：Debasmita Bhattacharya
- 程序：Wednesday 30 September 2026 / Entrainment and Dialogue Coordination
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/ries26_interspeech.pdf

## 问题
既有 entrainment 研究多限单语、固定自发度对话；半自发（准备独白+即兴提问）且跨语场景中，说话人如何在声学–韵律与语义上适应对方仍不清楚。

## 方法
在加拿大 Hansard 英法议会子集上，采样 40 段准备独白（10–20 分钟）+ 即兴提问（1–2 分钟），语言设置为 en-en/fr-fr/en-fr/fr-en。提取 eGeMAPSv02 声学–韵律特征与 RemBERT 语义嵌入，用余弦相似度相对随机配对零基线测全局与分段（独白初/中/末）entrainment；并用混合效应模型与特征消融解释贡献。

## 实验与结果
57.5% 交换呈显著声学–韵律 entrainment，语义更弱（17.5%）。时间上对独白开头与结尾对齐更强（首因/近因），约 82.5%/67.5% 交换可见。跨语交换中“初段语义对齐”显著正向预测“末段声学–韵律对齐”；单语则呈弱权衡。少数特征主导（F0、英语侧 MFCC、法语侧响度、政策类语义维），消融可大幅削弱全局 entrainment，跨语尤甚。

## 结论
半自发多语议会对话仍普遍存在多维 entrainment，并呈现首因/近因与跨语特有的语义→声学两阶段规划迹象。

## 点评
把记忆效应与跨语认知负荷接到可检验的分段相似度上，填补议会语料空白。样本仅 40 段交换、部分相关未达显著，外推需谨慎；排除语码混用与特权头衔后生态效度有所收窄。


# Speak or Stay Silent: Context-Aware Turn-Taking in Multi-Party Dialogue

- 论文编号：3083
- 报告人：Kratika Bhagtani
- 程序：Wednesday 30 September 2026 / Entrainment and Dialogue Coordination
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/bhagtani26_interspeech.pdf

## 问题
多人场景中暂停含义模糊，现有语音助手常把每次停顿都当发言邀请而打断；二元对话式 turn-taking 与仅做下一说话人预测，都未解决助手在每处暂停“说还是沉默”的上下文决策。

## 方法
把任务定义为：给定完整上下文与目标说话人，在每处暂停二分预测 SPEAK/SILENT。从 AMI、Friends、SPGI 构建约 12 万标注决策点，细分为显式称呼(I1)、语境介入(I2)、无指称沉默(S1)、被提及但非称呼(S2)。评估 8 个 LLM 零样本；再用 LoRA SFT，并可选蒸馏教师生成的一句推理痕迹。

## 实验与结果
零样本普遍接近随机或强 SPEAK 偏置（最佳约 BalAcc 64%）。SFT 可提升最多约 23 个百分点（如 Mistral-7B on AMI：BalAcc 48.93→72.28）；增益主要来自需保持沉默的 S1/S2。加推理痕迹再提约 7 Acc 点。人类在 Friends 子集 BalAcc 约 60–66%，模型可持平或略优。合并三域训练仍具跨域迁移。

## 结论
上下文感知 turn-taking 非 LLM 涌现能力，需显式监督（尤其是沉默类）；推理蒸馏有助于语用判断。

## 点评
问题定义贴近真实多人助手痛点，四类标签把“被提到≠被叫到”拆开很关键。当前仅文本转录、无声学/视觉线索，且标签由下一说话人启发式派生，对脚本剧与会议语体的生态效度需再验证。


# Speech Entrainment in Multi-Party Conversations with a Digital Agent

- 论文编号：2851
- 报告人：Nicholas Mehlman
- 程序：Wednesday 30 September 2026 / Entrainment and Dialogue Coordination
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/mehlman26_interspeech.pdf

## 问题
既有 entrainment 多研究人人二元对话；多人组与数字代理同场时，人类彼此及对人–机之间在局部/全局时间尺度上如何对齐仍不清楚，儿童–成人群体差异亦未知。

## 方法
采集成人组（30 场）与家庭组（10 场，儿童 8–14 岁）与 WoZ 数字代理（外星角色提问）的多人会话。用手工特征（幅度、PESTO 音高、VoxProfile 情绪）与 Whisper/Mimi/情绪嵌入测参与者–参与者(P2P)与参与者–代理(P2A)相似度。混合效应回归比较同轮 vs 跨轮（局部）及前 5 轮 vs 后 5 轮（全局）。

## 实验与结果
成人 P2P 局部 entrainment 几乎覆盖幅度、音高、情绪与嵌入；家庭 P2P/C2G 主要在情绪与嵌入，幅度/音高不显著。两组均无显著局部 P2A。全局：成人仅弱音高/Mimi 效应；家庭无显著 P2P 全局；儿童–代理在 Whisper 嵌入上全局收敛，但幅度发散（儿童音量随会话上升）。

## 结论
多人场景中人类间局部对齐强，对人–机局部对齐弱；与代理的收敛有限且依赖年龄/时间尺度，儿童更可能在语义表征上逐渐贴近代理。

## 点评
把数字代理嵌入真实多人场并分成人/家庭队列，填补人–机多党 entrainment 空白。局限是家庭场次少、代理固定访谈角色、会话前已有共处时间可能压低全局效应，嵌入可解释性有限。


# What happens when we speak together? Multidimensional convergence in face-to-face interaction

- 论文编号：2444
- 报告人：Lena Pagel
- 程序：Wednesday 30 September 2026 / Entrainment and Dialogue Coordination
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/pagel26_interspeech.pdf

## 问题
既有收敛研究常孤立看单一参数，且少控制信息结构，易把说话人内部的韵律突显变化误当成说话人间收敛；发音与伴随手势/头部运动的多维关系亦不清。

## 方法
15 对陌生德语说话人，在 DiCE 卡牌任务中先 solo 后对话；目标词受纠正焦点控制。用 EMA+麦克风同步采集，分析四参数：词时长、目标窗 F0 幅度、舌体垂直位移、头部最大切向速度。贝叶斯层级模型比较 solo→dialogue 的说话人间距离变化，并以伪 dyad 检验是否为真正的对方特异适应。仅纠正焦点 token 进入收敛分析。

## 实验与结果
时长在 9/15 dyad、F0 在 8/15、头部速度在 4/15、舌位移在 2/15 显示可信收敛（P≥0.90）；伪 dyad 分布居中于零。舌/头收敛常伴随时长或 F0，后两者可单独出现。作者以感知显著性、灵活性与暴露度解释参数易感性差异。

## 结论
面对面互动中收敛是多维且选择性的：声学–韵律线索最易对齐，伴随动作次之，舌体运动最弱；且反映对方特异适应而非模式切换伪影。

## 点评
信息结构控制 + 伪 dyad 对照使“收敛 vs 突显”可分离，多模态剖面结论扎实。任务高度脚本化、仅德语年轻成人，外推到自然闲聊需谨慎；舌位移仅分析部分目标词。


# When “yeah” means “not quite”: Multimodal detection of backchannels expressing incomplete understanding

- 论文编号：713
- 报告人：Olcay Türk
- 程序：Wednesday 30 September 2026 / Entrainment and Dialogue Coordination
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/turk26_interspeech.pdf

## 问题
表面肯定性反馈（如“mhm”+点头）未必反映真实理解；这种“不一致 backchannel”会误导 grounding，但其声学、头部与话语结构线索是否可系统区分尚不清楚。

## 方法
基于 MUNDEX 桌游讲解语料中 45 段德语互动：EE 事后 video-recall 自标理解水平，将表面肯定反馈标为 congruent（675）或 incongruent（809）。提取声学、头部运动（俯仰/滚转加速度等）与话语特征（话题时长、距既往提及距离等），用嵌套交叉验证的 XGBoost 分类并用 SHAP 解释。

## 实验与结果
CV：Average Precision 0.73、ROC-AUC 0.71、F1≈0.68；保留验证集准确率 0.73。SHAP 显示平均头俯仰角最重要（不一致时更中性直立）；话题时长与距既往提及次之；声学动态性偏低亦关联不一致。短而久未提及的话题、或新引入的长密话题更易预测为不一致。

## 结论
不一致与一致 backchannel 可由多模态特征系统分离；不一致反馈往往伴随更低信号努力（中性头姿、较低声学动态）。

## 点评
用 video-recall 锚定主观理解状态，把“假懂反馈”做成可学标签，对解释性对话系统有直接价值。局限是仅正面词汇反馈、德语桌游场景、单标注者理解归类，以及分类目标偏特征诊断而非实时检测。

