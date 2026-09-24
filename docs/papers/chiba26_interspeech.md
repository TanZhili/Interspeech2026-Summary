# Speech-based Psychological Crisis Assessment using LLMs

- 论文编号：997
- 报告人：Terumi Chiba
- 程序：Wednesday 30 September 2026 / Medical Dialogue and Conversational Understanding
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chiba26_interspeech.pdf

## 问题
心理支持热线危机分级依赖人工、一致性受培训与人力限制；纯转写文本丢失副语言线索，隐私与稀缺数据下难直接训 SpeechLLM。

## 方法
真实中文热线 154 通（约 100h），专家三分类：无危机/低/中高。SpeechLLM 抽取副语言线索写入 ASR 转写（paralinguistic injection），再由文本 LLM 分类；推理增强训练用 LLM 诊断理由作辅助监督；5 分钟分块增强 + 通话级多数投票；通话级 5 折。对比 OpenSMILE+SVM、零样本富文本 LLM、SpeechLLM 微调等。

## 实验与结果
系统 macro F1 0.802、准确率 0.805，优于声学、零样本 LLM 与 SpeechLLM 基线。作者定位为人工监督下的分流决策支持，非替代临床评估。

## 结论
显式副语言文本化在少数据隐私敏感场景下，可比直接微调 SpeechLLM 更有效；理由监督与分块增强有助于正则化。

## 点评
把副语言“写进文本”绕开稀缺语音端到端微调，务实。样本量仍小、分块多数票可能抹平局部危机信号；热线中文单中心，跨机构外推需验证。伦理上强调决策支持定位是必要边界。
