# Deriving Benchmarking Datasets from Long-Form Recordings: Challenges and Opportunities

- 论文编号：2363
- 报告人：Kaveri K. Sheth
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sheth26_interspeech.pdf

## 问题
儿童中心长时录音（LFR）生态效度高，但跨语料格式/同意书异构、缺少共享基准、且标准 ML 流程难以覆盖敏感儿童语音的隐私治理，三者相互牵制，导致多数工具只在单语料上训练评估。

## 方法
提出三件套框架：(S1) 用 DataLad + ChildProject 标准化 27 个含人工标注的儿童语料（18+ 语、14 国）；(S2) 可复现流水线派生四类基准——voice type classification (VTC)、addressee、vocal maturity (VCM)、orthographic transcription，均采用 child-disjoint 划分；(S3) ELSI 角色化生态（Custodian / Tool Creator / Analyst），按原始音频、带标签片段、派生指标分级授权。案例：同 VTC 2.0 架构（BabyHuBERT + 四路二分类头）在公共子集与全集合上重训。

## 实验与结果
表 1 汇总公共与非公共语料的剪辑数、时长与各任务 utterance 量。VTC hold-out：VTC-2.0 平均 F1 65.1；仅公共数据重训 44.4；含私有集合重训 62.2（KCHI 73.4、MAL 68.8 超过原 SOTA 的 70.0/65.1）。人工一致性参考平均 F1 约 69.8。

## 结论
标准化、基准派生与伦理治理必须联动：仅靠公开子集无法达到有竞争力的跨语/跨条件性能；治理使受限语料可参与共享评估而不放开原始音频。

## 点评
把“数据工程 + 基准 + 权限”当成一体问题，比单纯发一个挑战集更贴近 LFR 研究现实。案例清楚说明公共 CHILDES 类数据分布过窄；ELSI 的价值在于把“训练要音频、评估要片段、分析只要指标”拆开，但仍依赖托管方持续运营与同意条款可机读化。
