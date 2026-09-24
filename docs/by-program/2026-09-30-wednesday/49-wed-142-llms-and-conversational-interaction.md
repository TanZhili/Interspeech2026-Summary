# LLMs and Conversational Interaction

- 日期：Wednesday 30 September 2026
- 时间：16:30-18:30
- 形式：Long Oral
- Area：
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场聚焦 LLM 语音助手与多人对话交互：野外阿拉伯语交互数据、口音自适应语音智能体、会议中的受话人/话轮/下一说话人预测、单麦单摄像头多模态话轮投射、全双工轮级文本—语音交错，以及野外主动说话人检测新基准。

共同问题是级联 ASR 错误、口音可用性与信任、以及真实多人场景下的话轮管理。数据与评测资源（WASIL、AV Conversation Corpus、UniTalk）强调野外、未剪辑与跨域泛化，方法上则把置信门控、角色相对状态与动态轮级交错引入系统。

## 论文技术总结

# WASIL: In-the-Wild Arabic Spoken Interactions with LLMs

- 论文编号：2694
- 报告人：Shammur Absar Chowdhury
- 程序：Wednesday 30 September 2026 / LLMs and Conversational Interaction
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ali26c_interspeech.pdf

## 问题
阿拉伯语语音助手多为 ASR→LLM 级联；用户 dislike 可能来自 ASR 错误、固有不可答、或 LLM 本身，难拆开。缺含音频、转写、回复与显式反馈的野生方言数据。

## 方法
发布 WASIL：收集 9,304 条野生阿拉伯语口语提示（MSA + 方言）；用户 like/dislike 与多标签失败原因。2,573 条金标转写（人工后编辑，按国家匹配标注者），其中 1,777 为测试集；标注方言与可答性（可答/模糊需澄清/不支持/非请求噪声）。用多法官 LLM 对 ASR vs 金标转写下的回复做无参考评分。

## 实验与结果
数据集与标注流程是核心贡献；分析将固有不可答与 ASR 诱发劣化分开，并关联 dislike 与失败类别（指令遵循、事实、风格、文化/宗教等）。公开测试集于 Hugging Face。

## 结论
WASIL 为阿拉伯语语音–LLM 交互提供可拆分误差源的野生评测资源，支持下游导向 ASR 评估与方言覆盖分析。

## 点评
把“用户反馈 + 可答性 + 金标音频”绑在一起，正好打中级联助手评测的混杂因果。方言覆盖与文化/宗教失败标签对阿拉伯语境特别关键。金标子集相对全量仍有限；多法官 LLM 评分需防评判器偏置。


# When Machines Speak Like Local Peers: Improving Conversational Experiences with Accent-Adaptive Voice Agents

- 论文编号：2197
- 报告人：Shubhangi S. R. Garnaik
- 程序：Wednesday 30 September 2026 / LLMs and Conversational Interaction
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/garnaik26_interspeech.pdf

## 问题
公共场景语音助手对口音英语用户表现不均，损害可用性与信任。口音自适应回复（尤其带说话人脸视频）应如何安全部署仍缺系统证据。

## 方法
LocalMATE 机场场景端到端代理：WavLM 口音估计（印度/韩/西）+ 置信缓存；Whisper ASR；FAQ 嵌入检索；VEVO 口音条件 TTS + 同步说话人脸；低置信时置信门控回退。口音分类说话人独立评测；N=20 被试内用户研究比较正确/错误适配与回退策略。

## 实验与结果
口音估计：L2-ARCTIC 说话人独立准确率 85%；域外韩式 Speech Accent Archive 92.3%。用户研究：正确口音适配显著提高信心与信任、减少修复尝试（p<0.05）；错误适配降低信任并增加摩擦；置信门控回退可缓解并恢复信心。

## 结论
口音自适应能提升体验，但错误适配有害；置信门控是必要安全阀。

## 点评
把“适配收益”与“误适配成本”放在同一用户研究里，结论对部署很务实。场景限于 FAQ 机场助手与三种口音；信任指标自报、样本 N=20。TTS 口音迁移质量仍是体验瓶颈。


# Evaluating Large Language Models Abilities for Addressee, Turn-change, and Next Speaker Prediction in Meetings

- 论文编号：2923
- 报告人：Ryo Fukuda
- 程序：Wednesday 30 September 2026 / LLMs and Conversational Interaction
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/fukuda26b_interspeech.pdf

## 问题
多方会议轮次比双人更复杂：需推断受话人、是否换轮、下一位说话人。LLM/多模态 LLM 在这些任务上相对监督模型与人类的能力边界不清。

## 方法
在 AMI 上统一评测三任务：受话人检测、轮次变化（Shift/Hold）、下一说话人预测。对比监督基线、文本 LLM（Qwen3 等）、MM-LLM 与人类；输入含转写/音频/视频与会话上下文；另测 ASR 转写与 FOA 模块化设定。

## 实验与结果
LLM 在下一说话人预测上优于监督模型与人类，即使无音视频、未在目标域训练。MM-LLM 在受话人与换轮上优于纯文本 LLM，但仍低于人类，显示难有效利用原始视听信号。消融表明会话上下文尤其对下一说话人关键。人类与 LLM 错误模式相似，频繁换轮区间双方都难。

## 结论
文本上下文已携带强轮次线索；多模态 LLM 尚不能充分兑现原始音视频收益。框架为会议助手轮次理解提供统一基准。

## 点评
把人类表现纳入对比是稀缺且有价值的锚。下一说话人上 LLM 超人类，可能受益于完整转写上下文与允许多候选设定。近讲话筒泄漏（约 8.5%）可能泄漏下一说话人线索；AMI 角色会议外推到开放多方场景需谨慎。


# MuVAP: Multimodal Multiparty Voice Activity Projection for Turn-taking Prediction in the wild

- 论文编号：1381
- 报告人：Haotian Qi
- 程序：Wednesday 30 September 2026 / LLMs and Conversational Interaction
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/qi26_interspeech.pdf

## 问题
多方轮次模型常依赖复杂麦阵/多相机，难用于人机交互。现有视听语料多有剪辑切口，破坏因果跟踪；需在单麦+单相机下做说话人感知的未来语音活动预测。

## 方法
MuVAP：将 Voice Activity Projection 与人脸轨迹/主动说话人检测融合；Role-Relative Projection 把任意 N 人映射为固定的“当前 vs 下一持有者”状态。发布 Audio-Visual Conversation Corpus（约 31h 未剪辑单相机多方对话）。因果设定评测 Shift-Hold 与下一说话人，覆盖双人与三人场景。

## 实验与结果
在 Shift-Hold 与下一说话人任务上优于强基线；相对编辑过的语料，未剪辑数据更适合因果跟踪与野生部署评测。

## 结论
单通道音频 + 单视角视频即可做多方说话人感知轮次预测；角色相对投影缓解组合爆炸。新语料支撑野生视听轮次研究。

## 点评
把 VAP 从双人声学推广到“人脸锚定的多方”，部署约束更现实。Role-Relative 简化状态空间是实用工程选择，但可能损失更细的多人竞争结构。性能数字正文表格较多，结论依赖作者报告的相对优势；相机视角与人脸跟踪失败是现场脆弱点。


# TurnGuide: Enhancing Meaningful Full Duplex Spoken Interactions via Dynamic Turn-Level Text-Speech Interleaving

- 论文编号：1141
- 报告人：Wenqian Cui
- 程序：Wednesday 30 September 2026 / LLMs and Conversational Interaction
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/cui26_interspeech.pdf

## 问题
端到端全双工语音语言模型（FD-SLM）能学打断/重叠等自然轮次，但相对文本 LLM 语义能力下降；在双通道连续音频中插入离散文本易破坏时序对齐与交互流畅性。

## 方法
TurnGuide：动态按轮切分助手语音，在轮级联合生成文本与语音，用文本引导语义同时保持声学流。基于 GLM-4-Voice 在 Fisher 上训练；对比 dGSLM、STI/SCI、Moshi 及 Moshi-style 训练变体；GPT-4o 语义评分（无条件/条件生成，多温度）。

## 实验与结果
TurnGuide 语义分显著高于基线（Overall 约 7.27–7.79，视变体；Moshi TS 约 5.58，SCI 约 5.91）。L2:1/L3:1 损失加权变体进一步提升；作者称在多样轮次事件上达 SOTA。金标文本引导亦强，但提出方法在多项设定上更好或接近。

## 结论
轮级而非帧级文本–语音交错，可把 LLM 语义迁入全双工语音交互而不严重破坏时间对齐。

## 点评
把“文本引导”下沉到轮边界，抓住了全双工对齐痛点。评测偏 GPT 语义分与 Fisher 续写，对真实打断延迟/重叠自然度覆盖有限；多数竞品未完全开源，对比面受约束。9B 级训练成本与延迟是部署考量。


# Revisiting Active Speaker Detection: An In-the-Wild Benchmark for Generalization and Robustness

- 论文编号：581
- 报告人：Tuan Khai Nguyen
- 程序：Wednesday 30 September 2026 / LLMs and Conversational Interaction
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/nguyen26b_interspeech.pdf

## 问题
ASD 基准 AVA 几乎全来自老电影，SOTA 近饱和（mAP>95%）易让人误以为任务已解决；真实场景含少见语言、噪声、拥挤与复杂镜头，泛化不清。

## 方法
提出 UniTalk：规模可比 AVA、覆盖多样野生视频与难度子类（语言/噪声/视觉复杂度）。评测现有 SOTA 在 AVA vs UniTalk，以及 UniTalk 训练后向 AVA、Talkies、ASW 的跨域泛化与少样本适应。

## 实验与结果
AVA 近完美模型在 UniTalk 最强仅约 83.2 mAP，Hard 子集约 77.9。UniTalk 训练模型跨域更好：AVA/Talkies/ASW 约 88.0/91.4/90.4 mAP。预训练后快速适应可达约 92.4 mAP，接近全数据。

## 结论
ASD 在真实条件下仍未饱和；UniTalk 提供更现实的稳健性与泛化基准。

## 点评
用“电影饱和 ≠ 野生解决”直接打醒领域，Hard 子集设计有诊断价值。跨域数字显示数据域比架构口号更决定表现。标注噪声与类别定义细节会影响绝对 mAP；与 AVA 协议对齐仍是公平对比关键。

