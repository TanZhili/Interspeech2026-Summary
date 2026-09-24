# Evaluating Large Language Models Abilities for Addressee, Turn-change, and Next Speaker Prediction in Meetings

- 论文编号：2923
- 报告人：Ryo Fukuda
- 程序：Wednesday 30 September 2026 / LLMs and Conversational Interaction
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/fukuda26b_interspeech.pdf

## 问题
多方会议轮次比双人更复杂：需推断受话人、是否换轮、下一位说话人。LLM/多模态 LLM 在这些任务上相对监督模型与人类的能力边界不清。

## 方法
在 AMI 上统一评测三任务：受话人检测、轮次变化（Shift/Hold）、下一说话人预测。对比监督基线、文本 LLM（Qwen3 等）、MM-LLM 与人类；输入含转写/音频/视频与会话上下文；另测 ASR 转写与 FOA 模块化设定。

## 实验与结果
LLM 在下一说话人预测上优于监督模型与人类，即使无音视频、未在目标域训练。MM-LLM 在受话人与换轮上优于纯文本 LLM，但仍低于人类，显示难有效利用原始视听信号。消融表明会话上下文尤其对下一说话人关键。人类与 LLM 错误模式相似，频繁换轮区间双方都难。

## 结论
文本上下文已携带强轮次线索；多模态 LLM 尚不能充分兑现原始音视频收益。框架为会议助手轮次理解提供统一基准。

## 点评
把人类表现纳入对比是稀缺且有价值的锚。下一说话人上 LLM 超人类，可能受益于完整转写上下文与允许多候选设定。近讲话筒泄漏（约 8.5%）可能泄漏下一说话人线索；AMI 角色会议外推到开放多方场景需谨慎。
