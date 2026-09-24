# Vowel Allophony Improves Maximum-Likelihood Classification of Warlpiri Consonants

- 论文编号：3107
- 报告人：Coralie Cram
- 程序：Thursday 1 October 2026 / Speech Production and Perception 2
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/cram26_interspeech.pdf

## 问题
澳大利亚语言塞音部位对立多、方式对立少；仅靠辅音内在线索往往不足以区分密集部位连续统。Warlpiri 五部位塞音（无音位浊音对立）中，邻接元音的哪些外在线索最有助于分类仍不清晰。

## 方法
用 DoReCo 半自发叙事（14 名女性，25–50 岁）中的 VCV，对 /p t ó c k/ 做最大似然高斯分类。线索组：S=辅音内在（时长、爆破谱矩、E-H/M、强度、边界 F1–F4）；T=邻接元音前/后 25% 的 F1–F4 过渡；M=元音中点 F1–F4。对 CV/VC 分别训练 7 种 S/T/M 组合，分层 10 折宏平均 F，置换检验（Bonferroni α=0.005）。

## 实验与结果
仅 S 时辅音宏 F 约 0.654（CV）/0.647（VC），较易混淆。加入 M 比加入 T 提升更大：CV 上 SM 0.702 显著优于 ST 0.681；STM（0.691）反不及 SM。VC 类似，SM≈0.681、STM≈0.691。元音分类主要靠 M（F≈0.79–0.82），加 S/T 几乎不伤元音准确率。CV 整体略好于含 S 的 VC，作者联系再音节化/爆破与后接元音更近。

## 结论
辅音内在线索不足；邻接元音中点的音位变体信息对 Warlpiri 部位分类帮助最大，且不明显牺牲元音可分性。最大似然分类可为低资源语言感知建模提供系统级上界与混淆预测工具。

## 点评
把“最优听者能用什么线索”落到可比较的分类器消融，比单对对比更系统。中点变体增益大于过渡，对“澳大利亚语言弱化元音对辅音协同”的常见叙述是有益修正。局限是强制对齐爆破与半自发语体噪声；混淆矩阵细分析留作未来工作。
