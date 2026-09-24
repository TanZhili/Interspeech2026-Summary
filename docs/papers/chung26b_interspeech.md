# Robust Audio-Visual Emotion Recognition via Conditional Transformer U-Nets with Frequency-Injected Visual Stream

- 论文编号：2770
- 报告人：Hanwook Chung
- 程序：Thursday 1 October 2026 / Speech Emotion Recognition and Representation 3
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chung26b_interspeech.pdf

## 问题
噪声与混响严重损害 SER，进而拖累音视频情感识别（AVER）；现有多模态工作较少显式建模恶劣声学，视觉侧也少用频域线索刻画微表情动态。

## 方法
双路 CTr U-Net：音频流对 log-Mel 做 inverse-filtering CTF 前端增强，再进情感编码器+情感条件辅助特征解码器；视觉流用 EfficientFace 特征，在 CTr 的 Q/K/V 上注入空间维 FFT 对数幅度（frequency-injected）；瓶颈特征经融合解码器（含 prompt generation module）分类。两阶段训练：先 MAE 训前端，再联合交叉熵与重建正则。

## 实验与结果
CREMA-D / RAVDESS / IEMOCAP，噪声与 RIR 分 seen/unseen。干净 AVER：CREMA-D UAR/WAR 89.14/89.11，RAVDESS 91.69/90.97。鲁棒 AVER（cCTrU-FE）相对干净训练基线大幅稳住（如 CREMA-D 平均 UAR 86.14 vs 74.41）。鲁棒 SER 在 IEMOCAP+NOISEX 多 SNR 上优于多项基线（如 0 dB seen improvised UAR 75.76）。频注入与情感条件解码均有消融增益。

## 结论
作者认为 inverse-filtering 前端、频注入视觉与情感条件辅助解码共同提升恶劣声学下的 AVER 稳健性。

## 点评
把 dereverberation 直接嵌进 LMFB 域并与视觉频注入并联，工程完整。对比表跨论文设定不一，绝对排名需谨慎；RAVDESS 上个别先前工作 WAR 仍更高，显示数据集依赖。
