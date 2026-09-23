# Mind the Gap: Impact of Synthetic Conversational Data on Multi-Talker ASR and Speaker Diarization

- 论文编号：443
- 报告人：Alexander Polok
- 程序：Monday 28 September 2026 / Multi-Talker ASR & Speaker Diarization
- 技术分类键：asr-multitalker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/polok26_interspeech.pdf

## 问题
大规模真实会话数据稀缺，MT-ASR 与说话人日志（SD）高度依赖合成数据，但轮次动态、源域、声学增强与真实/合成混合策略对各任务的影响尚不清楚，且缺乏可复现的大规模会话仿真工具。

## 方法
发布开源仿真器 FastMSS，可配置 turn hold / turn switch / interruption / backchannel 等转移、混响与噪声，并与 Lhotse 集成。在 DiCoW（Whisper + 帧级 diarization 条件）与 Sortformer（EEND + Sort Loss）上系统消融：轮次统计（flat / NSF-1 / CALLHOME / OV boost）、源域（LibriSpeech、VoxPopuli、otoSpeech、AMI/NSF-1 close-talk 及 Combined）、noise/rvb 增强，以及 synthetic-only、real-only、joint、synthetic→real 训练策略。MT-ASR 用 tcpWER（5 s collar，ground-truth diarization）；SD 用 DER（0 s collar）。

## 实验与结果
轮次：OV boost 使 DiCoW 在 NSF-1 上达 22.1 tcpWER（优于 flat 的 24.8），但使 Sortformer macro DER 从 26.1 恶化到 27.6。源域：Combined 合成已优于 real-only 的 macro tcpWER（10.0 vs 10.9）；Real + Combined 进一步到 8.8。增强：对 DiCoW 增益有限；对 Sortformer，noise+rvb 将 macro DER 从 26.1 降至 22.2。合成+真实：DiCoW Synthetic→real macro 8.7；Sortformer Synthetic→real macro DER 15.5，优于 joint 与 real-only。

## 结论
最优仿真配方强依赖任务：提高重叠利 ASR、伤 diarization；多样源域优于单一域匹配；噪声+混响对 diarization 关键；精心配置的合成数据可接近甚至增强真实数据训练。

## 点评
把“同一套仿真能否服务 ASR 与日志”拆开验证，结论可操作：重叠与声学增强应按任务分菜。拼接仿真缺语义连贯性，作者靠冻结 ASR 解码器缓解，对依赖语言模型的链路可能仍有偏。全文末段结论略有截断，但核心四点结论在前文已完整给出。
