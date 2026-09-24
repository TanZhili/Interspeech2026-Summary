# Tongue2Speech: Real-Time Speech Synthesis from Tongue Ultrasound Videos via Spatiotemporal Transformers

- 论文编号：3023
- 报告人：Yash Sonkar
- 程序：Thursday 1 October 2026 / Beyond Speech Technologies in Healthcare
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/sonkar26_interspeech.pdf

## 问题
仅用舌部超声（UTI）重建可懂语音时，既有方法多依赖 CNN/LSTM，长距协同发音建模不足；评价常停在 MSE/MCD，对词汇可懂度洞察有限；跨说话人零样本因解剖与探头放置差异极难。

## 方法
Tongue2Speech：原始 scanline（64×842）经极坐标到笛卡尔楔形（64×64）；四层 3D Conv 时空编码 → 自适应平均池化得每帧 256 维；六层 Transformer（8 头，FFN 1024）建模长距动态；MLP 预测 80 维 mel，HiFi-GAN 声码。总参 19.17M（不含声码器 6.25M），L1 mel 损失。在 TaL1/TaL80 上对比 Conformer-U2S、STN-CNN、多种 3D/2D+BiLSTM 变体；多说话人后对未见说话人短时微调。

## 实验与结果
单说话人 TaL1：整体 WER 15.93%、MSE 0.594，优于最强基线 3D-CNN+BiLSTM+Skip（WER 24.15%）；Conformer-U2S/STN-CNN 近饱和不可懂。多说话人 TaL80：WER 31.64%（Skip 变体 33.23%）。对说话人 78–81 微调后 WER 约 27.62–46.07%。评价用 Whisper Medium ASR。

## 结论
3D 时空编码 + Transformer 可在仅舌部超声下得到可懂合成；MSE 不能可靠反映词汇正确性。跨说话人泛化仍难，个性化微调是实用路径。

## 点评
把可懂度（WER）提到主指标，纠正了 U2S 过度依赖谱失真的习惯。单说话人到多说话人 WER 翻倍，说明几何可变性仍是瓶颈；探头摆放敏感在会话间仍有约 9 点 WER 波动。
