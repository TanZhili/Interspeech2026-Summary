# Context-aware child-directed speech detection from long-form recordings

- 论文编号：2780
- 报告人：Théo Charlot
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/charlot26b_interspeech.pdf

## 问题
从日长录音中自动区分儿童指向语（CDS）与成人指向语（ADS）对规模化研究儿童语言环境很关键，但现有方法多在孤立短句上处理、以英语为主，且很少在自动分割后的端到端流水线中评估。

## 方法
在约 22 小时、6 语、182 名儿童的多语料上，微调六种自监督模型（W2V2、HuBERT、WavLM、W2V2-XLSR、W2V2-LL4300、BabyHuBERT），三类标签：KCDS、ADS、OTHER。上下文感知微调：将目标话语对称扩展到总长 x 秒（0–30s），编码器看全窗，但只对原话语帧做均值池化再分类。端到端评估时先用 VTC 2.0 检测成人语音，再分类；基线为“靠近目标儿童发声即判 KCDS”的规则系统。

## 实验与结果
验证集上 BabyHuBERT 平均 F1 最高（53.2%）。加 10 秒上下文后平均 F1 从 53.2% 升至 67.0%（+13.8%），再长则略降。测试集（10s 上下文）KCDS/ADS/OTHER F1 为 81.6%/78.9%/36.2%。heldout（Tseltal+Winnipeg）帧级 F1：人工分割下 BabyHuBERT-addressee 平均 74.1 vs 规则 35.1；VTC 2.0 分割下 38.6 vs 25.6，相对人工分割下降约 35.5 个点。

## 结论
领域匹配的多语儿童中心预训练与约 10 秒上下文是提升 CDS/ADS 分类的关键因素；全自动流水线可行但仍受分割误差传播限制。作者开源代码与模型。

## 点评
把“孤立短句分类”改成保留周围对话上下文，直击人工标注者实际依赖的线索，且用 heldout 与自动分割检验可部署性。OTHER 类仍弱、Tseltal 噪声户外场景掉点明显，说明跨文化/跨条件鲁棒性仍是瓶颈；上下文全编码代价高，文中提出的分层/交叉注意力是合理的后续方向。
