# Entrainment and Dialogue Coordination

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：11
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program ；https://www.isca-archive.org/interspeech_2026/index.html）。不补写摘要未给出的数字与细节。

## 技术趋势

本场研究对话中的协同与同步：发音协同（articulatory entrainment）、韵律–语义多粒度适配、多方场景下的话轮决策，以及多模态反馈信号。研究从双人自发对话扩展到议会半自发多语、人–数字代理多方互动，以及面对面多模态收敛。

方法上，声学–发音倒置与协调复杂度指标用于自闭与非自闭对话比较；议会语料引入跨语与首因/近因效应分析；多方 AI 助手场景把“每个停顿都开口”重新表述为上下文感知的说/沉默决策，并表明零样本 LLM 不足、需显式监督微调。多模态侧则把收敛视为跨声学、发音与共言语运动的多维现象，并用分类任务区分“表面理解”与真实理解不一致的 backchannel。

共同主题是：协同既是自动过程也受社会动机调节，代理参与会改变全局同步模式，而可靠对话 AI 需要超越简单停顿启发式。

## 技术内容

### 发音协同与议会多语适配

**Articulatory Entrainment and Coordination Complexity in Spontaneous Autistic and Non-autistic Dialogue**（论文 2855；Thanushi Withanage）  
提出说话人无关框架，用声学–发音倒置与协调复杂度量化自发双人对话中的发音协同。非自闭双人随时间协调复杂度与协同增强，自闭双人效应中等，混合双人对齐最弱；更强发音协同与更高自我报告对话成功相关。

**On Entrainment in Semi-Spontaneous Multilingual Parliamentary Speech**（论文 2492；Debasmita Bhattacharya）  
在 Hansard 英法议会半自发场景研究协同，考察此前较少关注的声学–韵律特征及多时间粒度语义方面。摘要称说话人在相互关联的协同维度与跨语设置中按首因与近因效应适配，为规划与启动机制提供新洞见。

### 多方话轮与人–代理协同

**Speak or Stay Silent: Context-Aware Turn-Taking in Multi-Party Dialogue**（论文 3083；Kratika Bhagtani）  
多方场景下把每个检测到的停顿决策为助手应说话或保持沉默。构建超 12 万条标注对话基准；八个近期 LLM 零样本一致失败。提出带推理轨迹的监督微调，平衡准确率最高提升约 23 个百分点，表明上下文感知话轮需显式训练。

**Speech Entrainment in Multi-Party Conversations with a Digital Agent**（论文 2851；Nicholas Mehlman）  
采集成人与家庭（亲子）多方会话中含数字代理的数据，比较知识驱动与模型基协同特征。摘要称个体与其他人局部协同存在，但全局协同及与代理的协同有限且依赖队列。

### 多维收敛与不一致反馈检测

**What happens when we speak together? Multidimensional convergence in face-to-face interaction**（论文 2444；Lena Pagel）  
基于 15 对双人、信息结构受控的交互语音，联合分析声学–韵律、发音与共言语运动参数，强调收敛与韵律突显结构的关系，提供更综合的多模态收敛描述。

**When “yeah” means “not quite”: Multimodal detection of backchannels expressing incomplete understanding**（论文 713；Olcay Türk）  
利用 45 场自然双人交互的声学、头动与话语相关数据，对一致与不一致 backchannel 做分类。不一致反馈通常头动更中性、声学动态更低，话语线索强烈影响分类；摘要称不一致反馈的信号努力相对较低。

## 本场要点

- 发音协同复杂度可区分自闭/非自闭/混合双人对话，并关联主观成功感。
- 议会半自发多语场景体现跨维度、跨语的首因/近因适配。
- 多方助手话轮需显式训练，非 LLM 涌现能力。
- 数字代理参与下全局与对代理协同有限且队列依赖。
- 面对面收敛应作为多模态、与韵律突显关联的现象研究。
- 多模态特征可分离“假装听懂”的不一致 backchannel。

## 覆盖核对

| id | title |
|---|---|
| 2855 | Articulatory Entrainment and Coordination Complexity in Spontaneous Autistic and Non-autistic Dialogue |
| 2492 | On Entrainment in Semi-Spontaneous Multilingual Parliamentary Speech |
| 3083 | Speak or Stay Silent: Context-Aware Turn-Taking in Multi-Party Dialogue |
| 2851 | Speech Entrainment in Multi-Party Conversations with a Digital Agent |
| 2444 | What happens when we speak together? Multidimensional convergence in face-to-face interaction |
| 713 | When “yeah” means “not quite”: Multimodal detection of backchannels expressing incomplete understanding |
