# Not Quite My Tempo: Voice Activity-aware Speech Synthesis for Lip-Synchronous Dubbing

- 论文编号：1407
- 报告人：Alejandro Pérez-González-de-Martos
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/perezgonzalezdemartos26_interspeech.pdf

## 问题
唇同步配音要求目标语语音–静音时间结构与片源严格对齐；现有方法多用唇动视频条件，依赖成对视频且面对卡通/多人场景脆弱。

## 方法
在类 F5-TTS 的 inpainting/流匹配 TTS 上加帧级二值 VAD 条件（Silero）：嵌入后加到编码器表示，约束 DiT 只在有声画布上生成。训练时随机 mask VAD，使推理可选开/关。架构含 ZipVoice 式平均上采样、显式说话人嵌入（FACodec、ERes2NetV2）与 GST，SoundStream 声码器。无视频，仅音频–文本。

## 实验与结果
English：LibriTTS-R；另训多语专有+公开数据。测 mTEDx（希/法/葡/俄→英，7–15s 且含 ≥500ms 停顿，291 句）。Silero VAD 帧准确率：无条件约 73%→有条件约 96%（LibriTTS 模型）；多语模型约 91.6%。静音起止偏差在条件开启时集中于 0。40 人主观：Placement/Prosody MOS 有无 VAD 差异不显著（约 3.7–3.8）。WER 略升（如 LibriTTS 8.5%→13.9%），与译文时长不适配有关；定性见省略/重复/重排以保住时间轴。

## 结论
轻量 VAD 条件即可高精度对齐配音时间结构且几乎不损韵律自然度；对未做等时适配的译文仍会牺牲可懂度。未来拟用更细粒度发音/唇动信息，并减少对等时 MT 的依赖。

## 点评
用二值活动掩码替代唇动视频，工程上很务实，且随机 mask 做成可选约束适合后期。边界情况清楚：模型优先保时间轴而非字面完整，说明系统假设「译文已大致等时」仍关键。
