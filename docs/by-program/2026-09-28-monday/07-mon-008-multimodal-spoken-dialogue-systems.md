# Multimodal Spoken Dialogue Systems

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
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

本场多模态口语对话系统覆盖会话情感识别、机器人在线动作生成、音视频问答、自我中心“是否在对我说话”，以及 Speech LLM 与文本 LLM 的能力对齐。情感侧从不确定度感知融合（EmoEUS）到图结构多模态融合与情绪惯性/传染 GNN（MF-EDM），强调冲突线索、噪声与缺失模态下的动态加权，以及说话人内持久与跨说话人交互。

交互与具身场景要求流式处理：Plan and Double-Check 把 Q-Former 动作生成扩展到短时块音视频特征与左上下文 query，并增量生成动作与确认消息；VividAC 用视觉智能体生成查询相关视频描述，再引导听觉智能体产出视觉情境化音频描述，免音视频联合训练即可提升 AVQA。Ego4D TTM 工作则联合说话人感知对话上下文与 Looking-at-Me 视觉骨干。

系统层，X-OPD 以跨模态 on-policy 蒸馏让 Speech LLM 在自身分布上 rollout，由文本教师给 token 级反馈，缩小相对文本模型的能力落差。瓶颈包括模态不确定度、情绪动态、流式延迟、朴素音频描述损害 AVQA，以及 E2E Speech LLM 相对级联/文本模型的性能缺口。

## 论文技术总结

# EmoEUS: Uncertainty Supervision for Multimodal Emotion Recognition in Conversation

- 论文编号：1996
- 报告人：Zilong Huang
- 程序：Monday 28 September 2026 / Multimodal Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/huang26n_interspeech.pdf

## 问题
多模态对话情感识别（MERC）常用 Transformer 融合，但往往默认各模态在所有话语上同等可靠，忽视噪声、缺失与冲突线索带来的模态不确定。已有不确定性建模多靠分类损失隐式学习，缺少对方差的显式监督与自适应加权。

## 方法
EmoEUS 含三块：
1. **ContextDEM**：模态特征经 Bi-GRU 后，用 Transformer + 残差与双 MLP 输出高斯均值 \(\mu\) 与方差 \(\sigma\)；
2. **UAMF**：按相对方差算模态置信度并 softmax，置信加权 \(\mu\) 后做多头注意力与 Transformer 融合，残差接回拼接均值；
3. **ESL**：按情感×模态维护分布簇中心（均值+方差，每 epoch 更新、不反传），用 2-Wasserstein 距离度量话语分布与簇中心偏差，监督预测方差与 \(\sqrt{D_{2W}}\) 对齐；总损失 \(L_{\mathrm{CE}}+\kappa\sum L_{\mathrm{ESL}}\)，\(\kappa\) 在 \(ep_{\mathrm{start}}\) 后打开。
特征：RoBERTa（文本）、Wav2vec2.0（音频）、CLIP（视觉）。

## 实验与结果
IEMOCAP（LOSO）与 MELD（官方划分），指标 Acc / w-F1。
- EmoEUS：IEMOCAP Acc 74.33、w-F1 74.36；MELD Acc 68.32、w-F1 67.53，整体优于所列基线（如 FEMI、CFN-ESA 等）。
- 消融：去掉 ESL 或 UAMF 均下降；相对 Concat/Attention/Transformer 融合亦更优。
- 模糊情感对误分率下降；分布表示 + 2W 优于点估计 + MSE；残差连接有益。

## 结论
显式不确定性监督使模型按话语自适应抑高不确定模态、强化可靠模态，在两基准上达文中报告的 SOTA，并改善易混情感对。未来计划加强跨说话人实时动态下的不确定性估计。

## 点评
关键是把“方差”从隐式正则拉成可监督信号，并用 Wasserstein 对齐情感簇，使融合权重有可解释的可靠性依据。强在组件消融完整、融合与监督耦合清晰；脆弱在簇中心依赖标签与 epoch 统计、ESL 权重调度敏感，以及 Sad/Angry 等个别类上仍可能不及部分基线——整体提升不保证每类最优。


# MF-EDM: Graph-based Multimodal Fusion and Emotional Dynamics Modeling for Emotion Recognition in Conversation

- 论文编号：1875
- 报告人：Sooyeon Hwang
- 程序：Monday 28 September 2026 / Multimodal Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/hwang26_interspeech.pdf

## 问题
多模态 ERC 面临两类难题：（1）early/late/图融合各有模态对齐与交互不足；（2）对话中情感随时间在说话人内持续（inertia）与说话人间传染（contagion），既有图方法常未显式拆分这两种动态。

## 方法
两阶段 MF-EDM：
**Stage 1 Intra-Utterance Graph**：文本 Bi-GRU、声学/视觉 MLP 得单模态节点；early fusion 得多模态锚点节点；单模态间无向多边 + 指向锚点的有向边，在图内做结构化跨模态聚合，并加说话人嵌入。
**Stage 2**：
- **EIGNN**：同说话人过去/未来窗口有向时序边，GCN+残差，建模情感惯性；
- **ECGNN**：窗口内跨说话人无向边 + 多频滤波（低频收敛、高频发散/互补），建模传染。
分类：拼接两路锚点特征后前馈 + 交叉熵与 L2。

## 实验与结果
四语基准（同设定复现基线）：IEMOCAP、MELD、K-MIND、M3ED；指标 w-F1 / Acc。
- MF-EDM：IEMOCAP 74.24 / 74.49；MELD 67.40 / 68.77；K-MIND 74.48 / 77.24；M3ED 55.05 / 56.15，均优于 MMGCN、MM-DFN、M3Net、GraphSmile。
- Stage 1：Intra-Utterance Graph 优于 Early / Late / 无锚点 Graph-based 变体。
- Stage 2：Inertia 子集上 EIGNN 更强，Contagion 子集上 ECGNN 更强；全量上两路互补，去掉任一通常下降。

## 结论
锚点引导的句内图融合 + 心理启发的惯性/传染双通路，在英/韩/普通话等多语对话上取得文中报告的 SOTA。边界：构图依赖说话人标签；未来可考虑自动说话人归属与自适应通路门控。

## 点评
设计把“融合结构”和“谁影响谁的时序边”拆开，并用子集消融验证心理学对应关系，比单一上下文 GNN 更可解释。强在多语复现与融合变体对照完整；脆弱在窗口超参按数据集调、Inertia 子集上 EIGNN-only 有时反超全模型，说明盲目跨说话人传消息可能冲淡说话人连续性。


# Plan and Double-Check: Streaming Multimodal Q-Former for Online Robot Action Generation

- 论文编号：2999
- 报告人：Chiori Hori
- 程序：Monday 28 September 2026 / Multimodal Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/hori26_interspeech.pdf

## 问题
基于演示视频的机器人动作规划与确认生成多依赖离线、预切分片段；真实交互需对未切分音视频流式处理。直接流式化易引入延迟与对齐困难，且缺少合适的人–机器人对话级时序标注。

## 方法
将 AVBLIP（音频–视觉 Q-Former + 冻结 OPT-2.7B）扩展为流式：
- 按约 1 秒 chunk 提取 Omnivore/CLIP/AST 特征并交错送入 Q-Former；查询嵌入可 attend 历史 chunk（左上下文），不看未来；
- LLM 对当前 chunk 自回归生成：输出 \(\langle S\rangle\) 及后续 token，或 \(\langle /S\rangle\) 表示本 chunk 无输出；
- 训练用注意力掩码实现并行：因果自注意力、chunk 级 cross-attention、流式 LLM 的 chunk 自注意力；
- 对齐策略对比：固定 clip 末、采样提前响应时刻、基于 CE loss 的 loss-based 选择（采样损失相对末 chunk 损失足够小时采用采样对齐）。
在线用 greedy 解码。未使用字幕（在线难以获得）。

## 实验与结果
YouCook2，验证集对半交叉验证。动作微步短语集来自既有标注。
- 离线基线 action BLEU-2 / METEOR：0.357 / 0.251；流式模型作离线使用时性能接近。
- 在线流式（loss-based）：平均延迟约 −2.92±2.20 s（相对 clip 结束提前），漏检率 4.40%；action BLEU-2 / METEOR 0.328 / 0.228，description 0.212 / 0.145；相对基线质量下降但文中称各序列指标相对降幅 <10%。
- loss-based 优于 clip-end 与单纯 sampling（延迟波动更小、指标更好）。

## 结论
通过 chunk 化 Q-Former、左上下文掩码与响应时刻对齐，可在接近离线并行训练效率下实现低延迟流式动作序列与确认句生成；loss-based 对齐优于其它对齐策略。准确率相对离线有可接受损失。

## 点评
把流式 ASR 的 chunk/interleave 思路迁到 Q-Former–LLM 动作规划，并用掩码保住并行训练，工程路径清晰。强在显式生成确认句以支持执行前人工复核；脆弱在依赖启发式对齐阈值、greedy 相对 beam 已有损失、且未接入流式 ASR 字幕——复杂厨房场景下漏检与错时触发仍是主要风险。


# VividAC: Visually Informed and Visually Interacted Audio Captioning for Enhancing Audio-Visual Question Answering

- 论文编号：3442
- 报告人：Mingi Kim
- 程序：Monday 28 September 2026 / Multimodal Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/kim26y_interspeech.pdf

## 问题
AVQA 中希望用文本 caption 撬动 LLM 推理，但朴素音频 caption 常与视觉场景不一致、缺少问题相关细节，甚至相对“仅视频”基线掉点。端到端 AV-LLM 联合训练成本高，跨模态证据对齐仍困难。

## 方法
VividAC：训练免费的级联智能体通信。
1. **Visual Agent（VLM）**：根据视频与问题名词短语生成 query-relevant 视频描述 \(C_v\)；
2. **过滤**：从 \(C_v\) 抽名词，用 CLIP 与问题名词相似度筛保留（阈值 \(\tau=0.8\)），得关键词；
3. **Audial Agent（ALM）**：在音频、\(C_v\) 与关键词提示下生成视觉语境化音频 caption \(C_a\)；
4. **推理 LLM**：综合视频描述、音频 caption 与问题作答。
方向固定为 Vision→Audio；全程自然语言接口，无音视频联合训练。

## 实验与结果
MUSIC-AVQA 官方测试（9192 QA / 6399 样本）；答案归一化后关键词包含判定准确率。
- 12 组 LLM–VLM 组合中 11 组相对 Naive 提升，最高约 +11.01%p（Llama-3.1 + Qwen2.5-3B）；唯一下降为 Llama-3.1 + InternVL2.5（Overall −0.63%p，但 A-Avg 仍 +2.37%p）。
- VividAC + Qwen2.5 达 Overall 59.91%，相对最强端到端 Video-SALMONN 52.91% 高 7.0%p。
- 方向消融：V→A 优于 No Interaction 与 A→V；给既有 AV-LLM 附加 VividAC caption 亦优于朴素 caption。

## 结论
结构化跨模态自然语言对话可在无需联合训练下显著提升零样本 AVQA；改进主要来自智能体交互而非特定模型配对。作者视其为对端到端路线的互补路径。

## 点评
抓住“音频 caption 必须被视觉与问题锚定”这一瓶颈，用轻量 CLIP 过滤缓解级联误差传播，实用性强。强在组合泛化与相对 AV-LLM 的零训练优势；脆弱在级联仍可能传错实体、依赖 caption 质量与 \(\tau\)，且评测为字符串关键词匹配——对开放式表述可能高估/低估真实语义正确性。


# Who is Talking to Me? Addressing Egocentric TTM with Speaker-aware Conversational Context

- 论文编号：2358
- 报告人：Fukun Chen
- 程序：Monday 28 September 2026 / Multimodal Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/chen26x_interspeech.pdf

## 问题
第一人称 Talking-to-Me（TTM）要判断说话人是否在对相机佩戴者说话。现有音视频融合缺长程对话历史；多任务方法未显式建模说话人角色；SICNet 等上下文方法身份表征粗、时间窗短。真实场景中交互伙伴常出镜外或移开视线，视觉线索缺失。

## 方法
多模态对话上下文框架，三模块：
1. **SSE**：Whisper 转写 + RoBERTa 话语特征；CAM++ 聚类做说话人日记化（佩戴者 ID 固定为 0）；可学习说话人 ID 与对话轮次嵌入与文本拼接投影；
2. **CCM**：当前及前 \(T-1\) 句的 SSE 特征入记忆库，经多层 utterance Transformer 自注意力建模多轮语义依赖；
3. **GVE**：冻结 LAM（Looking-at-Me）骨干提帧级注视相关视觉特征，时序池化后投影；
文本–视觉两 token 自注意力融合（取文本侧输出 + 残差）后 MLP 分类。Whisper/CAM++/LAM 冻结，微调 RoBERTa 部分层与下游模块。

## 实验与结果
Ego4D Social Interaction TTM：训练 389 clips / 验证 50 clips；验证集 2469 样本；指标 mAP（测试集不公开，报验证）。
- 全文模型 **72.40% mAP**，相对 SICNet 68.98 提升 3.42 点，优于 Ego4D-TTM、TalkNet、EgoT2 等。
- 消融：Baseline 66.52；去 CCM 68.01；去 GVE 70.80；去 SSE 69.84。
- 上下文长度：\(T=1\) 为 68.34，\(T=3\) 升至 70.89，约 \(T=10\) 达 72.29 后饱和；推理约 31.4 FPS。

## 结论
显式说话人感知语义依赖与 LAM 注视视觉线索联合，在 Ego4D TTM 上显著优于既有基线。失败多见于缺脸与语义模糊（如低头自语）。未来拟引入更大规模多模态 LLM。

## 点评
做法把“谁在对谁说话”拆成日记化身份 + 多轮文本上下文 + 注视先验，对出镜外场景用语义补视觉缺口，设计贴合自我中心社交。强在模块消融与上下文长度曲线清楚；脆弱点在依赖上游 Whisper/日记化质量，以及 LAM 在缺脸时失效——作者亦承认此类场景仍易误判。


# X-OPD: Cross-Modal On-Policy Distillation for Capability Alignment in Speech LLMs

- 论文编号：861
- 报告人：Di Cao
- 程序：Monday 28 September 2026 / Multimodal Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/cao26_interspeech.pdf

## 问题
端到端 Speech LLM 相对同系文本 LLM 在复杂指令、推理与知识任务上明显掉点；标准 SFT+RL 与离线蒸馏难弥合模态差距，且常有暴露偏差与灾难性遗忘。工业上仍常退回级联系统。

## 方法
X-OPD：跨模态 on-policy 蒸馏。
- 平行数据 \((S_i,T_i)\)：语义不变的语音–文本提示对（文本改写成口语风格后 CosyVoice3 合成，SenseVoice 回译 WER>5% 过滤）；约 27k 对。
- Student（Speech LLM）在语音/文本上 on-policy 多样本 rollout（\(n=4\)）；文本 teacher 在同步文本上给 token 级优势：
  - 模态内 \(A_{\mathrm{im}}=\log\pi_\phi(y_t|T,y_{<t})-\log\pi_\theta(y_t|T,y_{<t})\)
  - 跨模态 \(A_{\mathrm{cm}}=\log\pi_\phi(y_t|T,y_{<t})-\log\pi_\theta(y_t|S,y_{<t})\)
- 目标 \(\lambda L_{\mathrm{im}}+(1-\lambda)L_{\mathrm{cm}}\)（策略梯度 + 概率比）；全参训 LLM 骨干，冻结 audio tower 与 adapter。

## 实验与结果
基座 Qwen3-Omni-A3B-Instruct，teacher 为 Qwen3-A3B-Instruct；基准 BIG Bench Audio、Audio Multi-Challenge、VoiceBench（语音/文本双模态）。
- X-OPD 将平均掉点从 11.29%（S）/5.51%（T）降至 **3.43% / 0.97%**；如 BIG Bench Audio 语音 93.41 vs 基座 85.67。
- 同数据上 SFT、Offline KD、GKD 反而扩大掉点。
- 消融：同容量 teacher（A3B）优于更大 A22B；\(\lambda=0.5\) 优于纯文本/纯语音。
- MMAR 遗忘：SFT/KD/GKD 从 71.3 跌至约 60；X-OPD 仍约 69–70.7。

## 结论
On-policy 跨模态蒸馏可在少量无标注配对数据上对齐 Speech LLM 与文本能力，并显著减轻遗忘；为低成本基础对齐提供路径。

## 点评
抓住暴露偏差：让学生在自己轨迹上被文本 teacher 打 token 级分，比静态离线轨迹更贴推理路径。强在双优势与遗忘对比完整；脆弱在依赖合成语音–文本平行性与 teacher–student 容量匹配——过大 teacher 反而变差，说明“可吸收轨迹”比绝对教师强度更关键。

