# On Entrainment in Semi-Spontaneous Multilingual Parliamentary Speech

- 论文编号：2492
- 报告人：Debasmita Bhattacharya
- 程序：Wednesday 30 September 2026 / Entrainment and Dialogue Coordination
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/ries26_interspeech.pdf

## 问题
既有 entrainment 研究多限单语、固定自发度对话；半自发（准备独白+即兴提问）且跨语场景中，说话人如何在声学–韵律与语义上适应对方仍不清楚。

## 方法
在加拿大 Hansard 英法议会子集上，采样 40 段准备独白（10–20 分钟）+ 即兴提问（1–2 分钟），语言设置为 en-en/fr-fr/en-fr/fr-en。提取 eGeMAPSv02 声学–韵律特征与 RemBERT 语义嵌入，用余弦相似度相对随机配对零基线测全局与分段（独白初/中/末）entrainment；并用混合效应模型与特征消融解释贡献。

## 实验与结果
57.5% 交换呈显著声学–韵律 entrainment，语义更弱（17.5%）。时间上对独白开头与结尾对齐更强（首因/近因），约 82.5%/67.5% 交换可见。跨语交换中“初段语义对齐”显著正向预测“末段声学–韵律对齐”；单语则呈弱权衡。少数特征主导（F0、英语侧 MFCC、法语侧响度、政策类语义维），消融可大幅削弱全局 entrainment，跨语尤甚。

## 结论
半自发多语议会对话仍普遍存在多维 entrainment，并呈现首因/近因与跨语特有的语义→声学两阶段规划迹象。

## 点评
把记忆效应与跨语认知负荷接到可检验的分段相似度上，填补议会语料空白。样本仅 40 段交换、部分相关未达显著，外推需谨慎；排除语码混用与特权头衔后生态效度有所收窄。
