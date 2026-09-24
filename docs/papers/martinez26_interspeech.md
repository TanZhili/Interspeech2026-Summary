# findsylls: A Language-Agnostic Toolkit for Syllable-Level Speech Tokenization and Embedding

- 论文编号：820
- 报告人：Héctor Javier Vázquez Martínez
- 程序：Thursday 1 October 2026 / Speech signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/martinez26_interspeech.pdf

## 问题
音节级表征利于口语建模与无监督词发现，但经典包络法与神经音节器分散在不同实现/数据/协议中，难复现、难公平对比与组件消融。

## 方法
开源工具包 findsylls：统一包络计算（RMS、Hilbert、SBS、theta 等）、特征提取（MFCC、HuBERT、VG-HuBERT、Sylber）与分割算法（peakdetect、余弦合并、MinCut、CLS 阈值），支持混搭与伪包络导出；提供音节嵌入池化与相对 TextGrid 的核/边界/跨度 F1 评测。

## 实验与结果
七语料（英/西成人与儿向、Kono 手标）：核检测易、跨度难。Sylber 默认核 F1 93.3；VG-HuBERT+MinCut 边界 F1 65.0。混搭增益明显：Sylber 余弦 + peakdetect 边界 F1 升至 69.9、跨度 47.0。token 率约 3.1–5.8/s；经典包络吞吐远高于神经配置。

## 结论
单一接口可支撑高资源与低资源（含 Kono）上可复现的音节实验；实际增益常来自表征与分割器的重组而非固定流水线。

## 点评
基础设施论文：价值在标准化与可组合性。参考音节边界多由词典规则从强制对齐派生，跨度指标有标注歧义；RTFx 仅单机相对比较。
