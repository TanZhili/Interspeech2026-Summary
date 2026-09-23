# Audio-DeepThinker: Progressive Reasoning-Aware Reinforcement Learning for High-Quality Chain-of-Thought Emergence in Audio Language Models

- 论文编号：1720
- 报告人：Chenxing Li
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/he26e_interspeech.pdf

## 问题
LALM 多为感知—作答；SFT 模仿 CoT 受示范多样性限制，粗粒度 RL（准确率/格式）不直接约束推理内容，易产生形式上合格却与声学证据脱节的链条。

## 方法
Audio-DeepThinker：(1) 自动造参考链——Captioner 描述 → QA → DeepSeek 生成参考 CoT；(2) 混合推理相似度奖励——LLM 评逻辑路径/关键步覆盖等 + BGE-M3 嵌入相似；仅答对时发放；(3) 渐进两阶段纯 RL（无 CoT SFT）：Stage1 在 AVQA 等基础集上用完整奖励（准确+格式+一致性+混合相似）做 RL-Zero；Stage2 在边界难例上仅用准确+LLM 相似以鼓励策略多样性。优化用 GDPO，底座 Qwen3-Omni-30B-A3B-Instruct。

## 实验与结果
MMAR Acc 74.0%、Rubrics 65.29%，Single Model Track 第 1；MMAU-Test-Mini 78.5%。相对 Instruct 基线 +3.9 Acc。消融：混合相似奖励显著抬高 Acc 与 Rubrics；仅 Stage2 或跳过 Stage1 推理质量更差，说明需先建立基础推理再攻边界。

## 结论
细粒度推理内容监督 + 两阶段课程可使高质量 CoT 从探索中涌现；瓶颈更在奖励设计而非架构。

## 点评
把“推理像不像参考、关键步齐不齐”直接写进奖励，比只奖答对更能对齐 Rubrics。参考链由字幕+大 LLM 合成，仍可能偏文本先验；计算与裁判 LLM 成本高，但作为单模冠军方案，证明 RL 细粒度过程监督可行。
