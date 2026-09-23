# Lost in Phonation: Voice Quality Variation as an Evaluation Dimension for Speech Foundation Models

- 论文编号：736
- 报告人：Harm Lameris
- 程序：Tuesday 29 September 2026 / Audio & Speech Language Models: Evaluation, Representations, and Emerging Capabilities
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/lameris26_interspeech.pdf

## 问题
Speech Foundation Models 能直接处理原始音频，但对音质/发声类型（modal、breathy、creaky、end-creak）等副语言差异如何影响生成与情绪识别，缺少可控、开放式评测；MCQA 易掩盖生成行为偏移。

## 方法
构建 VQ-Bench：以 Buckeye、VCTK 说话人作 F5-TTS 参考，经 VoiceQualityVC 按目标声学参数合成四类平行音质提示（约 148 说话人 ×4 情境 ×5 题，共约 25h17m）。开放式长文任务覆盖治疗、职业建议、面试筛选、叙事；用 gemini-2.5-flash-lite 按量规打 1–5 分。另在 Buckeye 子集上对 xlsr-en-speech-emotion-recognition 做 SER，分析完整 logit。先做性别识别 sanity check。

## 实验与结果
OpenAI 实时 speech-to-speech API 将样本一律判为男性，后续分析转向 LFMAudio2-1.5B。CLMM 显示相对 modal，非 modal 音质在多数维度显著：如职业建议中 breathy/end-creak 更偏 STEM、creaky 更偏 care；面试中多数音质降低 shortlist/薪资/领导力背书；治疗中非 modal 提高 advice agency 与 improvement。女性相对男性在薪资与领导力背书上系统更低。SER：breathy 提高 calm/neutral、降低 fearful/surprised；creaky 降低 fearful/happy；女性提高 fearful/surprised。end-creak 效应更接近 breathy 而非持续 creaky。

## 结论
可控音质变化会系统改变 SFM 的共情、能动性、领导力判断与 SER 概率质量，并再现性别不对称；VQ-Bench 提供可复现的副语言评测框架，部署于招聘/治疗等场景前需纳入音质维度。

## 点评
用平行合成把“怎么说”从“说什么”和说话人身份中拆出，开放式生成比 MCQA 更能暴露社会偏见传导。商业 API 连性别 sanity check 都失败，说明部分系统可能几乎未接地副语言。局限包括二元性别源语料、LLM-as-judge、以及当前仅一个有效开放权重模型——框架价值大于单模型排行。
