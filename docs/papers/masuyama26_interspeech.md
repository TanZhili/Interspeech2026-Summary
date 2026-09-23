# HRTF Personalization via Sim-to-Real Neural Field

- 论文编号：1391
- 报告人：Yoshiki Masuyama
- 程序：Monday 28 September 2026 / Spatial Audio 1
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/masuyama26_interspeech.pdf

## 问题
个性化 HRTF 测量昂贵；仅靠 Mesh2HRTF 等仿真在高频有伪影。希望从日常可得的 3D 头模仿真，经 sim-to-real 得到逼近实测的个性化 HRTF，且无需实验室稀疏测量。

## 方法
S2RNF：共享神经场对方向 d、受试者参数 z_i、域参数 w_j（仿真 j=0 / 实测 j=1）预测 log-magnitude。推理时用 IGON 一步梯度从仿真 HRTF 推 ˆz_i（固定 w_0），再换 w_1 预测实测域。训练显式走同一路径，最小化实测损失 L1 + λL0（λ=1）。架构为 RFF 方向 + BitFit 式 FC（受试者/域偏置）。数据：扩展 SONICOM（200 对仿真–实测，160/15/25）；HUTUBS leave-one-out（对比 SPCA-DNN、BEM-DNN、Proto. DNN）。指标 MAE/RMSE/PolRMSE。

## 实验与结果
SONICOM：S2RNF MAE/RMSE/PolRMSE = 3.60/4.90/40.89，优于平均 HRTF 3.78/5.05/41.63 与 Mesh2HRTF 7.50/10.53/42.27（MAE 配对 t 检验 p=1.5%）；去 L0 变差。频谱上约 5–15 kHz 失真明显下降。HUTUBS：MAE 3.66，优于报告的 BEM-DNN 4.80，略优于 Proto. DNN 3.69，且不需人体测量特征编码器。

## 结论
域参数使受试者潜变量可从仿真推断并切换到实测域，实现无测量个性化；优于纯仿真与若干既有方法。未来拟用摄影测量头模。ITD 个性化留待后续。

## 点评
把 SuDaField 式域条件改造成可训练的显式 sim-to-real 路径，IGON 免额外编码器是实用点。增益相对平均 HRTF 不大但统计显著，且高频修正符合 Elevation 线索；对仿真网格质量与头模精度仍敏感。
