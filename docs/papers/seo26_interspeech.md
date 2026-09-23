# When Multiple Script Matters: Evaluating ASR in Clinical Settings

- 论文编号：1126
- 报告人：Minkyu Kim
- 程序：Monday 28 September 2026 / Spoken Language Processing: Evaluation and Metrics
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/seo26_interspeech.pdf

## 问题
非英语临床 ASR 中，同一医学术语可有多种合法正字形式（英文原形 vs 本地音译等），单参考 WER 会把正确变体当错；这与声学语码切换不同，是正字多脚本问题。

## 方法
构建 MultiClin：从 ACIBench 等英医患对话筛选、打 MEDICAL/NUMBER/UNIT 标签、译为韩语并保留双语脚本变体，护理背景人工复核；用 TTS + DSP（混响/HVAC）合成 HIPAA 合规音频，共 316 对话。评测协议对脚本实体在假设窗口内做 LCS 对齐，动态选择原形或音译作参考。零样本评 Whisper/Qwen3-ASR/Gemini；LoRA 微调 Whisper，并扫训练转写比例。

## 实验与结果
从单参考到多脚本感知评测，错误率大幅下降（如 Gemini 2.5 Pro WER 28.28%→15.78%）。开源中 Whisper v3 Turbo 多脚本 WER 约 23%；Gemini Pro CER 最佳约 4.86%。100% 统一本地脚本微调最优（Whisper Turbo CER 可至 6.16%）；训练脚本比例 50% 时熵最高、错误反弹（CER 57.47%），说明标签不一致伤害收敛。

## 结论
作者认为多参考评测更公平反映临床识别质量；训练端脚本统一优于混杂映射。

## 点评
把“评测假设失效”做成可发布基准与算法，对本地化临床 ASR 有直接意义。音频全合成，与真诊室声学仍有差距；标签靠 LLM+人工，Specialty 分布偏骨科。50% 比例的熵故事与结果吻合，是可操作的数据工程教训。
