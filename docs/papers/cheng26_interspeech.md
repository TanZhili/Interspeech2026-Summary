# Diffusion Reconstruction towards Generalizable Audio Deepfake Detection

- 论文编号：158
- 报告人：Bo Cheng
- 程序：Monday 28 September 2026 / Speech Deepfake Detection: Robustness, Generalization, Attribution
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/cheng26_interspeech.pdf

## 问题
ADD 对未见攻击泛化差；若能区分“重建得到的难样本”，模型更可能应付简单样本。何种重建范式最能造出有效难样本，以及如何用对比与正则提升跨域泛化？

## 方法
用 HiFi-GAN、DAC、Encodec、SemantiCodec（扩散）等重建真实/伪造语音作难样本。冻结 XLS-R 300M + 多层自适应聚合 → AASIST。训练目标含分类 CE 与 RACL：标准对比损失 + 专盯真实/重建真实的增强对比损失 + 批内方差正则促类内紧凑。

## 实验与结果
五测试集平均 EER：基线 15.789%；扩散重建 12.220%（相对降约 22.6%）；加聚合与 RACL 后最佳平均 8.247%（ITW 9.155、CodecFake 20.198 等）。扩散重建整体优于 HiFi-GAN/DAC/Encodec。

## 结论
以扩散重建构造难样本，并结合多层聚合与 RACL，可显著提升未见攻击泛化。

## 点评
“难样本分类→易样本自然变好”的思路清晰，重建选型消融有说服力。增强对比只盯真实侧，针对重建伪迹；代价是训练需多路重建数据，且 CodecFake 等仍偏高，泛化未彻底解决。
