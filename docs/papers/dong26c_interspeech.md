# Can Speech LLMs Approximate Human Ratings of Accentedness and Comprehensibility? Evidence from Correlational and Feature-Based Analyses

- 论文编号：1991
- 报告人：Wenwei Dong
- 程序：Monday 28 September 2026 / Paralinguistics
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/dong26c_interspeech.pdf

## 问题

二语音系评估常用 accentedness 与 comprehensibility 的人工量表，成本高。传统自动发音评估多走预定义维度或 ASR 指标，未必对齐人类感知。作者检验语音大模型能否近似人类评分、是否敏感于 CALL 前后进步，以及打分时依赖的音段/超音段线索是否与人类相近。

## 方法

印尼高中 EFL：33 名完成 36 天 ASR-CALL 练习者，前/后测各 28 句共 1848 句；9 名印尼母语专家用 9 点量表评分（高分=更接近母语/更好懂），ICC 很高。用 Qwen3-Omni-30B-Instruct 做 zero-shot 与 few-shot 提示打分；留出最低/最高各 1 名学习者作样例，其余 31 人（1736 句）测试。另提取 Praat 16 维、eGeMAPS 88 维、Whisper 词距离共 105 特征，经 Lasso 后按与分数的绝对 SPCC 排序，比较人类与 LLM 的线索重叠。线性混合效应模型以 Test（pre/post）为固定效应、说话人与句子为随机效应。

## 实验与结果

与人类相关中等：zero-shot 可懂度 SPCC 最高约 0.419；加朗读文本后两项相关下降。few-shot 中 Exp.6（低/中/高分各 2 例）MSE 最低（accent 0.82、comp 1.37），SPCC 分别为 0.283 与 0.497。LME 显示人类与 LLM 分数均显著 post>pre。句子级平均相关高于说话人级（可懂度句子级 SPCC 0.710）。特征上：人类 accentedness 更偏谱通量/响度等超音段，comprehensibility 以 Whisper Word Distance 居首；LLM 两边都重 duration、词距离、语速与响度，与人类部分重叠但不完全同序。

## 结论

语音 LLM 分数与人类中等相关，能捕捉 CALL 前后进步，并共享部分音段/超音段线索；仍需探索微调与融入语言学知识。提示设计敏感：分开打分优于同时打分，过多示例或附带文本可能干扰。

## 点评

工作价值在“对齐诊断”而不只报相关：用 LME 看发展敏感性，用特征排序看构念是否被误读。结果显示 LLM 更像粗糙的流利度/错误代理，对 accentedness 的超音段重心把握弱于人类。脆弱点是零/少样本未微调、评分者与学习者为同一 L1 背景、few-shot 样例选择可能影响尺度校准，且正文讨论后半有截断。
