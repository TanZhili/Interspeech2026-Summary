# SpkGuideDOA: Speaker-wise Representation Guidance for Multiple Moving Speaker Localization

- 论文编号：3131
- 报告人：Yongseok Choi
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/choi26g_interspeech.pdf

## 问题
多移动说话人定位在轨迹交叉、角度重叠时仅靠空间 cue（如 DP-IPD）难稳定分轨；分离再关联或 SELD 多任务方案又重、或与纯定位目标不符。

## 方法
SpkGuideDOA：Spatial Cue Estimator 估 DP-IPD；Guidance Generator 从多通道幅度经 band-wise 特征与 SP-SimA+Mamba 得到说话人引导图，在池化分辨率上对 SCE 特征做 sigmoid 门控残差调制。训练用 Joint-PIT 共享排列，LIPD+αLVAD；VAD 损失梯度不回传到 SCE，保持定位为主任务。

## 实验与结果
仿真与 LOCATA：Ours MDR/FAR/MAE 仿真 4.0%/15.8%/5.7°、真实 9.2%/8.9%/5.5°，优于 IPDNet、TF-Mamba、IPDNet2，FLOPs 与 IPDNet2 同为 1.1 G/s。小角度间隔时检测与 MAE 更稳。消融去 GG、去 VAD、VAD 挂到 SCE、去 Joint-PIT 均变差。

## 结论
池化说话人残差引导可缓解重叠歧义并保持低开销；框架可扩展到更多说话人数。

## 点评
把“说话人区分”做成 localization enhancer 而非分离/多任务头，梯度路由与 Joint-PIT 设计干净。K=2 与仿真轨迹设定下结果强；更大 K、更极端交叉与在线时延仍是压力测试点。
