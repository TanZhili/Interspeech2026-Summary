# NeuroMultiSpEx: Neuro-Guided Target Speaker Extraction for Multi-Speaker Scenarios

- 论文编号：1120
- 报告人：Siqi Cai
- 程序：Tuesday 29 September 2026 / Target Speaker Extraction, Speech Separation and Audio Understanding
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/silva26_interspeech.pdf

## 问题
神经引导说话人提取多用 scalp-EEG、且几乎只做 2 说话人；真实鸡尾酒会常 ≥3 人，排列歧义更大，仅 envelope 或仅身份线索不足，可穿戴 ear-EEG（cEEGrid，20 通道）信息量也更受限。

## 方法
NeuroMultiSpEx 输入 4 说话人混合物 + 20 通道 ear-EEG：EEG-Envelope Encoder（Pre-Conv + 4×SA/TCN）重建目标 envelope 并输出时序线索；EEG-Speaker Encoder（XAGnet：双耳 GCN + 跨耳 CA，MHA Adapter）输出 4 类身份与时序身份特征；Gated Fusion 自适应加权“何时/何人”得 HRef；Conv-TasNet 式提取网络用交叉注意力以 HRef 为 Query 调制混合编码并生成 mask。联合损失 SI-SDR + λ1 CE + λ2 PCC。

## 实验与结果
PKU Ear-EEG（16 人，±30°/±90°，0 dB SNR，trial 独立 80/10/10）：NeuroMultiSpEx SI-SDRi 9.613、PESQ 2.08、STOI 0.708、AAD 82.4%、envelope PCC 0.023，显著优于 NeuroSpEx+（8.904 / 1.84 / 0.683）等基线。说话人编码器消融：XAGnet 优于 FC/CNN/STAnet/XAnet；去掉身份编码器降幅最大（−0.407 dB），去掉门控改拼接亦降约 0.2 dB。

## 结论
在可穿戴 ear-EEG 上首次将神经引导提取扩展到 4 说话人；时序与身份双线索加学习门控优于单线索，朝脑控助听更近一步。局限含跨被试、混响与听障用户未评。

## 点评
抓住多说话人下“错抽干扰”的排列风险，用 AAD 式身份显式消歧，再靠 envelope 补帧级“何时”。强在双编码器与门控设计贴合场景；评测说话人依赖、PCC 绝对值低反映 ear-EEG 空间分辨率限制，跨被试泛化仍是落地关键。
