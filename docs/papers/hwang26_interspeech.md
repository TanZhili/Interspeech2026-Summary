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
