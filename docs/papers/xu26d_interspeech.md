# Speech Enhancement Based on Drifting Models

- 论文编号：833
- 报告人：Liang Xu
- 程序：Monday 28 September 2026 / Neural Speech Enhancement: Survey, Diffusion and Flow Matching
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/xu26d_interspeech.pdf

## 问题
扩散/流匹配类增强推理常需多步离散化，低 NFE 难逼近弯曲轨迹；一致性蒸馏等一方法仍根植于轨迹压缩。需要一种原生单步、且可按分布匹配而非成对回归学习的生成式增强框架。

## 方法
DriftSE 将增强写成 pushforward 分布的平衡问题：映射 f_θ 一次输出增强样本，在冻结 SSL（HuBERT/WavLM/DistilHuBERT）多层潜空间用 mean-shift 式 Drifting Field（吸引干净帧、排斥当前生成帧）作 stop-grad 回归目标，使生成分布逼近干净分布。两种设定：直接映射 ˆx=f_θ(y+σϵ)；条件生成 ˆx=f_θ(ϵ,y)。骨干为无时间嵌入的 NCSN++V2；推理直接映射取 σ=0。因监督是 batch 内潜空间相似度，天然支持 unpaired 训练。

## 实验与结果
VoiceBank-DEMAND：DistilHuBERT、σ=0 达 PESQ 3.15、SI-SDR 16.1 dB，超 30 步 SGMSE+ 与一法 MeanFlowSE；加辅助 PESQ/SI-SDR 损失的 DriftSE† 更具竞争力。条件变体 SCOREQ 达 4.33、DNSMOS 3.64。DNS 2020 盲测：DistilHuBERT 变体 WV-MOS 2.65、SCOREQ 2.97 等领先或很强。Unpaired 跨数据集/跨性别仍有可用非侵入分（成对保真下降符合预期）。可视化显示潜空间分布由噪声向干净收敛。

## 结论
作者认为潜空间漂移场可在 1 NFE 对齐干净语音分布，达到有竞争力的感知与泛化，并支持完全 unpaired 设定，为原生单步生成式 SE 提供新范式。

## 点评
相对“压轨迹步数”，这里用分布平衡 + SSL 语义距离做生成监督，解释了为何能 unpaired。直接映射与条件生成在保真/感知上可切换，实用。依赖外部 SSL 层选择与温度核；† 变体加了成对指标损失后才逼近部分蒸馏基线，说明纯漂移未必在 PESQ 上压过强辅助损失系统。跨性别 unpaired 会改说话人属性，边界也写清楚了。
