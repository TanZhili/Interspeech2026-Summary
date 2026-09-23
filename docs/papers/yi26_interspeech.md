# Exploring the Scale and Diversity of Speech Anti-spoofing Datasets: Experiments and Analysis

- 论文编号：157
- 报告人：Zhuolin Yi
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/yi26_interspeech.pdf

## 问题

近十年反欺骗训练集规模指数膨胀，隐含“更大更好”。但在固定生成方法下盲目扩规模是否同步提升跨域泛化，以及多样性（本文主要指生成方法种类）是否比规模更关键，仍缺可控实验。观测上 Speechfake 虽小于 Spoofceleb 却可能因攻击种类更多而泛化更好，需去混杂验证。

## 方法

固定 Wav2Vec-AASIST（XLS-R 300M）+ RawBoost，做两组实验。(1) 规模：在 Speechfake-BD、ASVspoof5 训练集上按 1%/5%/10%/20%/50%/100% 随机子采样，保持生成方法集合不变，做域内与跨集（含 CD-ADD、Spoofceleb、FSW、In-the-Wild、VoiceWukong）评测。(2) 多样性：从 ASVspoof5、Speechfake-BD、CD-ADD、Spoofceleb 各生成方法抽 1000 条假样本，真实样本仅来自 Speechfake-BD，组成约 63k 句、53 种生成方法、约 94 小时的复合集，再与各全量原集在 In-the-Wild、VoiceWukong、FSW 上比跨域 EER。

## 实验与结果

规模实验：性能不随数据量单调上升；Speechfake-BD 上域内 50% 与 100% 接近甚至 50% 略好，跨域最佳多在约 20%；ASVspoof5 最佳常在 10%–20%。多样性实验：复合集平均跨域 EER 13.03，优于 CD-ADD（21.65）、ASVspoof5（27.92）、Speechfake-BD（17.52）、Spoofceleb（19.67），尽管 Spoofceleb 时长最大（约 1982h）但仅 10 种生成方法。

## 结论

固定生成方法下过度扩规模易过拟合训练集攻击分布、伤害跨域；更小但生成方法更多的复合集泛化更好。未来建库应优先扩攻击/生成多样性，而非单纯堆时长。局限：模型容量固定、子采样多为随机、多样性定义偏窄。

## 点评

用控制变量把“规模神话”拆开，对社区建库资源分配有直接政策含义。复合集设计把多库生成方法并置，能解释为何大库未必赢。脆弱点是随机子采样可能混入信息量差异，且跨库“同名方法不同流水线”被当作不同方法，多样性度量仍偏操作化；未联合扫描模型容量与数据预算。
