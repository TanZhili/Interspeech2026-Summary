# Towards Detecting Neural Audio Codec Synthesized Heart Sounds

- 论文编号：2116
- 报告人：Orchid Chetia Phukan
- 程序：Thursday 1 October 2026 / Spoofing and Deepfake Detection 3
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/girish26_interspeech.pdf

## 问题
心音（PCG）被视为难伪造的活体生物特征，但神经音频编解码器（NAC）可合成感知上接近真实的心音，对心音生物识别构成新威胁。尚无针对 NAC 合成心音的检测任务与公开基准。

## 方法
提出 Synthetic Heart Sound Detection (SHAC)，并发布 CARDIOFAKE：基于 CirCor DigiScope（3163 条真实 PCG），经 7 种 NAC（DAC、EnCodec、SoundStream、Speech Tokenizer、FunCodec、AudioDec、SNAC）encode–decode 得到 22141 条合成样本；划分 seen（训练见过的 codec）与 unseen（FunCodec、AudioDec）协议。特征侧评估 MFCC/LFCC 与冻结 SSL（Wav2vec2、Unispeech-SAT、WavLM）平均池化表示，下游用 FCN 或 1D-CNN。融合框架 GROOT：两支特征经 CNN 投影后，用基于 gram 矩阵 Frobenius 距离的 Sinkhorn 最优传输（Gram-OT）互相对齐并与原特征拼接，再经 FCN 二分类。

## 实验与结果
身份保持实验：Real→Fake 用户识别准确率仍达 86.29%（Real→Real 89.11%），说明合成心音高度保留身份。单特征：CNN+WavLM 最强（seen EER 9.45%、unseen 13.39%）。融合：MFCC+WavLM 的 GROOT 达 seen Acc 93.20%/EER 5.86%，unseen Acc 86.10%/EER 9.75%，优于简单拼接与普通 OT，也优于按相同训练设定的 AASIST、MiO 基线。

## 结论
作者认为 NAC 合成心音是可信且危险的身份保持伪造；CARDIOFAKE 与 GROOT（谱特征+SSL 的 Gram-OT 融合）为 SHAC 提供首个基准与强基线。

## 点评
把语音编解码伪造威胁迁移到心音模态，问题定义与数据管线清晰。GROOT 用 gram 空间对齐谱与 SSL，贴合“声学伪迹 vs 时序结构互补”的假设。脆弱处在于合成仅来自 resynthesis 闭环、未见更复杂攻击或信道失真，且 SSL 骨干仍是语音预训练，跨域表征是否最优未充分论证。
