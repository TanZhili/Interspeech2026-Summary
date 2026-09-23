# VAD to the Bone: Ultra-Tiny Speech Activity Detection for Edge Deployment

- 论文编号：2523
- 报告人：Shanza Iftikhar
- 程序：Monday 28 September 2026 / Audio segmentation
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/bauer26_interspeech.pdf

## 问题
端侧常开场景需要极小、低时延、可部署的 VAD，但近期紧凑模型常依赖可学习滤波带、RNN/特殊激活或非因果滑窗评测，与嵌入式 DSP/TFLM 工具链不兼容，且参数量或因果性能被夸大。

## 方法
提出 kiloVAD：标准 Mel 特征 + 纯 CNN（深度可分离卷积、全局平均池化、线性分类），用 1×1 adapter 解耦 Mel 维与内部通道，并对每帧 Mel bin 做窗内零均值单位方差归一化。压缩上：(1) 按层独立剪枝比，用 Optuna 多目标搜索（验证集 FPR@TPR=0.95 与参数量），剪后以未剪模型为教师做自蒸馏微调；(2) 角度感知自蒸馏 QAT：冻结全精度分类器权向量为原型，量化骨干特征对目标原型对齐、对非目标铰链排斥，针对低比特角度误差。默认约 200 ms 上下文、64 Mel bins；严格因果、无未来上下文与时间平滑的逐帧评测。

## 实验与结果
训练：LibriSpeech train-clean-100 混合清洁/风噪/DNS 噪声与部分混响。评测 AVA-Speech AUC。完整模型约 81.1k 参数、AUC 0.862；剪至 2.1k 仍约 0.850（相对未剪约 1.3% 内），匹配 MarbleNet 的 0.850 但参数少约 43×、上下文 200 ms 对 630 ms。INT8 近无损；INT4 下角度 QAT 相对标准 STE QAT 提升约 1–4%（如 2.1k：0.693→0.719）。上下文到 360 ms 可达约 0.872 AUC。

## 结论
作者认为在满足 Mel 前端、可移植算子、低时延与因果评测的前提下，kiloVAD 以极小 CNN + 按层剪枝与角度 QAT 达到可部署的因果 VAD SOTA 级表现；相对依赖特殊结构或非因果协议的紧凑模型填补了部署缺口。

## 点评
问题定义清楚：把“能不能上 MCU”拆成前端、算子、时延、因果四条硬约束，再围绕可剪枝 CNN 做压缩，比单纯追参数量更贴近工程。按层 Pareto 剪枝 + 角度几何 QAT 针对极端压缩是合理路线。对比表中他人数字协议不一，作者已提醒不可直接比 AUC；训练偏朗读语音加合成噪声、评测换域到 AVA，极端剪枝有种子层崩，仍需实机功耗/时延验证。
