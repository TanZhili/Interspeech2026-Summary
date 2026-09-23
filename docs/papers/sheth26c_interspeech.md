# ELSI: An Interface for Standardizing Child-Centered Datasets, Applying Machine Learning Models, and Extracting Metrics

- 论文编号：3583
- 报告人：Kaveri K. Sheth
- 程序：Wednesday 30 September 2026 / Speech and Language Processing for Health and Accessibility
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sheth26c_interspeech.pdf

## 问题
儿童中心长时录音（LFR）语料目录/元数据不统一，开源模型需编程门槛，商业 LENA 闭源；发展研究者难系统比较发声/轮次等指标可靠性。

## 方法
开源网页界面 ELSI：底层 ChildProject 自动标准化语料；一键跑 VTC（说话人类型切分）与 ALICE（成人音素计数等）；导出儿童/其他儿童/男女成人发声与对话轮次及音素/音节/词计数。重计算在机构服务器，用户浏览器访问，无需本地 GPU。Show and Tell 演示存档→处理→CSV。

## 实验与结果
正文为系统与流程说明，报告经 ERC 资助试点与合作语料试用；未给出大规模基准数字。强调降低技术门槛以支持低资源语言社区参与跨语料比较。

## 结论
ELSI 作为共享基础设施，把标准化、模型与指标串成可复现流水线；计划扩展模型与可持续托管。

## 点评
面向发展心理学而非工程用户，把 ChildProject/VTC/ALICE 包进 GUI，对“一起说话”主题很贴。强在开放与去编程化；弱在依赖中心服务器、指标仍受底层模型质量约束，正文缺定量验证。
