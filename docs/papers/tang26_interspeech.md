# ADALA: A Wake-up Word Detection Framework Based on Adaptive Semi-supervised learning and Large Language Model

- 论文编号：493
- 报告人：Nianhang Tang
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/tang26_interspeech.pdf

## 问题
唤醒词检测是开放集拒识问题，固定规则挖负例或低层对抗难覆盖语义/语音相似的未见硬负例，唤醒率与误唤醒难兼顾。

## 方法
ADALA：用 PPO/Actor-Critic 微调 Qwen2.5-14B，结合专家先验提示生成候选短语，CosyVoice2 TTS 成音频；奖励由 WUW 模型与 FunASR 联合判定（误触发且 ASR 非真词给正奖，真词混淆强惩罚等）。生成硬负例与有标/无标真实数据在半监督框架联合训练（监督 max-pool、教师–学生一致性、域对抗减轻 TTS 伪迹）。目标词“xiao fei xiao fei”，并测英语 “Hello Wikka”。

## 实验与结果
室内自建约 1430 小时普通话数据。相对 Hard-Negative Mining：平均唤醒率 87.75%→90.43%，相似词 FAR 5.87%→3.19%；相对 GraphemeAug 在略高 FAR 下显著更高唤醒率。消融：SSL 主抬唤醒率，RL 生成主降 FAR。英语小集：唤醒约 90.42%，FAR 约 1.67%，优于两基线。

## 结论
RL 驱动 LLM 持续生成决策边界硬负例，再与半监督融合，可在保持低误唤醒下提升唤醒率，并具跨语迁移迹象。

## 点评
把“语义级硬负例”做成与检测器共进化的闭环，针对开放集误唤醒痛点。强依赖 TTS 与内部大规模数据；商用工作点（48 小时一次误触发）标定细节与公开复现难度需注意。
