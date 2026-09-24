# Speaker Verification and Anti-Spoofing

- 日期：Tuesday 29 September 2026
- 时间：09:00-11:00
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

本场同时覆盖反欺骗（anti-spoofing）检测器改进、语言学偏置缓解、欺骗鲁棒 ASV（SASV）双向融合，以及针对 CM / VAS / SASV 管线的黑盒对抗攻击。攻防同台：一侧追求更低 EER、更好校准与部署效率，另一侧展示静态检测器可被频谱操控或联合梯度攻击击穿。

训练策略上出现“看似用参考、实则学到不变性”的现象：RAT 显示参考通道在推理中贡献迅速消失，但参考增强训练仍提升检测；SpAArSIST 则从 AASIST 后端删冗余，用显式池化比与幅度打分换算力。泛化瓶颈被归因于语言线索依赖，梯度反转教师–学生加 Variational Information Bottleneck 用于压制语言信息同时保留非语言线索。

SASV 融合从单向 CM→ASV 走向双向调制与双粒度融合。攻击侧 SMIA 与 AGENT 分别强调不可听频段操控与解决 ASV–CM 梯度冲突的分数最大化，摘要报告的高攻击成功率被用来论证需要动态自适应防御。

## 论文技术总结

# RAT: Reference-Augmented Training for ASV Anti-Spoofing

- 论文编号：132
- 报告人：Vojtěch Staněk
- 程序：Tuesday 29 September 2026 / Speaker Verification and Anti-Spoofing
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/stanek26c_interspeech.pdf

## 问题
传统 ASV 反欺骗多为单句检测，未利用注册参考；直接做参考条件架构时，作者发现模型训练后推理常忽略参考，但参考增强训练仍带来泛化收益。需解释并利用这一现象。

## 方法
RAT：共享 XLS-R 300M 提参考/测试多层特征；Reference-Informed Block 含测试侧 MLP 与测试 query–参考 key/value 的多头交叉注意力，残差相加后跨层与时间均值池化，MLP 输出 bona/spoof logits。训练时同说话人 bona fide 随机配对参考；两阶段（冻结前端再联合微调）+ 时间掩蔽/mu-law/RawBoost/噪声滤波等增强。推理可换零向量参考。

## 实验与结果
ASVspoof 5：RAT 零参考推理 EER 2.57%、minDCF 0.074，优于同配方单句 XLS-R 基线（4.87%/0.141），并超过文献单模型与接近 12 模型融合冠军。噪声、截断、静音、噪声参考、说话人不匹配等推理消融性能几乎不变。训练动力学显示参考依赖迅速下降。

## 结论
参考通道主要改善优化与表示，而非推理必需；RAT 以单检测器达到强 ASVspoof 5 表现。代码与权重已公开。

## 点评
把“参考条件失败”转成可复用训练策略，发现扎实。残差设计使模型可退回单句路径，解释了零参考仍强；代价是大 SSL 前端与 Open 条件设定，与挑战闭集规则不完全对齐。


# SpAArSIST: Sparsified AASIST for Efficient and Reliable Anti-Spoofing

- 论文编号：2430
- 报告人：Anton Firc
- 程序：Tuesday 29 September 2026 / Speaker Verification and Anti-Spoofing
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/firc26b_interspeech.pdf

## 问题
SSL+AASIST 图池化反欺骗常用但公开实现含冗余操作，算力偏高；需在不牺牲判别力下简化后端，并兼顾域外稳健与校准。

## 方法
SpAArSIST：保留 XLS-R 前端与 AASIST 图交互骨架，改三点——训练/推理分离的 top-k 保留比 (k_tr, k_inf)；用节点特征幅度（L2）替代可学习打分；用均值聚合替代高温 softmax 的 stack-node 注意力（或降温度对照）。在 ASVspoof 5 两阶段训练，并在 In-the-Wild 测域外。用判别+校准+算力的双轨复合分排序配置。

## 实验与结果
最佳配置后端 MACs 195.045M→154.706M（约 −20.7%），参数 611.8k→586.4k（−4.1%）；ITW EER 4.64%→2.82%、minDCF 0.133→0.078；ASVspoof 5 上仍具竞争力。幅度打分 + 更激进剪枝（如 k_tr=0.3, k_inf=0.1）常居复合分前列。

## 结论
简化图池化与读出可在降算力同时提升域外稳健；训练–推理分离稀疏比为部署提供旋钮。复合分便于在准确、校准与算力间选模型。

## 点评
相对“加模块刷分”路线，做减法并量化每项贡献，工程价值高。幅度代理可解释但未必普适；结论依赖固定 XLS-R 配方，跨前端迁移需再验证。


# Linguistic Bias Mitigation for Spoofing Detection via Gradient Reversal and A Variational Information Bottleneck

- 论文编号：676
- 报告人：Mickael Rouvier
- 程序：Tuesday 29 September 2026 / Speaker Verification and Anti-Spoofing
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/dao26_interspeech.pdf

## 问题
ASVspoof 5 上 bona/spoof 的所说内容分布不匹配，检测器可能走语言捷径而非生成伪迹，导致跨库泛化差；无转录时难以直接对齐文本。

## 方法
SONAR 与自建短语内容教师嵌入的聚类/t-SNE 诊断语言偏置。IVLing-VIB：Common Voice 英语子集训 XLSR+MHFA 短语 ID 教师；学生含 spoof 头与经 GRL 的短语内容头，对抗压低语言信息；内容支路用 MHFA-VIB（对 key 做高斯后验+KL）约束抑制强度，避免误删有用伪迹线索。在 ASVspoof 5 训练，于 DF Arena 多英语集评测。

## 实验与结果
相对 MHFA，IVLing-VIB 跨集合并阈值 EER 约降 36% 至约 9%；多数单集最低（如 ITW 1.88%、ASV19 LA 4.07%）。相对挑战榜前列，ASVspoof 5 本集略高但其他库大幅更好，平均 EER 3.97%。

## 结论
语言偏置是跨数据退化的重要来源；教师–学生 GRL + VIB 可在无测试转录下学语言不变表示并提升泛化。

## 点评
把 shortcut 从静音等已知偏置扩到内容分布，分析与方法衔接清楚。教师在外部短语分类上的代理质量决定上限；过强对抗仍可能伤说话人/信道相关线索，VIB 是必要缓冲。


# Spectral Masking and Interpolation Attack (SMIA): A Black-box Adversarial Attack against Voice Authentication and Anti-Spoofing Systems

- 论文编号：2736
- 报告人：Kamel Kamel
- 程序：Tuesday 29 September 2026 / Speaker Verification and Anti-Spoofing
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kamel26_interspeech.pdf

## 问题
语音认证与反欺骗常被合成语音及对抗扰动绕过；既有黑盒攻击对联合 VAS+CM 管线或加固商业系统效果有限。作者从防御评估视角报告一种针对不可闻谱区的黑盒对抗威胁。

## 方法
论文提出 SMIA：在克隆/合成语音上，用黑盒优化（基于查询反馈的贝叶斯式参数搜索）调节谱掩蔽与插值类扰动，目标是在保持听感自然的同时同时迷惑说话人验证与反欺骗。威胁模型假设仅标签或分数反馈、无模型内部信息。本文摘要层面不展开具体参数搜索与扰动实现细节。

## 实验与结果
作者报告：对独立 CM 攻击成功率最高约 100%，对 VAS 约 97.5%，对联合管线约 82%；在 ASVspoof 2019 / LibriSpeech 及过线仿真条件下优于若干既有基线；消融显示插值、掩蔽与混合模式对不同检测器贡献不同。

## 结论
作者认为静态检测易被谱域不可闻扰动绕过，呼吁更动态自适应的防御。局限包括真实部署约束、告警机制与法律合规场景未充分讨论。

## 点评
属安全评测向的攻击论文，价值在揭示联合认证–反欺骗管线的脆弱面。摘要级方法描述足以把握威胁主张；完整复现参数与优化目标见原文，防御侧应关注不可闻谱区建模与查询限流等加固，而非照搬攻击流程。


# BiSASV: Bidirectional Feature Modulation with Dual-Granularity Fusion for Spoofing-Robust ASV

- 论文编号：1532
- 报告人：Ji Liu
- 程序：Tuesday 29 September 2026 / Speaker Verification and Anti-Spoofing
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhou26d_interspeech.pdf

## 问题
SASV 特征融合多把 CM 分数单向门控 ASV，忽略说话人全局上下文对伪迹标定的帮助，且 ASV/CM 特征需求冲突使端到端难平衡。

## 方法
BiSASV：预训练 ECAPA-TDNN（ASV）与 AASIST（CM）。双向调制——用注册/测试 ASV 均值方差与余弦相似度拼成 z_stat，经 FiLM（γ,β）仿射调节 CM 特征；增强后的 CM 再经 sigmoid 通道门控 ASV。双粒度融合：粗粒度把 CM 特征与余弦相似度映射；细粒度对 ASV 交互向量（拼接差与积）做通道重加权后与粗特征拼接。联合训练，无需交替更新。

## 实验与结果
ASVspoof 2019 LA：SASV-EER 0.73%、min a-DCF 0.0153（95% CI 见文），显著优于单向 ATMM-SAGA（约 2.18%/0.048）及多种分数/嵌入融合基线；SV-EER 1.02%、SPF-EER 0.47%。

## 结论
ASV↔CM 互惠调制加粗–细双路径可提升欺骗稳健说话人验证，超越单向门控范式。

## 点评
把说话人统计显式注入 CM 再回控 ASV，闭合了单向设计缺口。强依赖强预训练专家；在更新攻击/域移上的稳定性未在本文充分展开。


# AGENT: A Black-box Adversarial Attack Exposing the Achilles' Heel of SASV Systems

- 论文编号：3207
- 报告人：Yowon Lee
- 程序：Tuesday 29 September 2026 / Speaker Verification and Anti-Spoofing
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26x_interspeech.pdf

## 问题
SASV 通过 ASV+CM 联合决策缓解欺骗与对单 ASV 的对抗；针对完整管线（级联或分数融合）的黑盒对抗仍不足，既有方法常依赖辅助网络或迁移弱。

## 方法
论文提出 AGENT：在替身 ASV/CM 上联合优化，使输入扰动同时抬高说话人相似度并维持反欺骗通过；用方向选择式梯度融合缓解两目标梯度冲突，再在幅度约束下迭代更新，并将样例迁移到受害 SASV。强调分数最大化以加强跨架构迁移。本文摘要不复述算法逐步更新式与超参配方。

## 实验与结果
作者报告跨多种 SASV 配置攻击成功率最高约 99.62%；在级联结构上相对 FAKEBOB、Double-deceiver 等基线显著更高，并在替身–受害架构不匹配时仍保持较强迁移。

## 结论
作者认为当前 SASV 联合边界仍可被专门设计的黑盒对抗击穿，需更强实战防御。价值在安全评测与风险提示。

## 点评
把攻击目标从单 ASV 扩到 ASV–CM 联合决策，指出梯度冲突是联合攻击难点。防御侧宜关注联合对抗训练、查询限流与决策校准；完整攻击程序细节应留在原文，本总结仅记录研究主张与量级结果。

