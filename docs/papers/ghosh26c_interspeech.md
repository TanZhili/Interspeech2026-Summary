# V-Align: Visual Forced Alignment via Phoneme to Video Optimal Path Traversal

- 论文编号：560
- 报告人：Souvik Ghosh
- 程序：Thursday 1 October 2026 / Speech signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ghosh26c_interspeech.pdf

## 问题
音频强制对齐在噪声/缺失音频时失效；视觉强制对齐（VFA）研究少，既有方法多靠音频派生边界监督，且难得到尖锐、时序一致的音素边界。

## 方法
V-Align 将 VFA 建模为帧–音素兼容格上的最优单调路径：冻结 VTP 唇动与 XPhoneBERT 音素嵌入，经卷积投影用高斯距离核建软遍历后验 Γ，Viterbi 式 DP 解码边界。Stage 1：forward-sum + 路径二值化，无边界标注；Stage 2：词级聚合后用 MFA 词边界监督细化。

## 实验与结果
LRS2/LRS3：Stage 1 已强于多数有监督基线；Stage 2 SOTA——LRS2 MAE 32.9 ms / ACC 91.2%，LRS3 56.9 ms / 88.5%，相对先前最优约降 17.3 / 13.6 ms。消融：最优路径解码优于贪心/帧 argmax；三损失合用最佳。噪声 MFA 监督下，保留路径目标比纯监督更稳健。

## 结论
结构化单调路径学习使无边界监督即可学出对齐结构，加词级 MFA 细化达视觉强制对齐 SOTA。

## 点评
把 TTS 对齐里的路径边际化迁到视听，Stage 1 对无可靠音频标注场景很实用。Stage 2 仍依 MFA，音素清单失配靠词级回避；评估指标相对 MFA 派生标签，噪声场景优势更有说服力。
