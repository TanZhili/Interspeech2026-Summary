# Quantifying the Uncertainty of Blindly Estimated Room Embeddings Using a Dispersion-Calibrated Score

- 论文编号：1357
- 报告人：Yang Xiang
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xiang26_interspeech.pdf

## 问题
从混响语音盲估房间嵌入时，内容、噪声与丢包等会在房间与几何不变时扭曲表示，下游不可靠；现有工作缺少面向表示可靠性、可单句推理的任务无关不确定性分数。

## 方法
三阶段：Stage-1 在 RIR log-mel 上训 VAE 得结构化潜空间；Stage-2 用混合 CNN–Transformer 语音编码器，多视角 batch（同 RIR 多句）做 KL 对齐到冻结 RIR 后验，并加 multi-positive 对比；Stage-3 冻结编码器，用轻量 MLP 头预测不确定性 U，以干净–损坏嵌入余弦色散 δ 为监督，margin 排序损失保证 U 与 δ 单调一致。

## 实验与结果
约 3000 实测 RIR×EARS 语音。Proposed 验证 AP=0.99，MAErec≈4.06 dB，优于 FiNS 与 MRL-SV；多视角是内容鲁棒主因，对比项带来小幅验证增益。U 与 δ 全局 Spearman ρ=0.90（噪声/频掩/时掩均高），选择性预测上优于按 corruption 强度排序。

## 结论
多视角对齐 + 色散校准不确定性可在单句推理下识别不可靠房间嵌入；局限包括非真正后验、训练需 clean–corrupt 对、按 RIR 划分而非严格房间不相交、损坏类型有限。

## 点评
把“嵌入是否可信”从下游任务解耦成表示级分数，对检索/参数估计统一有用。多视角消融清晰；野外干扰说话人、设备失配等未覆盖，分数解释仍属相对排序而非校准误差条。
