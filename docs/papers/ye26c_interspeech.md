# Reinforcement Learning for Data-Efficient Code-Switched ASR

- 论文编号：2667
- 报告人：Ziwei Ye
- 程序：Thursday 1 October 2026 / Code-Switching ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ye26c_interspeech.pdf

## 问题
语音 LLM 可提示做码切换，但自回归交叉熵未直接优化序列级错误，切换边界易出现翻译整段、脚本污染等失败；标注 CS 数据稀缺。

## 方法
以 Qwen2-Audio 为可控试验台，用 GRPO 做 RLVR：组内采样 G=8 候选，用可验证奖励做相对优势。奖励 = −CER + β_sf·Script（β_sf=0.05），Script 要求字符落在语言对允许 Unicode 脚本并集。训练期两遍 draft-and-refine：第一遍 GRPO，再以最高奖励草稿条件第二遍；测试仍单遍。仅更新解码器，音频编码器冻结。

## 实验与结果
在 CS-FLEURS XTTS-TRAIN（TTS 合成）上训，评 READ-TEST 与零样本 SwitchLingua。10% 数据的 RLVR（CER+SHR+refine）可匹配全量 LoRA SFT；20% 时微均 CER 0.147 优于全量 LoRA 0.159。SHR 奖励显著降脚本幻觉且不伤 CER；CER 奖励几乎消除翻译错误。收益在类型学上更远的语对（如 ara/jpn/rus）最大。训练全用 TTS，零样本转移到真人录音。

## 结论
序列级可验证奖励 + 脚本保真与两遍自修正，能以远少于 SFT 的数据把语音 LLM 对齐到码切换转写行为，并跨声学域迁移。

## 点评
把 CS 失败拆成“翻译”与“错脚本”两条奖励通路，分析清楚；两遍 refine 对部分语对有益但阿拉伯语可能过修正，需 SHR 约束。定位是数据效率与奖励设计研究，非追 SOTA。
