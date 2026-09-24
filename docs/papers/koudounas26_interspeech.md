# Synthetic Pathological Speech at Scale: A Flow Matching Approach for Clinical Data Augmentation

- 论文编号：2313
- 报告人：Alkis Koudounas
- 程序：Wednesday 30 September 2026 / Pathological Speech Assessment 3
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/koudounas26_interspeech.pdf

## 问题
病理嗓音数据稀缺且不平衡；噪声/变调等线性增强几乎无助，因其抓不住声门非线性不稳。需可控生成健康/病理持续元音并验证合成规模对下游检测的缩放律。

## 方法
在 F5-TTS（Conditional Flow Matching + DiT）上以 “⟨healthy|pathological⟩ + 元音音素” 文本条件微调；参考音频引导说话人/韵律，ODE 生成 mel。训练语料：SVD / AVFAD / VOICED / PVQD 共 7,211 条（四语）。下游用 HuBERT-AS + MLP 做健康/病理二分类；合成规模 \(N\in\{10^2,10^3,10^4,10^5\}\)。

## 实验与结果
仅合成 100k 训、真实 held-out 测：Acc 0.836 vs 真实基线 0.804（+3.9%），Sensitivity +13.3%。Real+Synth 随规模单调升，传统 Real++ 几乎无效。OOD：FEMH/IPV 多类 F1 约 +10.0%/+7.4%；PC-GITA 零样本帕金森 Acc 在 10k 达 0.647（+6.8%），100k 回落。Praat 显示合成病理 jitter/shimmer/HNR 接近真实。

## 结论
流匹配合成可按规模缓解临床数据短缺并提升跨域稳健性；过大合成对远 OOD 任务可能过拟合一般病理模式。

## 点评
缩放律实验设计清楚，且用声学特征与 t-SNE 核对合成是否保留病理线索。二值流形对细粒度病种与 PD 特异特征覆盖有限，作者对 100k 零样本回落的解释合理。
