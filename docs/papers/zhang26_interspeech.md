# AURA: Audio-Geometry Conditioned U-Net Refinement with Flow Matching for High-Fidelity Monaural-to-Binaural Synthesis

- 论文编号：87
- 报告人：Wenjie Zhang
- 程序：Tuesday 29 September 2026 / Spatial Audio 3
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26_interspeech.pdf

## 问题
从单声道合成双耳声需在保持音色细节的同时推断空间线索，传统 HRTF 管线难适应动态相对位姿与真实环境；现有深度学习方法仍难达到与真实录音难以区分的保真度。作者聚焦仅单声道+几何条件的设定。

## 方法
两阶段框架 AURA：(1) 经 Time Dynamic Warping 后，用 Transformer–CNN 下采样块（TCDB）与空间增强残差上采样块（SERUB）生成粗糙双耳估计，并以 Spatial-Awareness and Motion Attention（SAMA）融合位姿（位置+四元数朝向）；(2) 条件流匹配（CFM）以粗糙估计加噪为先验、真值为目标，在 OT 线性路径上学习速度场并 ODE 积分细化。总损失含波形 L2、相位/幅度 STFT 损失与 LCFM。

## 实验与结果
数据为 [11] 的 KEMAR 室外约 2 小时 48 kHz 配对单/双耳录音。客观：Wave-L2 0.123、Amp-L2 0.028，优于 BinauralGrad（0.128/0.030）等；Phase-L2 0.843。主观（15 听者）：MOS 3.82、Spatial MOS 3.89、Similarity MOS 4.21，均高于对比方法。消融去掉 TDW、Trans/CNN 分支、SAMA 或 CFM 均使 Wave-L2 变差，无 CFM 时升至 0.183。

## 结论
作者认为混合 U-Net 粗估计 + 流匹配细化、配合音频–位姿交互，可提升单声道到双耳的自然度与保真度；后续将探索更真实场景下的双耳合成。

## 点评
把流匹配用作“粗预测残差细化”而非端到端生成，较贴合单声道缺空间信息的结构。客观与主观一致优于扩散类两阶段基线，且参数/MACs 相对可控。弱点是评测依赖单一公开数据集与固定分裂，Phase-L2 并非最优，空间 MOS 跨模型差距也相对有限。
