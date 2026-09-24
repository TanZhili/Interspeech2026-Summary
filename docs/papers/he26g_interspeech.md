# MOV-AAD: A Large-Scale Multimodal Dataset for Auditory Attention Decoding During Moving Conversations

- 论文编号：3556
- 报告人：Nima Mesgarani
- 程序：Tuesday 29 September 2026 / Audio-Visual and Multimodal Perception
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/he26g_interspeech.pdf

## 问题
多数听觉注意解码（AAD）公开数据偏静态双讲者、缺同步自主神经与行为指标，生态效度不足，难研究动态空间场景下皮层–外周协同。

## 方法
发布 MOV-AAD：50 名正常听力被试；64 导 EEG（1200 Hz）同步眼动、呼吸、GSR、心率、SpO2、体温、加速度、PPG 等。单会话（40 trial）与多会话竞争（56 trial，声源在 ±90° 动态移动、轮流）；HRTF 空间化，背景噪声相对语音 −9/−12 dB RMS；重复词检测作注意行为；另有方位定位任务与预处理（坏导插值等）流程。数据开源。

## 实验与结果
正文给出定位任务：9 方位 −90°–+90°，报告准确率与 MAE（机遇 MAE 约 66.7°）；重复词检测在 SC/MC 上报告准确率/F1，并用 Wilcoxon 等检验。数据集相对 KULeuven、DTU、PhyAAt 等的独特组合见表 1。具体群体数值因篇幅以协议描述为主。

## 结论
MOV-AAD 为真实空间动态下的稳健 AAD、多模态注意与听努力、被试间神经相关提供基准资源。

## 点评
贡献是生态化多模态基础设施，而非新解码算法。强在移动交谈 + 外周生理齐全；脆弱点在实验室 HRTF/固定噪声级与真实鸡尾酒会仍有差距，以及 N=50 对个体差异建模的上限。
