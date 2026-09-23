# The Interspeech 2026 Audio Reasoning Challenge: Evaluating Reasoning Process Quality for Audio Reasoning Models and Agents

- 论文编号：118
- 报告人：Ziyang Ma
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/ma26_interspeech.pdf

## 问题
既有音频推理基准几乎只评最终答案正确率，掩盖捷径与不可解释推理；LLM-as-a-judge 的系统级打分又不稳定。社区需要面向 CoT 过程质量的共享任务与更可靠评测协议。

## 方法
举办 Interspeech 2026 Audio Reasoning Challenge：Single Model（端到端、禁外部工具）与 Agent（可编排开源模型/工具）双赛道。提出 MMAR-Rubrics：答案错误则过程分记 0；答案正确时，由 Gemini-2.5-Pro 从人工金标 CoT 生成 k=5 条可检核准则，GPT-4o 做二值判定并附简短理由，实例分为准则满足率。相对系统级 5 分量表，实例级协议提高评分者间/内一致性与人类偏好对齐。

## 实验与结果
156 队 / 18 国家地区报名；终榜 Single 14 队、Agent 16 队。Agent 整体 Rubrics 更高（冠军 69.83 vs 单模冠军 65.29）；准确率差距相对较小。单模前列多为 Qwen3-Omni 家族：两阶段 RL/GRPO、训练无关注意力操纵、高质量 LoRA SFT。Agent 前列：40+ 工具迭代取证、多模型投票+VLM 谱图数值推理、多智能体辩论共识。

## 结论
挑战把评测重心从“答对与否”转向“推理是否事实、逻辑、完整”；开源 MMAR-Rubrics 数据与脚本。当前 agent 在过程质量上领先，单模经 RL/数据管线快速追赶。

## 点评
“答错过程分归零”强制正确性与可检过程绑定，避免华丽胡编拿高分。实例级原子准则比笼统打分更稳，但仍依赖闭源评判模型；双赛道拆分便于公平比较“内化推理”与“工具编排”两条路线。
