# DECRA: Dynamic Emotion Control for Real-time Speech Anonymization

- 论文编号：2927
- 报告人：Ghady Nasrallah
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/nasrallah26_interspeech.pdf

## 问题
实时说话人匿名化既要抹去身份，又要控制/中和情感以防副语言泄露。现有流式 VC 多只管身份、无意中保留情绪；情感 VC 则多为离线、句级全局条件，无法因果低延迟地做时变、闭环情感操控；说话人嵌入常与情绪纠缠。

## 方法
**DECRA** 以 TVTSyn 为流式骨干，加入：
1. 对抗学习：把全局说话人嵌入投影到「去情绪」音色子空间（GRL + V/A 回归），情绪信息改由连续 valence–arousal 轨迹回注解码器。
2. 离线 SER 伪标签在大规模自然语音（LibriTTS + Natural Voices）上监督；训练时用时变 V/A 条件（250 ms hop）。
3. 因果 SER 头挂在 VQ 前内容特征上，在线预测帧级 V/A，闭环反馈到情感控制器；波形解码用 Conditional LN Fusion 融合 TVT 与 V/A。端到端可流式，GPU 延迟 <80 ms。

## 实验与结果
情感评测在 ESD。中和/转换相对 SeedVC、Vevo、TVTSyn：DECRA 的 CCC(A) 更高（中和 0.81、转换 0.74），WER/说话人相似可竞争；NISQA 低于离线基线，作者归因于流式约束而非情感模块。主观：怒/喜→中性准确率约 91–92%，悲→中性较弱；中性→情绪方向亦多数优于无控制骨干。动态 arousal 斜坡与预测轨迹相关约 0.78，valence 仅约 0.21。VPC’24：EER 46.64、WER 4.90、UAR 48.70，在匿名与情绪保留间更平衡。流式：76.1 ms 延迟、RTF 0.268。

## 结论
作者给出可同时做身份转换与闭环时变情感控制的因果流式系统；局限是 valence 控制弱于 arousal，未来拟用更丰富 SSL 情绪嵌入并加强与内容/说话人解耦。

## 点评
问题组合很贴隐私场景：匿名化若「保情绪」会泄露，若「抹情绪」又需实时可控。对抗解耦 + 在线因果 SER 闭环是清晰设计。结果也诚实：arousal/prosody 跟得上，valence 难控；音质代价主要来自流式而非控制头。脆弱点：伪标签 SER 误差会传导；与离线高保真情感 VC 比，质量–延迟权衡仍陡。
