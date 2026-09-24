# Edit Content, Preserve Acoustics: Imperceptible Text-Based Speech Editing via Self-Consistency Rewards

- 论文编号：1186
- 报告人：Yong Ren
- 程序：Wednesday 30 September 2026 / Voice Editing
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ren26e_interspeech.pdf

## 问题
基于文本的语音编辑需改内容却尽量听不出痕迹。直接在声学 token 上编辑内容–风格纠缠，易幻觉与边界伪影；NAR 韵律偏平，AR 稳健性不足。现有语音 RL 奖励多对准 TTS 指标，难保证编辑区与上下文无缝融合。

## 方法
原则 “Edit Content, Preserve Acoustics”：(1) 语义空间编辑：语义 tokenizer 得 token，PSM 格式条件填充中间段，Flow Matching 解码器重建波形（CosyVoice3 组件冻结）。(2) Self-Consistency Rewards GRPO：组采样估优势；冻结预训练 TTS 对编辑 token 的平均 log-prob 作一致性奖励；ASR WER 作可懂度奖励；门控要求 WER 与时长相对误差均 ≤0.2，否则奖励为 0。Libriheavy 监督预训练后再 RL。

## 实验与结果
Ming-Freeform-Audio-Edit（插入/删除/替换）上，语义编辑 + GRPO 相对 FluentSpeech、VoiceCraft、Ming-UniAudio 取得更低 WER、更高 SIM/DNSMOS/MOS；删除任务 GRPO 后 basic WER 降至约 0.47% 量级改进显著。Seed-TTS 子集掩码 0.5–2.5 s：长编辑下 WER/SIM 衰减更缓，GRPO 对长时长自然度增益更明显。

## 结论
语义空间解耦提供声学保持结构基础，TTS 一致性批评 + WER/时长门控的 GRPO 进一步做感知对齐，在多类编辑与长时长上优于主流 AR/NAR 基线。

## 点评
把编辑从声学 token 挪到语义 token，与“结构基础 + 感知对齐”两段叙事一致；用预训练 TTS 似然当隐式批评，比只追说话人相似更贴“听不出拼接”。门控防奖励黑客设计务实。SIM 主要靠冻结解码器，GRPO 对音色增益有限；依赖 CosyVoice3 组件与高质量对齐区间。
