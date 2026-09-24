# Looking for Affect in Spontaneous Finnish Speech through Linguistic Interpretability

- 论文编号：2452
- 报告人：Kalle Lahtinen
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/lahtinen26_interspeech.pdf

## 问题
效价与唤醒在自发语音中分别多大程度依赖文本 vs 声学，芬兰语既往研究多单模态，互补作用不清。

## 方法
FinnAffect 标注子集（12k 句，效价/唤醒 [-1,1]）。系统比较 127 组显式/隐式特征组合：文本侧 ModernBERT、FinnSentiment、情感词典、Trankit 语言学特征（口语/标准转写）；音频侧 ExHuBERT、eGeMAPS；可选交叉用另一维标注。MLP 回归，报告 CCC。

## 实验与结果
效价：文本+音频组合显著优于单模态，最佳测试 CCC≈0.42–0.43（含 ModernBERT+ExHuBERT+FinnSentiment±唤醒）；纯音频约 0.21，词典/语言学显式特征较弱。唤醒：声学主导，模态互补增益不大。口语 vs 标准转写差异多不显著。

## 结论
自发芬兰语中，效价感知更依赖语–音互补，唤醒主要靠声学，与跨语言既有发现一致。

## 点评
用可解释显式特征与预训练表征并排消融，比端到端黑盒更能回答「哪类线索在起作用」。训练标注多为单听者，测试为五人金标，标注噪声会压 CCC 上限；口语转写标准化用 GPT，可能引入额外偏差。
