# When Spoof Detectors Travel: Evaluation Across 66 Languages in the Low-Resource Language Spoofing Corpus

- 论文编号：345
- 报告人：Kirill Borodin
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/borodin26b_interspeech.pdf

## 问题

反欺骗对策（CM）常在少数高资源语上训练，语言失配会使其依赖语言/音系相关伪影而非真正伪造线索。现有多语假音库在低资源语覆盖、生成器多样性或可控（语言×合成器）对比上不足，难以把“语言”当作独立域偏移轴来压力测试。

## 方法

发布仅合成的 LRLspoof：2732 小时、66 语（按 Common Voice 脚本语音 <100h 操作性定义含 45 个低资源语）、24 个开源 TTS（经典到零样本克隆）。评测 11 个公开 CM：在汇合外部真假基准（ASVspoof5、ASVspoof2021 LA/DF、In-the-Wild、DFADD、ADD2022）上标定 EER 阈值，再固定转移到 LRLspoof，报告 spoof rejection rate（SRR）。用固定 CM+固定 TTS、仅改语言的对照，隔离语言效应。故意不含目标语真实语音，以免域标签混入真假判别。

## 实验与结果

阈值转移下 SRR 跨语言与跨模型差异极大（如 aasist3 英语 93.33%、车臣 99.86%；nes2net 在加泰罗尼亚可近 0%、车臣近 100%）。语言均值 SRR：aasist3 约 90.4%，w2v2-300 约 80.5%，若干 SSL/图注意力系统均值仅约 26–46%。固定 TTS 的对照中语言差可达数十个百分点（如 Parler-TTS 英—波对 w2v2-300 差 94.46 pp；Piper 丹—威对 aasist3 差 99.51 pp）。低资源子集上部分模型进一步退化。

## 结论

语言是反欺骗独立的域偏移源；同一合成器下跨语 SRR 可剧烈变化，暴露语言伪影依赖。LRLspoof 定位为 spoof-side 跨语诊断库，强调报告跨语差距而非仅匹配语结果。局限：无目标语真实样本，SRR 高不等于完整工作点（缺 FRR）。

## 点评

用“阈值转移 + 固定合成器变语言”把语言偏移做得干净，对部署多语 CM 很有诊断价值。spoof-only 设计诚实避开了真假混域捷径，但也意味着不能直接读安全工作点。脆弱点是各语合成器覆盖不均、时长偏斜，且外部标定阈值可能对某些语过严/过松。
