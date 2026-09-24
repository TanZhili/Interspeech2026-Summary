# OnDA: On-device Channel Pruning for Efficient Personalized Keyword Spotting

- 论文编号：1253
- 报告人：Alessio Burello
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/risso26_interspeech.pdf

## 问题
端侧个性化关键词检测既要适配用户/环境分布偏移，又受内存、时延与能耗约束。已有自学习流水线主要在线更新权重；架构（通道数）通常只做部署前离线剪枝，未必匹配现场分布。

## 方法
**OnDA** 在 [3] 的 ProtoNet 自学习管线（预训练 → 伪标签 → 端侧 triplet 微调）上加入结构化通道剪枝：
- **OnDA-1**：用数据感知 **HAP**（Hessian-trace 加权幅度）在适配初期、基于伪标签数据剪枝，再微调。
- **OnDA-2**：先微调，再用数据无关全局 L1 剪枝，再二次微调。
可与离线剪枝叠加。剪枝对象为卷积输出通道，得到仍稠密的子网络。

## 实验与结果
MSWC 预训练；HeySnips / HeySnapdragon 个性化评测。相对未剪基线，iso 任务表现（Acc@FARh=0.5）下最高约 9.63× 模型体积压缩；Pareto 前沿显示域内数据剪枝优于直接微调更小的离线剪枝网。Jetson Orin Nano：相对仅权重适配，训练/推理时延与能耗最高约 1.52×/1.57× 与 1.64×/1.77× 改善；数据感知剪枝可前置，从而降低后续微调成本。

## 结论
作者认为个性化 KWS 应同时适配权重与架构；用现场伪标签做在线结构化剪枝，可在保持任务表现下显著压缩并加速端侧训练/推理。

## 点评
问题提得准：分布偏移不只改最优权重，也改「够用多深的通道」。把 HAP 前移到适配起点，用少而贴域的伪标签做架构决策，比「先离线剪小再硬微调」更贴部署现实。脆弱点：伪标签噪声会影响 HAP 分数；二次微调增加流水线复杂度；结论主要来自两类唤醒词数据集与 Jetson 测量，换 MCU 级平台收益需另证。
