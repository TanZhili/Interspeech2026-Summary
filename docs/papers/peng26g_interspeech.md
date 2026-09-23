# Cross-modal Consistency Guidance for Robust Emotion Control in Auto-Regressive TTS Models

- 论文编号：1986
- 报告人：Yizhou Peng
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/peng26g_interspeech.pdf

## 问题
自然语言情绪指令的 AR TTS 在「文本语义情绪」与「要求渲染的语音情绪」冲突时（如用惊讶语气说悲伤内容），表现力、自然度与音质会明显下降。标准 CFG 用无条件 dropout 外推，难以对抗文本语义拉力，且易引入伪影。

## 方法
在 CosyVoice2 上提出 **CCG-CFG** 及其蒸馏：
1. 外部 LLM 抽取 Text-Emo，并判定与 Rendered-Emo 的不一致程度（Identical / Inconsistent / Highly Inconsistent）。
2. **CCG-CFG**：不一致时把 CFG 的无条件支路换成 Text-Emo 条件，放大 Rendered-Emo 与 Text-Emo 的 logit 差；一致时退回标准 CFG。
3. **DS-CCG-CFG**：按不一致档位动态设 guidance scale（网格搜索得 {1.0, 2.5, 3.0}）。
4. **蒸馏**：用硬样本挖掘构造文本–对立情绪对，多尺度/多种子生成候选，按 \(0.5(1-\mathrm{WER})+0.5\cdot\mathrm{EmoConf}\) 排序做 DPO，把引导内化，去掉双通道推理与 CFG 伪影。

## 实验与结果
合并 ESD/MESS/MEAD/TESS/SAVEE/LibriTTS/VCTK 等，七情绪；约 40h 训练。中性参考下相对 CosyVoice2-N（EmoACC 50.63%）：
- DS-CCG-CFG：EmoACC 64.83%，MaJ 58.4（训练免费最佳之一），但 WER 升至 7.86%。
- DS-CCG-CFG-DPO+硬样本：EmoACC 59.55%，WER 3.76%，UTMOS/DNSMOS 保持高；主观 MOS 4.33、EMOS 3.67、NMOS 3.94，优于 CosyVoice2-N/R，并接近 Qwen3-TTS-R。
不一致子集上增益最大；传统高尺度 CFG 则显著伤 WER。

## 结论
作者认为用文本情绪作对比条件、按不一致动态尺度，再蒸馏进模型，可在冲突场景下显著提升情绪表达并保住可懂与自然度。

## 点评
问题设定很现实：NLEC 的失败模式往往不是「不会说情绪」，而是「文本语义把渲染情绪拉回去」。把 unconditional 换成 Text-Emo，等于显式做跨模态对照，比盲目加大 \(w\) 更对症；动态尺度与 DPO 蒸馏则分别处理「何时用力」与「推理成本/伪影」。脆弱点：推理期依赖外部 LLM 判不一致（蒸馏后可摆脱）；EmoACC 依赖 SER，与文本语义冲突时「正确情绪」定义本身主观；硬样本挖掘的对立情绪配对策略会影响泛化边界。
