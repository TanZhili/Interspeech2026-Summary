# EChO-Agent: Evidence Chain Orchestration Agent for Audio Reasoning

- 论文编号：1313
- 报告人：Siyuan Zhang
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26t_interspeech.pdf

## 问题
复杂音频 QA 中 LALM 缺少问题条件感知、可核验推理链、领域知识与“回头再听”能力；现有工具增强 agent 多解决“采什么信息”，却少把工具输出蒸馏成决策关键证据并做证据—答案一致性校验。

## 方法
EChO-Agent 四阶段：Tool→Evidence→Reason→Verify。按题型静态调度 YAMNet AED、Whisper ASR、SpeechBrain SER、Essentia 音乐分析等；DeepSeek-V3 做相关性过滤、跨观察综合与证据结构化；Qwen3-Omni-Instruct 在原音频+结构化证据上按步进式提示推理，双配置各跑一次；LLM 做格式修复、推理—答案一致性检查与双候选仲裁。

## 实验与结果
MMAR：Acc 71.0%、Rubrics 63.0，Agent Track 约第 5；相对同底座 Instruct 基线 +2.3 Acc、+4.3 Rubrics。消融：去掉证据整合最伤（Acc 65.4 / Rubrics 56.9，甚至低于无工具基线）；去掉观察或验证亦有下降。混模态增益更明显。

## 结论
可审计证据链编排优于把原始工具输出直接塞给 LALM；证据整合是关键，验证主要修最后一公里错误。感知工具粒度（如 YAMNet）仍限制细粒度声音题。

## 点评
消融很有说服力：乱塞工具噪声会负优化，结构化证据才是桥。设计清晰、可复现性强，但静态题型路由与较粗事件标签限制上限；相对冠军级大规模工具迭代/可靠性分层系统，定位更偏精简可审计流水线。
