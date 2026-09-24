# Semi-Supervised Joint Separation and Diarization for Multichannel Noisy Speech Mixtures

- 论文编号：3308
- 报告人：Yuto Nozaki
- 程序：Thursday 1 October 2026 / Source Separation 2
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/nozaki26_interspeech.pdf

## 问题
联合分离与日志（diarization）在多通道噪声混合中，neural FCASA 主要依赖空间协方差，对扩散噪声、近距离干扰或非平稳噪声稳健性不足，分离结果易残留噪声；完全仿真配对又易域失配，而真实环境又难拿到孤立语音源。

## 方法
在 neural FCASA（LGM + 联合对角化 SCM + 说话人活动）基础上做半监督扩展：训练时用干净语音混合（如会议录音）与噪声单独录音相加构造噪声混合。统一生成模型中显式写 \(x_{ft}=c_{ft}+n_{ft}\)，并给出干净混合的似然。半监督分离目标在原 ELBO 外加三项：阈值 SNR（\(L^{(snr)}\)）、干净混合负对数似然（\(L^{(nll)}\)）、多通道 Itakura–Saito 距离式后验项（\(L^{(misd)}\)）；日志仍用监督 BCE。推理网络结构沿用 RE-SepFormer + ISS 块。

## 实验与结果
用 JSALT2020 Simulate + LibriSpeech + DEMAND 构造 4 通道、最多 4 说话人合成会议数据（SNR 约 2–6 dB）。相对 Neural FCASA（SDR 12.3、PESQ 1.83、DER 4.2），组合三项目标的 P7 达 SDR 13.9、PESQ 2.18、UTMOS 2.19、DNSMOS 2.70、DER 3.6；单独 \(L^{(snr)}\) 对分离提升最大，\(L^{(nll)}\)/\(L^{(misd)}\) 对日志也有帮助。听感上可去掉 FCASA 残留的非平稳噪声。

## 结论
在无需孤立语音源的前提下，用干净混合与噪声录音的半监督目标可同时提升噪声场景下的分离与日志；后续拟扩展到移动说话人/噪声源。

## 点评
把“易采的干净混合 + 噪声”换成可解释的概率目标，比纯仿真更贴近真实会议，且与 FCASA 生成模型一致。仍依赖合成评测与固定阵列几何；空间模型本身对极近干扰或严重扩散噪声可能仍偏弱，三项权重需调。
