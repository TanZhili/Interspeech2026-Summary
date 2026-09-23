# Preserving Acoustic Cues for Video Reasoning: An Efficient Uniqueness-Driven Token Compression Framework

- 论文编号：3512
- 报告人：Zichao Nie
- 程序：Monday 28 September 2026 / From Self-Supervised Pre-training to Phonetic Analysis of Speech Models
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/xue26d_interspeech.pdf

## 问题
视频推理常丢弃音频或只用 ASR 文本，丢掉韵律、环境声、说话人等声学线索；若把全部音频 token 送进 MLLM 则算力过高。视觉 token 压缩不能直接套用到一维、短时平稳的音频序列。

## 方法
提出 **Flash-VAReason**：Whisper 编码器提音频特征后，按信息唯一性做三阶段压缩，无需改 MLLM 架构或额外训练——
1. **Audio Time Fusion**：相邻帧余弦距离低于阈值则平均池化合并，去短时冗余；
2. **Budget Control**：按原始长度比例定保留数 \(K\)，过长先均匀下采样到 \(L_{\max}\)；
3. **Spatial Dynamic Compression**：全局唯一性排序 + 贪心去重与邻域融合，保留 top-\(K\) 并更新位置编码。

视觉侧沿用 UniComp。在 CharadesEgo、Ego4D 上评 BERTScore 与 QwenJudge（语义/完整/无幻觉）。

## 实验与结果
相对 AKeyS、mPLUG-Owl3、Grounded-Video-LLM、FlashVID、UniComp，Flash-VAReason 在两数据集多数质量指标最优（如 CharadesEgo Overall 2.3789，Ego4D 1.6480），推理约 6.10 s / 13.74 s，远快于 Grounded-Video-LLM。相对视觉-only UniComp 质量更好且速度相当。消融：全 token Overall 2.3838 但约 1.75× 更慢；均匀采样质量崩到 2.0121；去 ATF/SDC 分别伤质量或速度。

## 结论
声学线索可提升视频推理；唯一性驱动压缩能在近似全 token 质量下大幅降延迟。局限：细粒度音频事件未充分纳入、唯一性时变剧烈时压缩变差、目前偏离线。

## 点评
问题抓的是“视听联合推理里音频侧的上下文预算”，用与视觉同源的唯一性原则做训练无关压缩，工程上干净。脆弱处：依赖 Whisper 前端与启发式阈值；评测偏 LLM-as-judge；结论图中示例名写 AcousticCues-VR，与正文 Flash-VAReason 命名略混，但不影响主结果。
