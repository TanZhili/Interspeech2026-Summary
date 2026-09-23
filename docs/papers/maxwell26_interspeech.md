# Pronunciation and Intonation Structured Markup (PRISM): A Dataset for Australian English Pronunciation Feedback

- 论文编号：2830
- 报告人：Olga Maxwell
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/maxwell26_interspeech.pdf

## 问题
商业/自动发音反馈工具反馈有限、常缺科学依据，且忽视世界英语与 ESL 语音变异；现有学习数据语言覆盖窄或不开源，难以支撑面向澳大利亚英语（AusEng）、含韵律的个性化反馈。

## 方法
从 CommonVoice 英语分区（v21.0）按人口学分层抽取 Hong Kong、South Asia、Indonesia 口音子集；Montreal Forced Aligner（english_mfa）做词级对齐并由语音学家校正。三位语音学家按 AusEng 与自组织音系/韵律方案标注：13 大类、53 细类（元音/辅音、核调、停顿、突出、节奏、拼写、连读等），“error”定义为相对 AusEng 的差异。平台 ingest TextGrid；本文报告 859 条标注的初步分布。

## 实验与结果
分段错误约占 49.9%，韵律约 46.1%；最常见细类为 pause insertion（10.2%），其后 linking、rhythm 等。口音不均衡：印尼说话人贡献约 42.6% 观察（仅 3 人但人均录音多），Hong Kong 停顿与辅音比例更高，印尼元音/节奏/重音更突出，南亚多见摩擦音（齿擦音停顿化）等口音特异模式。说话人表：南亚 50/82、香港 19/53、印尼 3/82。

## 结论
作者提供面向 AusEng 反馈的开放标注框架与初步错误模式，强调音系–计算机跨学科协作；标注验证与互评信度为进行中工作，并指出开放数据人口学不平衡等挑战。

## 点评
把“对/错二元”换成相对 AusEng 的语言学可解释类目，并显式纳入韵律，适合教学反馈建模。强在透明编码与口音对比；弱在说话人极不均衡（尤其印尼）、全文在结果段有截断、且尚无互评信度与下游模型数字，现阶段更像方法与数据白皮书。
