# Speak or Stay Silent: Context-Aware Turn-Taking in Multi-Party Dialogue

- 论文编号：3083
- 报告人：Kratika Bhagtani
- 程序：Wednesday 30 September 2026 / Entrainment and Dialogue Coordination
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/bhagtani26_interspeech.pdf

## 问题
多人场景中暂停含义模糊，现有语音助手常把每次停顿都当发言邀请而打断；二元对话式 turn-taking 与仅做下一说话人预测，都未解决助手在每处暂停“说还是沉默”的上下文决策。

## 方法
把任务定义为：给定完整上下文与目标说话人，在每处暂停二分预测 SPEAK/SILENT。从 AMI、Friends、SPGI 构建约 12 万标注决策点，细分为显式称呼(I1)、语境介入(I2)、无指称沉默(S1)、被提及但非称呼(S2)。评估 8 个 LLM 零样本；再用 LoRA SFT，并可选蒸馏教师生成的一句推理痕迹。

## 实验与结果
零样本普遍接近随机或强 SPEAK 偏置（最佳约 BalAcc 64%）。SFT 可提升最多约 23 个百分点（如 Mistral-7B on AMI：BalAcc 48.93→72.28）；增益主要来自需保持沉默的 S1/S2。加推理痕迹再提约 7 Acc 点。人类在 Friends 子集 BalAcc 约 60–66%，模型可持平或略优。合并三域训练仍具跨域迁移。

## 结论
上下文感知 turn-taking 非 LLM 涌现能力，需显式监督（尤其是沉默类）；推理蒸馏有助于语用判断。

## 点评
问题定义贴近真实多人助手痛点，四类标签把“被提到≠被叫到”拆开很关键。当前仅文本转录、无声学/视觉线索，且标签由下一说话人启发式派生，对脚本剧与会议语体的生态效度需再验证。
