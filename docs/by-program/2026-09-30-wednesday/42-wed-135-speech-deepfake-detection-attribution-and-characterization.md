# Speech Deepfake Detection, Attribution and Characterization

- 日期：Wednesday 30 September 2026
- 时间：16:30-18:30
- 形式：Oral
- Area：4
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场聚焦语音深度伪造检测的泛化：老年合成语音缺口、域泛化元学习中的梯度冲突、强化学习微调、域自适应双门控 MoE、质量感知多中心一类学习，以及时长变化下的自注意力偏置校正。

共同挑战是未见攻击、声学条件与说话人群体（尤其老年）上的域移。方法上从“单一真伪中心”扩展到质量子空间多中心，从监督微调扩展到 GRPO 类 RL，并从固定长度训练扩展到显式时长嵌入。

## 论文技术总结

# Bridging the Age Gap: Towards Detecting Neural Audio Codec Synthesized Elderly Speech Deepfake

- 论文编号：2283
- 报告人：Orchid Chetia Phukan
- 程序：Wednesday 30 September 2026 / Speech Deepfake Detection, Attribution and Characterization
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/phukan26_interspeech.pdf

## 问题
CodecFake（CF）检测基准多基于年轻成人，老年语音声学差异大；现有 CF 检测器跨年龄泛化差，老年人群更易受害。

## 方法
提出 ECFD 任务与 Elderly-CodecFake（ECF）数据：真实老年语音来自 SeniorTalk（汉语）与 TIS（英语老年子集），用 14 种 NAC（DAC、EnCodec、SoundStream 等）编解码生成伪样本（约 6 万真实、85 万 CF）。评测既有 CF 检测器的零样本迁移；比较语音 FM（Wav2vec2/WavLM/Whisper）与多模态 FM（LanguageBind、ImageBind）；提出 BONSAI，用 Jensen–Shannon Divergence 对齐融合两路 FM 表征。

## 实验与结果
在 Lu et al. CF 数据上训练再测 ECF：老年 EER 约翻倍于年轻子集（如 Wav2vec2-AASIST 年轻 12.89 vs 老年 25.76）。域内：多模态 FM+CNN 优于语音 FM（LB 平均 EER 4.56）。BONSAI 融合 LB+IB 平均 EER 1.66，优于拼接与单模型。

## 结论
老年 CodecFake 是独立且更难的检测场景；多模态预训练先验与 JSD 对齐融合可显著提升 ECFD。

## 点评
把年龄缺口做成公开任务与数据，填补 CF 检测人口盲区。多模态 FM 优势被解释为预训练接触老年视觉语境，属合理假设但仍间接；跨 codec 测试划分有助于测泛化，后续需更严的未见 codec/未见录音条件评估。


# DGS-MLDG: Domain Gradient Surgery Guided Meta-Learning for Domain Generalization in Speech Deepfake Detection

- 论文编号：1042
- 报告人：Youzhi TU
- 程序：Wednesday 30 September 2026 / Speech Deepfake Detection, Attribution and Characterization
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/qin26_interspeech.pdf

## 问题
语音深度伪造检测在未见域上易失效。MLDG 通过元训练/元测试模拟域偏移，但两目标梯度常冲突（余弦相似为负），朴素聚合会抵消更新。

## 方法
提出 Domain Gradient Surgery (DGS)：不对称地把冲突的元测试梯度投影到元训练梯度的法平面，去掉破坏性分量。Layer-wise DGS (LW-DGS) 按实时余弦相似度只对冲突层做手术。骨干为 XLSR-Mamba 类检测器；与 ERM、标准 MLDG、PCGrad/GradVac/CAGrad 对比。

## 实验与结果
跨数据集平均相对 ERM：DGS-MLDG +5.29%，LW-DGS-MLDG +4.04%。In-the-wild / CodecFake 上 DGS 达 5.23% / 6.76% EER，优于对称梯度手术。反向投影或只手术 SSL 骨干会变差；冲突负比例由约 33% 降至约 23.5%。

## 结论
针对元学习双层结构的不对称梯度手术可稳定 MLDG，提升跨编码与真实场景泛化；层选择版在效率与收益间折中。

## 点评
抓住“元训练应主导、元测试只纠偏”的双层不对称性，比把两任务当对等 MTL 更贴合 MLDG。增益在难集更明显；平均相对提升约 5% 不算革命性，但是干净的优化向改进。


# Does Fine-tuning by Reinforcement Learning Improve Generalization in Binary Speech Deepfake Detection?

- 论文编号：589
- 报告人：Xin Wang
- 程序：Wednesday 30 September 2026 / Speech Deepfake Detection, Attribution and Characterization
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26k_interspeech.pdf

## 问题
主流 SSL 深度伪造检测多用监督微调（SFT），易对目标域过拟合。受 LLM 启发，问 Group Relative Policy Optimization (GRPO) 能否改善未见攻击/域泛化。

## 方法
在 AntiDeepfake 多阶段管线（预训练 SSL + 后训练 + 微调）上，对 XLS-R-2B / MMS-1B / MMS-300M 等二分类检测器试纯 GRPO、SFT、SFT→GRPO 及简化/无负样本/不同 β 变体。目标域 DFE24；域外 ADD23、FoR、DEEP-VOICE、In-the-Wild。消融负奖励与正则项。

## 实验与结果
XLS-R-2B：纯 GRPO 域内平均 EER 约 9.93，域外平均 2.69，优于 SFT（10.26 / 6.28）与多数混合设置。去掉负样本后域外变差；过大 β 严重损害域内。无后训练时 GRPO 域外仍差，说明后训练表征是前提。分布漂移测量支持上述发现。

## 结论
纯 GRPO 微调可在保持目标域性能的同时显著提升域外泛化；负奖励可能是关键因素。面向 SSL 前端二分类检测器的结果据作者称属新发现。

## 点评
把 LLM 对齐工具迁到反欺骗，问题设定清楚。纯 RL 优于 SFT→RL 暗示过强监督会锁死决策边界；依赖大规模后训练与算力，落地成本不低。


# Domain-Adaptive Dual-Gating Mixture of Experts for Generalizable Speech Deepfake Detection

- 论文编号：1778
- 报告人：Zhe LI
- 程序：Wednesday 30 September 2026 / Speech Deepfake Detection, Attribution and Characterization
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/qin26b_interspeech.pdf

## 问题
MoE 有助 SDD 泛化，但现有门控多为通用 FFN，忽略深度伪造的声学/时序伪迹，难以把不同攻击模式路由到专长专家。

## 方法
DADG-MoE：双门控对原始波形与 XLSR SSL 特征分别用 Sinc / depthwise Sinc 滤波提取伪迹，再结合可学习域原型生成路由权重；专家为极轻量仿射（BN 的 γ/β）。Top-k 聚合后接 AASIST。在 ASVspoof2019 LA 训练，测 21DF、ITW、FoR、ADD2023。

## 实验与结果
相对 XLSR-AASIST：21DF 3.69→2.54（−31.2%）、ITW 10.46→6.35（−39.3%）、FoR 7.47→4.42（−40.8%相对）。仅增约 0.17M 参数。消融：去掉 Raw-Gating 掉点最大；原型与 SSL-Gating 对域外重要。top-k=2 较稳。

## 结论
语音特异双门控 + 域原型 + 仿射专家，能以极低参数代价提升未见攻击/条件泛化。

## 点评
门控真正“听”伪迹而不是只看高层嵌入，方向正确；仿射专家把域差异压到统计仿射上，解释与效率兼顾。与通用 MoE 基线对比仍偏少，但相对强基线增益清晰。


# QAMO: Quality-aware Multi-centroid One-class Learning For Speech Deepfake Detection

- 论文编号：1098
- 报告人：Eng Siong Chng
- 程序：Wednesday 30 September 2026 / Speech Deepfake Detection, Attribution and Characterization
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/truong26_interspeech.pdf

## 问题
单中心一分类（OCL）把真实语音压到一个质心，易过度简化；真实语音质量（自然度）跨样本差异大，且 MOS 可廉价估计，却常未被显式建模。

## 方法
QAMO：用 Scoreq 预测 MOS，阈值为高低质量两级；为真实类学多个质量感知质心，并用质量分类损失拉开；推理时对多质心距离做集成打分，无需质量标签。接在 XLSR-Conformer-TCM / Nes2NetX 上；增强样本视为低质量。

## 实验与结果
XLSR-Conformer-TCM + QAMO：21DF 1.63%、ITW 5.21%、FoR 3.45%，优于 WCE、OC-Softmax 与先前质量感知系统。消融去掉质量分类或改用 max-score 推理均变差。UMAP 显示高低质量真实/伪造子空间更清晰。

## 结论
按质量多中心建模真实类，比单中心 OCL 更能保留类内变异并改善未见场景检测。

## 点评
用 MOS 代理代替说话人身份做多中心（相对 SAMO）更可部署。τ=2.5 二分与增强=低质量是粗近似，但与 MOS 分布位移一致；ITW 5.21% 是亮点数字。


# Duration-aware self-attention for speech deepfake detection

- 论文编号：2200
- 报告人：Youzhi Tu
- 程序：Wednesday 30 September 2026 / Speech Deepfake Detection, Attribution and Characterization
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/tu26_interspeech.pdf

## 问题
深度伪造检测训练/评测常固定时长（填充或截断），与真实可变时长不符，易引入边界伪迹或丢掉关键片段。

## 方法
由整段时长与片段偏移构造 timing embedding，注入自注意力以修正注意力偏置图，称 Duration-aware Self-Attention (DASA)。三种实现：帧无关、帧相关、相对位置编码（RPE）相关。用于 ConFusionformer / Conformer，在 ASVspoof21、In-the-Wild、CodecFake 上评测。

## 实验与结果
RPE-dependent DASA 一致有益：ConFusionformer-9 上 ASVspoof21-LA 最佳/平均 EER 1.01/1.13，DF 1.53/1.71，优于标准注意力；另两种 DASA 常恶化。时长失配实验中，RPE-DASA 在 2/6s 与全长上更稳，标准 SA 在训练=评测时长时最好、失配时骤降。

## 结论
把全局时长语境写入 RPE 约束下的注意力偏置，可缓解时长变化带来的性能波动。

## 点评
问题真实且实现轻量；关键是“有界纠偏”（RPE）而非任意帧级调制。增益幅度中等，但对可变时长部署有直接工程意义。

