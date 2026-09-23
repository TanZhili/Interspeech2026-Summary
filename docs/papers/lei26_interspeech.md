# ARCHES: An Agent-Based Refinement Cycle for Hierarchical Synthesis of Sound Effects for Variety Shows

- 论文编号：561
- 报告人：Li Liu
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/lei26_interspeech.pdf

## 问题
综艺音效依赖人工剪辑，成本高、难规模化；通用文本/视频到音频模型偏现场自然声（diegetic），难覆盖风格化、喜剧化、稀有签名音效，且时序与情绪控制不足。

## 方法
ARCHES 多智能体迭代：Planning 检测需增强的事件 → Generation 条件合成 → Checker 评估后经 AXIS 路由到时序/情绪等细化智能体。AURA 用 Qwen2-Audio 多模态检索 26k+ 专业音效库作上下文示例；CEB 记录成功交互作模板捷径。生成骨干基于 MultiFoley，高层规划多用 Gemini-2.5 Pro。自建 VSSE-Bench（约 1000 集综艺切分）评测。

## 实验与结果
相对 MMAudio、Kling-Foley、HunyuanVideo-Foley、FoleyCrafter：LSD 0.77、OD 0.048 s、FAD 7.04、A-MOS 2.68 及主观 MOS-S/T/E（4.04/4.54/4.46）均最优。消融：无 AURA 损害多样性/FAD；无 AXIS 时序误差大增；无 CEB 略降。换 MLLM 骨干时 Gemini-2.5 Pro 最好，开源 Qwen3-VL 仍可用。

## 结论
检索增强 + 智能路由细化 + 经验库可使综艺风格音效在保真、同步与情绪匹配上显著优于通用 V2A；未来将降延迟、减对底层模型依赖并扩展跨模态生成。

## 点评
把后期剪辑流程 agent 化，切中综艺非叙境音效痛点；新基准与音效库是实质贡献。系统强依赖闭源/强 MLLM 与外部库质量，消融已显示去掉检索或细化回路即掉点；客观 LSD/FAD 对“喜剧恰当性”覆盖有限，主观三项是更关键证据。
