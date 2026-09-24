# SARA: A Dual-Stream VAE for High-Fidelity Speech Generation via Integrating Semantic and Acoustic Representations

- 论文编号：2082
- 报告人：Peijie Chen
- 程序：Wednesday 30 September 2026 / Acoustic Signal Analysis and Generation
- 技术分类键：signal
- 全文：https://www.isca-archive.org/interspeech_2026/chen26v_interspeech.pdf

## 问题
零样本 TTS 的语音 tokenizer 在保真与可控间权衡：声学编解码保细节但缺语言约束（易内容错），SSL 语义 token 对齐好但丢音色/韵律。加复杂语义正则往往难平衡。

## 方法
SARA 双流 VAE：冻结 W2v-BERT 2.0 作语义锚 + 残差 CNN–LSTM 声学编码器，50 Hz 对齐后拼接投影为 64 维连续潜变量；HiFi-GAN 式解码器，多尺度 mel + 对抗/特征匹配 + KL。在 LibriTTS+LibriHeavy（>50k 小时，统一 24 kHz）训练。下游以 F5-TTS 用 SARA 潜变量替代 mel 做零样本 TTS。

## 实验与结果
- 重构（LibriSpeech test-clean）：PESQ 4.389、STOI 0.993、UTMOS 4.100，优于 Vanilla VAE / Semantic-VAE / Vocos。
- 下游 F5-TTS-Small+SARA：WER 1.79、SIM 0.63；Base+SARA：WER 1.74、SIM 0.655，内容准确优于 CosyVoice/E2 TTS/原版 F5。
- 消融：去残差编码器 SIM/PESQ 大降；去 SSL 则 WER 变差。NFE=8 时仍可接近 32 步基线质量（RTF 0.079 vs 0.115）。

## 结论
结构上直接融合语义锚与声学残差，无需复杂正则即可在紧凑潜空间兼顾重构与生成；加速推理下仍稳。未来拟多语与自回归扩展。

## 点评
用“冻结 SSL + 学残差”把 Semantic-VAE 的正则思路换成架构约束，简洁且消融干净。50 Hz/64 维瓶颈对 flow matching 友好，解释了低 NFE 仍稳。训练数据与评测同属有声书英语域，跨领域/多语鲁棒性仍待验证。
