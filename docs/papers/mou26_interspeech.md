# DuraMark: Duration-Embedded Watermarking in LLM-based TTS

- 论文编号：2298
- 报告人：Zhenwei Mou
- 程序：Thursday 1 October 2026 / Audio Watermarking and Source Verification
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/mou26_interspeech.pdf

## 问题
LLM-TTS 高逼真克隆带来 deepfake 风险。主流信号级水印易被神经编解码/声码器等生成式重合成抹掉；既有信息级方法（如改 pitch）又易导致韵律不自然。

## 方法
DuraMark 在信息级嵌入：基于 CosyVoice 式 LLM + flow matching 的时长可控 TTS，按音节预测时长与语音 token，并用时长提取器（文本–Mel Transformer 帧级归属）与 guide loss 强制解码器遵循指定时长。嵌入时将各音节时长奇偶编辑到目标比特（0/1）；检测时提取时长序列，映射到 [-1,1] 后与水印相关，超阈值 τ 判有水印。支持知情检测（真值文本）与盲检（ASR 转写）。

## 实验与结果
WenetSpeech 训练、AISHELL-3 评测。33–64 音节时 Info/Blind TPR@1%FPR 约 0.998/0.987。对 EnCodec/DAC/SpeechTokenizer/FACodec、多类声码器、增强、压缩与常规信号处理，DuraMark 平均 TPR 约 0.993（Info）/0.978（Blind），显著高于 AudioSeal、Timbre、WavMark（后者在多数生成攻击下崩溃）。CER/MOS 与未加水印接近。消融去掉 duration 输入或 L_guide 后 TPR 大幅下降。

## 结论
作者认为通过合成阶段编辑音节时长可实现抗生成式攻击的稳健水印，同时保持自然度；显式时长控制与引导损失是关键。

## 点评
把水印从波形细节挪到韵律时长，正好避开信号级“被重合成抹平”的弱点。依赖文本/音节对齐与中文一字一音节设定；盲检依赖 ASR，跨语种与强时间拉伸攻击下的表现正文未充分展开。
