# UniVoice: Unifying Autoregressive ASR and Flow-Matching based TTS with Large Language Models

- 论文编号：2194
- 报告人：Wenhao Guan
- 程序：Thursday 1 October 2026 / Speech Production and Perception 2
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/guan26b_interspeech.pdf

## 问题
现有 LLM 语音框架常把 ASR 与 TTS 割裂；离散 codec token 便于统一建模但量化损失会损害识别精度与合成保真度。需要在连续表示空间里同时做自回归理解与高保真生成。

## 方法
UniVoice 以 SmolLM2-360M 为骨干：ASR 支路用 Whisper 编码器 + adapter 池化进入 LLM，因果掩码自回归预测文本；TTS 支路用 OT 条件 flow matching，以文本前缀引导的 speech infilling 在 DiT 风格 Transformer（去掉 AdaLN-zero，时间嵌入拼到噪声 mel 序列前）上重建被掩码 mel，双向注意力；总损失为 λ·LM + CFM，推理时 TTS 用参考音/文做 prompt 并经 BigvGAN 声码。

## 实验与结果
在 LibriHeavy 50K 小时训练。统一模型 SIM 0.56、TTS WER 4.06、UTMOS 3.72，LibriSpeech ASR WER clean/other 为 3.0/6.3，相对多个统一基线有竞争力；相对专用 CosyVoice2 等仍有 SIM/自然度差距。消融：infilling 优于 speaker embedding 条件；TTS 用 Full Mask 明显优于 AR Mask；λ=0.005 优于 0.01。

## 结论
单一连续表示 LLM 可同时胜任自回归 ASR 与 flow-matching 零样本 TTS；双注意力掩码与文本前缀 infilling 是打通因果/双向分歧的关键。当前聚焦 ASR+TTS，未来拟扩展更多语音任务并开源。

## 点评
用连续 mel + FM 避开离散 token 信息损失，同时用双掩码解决 AR/非 AR 结构冲突，设计动机清晰。联合训练相对单任务有可懂度收益但也有自然度折中，且去掉 AdaLN 可能削弱说话人适应——作者也承认 SIM 落后专用 TTS。参数量（0.4B）与 50K 小时数据下能逼近更大统一模型，对端侧一体化交互有实用意义。
