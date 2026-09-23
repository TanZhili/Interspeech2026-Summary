# ZeSTA: Zero-Shot TTS Augmentation with Domain-Conditioned Training for Data-Efficient Personalized Speech Synthesis

- 论文编号�?269
- 报告人：Youngwon Choi
- 程序：Monday 28 September 2026 / Scaling and Zero-Shot Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/choi26b_interspeech.pdf

## 问题
个性化 TTS 在目标说话人录音极少时难适配。用零样�?TTS 合成词句丰富的增强数据再微调轻量模型看起来可行，但作者观察到：大量合成音与少量真录音简单混训，可懂度上升�?*说话人相似度却掉**——模型被拉向合成域声学。需要不改主干架构、又能稳住身份的受控增强策略�?

## 方法
**ZeSTA**�?
1. 用开�?ZS-TTS�?*Fish-Speech**�?*CosyVoice 2**）在目标参考上合成分配给训练文本的语音；低资源设定保留 **Real 10%**，其�?**Synth 90%**（最长可用真录音�?prompt）�?
2. **Domain-conditioned training (DC)**：每条样本带 \(d\in\{\mathrm{real},\mathrm{synthetic}\}\) 域嵌入；文本编码器学说话人无关语言表示，声学模块条件于 \(d\)；推理时固定 \(d=\mathrm{real}\)。在多说话人 **VITS** 上复用说话人嵌入矩阵，隐层从 256 改为 **64** 作域嵌入�?
3. **Real-data oversampling (OS)**：真录音重复�?**3 �?*，强调稀缺真实域�?

目标模型先在 VCTK 按原 VITS 设定预训练；微调 LibriTTS 8 人与内部 YoBind 6 人语音助手数据，lr \(1\times10^{-5}\)�?00 epoch，单 A100�?

## 实验与结�?
指标：ECAPA-TDNN SECS、Whisper medium CER/WER；主�?MOS �?ABX�?
- Naive Real10+Synth90：相�?Real10 明显�?CER/WER，但 SECS 大跌（如 LibriTTS Fish�?.818�?.765）�?
- **DC+OS**：SECS 回升接近 Real10 / Real100（LibriTTS Fish/CV2 均约 **0.815**），同时保留合成带来的可懂度收益；两�?ZS-TTS 趋势一致�?
- 额外扩合成（VCTK 文本 + WER 低于 5% 过滤）：SECS 略降、CER/WER 再降�?
- 主观：MOS 不降；ABX 偏好提出法相�?naive 基线（LibriTTS FS 70.8%，YoBind 66.7% 等）�?
- 消融：OS 单独不稳；域嵌入 64 折中优于 16/256�?*说话人不匹配**合成相对匹配设置 SECS 更差�?.792 vs 0.807），说明需说话人一致增强�?

## 结论
ZS-TTS 增强有效，但必须用域条件与真数据过采样抑制合成域偏置；ZeSTA 在不�?VITS 主干下提升说话人相似度并保留可懂度。作者指出可扩展到更�?TTS 架构与架构专用条件策略�?

## 点评
问题定义很准：增强的「语言学红利」与「声学域偏置」分开处理——语言走文本支路、身�?域走条件嵌入。强在双数据源、双 ZS 生成器复现与 speaker-matched 对照；脆弱处是仍依赖外部 ZS-TTS 质量与参考时长，且目标骨干限定为 VITS，换流匹�?LLM-TTS 时域注入位置可能要重设计�?
