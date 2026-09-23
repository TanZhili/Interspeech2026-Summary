# Smooth Formant Tracking with Differentiable Linear Prediction

- 论文编号：1222
- 报告人：Bryn Luisi
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/luisi26_interspeech.pdf

## 问题
经典线性预测（LP）共振峰估计快且可解释，但假设局部平稳与高斯残差、帧间独立；混合神经方法更准却难可微、难嵌入端到端系统。

## 方法
LP-DDSP：以 log-area ratio（LAR）为可优化变量，经 Forward Levinson 得全极点系数，损失为残差 L2+0.5 L1+0.1 帧间 LAR 时序正则，Adam 迭代优化，再求根得共振峰。SMELP：CNN 由 STFT 预测 LAR，同一可微 LP 损失 + 与自相关 LP 系数 MSE + 共振峰监督 MSE，LSTM 解码轨迹。VTR Formants（TIMIT 子集）评测，仅在有共振峰音素上比 RMSE。

## 实验与结果
测试集总体 RMSE：LP-DDSP 246 Hz，优于 LP 基线 378、Praat 344，接近 KARMA 254；SMELP 166，优于 LP-LSTM 171，F1/F2/F4 最低。谱包络可视化显示 LP-DDSP 轨迹更平滑。

## 结论
可微 LP 损失可同时缓解非高斯残差与帧独立假设，并支撑可解释端到端共振峰跟踪；可扩展到其他语音处理任务。

## 点评
把经典全极点物理参数接进 DDSP，保留可解释性又允许反向传播。强处是 L1+时序正则设计清楚；脆弱处是仍依赖根挑选启发式，SMELP 监督仍用自相关 LP 作伪标签可能带偏差。
