# The Voice Behind the Words: Quantifying Intersectional Bias in SpeechLLMs

- 论文编号：1918
- 报告人：Shree Harsha Bokkahalli Satish
- 程序：Monday 28 September 2026 / Spoken Language Processing: Evaluation and Metrics
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/bokkahallisatish26_interspeech.pdf

## 问题
端到端 SpeechLLM 保留口音、感知性别等副语言线索，可能使相同文本问题因说话人身份得到不同质量回答；交叉身份效应与开放生成评测方法仍不足。

## 方法
用 MegaTTS3 对 6 种口音（EdAcc）× 2 种感知性别克隆固定文本（含犹豫变体），共 960 语音提示，喂给 LFM2-Audio、OmniVinci、Qwen3-Omni，得 2880 次交互。先查口音/性别识别与转写 WER/UTMOS；再用 Gemini 做点评分、成对比较与 Best–Worst Scaling（helpful/competence/formality/condescension）；Prolific 人工 BWS 验证。

## 实验与结果
模型几乎不能识别口音（多默认美式），但性别识别因模型而异；OmniVinci/Qwen3 各口音转写 WER 相近。点评分主效应弱；成对比较中东欧口音胜率最低（31.6%，p=0.007），礼貌维度多平局——偏见体现在帮助性而非粗鲁。交叉：东欧女性帮助性最低（约 3.15）。人工 BWS 对口音反差更敏感；LLM 法官抓方向但灵敏度较低。

## 结论
作者报告口音–性别交叉的帮助性差距，语气仍礼貌；并开源数据与评测提示。

## 点评
用克隆控内容、变身份，是测生成偏见的干净设计。合成语音与真口音社会感知仍有落差；依赖 LLM 法官需人工校准——本文这一步做得好。偏见主要在“帮得少”而非“说得凶”，对部署友好度审计有启发。
