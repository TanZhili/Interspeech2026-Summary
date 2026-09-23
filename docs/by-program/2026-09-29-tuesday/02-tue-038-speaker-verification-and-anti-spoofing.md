# Speaker Verification and Anti-Spoofing
- 日期：Tuesday 29 September 2026 / 时间：09:00-11:00 / 形式：Oral（Area 4）/ 论文数：6
- 材料：官方程序论文摘要。未出现的数字与细节不写。

## 技术趋势

本场同时覆盖反欺骗（anti-spoofing）检测器改进、语言学偏置缓解、欺骗鲁棒 ASV（SASV）双向融合，以及针对 CM / VAS / SASV 管线的黑盒对抗攻击。攻防同台：一侧追求更低 EER、更好校准与部署效率，另一侧展示静态检测器可被频谱操控或联合梯度攻击击穿。

训练策略上出现“看似用参考、实则学到不变性”的现象：RAT 显示参考通道在推理中贡献迅速消失，但参考增强训练仍提升检测；SpAArSIST 则从 AASIST 后端删冗余，用显式池化比与幅度打分换算力。泛化瓶颈被归因于语言线索依赖，梯度反转教师–学生加 Variational Information Bottleneck 用于压制语言信息同时保留非语言线索。

SASV 融合从单向 CM→ASV 走向双向调制与双粒度融合。攻击侧 SMIA 与 AGENT 分别强调不可听频段操控与解决 ASV–CM 梯度冲突的分数最大化，摘要报告的高攻击成功率被用来论证需要动态自适应防御。

## 技术内容

### 反欺骗训练、部署压缩与语言不变性

**RAT: Reference-Augmented Training for ASV Anti-Spoofing**（论文 132；presenter：Vojtěch Staněk）
观察带说话人参考的反欺骗架构在推理中实际忽略参考，但参考增强训练仍诱导有利于 deepfake 检测的不变性。提出 RAT：即使推理用零向量替换参考也优于单话语基线。摘要报告 ASVspoof 5 上单检测器 SOTA 级 EER 与 minDCF。

**SpAArSIST: Sparsified AASIST for Efficient and Reliable Anti-Spoofing**（论文 2430；presenter：Anton Firc）
面向部署精简 SSL 反欺骗常用的 AASIST 图池化后端：分离训练/推理池化比、幅度节点打分、均值聚合。摘要称后端算力与参数下降，In-the-Wild 鲁棒性提升，并提供综合准确率、校准与算力的选择分数。

**Linguistic Bias Mitigation for Spoofing Detection via Gradient Reversal and A Variational Information Bottleneck**（论文 676；presenter：Mickael Rouvier）
域外泛化差可归因于语言偏置。语言感知教师经梯度反转引导学生减少语言信息，并用 Variational Information Bottleneck 避免误删非语言线索。摘要称在九个 DF Arena 数据集上相对基线最大相对 EER 降幅。

### SASV 双向融合与黑盒对抗攻击

**BiSASV: Bidirectional Feature Modulation with Dual-Granularity Fusion for Spoofing-Robust ASV**（论文 1532；presenter：Ji Liu）
既有特征级 SASV 融合多为单向 CM→ASV。BiSASV 建立双向流：向 CM 注入全局说话人上下文，增强 CM 特征再门控 ASV 嵌入，并探索双粒度融合。摘要给出 ASVspoof 2019 LA 上 SASV-EER 与 min a-DCF。

**Spectral Masking and Interpolation Attack (SMIA): A Black-box Adversarial Attack against Voice Authentication and Anti-Spoofing Systems**（论文 2736；presenter：Kamel Kamel）
黑盒攻击在 AI 生成音频的不可听频段做掩蔽与插值，同时欺骗 VAS 与 CM。摘要报告在开源与商业系统、模拟真实条件下对独立 CM、VAS 及组合管线的攻击成功率，并呼吁动态自适应防御。

**AGENT: A Black-box Adversarial Attack Exposing the Achilles' Heel of SASV Systems**（论文 3207；presenter：Yowon Lee）
针对完整 ASV–CM 管线：分数最大化目标放大 ASV 置信，方向选择梯度融合解决模块间梯度冲突。摘要称跨多种 SASV 架构攻击成功率可达很高水平，揭示现有 SASV 脆弱性。

## 本场要点
- 参考增强训练可提升反欺骗，即使推理不再依赖参考通道。
- 部署导向的 AASIST 稀疏化在降算力同时改善部分域外指标。
- 语言偏置被明确为跨域泛化失败机制之一，需对抗式去语言信息。
- SASV 融合走向 ASV↔CM 双向调制与多粒度线索。
- 黑盒攻击同时瞄准认证与反欺骗，静态 CM 假设受挑战。
- 攻防结果均以各摘要自报指标为限，不宜跨数据集直接对比。

## 覆盖核对
`132 | RAT: Reference-Augmented Training for ASV Anti-Spoofing`
`2430 | SpAArSIST: Sparsified AASIST for Efficient and Reliable Anti-Spoofing`
`676 | Linguistic Bias Mitigation for Spoofing Detection via Gradient Reversal and A Variational Information Bottleneck`
`2736 | Spectral Masking and Interpolation Attack (SMIA): A Black-box Adversarial Attack against Voice Authentication and Anti-Spoofing Systems`
`1532 | BiSASV: Bidirectional Feature Modulation with Dual-Granularity Fusion for Spoofing-Robust ASV`
`3207 | AGENT: A Black-box Adversarial Attack Exposing the Achilles' Heel of SASV Systems`
