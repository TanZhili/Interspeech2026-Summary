# VoiceTTA: Enhancing Zero-Shot Text-to-Speech via Reinforcement Learning-Based Test-Time Adaptation

- 论文编号�?757
- 报告人：Li Liu
- 程序：Monday 28 September 2026 / Scaling and Zero-Shot Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xie26c_interspeech.pdf

## 问题
零样�?TTS 多在播客、影视、有声书等常见域上训，遇到相声、方言、含糊、儿童语音等非常�?prompt 时，音色能贴上但夸张韵律与口音难仿。微调需要大量高质量目标数据；说话人嵌入适配又依赖嵌入模型，且对多样风格泛化不足。需要在推理时用极少参考音、轻量参数做在线适配�?

## 方法
**VoiceTTA**：在 flow matching 零样�?TTS（骨�?**F5-TTS**）上做强化学习式 **test-time adaptation**�?
1. 在首�?DiT 输入前接 **可学�?prefixes**（默�?4 个）；主网冻结，只训 prefixes�?
2. 用温�?\(T\sim U(0.5,1.5)\) 采样 \(k=4\) 条候选；奖励含：F0-CV 差、Energy-CV 差、说话人相似�?S-SIM，以�?Whisper WER 可懂度奖励；归一化后加权（\(\lambda_{1}=\lambda_{2}=0.2,\lambda_{3}=1,\lambda_{4}=1.5\)）�?
3. **GRPO** 优化 prefixes：因 flow matching 不产 token 概率，用 flow matching 损失差近似概率比；无 KL 项（只动轻量前缀）。每样本 \(G=50\) 步适配后合成；下一样本前随机重�?prefixes。每人约 **16 KB** 前缀可存�?

## 实验与结�?
内部 200 条非常规风格（口�?90 / 儿童 40 / 含糊 30 / 中国相声小品 40�? KeSpeech 八方言�?20 条；对比 CosyVoice、MaskGCT、Vevo、F5-TTS�?
- **平均**：Ours WER 3.12、S-SIM 0.64、S-MOS 3.27、N-MOS 3.35；优于或接近各基线（F5-TTS�?.19 / 0.57 / 3.07 / 3.36），风格相似度最高，自然度不掉�?
- 分场景：口音、儿童、含糊、方言等上 S-SIM / S-MOS 多领先；部分场景 WER �?F5-TTS 接近�?
- 消融：仅可懂�?�?WER 最好但 S-SIM 0.43；仅风格三项 �?S-SIM 0.67 �?WER 7.04；四奖励并用才平衡。前缀数在域外升、域�?Seed-TTS 上过多则伤；过大 \(T\) 伤可懂度�?

## 结论
�?GRPO 与复合风�?可懂度奖励在测试时适配轻量前缀，可显著提升非常�?prompt 上的风格模仿，同时保持清晰度与自然度，且参数与存储开销极小，适合在线个性化。边界是适配步数带来推理时延，且奖励依赖 ASR 与说话人嵌入模型质量�?

## 点评
把「域外风格」从离线微调挪到推理�?RL 适配，奖励设计直接对准韵律动态（F0/能量 CV）而非只追 embedding。强在非常规五场景与消融把风格–可懂权衡写清；脆弱处是 GRPO 多候选采样成本、以�?reward hacking（贴 CV/SIM 却不真「像」）风险，主观自然度仍略低于大规模后训的 CosyVoice�?
