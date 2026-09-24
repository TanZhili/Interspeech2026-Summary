# AudioNoisePrints: Model-free audio watermarking using spatial correlation in flow matching TTS

- 论文编号：2165
- 报告人：Timothy Tin-Long Tse
- 程序：Thursday 1 October 2026 / Audio Watermarking and Source Verification
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/tse26_interspeech.pdf

## 问题
Flow matching / diffusion TTS 水印若用后处理会改音质并有额外开销，且易被同款开源水印覆盖；若重训模型则成本高、可能伤质量。需要不重训、不改生成质量的水印方案。

## 方法
AudioNoisePrints 利用初始高斯噪声与生成 Mel/音频之间的空间相关：生成时使用由哈希确定的特殊初始噪声；检测用余弦相似度（或点积）相对随机噪声的经验 p-value 判定（model-free）。另训轻量 4 层 Conv2D ResNet 检测器，对指定噪声周期平铺到 Mel 帧长，并以压缩等增强提高稳健性。在 F5-TTS、MatchaTTS 及 DiffWave 声码器上验证相关性质。

## 实验与结果
相对 AudioSeal：强增强下（噪声、滤波、裁剪、变速等）整体更稳，尤其速度拉伸时 AudioSeal 几乎失败而本方法仍可用；MP3 影响很小；Echo 上本方法较弱。余弦相似度优于 L1/L2。多模型上 originated noise 与输出的相似度显著高于随机噪声（p≈0）。检测器在 AAC 等压缩上可达约 0.99 准确率。

## 结论
作者认为对 FM/diffusion TTS（及声码器）可在零生成开销、不伤音质下做可检测水印，且空间相关具一定普适性；可选外部检测器提升复杂攻击下的稳健性。

## 点评
把图像域 NoisePrints 迁到音频，抓住“噪声指纹”而非改波形，产品友好。需持有/复现初始噪声假设，适合“我自己的合成管线可追溯”；对未知模型来源或彻底重采样后的伪造场景覆盖有限，Echo 等未训增强仍是短板。
