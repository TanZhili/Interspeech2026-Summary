# Correct Then Detect: Zero-Shot FVMC Annotation for Child Language Sample Analysis

- 论文编号：2593
- 报告人：Wei Bo
- 程序：Wednesday 30 September 2026 / Child Speech and Health
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hou26b_interspeech.pdf

## 问题
Finite Verb Morphology Composite (FVMC) 对识别 Developmental Language Disorder (DLD) 临床有效，但依赖人工标注强制时态语境（正确/错误/省略），无监督语料，端到端 LLM 提示易幻觉。

## 方法
零样本分解：① 受限语法纠错（仅动词形态与省略 be/助动词等）——GECToR 标签受限或 LLM 提示纠错；② 在纠正句上用 Stanza UD 规则检测强制语境；③ 最小编辑距离对齐原文，按替换/插入判定 correct / incorrect / omitted。在 ENNI 儿童叙事（SLP 金标）故事级评测，对比直接 LLM 标注。

## 实验与结果
直接非推理 LLM 很弱；推理模型（如 GPT 5.2-R、Sonnet 4.6-AT）显著提升。提出管道更优：GPT 5.2+Stanza 在 correct/omitted F1 达 97.05%/70.23%；Sonnet 4.5+Stanza 在 incorrect F1 60.15%；相对最强推理 LLM 基线三类分别 +1.99/+4.72/+6.21。纠错用非推理模型即可，成本低于全程推理。

## 结论
据作者称，这是首个实用零样本 FVMC 自动标注管道；任务分解优于端到端 LLM。未来接 ASR、扩展到会话及其他语法指标。

## 点评
把临床规则拆成“纠错 + 句法检测 + 对齐”，让 LLM 只做擅长的受限改写，是临床 NLP 里可复用的范式。incorrect/omitted 仍远低于 correct，类别极不平衡与省略检测难度仍在；仅 ENNI 叙事，会话场景外推未证。纠错范围若漏改/过改会直接污染对齐标签。
