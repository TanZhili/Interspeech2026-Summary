# Exploring the potential and limitations of Model Merging for Multi-Domain Adaptation in ASR

- 论文编号：1969
- 报告人：Carlos Carvalho
- 程序：Wednesday 30 September 2026 / Domain Adaptation & Accented ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/carvalho26_interspeech.pdf

## 问题
语音基础模型常按域分别微调，产生大量专用 checkpoint；新域到来时再做全量联合微调成本高且数据可能不可用。模型合并可免重训拼能力，但 ASR 多域合并系统评测与 OOD/跨语保持仍不足。

## 方法
在 WhisperLv3-X 上对 10 个欧洲葡萄牙语（EP）域独立微调后，基准 11 种合并算法（参数空间 / τ-space / τ-subspace）。提出 BoostedTSV-M：在 TSV-M 上对小奇异值做 boosting 缓解秩塌缩，并用 Newton–Schulz 正交化提升数值稳定。开源 MergeWhisper。评测 EP ID/OOD、非洲/巴西葡语、OpenASR-HF、FLEURS。

## 实验与结果
Full-FT 把 EP ID 从 15.62 降到 8.54，但伤非 EP OOD。BoostedTSV-M EP Full Avg. 11.55，略优于 Full-FT 的 11.58（MAPSSWE p<0.001），EP OOD 优于 Full-FT；相对 TSV-M 更偏 ID、略损部分非 EP OOD。PS 类（如 Karcher、Model Stock）非 EP/多语更好；τSpa（如 TIES）可伤英语。β 越小 ID 越好、EP OOD 越差，体现特化–共享权衡。

## 结论
合并是多域 ASR 相对 Full-FT 的可行替代：BoostedTSV-M 在 EP 上可匹敌甚至略超全微调，并更好保留部分泛化；但存在目标特化与跨语鲁棒的明确权衡。

## 点评
把 NLP/CV 合并族系统迁到 Whisper 多域，并量化“合并不会免费”的 OOD 代价，工程价值高。BoostedTSV-M 针对秩塌缩的修复点明确。局限是单语种族（EP）扩展为主；合并质量依赖各域微调质量与域相似度。
