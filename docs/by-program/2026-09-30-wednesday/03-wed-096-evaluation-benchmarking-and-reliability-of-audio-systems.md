# Evaluation, Benchmarking, and Reliability of Audio Systems

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：5
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕音频系统的评测、基准与可靠性展开，覆盖质量评估、深度伪造检测、无损压缩、空间表示探测以及可解释的编辑评测等方向。共同背景是生成式音频与处理算法快速迭代，静态评测模型与固定决策边界难以跟上新失真类型与域漂移。

质量评估侧出现两条互补路径：一是以持续学习应对语音与音乐等多域任务序列，用双分支与知识蒸馏在可塑性与稳定性之间权衡；二是把多模态大模型当作“评委”，用链式思维对音频编辑结果做自然语言可解释评分。真实性与安全侧则从“拟合已知伪造分布”转向建模真实流形，并推动环境声深度伪造检测挑战的数据集与评测协议建设。

压缩与表示评测方面，语言模型式无损压缩被扩展到全保真（16/24-bit）音频，字节级分词缓解词汇表爆炸；空间音频预训练表示则通过受控探测基准系统检验方位、距离与房间参数等空间因子是否可解码。整体上，评测从单一分数走向挑战赛洞察、可解释文本评测与开放基准，强调对分布漂移与跨域泛化的鲁棒性。

## 论文技术总结

# CAQA-Net: Continual Audio Quality Assessment Across Speech and Music Domains

- 论文编号：476
- 报告人：Naiyuan Li
- 程序：Wednesday 30 September 2026 / Evaluation, Benchmarking, and Reliability of Audio Systems
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26d_interspeech.pdf

## 问题
生成与处理模型不断引入新失真与新域，静态 AQA 难跟进；联合重训代价高，微调又灾难性遗忘，跨语音–音乐回归任务的持续学习几乎空白。

## 方法
CAQA-Net：可训波形支路 M2D + 冻结谱图语义锚 BEATs，特征拼接后接多任务头；训练用知识蒸馏正则保旧知识；推理用基于 BEATs 原型的门控做任务无关加权。任务序列：TCD–VOIP → NISQA–SIM → Tencent → SingMOS → MusicEval。

## 实验与结果
相对 FT/MH-FT 等，CAQA-Net（LwF）mSRCC 0.754、mPSI 0.887，接近联合学习上界 JL 的 0.790（差约 0.036 SRCC / 4.6%）。EWC/MAS 变体亦优于朴素微调。语音到音乐域移仍是主要难点。

## 结论
双分支多头 + 蒸馏与原型门控可在语音/音乐 AQA 流上平衡塑性与稳定性，接近联合学习而不必重训全数据。

## 点评
把持续学习真正落到跨域 MOS 回归，填补评测侧空白。评分标准不一致与标签噪声仍会放大切换不稳定；未来需更强处理语音–音乐鸿沟。


# The First Environmental Sound Deepfake Detection Challenge: Benchmarking Robustness, Evaluation, and Insights

- 论文编号：1599
- 报告人：Yang Xiao
- 程序：Wednesday 30 September 2026 / Evaluation, Benchmarking, and Reliability of Audio Systems
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yin26_interspeech.pdf

## 问题
环境声生成（TTA/ATA/VTA）可伪造警报、枪声等，威胁公共安全；相对语音/歌声 deepfake，环境声 deepfake 检测（ESDD）缺乏统一基准与挑战。

## 方法
介绍首届 ESDD Challenge：两赛道—(1) 未见生成器检测（EnvSDD），(2) 黑盒低资源；(EER 为指标；基线 AASIST 与 BEATs+AASIST。汇总 97 队、约 1700+ 有效提交，并分析顶尖系统架构与训练策略。

## 实验与结果
Track 1 基线 BEATs+AASIST EER 13.20%；榜首 AHU EAT+AASIST 集成达 0.30%。Track 2 基线 12.48%，顶尖约 0.25%。常见有效策略：大规模 SSL/EAT 表征、增广、跨层融合、集成；未见/黑盒生成器仍显著拉垮朴素系统。

## 结论
高保真生成器挑战大，但 SSL+增广+集成可获强泛化；挑战为后续 ESDD 提供基准与方向。

## 点评
把环境声反欺骗从语音反欺骗邻域单独立题，数据与赛道设计对安全评测很及时。论文偏挑战综述，具体系统细节依赖各队报告；真实野外部署噪声与复合伪造仍待 ESDD-2 等跟进。


# Benchmarking Language Modeling for Lossless Compression of Full-Fidelity Audio

- 论文编号：1748
- 报告人：Phillip Long
- 程序：Wednesday 30 September 2026 / Evaluation, Benchmarking, and Reliability of Audio Systems
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/long26_interspeech.pdf

## 问题
自回归语言模型可经算术编码做无损压缩，但既往多限于 8-bit/16 kHz；16/24-bit 全保真下词表爆炸（65K/16.7M），能否实用并与 FLAC 竞争未知。

## 方法
系统基准音乐/语音/生物声学、16–48 kHz、8/16/24-bit。提出 Trilobyte：将每样本拆成字节交错，词表恒为 256（O(1) vs O(2^b)），序列长度增约 ⌈b/8⌉ 倍，使 24-bit LM 压缩首次可训。用 GPT-2 类 AR + 算术编码；亦可用 NLL 估计码率。

## 实验与结果
LM 在 8-bit 与 16-bit 上持续优于 FLAC 并达 SOTA 量级；随 bit depth 升高相对增益变小。Trilobyte 改善 16-bit 并首次使 24-bit 可处理。作者指出 bit depth（相对采样率或领域）是限制可学压缩增益的关键因素。

## 结论
字节级分词让全保真无损 LM 压缩可行；高 bit depth 下相对传统编解码器的优势收窄。

## 点评
把“LM 无损压缩”从玩具 8-bit 推到 CD/专业位深，工程贡献清楚。上下文窗口与算力仍远高于 FLAC；随深度升高收益递减提示与线性预测的信息论重叠。


# Probing Spatial Structure in Pretrained Audio Representations

- 论文编号：2506
- 报告人：Sivan Ding
- 程序：Wednesday 30 September 2026 / Evaluation, Benchmarking, and Reliability of Audio Systems
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26ba_interspeech.pdf

## 问题
多通道/空间音频预训练模型增多，但端到端流水线难分离“表征里到底编码了哪些空间因素”；缺可控探测基准。

## 方法
提出 SARL：合成单源场景，独立控制源因素（方位、俯仰、距离、事件类）与房间因素（RT60、体积、形状）；对多种冻结编码器做统一线性探测，并比较源/房间扰动下的表征敏感度。覆盖 FOA/立体声等输入与 SSL/监督/编解码类模型。

## 实验与结果
三规律：(1) 输入配置与训练范式塑造空间编码；(2) 源因素 systematically 比房间因素更易解码；(3) 敏感度分析显示对源扰动响应更大、对房间更异质。FOA 输入 + SSL 倾向更稳健的空间因子编码。

## 结论
当前预训练表征对源属性偏置明显、对全局房间属性偏弱；SARL 开源以支持可复现空间表征评估。

## 点评
用可控合成把“空间信息是否在嵌入里”从下游任务里剥离出来，对机器人/沉浸音频表征很有诊断价值。线性探测与均值池化、单源设定会低估非线性可及信息与真实多源复杂度。


# Interpretable Audio Editing Evaluation via Chain-of-Thought Difference-Commonality Reasoning with Multimodal LLMs

- 论文编号：3176
- 报告人：Yuhang Jia
- 程序：Wednesday 30 September 2026 / Evaluation, Benchmarking, and Reliability of Audio Systems
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jia26b_interspeech.pdf

## 问题
音频编辑需同时衡量“改到了什么”与“保留了什么”；既有自动 MOS/目标指标或缺可解释性，或缺对成对编辑的结构化推理。

## 方法
基于 Qwen2-Audio，用混合/重排构造约 3 万伪成对样本，LoRA 微调 Difference / Commonality 双 caption 任务；再设计 Chain-of-Thought 提示做逐步差同推理，导出 Edit score 与 Faith score。在 AuditScore 上与专家分及 AuditEval-ssl 等相关对比，并用 Qwen2.5-Omni 做 A/B 投票消融。

## 实验与结果
SFT 后 Difference/Commonality caption 从近零跃升（FENSE 约 0.83 / 0.69）。Difference 质量与编辑有效性指标正相关、与保真负相关；Commonality 相反，形成互补模式。Edit score 在编辑有效性上 LCC/SRCC 超 AuditEval-ssl（如 Edit LCC 0.765 vs 0.620）；Faith score 对保真更弱。A/B 显示优化 CoT 流程优于原始提示。

## 结论
差同叙述 + CoT 可给出可解释、与人类更对齐的音频编辑自动评测；代码将开源。

## 点评
把 LLM-as-Judge 落到“改/留”双轴，比单分数 MOS 更贴编辑任务。伪配对与另一 MLLM 当裁判可能引入同族偏差；Faith score 仍明显弱于专用保真模型。


# DASM: Detecting AI-Synthetic Music via Authentic Manifold Deviation Modeling

- 论文编号：3245
- 报告人：Xinya Zhu
- 程序：Wednesday 30 September 2026 / Evaluation, Benchmarking, and Reliability of Audio Systems
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhu26d_interspeech.pdf

## 问题
音乐 deepfake 检测多拟合已知伪造分布；生成器迭代导致非平稳漂移，判别边界易失效。

## 方法
提出 DASM：仅在真实样本上用重建损失训练可学习 memory bank，压缩真实音频流形先验；双分支分类器同时用原特征与 memory 重建特征，以相对真实流形的偏差识别伪造。对冻结 MERT 编码器做轻量 prompt tuning。在 SONICS 及声学降质条件下评测。

## 实验与结果
SONICS 上 EER 0.13%、Acc 99.89%、AUC 99.98%，优于 SpecGraph、WPT-XLSR-AASIST 等基线；在多种声学退化下保持稳健。

## 结论
锚定真实流形、不以伪造分布为跟踪目标，对 AI 合成音乐检测更稳，也可量化 AI 参与程度。

## 点评
把“追假”改成“离真多远”，理论上更抗未见生成器。主结果集中在 SONICS；跨生成平台与 AI 辅助混音的细粒度外推仍需更多证据。

