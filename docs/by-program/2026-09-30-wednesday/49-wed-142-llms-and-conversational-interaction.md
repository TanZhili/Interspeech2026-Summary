# LLMs and Conversational Interaction

- 日期：2026年9月30日（周三）
- 时间：16:30-18:30
- 形式：Long Oral
- Area：未标注
- 论文数：6
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。仅依据摘要表述，不补写未给出的实验细节。

## 技术趋势

本场聚焦 LLM 语音助手与多人对话交互：野外阿拉伯语交互数据、口音自适应语音智能体、会议中的受话人/话轮/下一说话人预测、单麦单摄像头多模态话轮投射、全双工轮级文本—语音交错，以及野外主动说话人检测新基准。

共同问题是级联 ASR 错误、口音可用性与信任、以及真实多人场景下的话轮管理。数据与评测资源（WASIL、AV Conversation Corpus、UniTalk）强调野外、未剪辑与跨域泛化，方法上则把置信门控、角色相对状态与动态轮级交错引入系统。

## 技术内容

### 野外交互数据与口音自适应智能体

**WASIL: In-the-Wild Arabic Spoken Interactions with LLMs**（论文 2694；Shammur Absar Chowdhury）  
发布含音频、ASR 假设、助手回复与显式喜欢/不喜欢反馈的野外阿拉伯语交互提示，覆盖 MSA 与四种主要方言及标签；提供多 ASR 一致性引导的低成本金标转写，并标注可答性类别以分离固有不可答与 ASR 诱导退化；同时描述用多裁判 LLM 打分对 ASR vs 金标转写回复做可扩展无参考评估。

**When Machines Speak Like Local Peers: Improving Conversational Experiences with Accent-Adaptive Voice Agents**（论文 2197；Shubhangi S. R. Garnaik）  
LocalMATE 端到端机场口音自适应对话智能体：置信校准口音估计、检索答案、口音条件语音与同步说话人脸视频，不确定时置信门控回退。摘要称口音估计在 L2-ARCTIC 说话人不相交准确率 85%，域外韩式口音 92.3%；N=20 被试内用户研究中正确口音适应显著提升信心与信任（摘要此处截断于 p 值）。

### 多人话轮预测与全双工交错

**Evaluating Large Language Models Abilities for Addressee, Turn-change, and Next Speaker Prediction in Meetings**（论文 2923；Ryo Fukuda）  
在 AMI 上比较监督模型、文本 LLM、多模态 LLM 与人类。摘要称 LLM 在下一说话人预测上优于监督模型与人类（即使无音视频）；MM-LLM 在受话人与话轮变化上优于文本 LLM 但仍低于人类；消融显示对话上下文关键，人类与 LLM 预测模式相似。

**MuVAP: Multimodal Multiparty Voice Activity Projection for Turn-taking Prediction in the wild**（论文 1381；Haotian Qi）  
因果多模态框架用单声道音频与单摄像头人脸轨迹做说话人感知话轮投射；Role-Relative Projection 将任意 N 说话人映射为固定当前/下一持权状态；并发布约 31 小时未剪辑单摄像头多人对话语料。摘要称在两/三人场景的 Shift-Hold 与下一说话人预测上优于强基线。

**TurnGuide: Enhancing Meaningful Full Duplex Spoken Interactions via Dynamic Turn-Level Text-Speech Interleaving**（论文 1141；Wenqian Cui）  
提出轮级文本—语音交错框架，动态切分助手语音并联合生成文本与语音，以利用 LLM 语义能力同时保持声学流畅。摘要称显著改善语义连贯，并在多样话轮事件上达到 SOTA。

**Revisiting Active Speaker Detection: An In-the-Wild Benchmark for Generalization and Robustness**（论文 581；Tuan Khai Nguyen）  
发布强调挑战场景的 UniTalk，覆盖低资源语言、噪声背景与拥挤场景，规模可比 AVA。摘要称 AVA 近饱和的 SOTA 在 UniTalk 上未饱和；在 UniTalk 训练的模型对 Talkies、ASW 等现代野外数据泛化更好。

## 本场要点

- 野外交互数据需同时标注反馈、方言与可答性，以分离 ASR 错误与固有不可答。
- 口音自适应与置信门控可提升公共语音智能体的信任与可用性。
- LLM 在会议下一说话人预测上表现突出，但对原始音视频信号利用仍有限。
- 单麦单摄像头角色相对投射使野外多人话轮预测更可部署。
- 全双工需轮级交错以兼顾语义与时序；ASD 需要新的野外泛化基准。

## 覆盖核对

- 2694 | WASIL: In-the-Wild Arabic Spoken Interactions with LLMs
- 2197 | When Machines Speak Like Local Peers: Improving Conversational Experiences with Accent-Adaptive Voice Agents
- 2923 | Evaluating Large Language Models Abilities for Addressee, Turn-change, and Next Speaker Prediction in Meetings
- 1381 | MuVAP: Multimodal Multiparty Voice Activity Projection for Turn-taking Prediction in the wild
- 1141 | TurnGuide: Enhancing Meaningful Full Duplex Spoken Interactions via Dynamic Turn-Level Text-Speech Interleaving
- 581 | Revisiting Active Speaker Detection: An In-the-Wild Benchmark for Generalization and Robustness
