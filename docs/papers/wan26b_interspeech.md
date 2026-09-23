# Continuous Time-Varying Emotion Control Zero-Shot Text-To-Speech With Emotion Orthogonal LoRA

- 论文编号：1798
- 报告人：Chenchen Wan
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/wan26b_interspeech.pdf

## 问题
高质量情感 TTS 常依赖大规模语料与粗糙离散标签，难以做细粒度、随时间变化的控制。参考音频提示易把情绪与说话人/内容韵律缠在一起；句内情绪转折容易被平滑或被 prompt 情绪拖偏。

## 方法
在预训练 flow matching TTS（F5-TTS / DiT）上提出两阶段方案：
1. **EO-LoRA**：在选定线性层（默认 attention 的 Value/Output 与 FFN）插入三条分别对应 Valence、Arousal、Dominance 的低秩分支（r=16），每帧用对应 VAD 标量缩放更新；用 Frobenius 余弦正交正则 \(L_{\mathrm{orth}}\) 抑制维度间干扰。支持句级常数或帧级时变 VAD。
2. **Flow-DGPO**：对候选组做偏好对齐，用组内标准化优势把样本分成正/负集，以 flow matching loss 相对冻结参考模型的间隔做偏好目标；奖励综合情绪相似度、说话人相似与 (1−WER)。
Stage1：\(L_{\mathrm{FM}}+\lambda_{\mathrm{orth}}L_{\mathrm{orth}}\)；Stage2：Flow-DGPO。帧级 VAD 由 wav2vec2 预测器（MSP-PODCAST）提取并归一化到 \([-0.5,0.5]\)。

## 实验与结果
训练：EmoVoice-DB（约 40h）+ ESD 英语（约 10h）。评测：EMO-Change（时变转折）、JVNV S2ST（日→英跨语）。相对细调 F5-TTS，EO-LoRA + Flow-DGPO 在 EMO-change 上 SIM-o 0.751、WER 0.2%、AutoPCP 3.60、Emo SIM 0.778、Aro-Val SIM 0.914；主观 SMOS/NMOS/EMOS 亦最高。数据量远小于 EmoCtrl-TTS 的大规模设定，但可控性指标可竞争甚至更优。消融：去掉 \(L_{\mathrm{orth}}\) 或改注入位置（含 Q/K）会削弱可控性；Flow-DGPO 进一步提升可控与可懂度。

## 结论
作者认为 EO-LoRA 与 Flow-DGPO 能在有限情感数据下实现稳健的连续/时变零样本情绪控制，并保持可懂度与说话人相似；计划扩展到其他生成骨干。

## 点评
核心设计是「把 V/A/D 拆成三条正交低秩调制」，比单条 LoRA 或外挂条件流更可解释，也直接服务帧级轨迹控制。Flow-DGPO 用复合奖励把情绪对齐与质量约束绑在一起，缓解了只追情绪相似度时的崩坏风险。脆弱点：VAD 依赖外部预测器质量；跨语设定下骨干未学日语，SIM/WER 仍有差距；EmoCtrl-TTS 结果来自原文报告而非同环境复现，跨论文对比需谨慎解读。
