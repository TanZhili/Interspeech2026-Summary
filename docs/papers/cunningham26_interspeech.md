# Decolonizing Linguistic Policies in Automatic Speech Recognition: A Framework for Cross-Culturally Competent Speech AI

- 论文编号：3351
- 报告人：Jay L. Cunningham
- 程序：Tuesday 29 September 2026 / Multilingual Speech 1
- 技术分类键：multilingual
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/cunningham26_interspeech.pdf

## 问题
ASR 与语音界面已介导公共服务、医疗与教育，但对低资源、原住民与非标准变体的持续失败常被当作技术误差；作者认为这些失败是隐式“语言政策”，通过数据、指标与模型先验再生产殖民式语言等级，使部分声音在机器侧不可读。

## 方法
本文不提新 ASR 架构或基准数字，而是提出人文评估框架。理论综合语言资本、种族语言学意识形态、语言政策研究与去殖民计算，给出七层情境化模型（语言→民族国家→地域→族群语言→社会语言意识形态→社会公正关联→社会技术后果）。引入 Three Harms（3M）：Misrecognition、Misalignment、Mistrust；将训练数据策展、WER 等指标、LM 先验与部署回退行为诊断为 policy sites；并提出参与式框架与最低审计协议（评估者角色、采样、指标、标注与裁决），主张受影响社区作为共设计者、评估者与治理伙伴。另建议在 WER/CER 之外补充 Tone Error Rate（TER）、click 辅音专项错误率与社区加权伤害分。

## 实验与结果
全文为理论与框架论文，无自建模型实验。正文举例说明政策效应，如标准美式英语 WER 约 5% 而非裔美式英语约 35%、界面支持巴黎法语但不支持塞内加尔法语等；并讨论 WER 对声调语言（如约鲁巴）与 click 辅音语言的失效。抽取文本在“语言政策三层次：数据策展…”处截断，后续参与式框架细则与协议条款未完整可见。

## 结论
作者主张把 ASR 设计选择视为可审计的语言政策，用 3M 与七层模型定位伤害，用社区参与与最小审计协议推动文化胜任的语音 AI；目标是补足 WER 中心评估对文化情境伤害的欠规范。边界在于这是评估/治理框架而非系统性能提升方案。

## 点评
抓的是“谁的口音被算作合法输入”这一制度层问题，而不是再刷多语 WER。强处是把数据菜单、参考转写、回退到英语等工程细节明确标成政策位点，并要求声调/click 等语言学敏感指标。弱处是可操作性依赖社区资源与组织成本，且全文抽取截断，审计协议落地细节不完整；若不与具体系统审计绑定，易停留在概念层。
