# Long-form Audio & New Attention Approaches

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：8
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕长音频场景与注意力机制改进：一端是呼叫中心长对话评测与长时自发口语评分，另一端是 AED/SSM/对比解码与可解释注意力。核心矛盾是：模型常在短切分或受限上下文上训练，却要在连续长编码、多口音与噪声条件下稳定工作。

长形声学编码暴露 AED 的位置编码陷阱——段边界外的隐式绝对位置线索在连续解码时消失，交叉注意力对 key/value 的置换不变性削弱排序能力。相应修复包括显式位置、长上下文训练、段拼接与语义切分对齐。评测侧则强调未预训练泄漏的多口音长对话基准，以及多模态（音频+ASR 文本+题目）的长答卷评分。

注意力新路径包括：把通道维局部注意力嵌入 SSM 以动态参数化状态转移；在 AVSR 的对比解码中按注意力与预测分歧自适应缩放干预强度；以及用熵引导的注意力 rollout 做更忠实的 ASR 归因。总体趋势是“长时上下文可训可评”与“注意力可诊断、可自适应”。

## 论文技术总结

# AppTek Call-Center Dialogues: A Multi-Accent Long-Form Benchmark for English ASR

- 论文编号：2047
- 报告人：Eugen Beck
- 程序：Thursday 1 October 2026 / Long-form Audio & New Attention Approaches
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/beck26_interspeech.pdf

## 问题
公开英语 ASR 基准多为短切分、朗读/准备语料，且缺少显式方言标注，难以评估对话式、长时、多口音场景；大型开源模型还可能污染公开测试集。呼叫中心类应用尤其需要自发交互、命名实体与领域词汇下的稳健评测。

## 方法
发布 **AppTek Call-Center Dialogues** 评测语料（非训练用）：角色扮演的 agent–customer 对话，覆盖 14 种英语口音、16 类服务场景；专业人工逐字转写（含犹豫、截断等标记）与多轮 QA；另有约 5 小时译成中/德/日/西供 IWSLT 盲测。对多种开源 ASR，在人工切分、AppTek 切分、Silero VAD、固定 30s/60s 切分下按会话聚合 WER 评测。

## 实验与结果
规模：128.6 小时、156 说话人、873 通话、约每口音 8–11 小时。多数模型人工切分 WER 最低；Qwen3-ASR 在 60s 固定切分上更优。Silero 设置下口音间差距大，en SG/CN/GB SCT/IN 普遍偏高，en AU/US General 偏低；强弱口音差距常超 10% 绝对，且平均 WER 好不意味着口音稳健性好。无外部切分时仅少数模型可用。

## 结论
该语料从零采集、未用公开网页材料，便于可复现的长时对话与口音评测；边界检测与口音多样性仍是开放问题，平均准确率提升不能自动转化为口音稳健性。

## 点评
贡献主要在「干净评测基准」：新数据、口音标签、切分消融协议三位一体，对 conversational AI 部署很有针对性。局限也写得很清楚——角色扮演非真实通话、性别不平衡、口音自报+离散标签、无正式 IAA——解读结果时需按「所代表说话人样本」而非整口音社群。


# Segmental Attention Decoding With Long Form Acoustic Encodings

- 论文编号：341
- 报告人：Xinwei Li
- 程序：Thursday 1 October 2026 / Long-form Audio & New Attention Approaches
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/swietojanski26_interspeech.pdf

## 问题
AED 在分段语料上训练时，交叉注意力会利用段边界「残缺上下文」作隐式绝对位置锚点；长时流式编码（LFE）消除这些边界线索后，因 key/value 置换不变性无法排序声学编码，表现为重复转写、难以发 EOS，自回归注意力解码崩溃。

## 方法
四项修改：
1. **交叉注意力绝对位置编码**：对每段 \(H_s\) 加段内复位的位置码，再进 cross-attention。
2. **声学上下文扩展 (AC)**：训练时为 LF 样本左右扩上下文，使段内编码成为真 LFE，但不对损失使用两侧无效帧。
3. **段拼接 (SC)**：拼接连续段与非语音邻域，丰富时长与 LFE 暴露。
4. **语义切分 (SS)**：CTC 头预测语义句界 token，触发二遍 AD，优于纯 VAD。

模型为 CTC-AED（Ours.base ~90M / Ours.small ~240M），编码器因果 Conformer + 可变 chunk，解码器固定约 18M。

## 实验与结果
TED-LIUM3 消融：基线 LFE 上纯 AD WER 达 295%；SC+AC+PE 后 AD 与 SFE 持平（约 5.0%）；加 SS 后 CTC-Att 达 4.3%。最终：Ours.small CAT@3.84s 在 Tedlium3 LF 3.9%、Earnings21 11.4%，短切分任务也不退化；相对同量级 Whisper 延迟更低、多数集合更优（部分集合作者注明非零样本）。

## 结论
AC 与段级 PE 互补，可关闭连续编码与分段编码的精度差距，使注意力解码器可对长时编码自回归使用；CTC 语义切分优于 VAD，混合 CTC-Att 更稳。

## 点评
问题诊断很扎实：把长时失败归因到「边界捷径消失 + 置换不变」，对策也对准这两点。强在系统消融清晰、部署上保留流式编码器与轻量解码器；脆弱点是强依赖训练侧 AC/SC 数据改造，且对伪标签 SpeechCrawl 质量敏感，语义 seg 标签本身也引入外部 Segment any Text 管线。


# M-LAMA: Multimodal Automated Scoring of Long-form Spoken English

- 论文编号：1542
- 报告人：Minh Dao-Xuan-Quang
- 程序：Thursday 1 October 2026 / Long-form Audio & New Attention Approaches
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/daoxuanquang26_interspeech.pdf

## 问题
真实口语考试需对多分钟自发回答做发音、流利、词汇、语法、语篇等多维评分，但既有工作多聚焦短句或发音；公开数据也缺乏长时、多标准熟练度标注。通用音频语言模型对细粒度发音/韵律与钟形分数分布不够适配。

## 方法
提出 **M-LAMA**：双流编码 + 语篇感知融合。
- 音频：冻结 Whisper-Large + bottleneck adapter；3–5 分钟回答切成 30s chunk，按考试三部分分层注意力池化并加位置嵌入。
- 文本：冻结 Qwen2-1.5B 编码转写与题目；题目条件交叉注意力评估任务完成度；双向 audio↔text 注意力与门控融合（含双线性交互），输出 0–10（0.5 步）21-bin 期望分数。
- 训练三阶段：对比对齐 → 粗档分类（低/中/高）→ MAE+Focal 细粒度回归，缓解中档主导。

## 实验与结果
数据：约 86,491 场、29,034 考生、~4,845 小时（按考生切分防泄漏；因保密不可公开）。全测集上 Multi-stage 相对最强开源基线（Qwen-2.5 Omni）五维 MAE 约降 15–29%、QWK/Acc@1 全面提升；相对 GPT-4o Audio 等 API（1k 子集）亦明显更好。消融：Text+Audio Acc@1 90.82% 远高于单模态；去题目模块伤语篇管理；单阶段训练明显弱于多阶段。chunk 留一分析显示前部段贡献更大但仍全局聚合。

## 结论
长时口语评分需要结构化多模态对齐（声学交付 + 语言内容 + 题目语境）与分布感知训练；M-LAMA 在五维标准上显著提升可靠性。代码与检查点公开，数据可按申请分享。

## 点评
把评分量表拆到架构组件（部分结构、题目条件、双向融合）和「先对齐再分档再回归」的三阶段优化，针对考试分数钟形分布很对症。强在大样本机构数据与完整消融；主要风险是数据不可公开、依赖 Whisper/Qwen 冻结表征，以及商业 API 只在 1k 子集对比，外推需谨慎。


# Attentive Mamba: Channel-wise Local Attention for Speech Recognition

- 论文编号：1708
- 报告人：Jen-Tzung Chien
- 程序：Thursday 1 October 2026 / Long-form Audio & New Attention Approaches
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/chien26_interspeech.pdf

## 问题
Transformer 自注意力全局建模强但 \(O(T^2)\) 且局部细粒度不足；Mamba 等 SSM 线性复杂度、擅长长程，但局部聚合依赖**静态**深度卷积，缺乏内容自适应。希望在保持 SSM 全局状态建模的同时，为局部特征引入动态注意力。

## 方法
提出 **Attentive Mamba (attMamba)**：用**通道维局部注意力**替换 Mamba2 中的静态因果卷积。
1. 对各通道用因果深度卷积上下文化生成 \(q,k,v\)（而非逐时刻线性投影）。
2. 在因果局部窗口 \(w\) 上做跨通道点积注意力，得到内容感知局部摘要 \(u_t\)。
3. 用 \(u_t\) 动态参数化 SSM 状态转移 \(A,B,C\)。
编码器为双向 attMamba；训练可联合 CTC 与 AED，并可加 4-gram LM 重打分。

## 实验与结果
LibriSpeech 960h：attMamba-CTC (S, 21.2M) test-clean/other 6.24/12.31，优于同配置 conformer-CTC (S, 30.0M) 的 6.59/12.57。TED-LIUM3：S/L 上均优于 conformer；attMamba+lm-CTC+AED (L) test 4.98。消融：双向相对单向 Mamba2 大幅降错；再换通道注意力进一步改善。进阶 CTC+AED+LM 下 attMamba+lm 达 test-clean/other 2.73/6.02，优于同设置 conformer 与若干自监督基线。特征图显示通道注意力使各通道时间轴更均匀，体现通道级动态调制。

## 结论
把静态卷积局部聚合换成卷积上下文化的通道维局部注意力，可增强 SSM 状态参数化，在更小参数量下于朗读与自发语音 ASR 上低于 conformer/Mamba2。

## 点评
抓的是 Mamba「时间混合强、局部聚合钝」的瓶颈，设计贴合频谱「通道内时域相干、再跨通道融合」的结构先验。强在参数更少且消融干净；脆弱点在窗口 \(w=4\) 等超参敏感、双向实现偏离严格因果流式，以及与更强预训练编码器对比时收益边界仍待更大尺度验证。


# Attention-Guided Reliability Scaling for Contrastive Decoding in Robust Audio-Visual Speech Recognition

- 论文编号：929
- 报告人：Da-Hee Yang
- 程序：Thursday 1 October 2026 / Long-form Audio & New Attention Approaches
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/kim26h_interspeech.pdf

## 问题
LLM 系 AVSR 在噪声下仍可能过度依赖受损音频。对比解码（Expert=音视频、Amateur=仅音频）无需训练即可削弱声学偏置，但固定对比强度会在强噪声与干净条件间权衡：强干预利于低 SNR，却可能在干净语音上过纠。

## 方法
在同一 LLM-AVSR 上做训练无关对比解码，用 token 级软门控 \(w_t\) 缩放有效强度 \(\lambda_{\mathrm{eff}}^{(t)}=w_t\lambda\)。\(w_t\) 为三项乘积（保守激活）：
- **相对音频能量 \(E_t\)**：末层末 token 对音频区注意力相对本句运行均值；
- **音频熵 \(H_t\)**：音频区注意力分散度（按头独立算再平均）；
- **JS 散度**：Expert/Amateur 预测分歧，经高斯「甜区」滤波（\(\mu_{\mathrm{sweet}}=0.35\)）抑制过同或过崩塌分歧（防 rank distortion）。

## 实验与结果
LRS3 训练，MUSAN 噪声注入到 0/−5/−10/−15 dB；OOD 到 LRS2。在 Llama-AVSR(8B)、Omni(1B)、Qwen(0.5B) 上相对 AV 基线平均相对改进约 5–10%；干净与噪声均有收益。固定 \(\lambda\) 最优值随 SNR 变化；自适应在各条件更均衡。消融显示 JS 偏稳干净/轻噪，\(E_t/H_t\) 偏助重噪。延迟约 +8.6%。

## 结论
基于注意力与预测分歧的可靠性缩放，可在不改参数的前提下同时改善干净与强噪声 AVSR，避免固定 CD 的鲁棒–干净权衡。

## 点评
把「何时该压音频偏置」做成可观测门控，比一刀切 \(\lambda\) 更贴 SNR 波动。强在即插即用、跨模型尺度可迁移；脆弱点是依赖特定拼接布局提取音频索引、门控超参仍需验证集调，且极端 JS 崩塌时对比项本身就不稳定。


# Listening with Attention: Entropy-Guided Explainability for Transformer-Based Audio Models

- 论文编号：593
- 报告人：Ravi Kumar
- 程序：Thursday 1 October 2026 / Long-form Audio & New Attention Approaches
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/kumar26_interspeech.pdf

## 问题
Whisper 等 Transformer ASR 精度高但难解释；LIME/SHAP/IG 等事后解释对语音时序不友好，常不忠实且时间定位粗糙。需要与模型内部计算一致、并对齐到解码 token 的时域归因。

## 方法
LEAF-X：对每个解码 token 产生帧级归因。对 cross-attention（或 decoder-only 中指向音频伪 token 的注意力）算头熵，低熵头获更高权重并层内聚合；再用多层 attention rollout 累积证据；可用梯度调制压制对 token 概率影响小的注意力；可选按层消融 cross-attention 造成的 NLL 上升作因果重加权。输出归一化 token-to-frame 分布，映射回波形时间轴。适用于 Whisper 与 speech-augmented decoder-only（如 Canary-Qwen）。

## 实验与结果
模型：Whisper-large-v3（LibriSpeech）、Canary-Qwen-2.5B（TED-LIUM 3）。指标（归一化）：D-AOPC↓、TLoc↑、SPR↑、STAB↑、INF↓。Whisper：LEAF-X 为 0.45 / 0.72 / 0.70 / 0.78 / 0.45，全面优于多数基线，TLoc 略低于 SaCo（0.73）。Canary：0.48 / 0.70 / 0.68 / 0.76 / 0.47。消融显示去掉熵加权或 rollout 损害最大；insertion/deletion 曲线支持更高忠实度。作者强调指标为代理，非人类可信证明。

## 结论
LEAF-X 用熵引导头选择、多层 rollout 与轻量因果重加权，为 Transformer ASR 提供更忠实、稀疏且稳定的 token–时间归因，利于高风险场景下的可审计分析；局限含骨干/数据/语言覆盖、校准敏感、缺用户研究等。

## 点评
核心是把“哪些帧支持这个词”建成模型内禀流程，用低熵注意力过滤弥散头，比纯扰动或原注意力更贴计算路径。因果层消融有额外前向开销，可关掉；解释质量仍绑定注意力机制假设，对噪声域移与非注意力主导错误模式可能脆弱。

