# Imitation Learning for Elder-Facing Speech Synthesis

- 论文编号：2107
- 报告人：Dongrui Han
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/han26d_interspeech.pdf

## 问题
通用 TTS 未照顾老年听感；直接收老人偏好成本高、易疲劳。用专家示范做 RL 微调时，固定奖励易 reward hacking（过度放慢、插停顿）。

## 方法
模仿学习框架：医护人员录制面向老人的粤语示范（及中性对照）；专家奖励头接冻结 StyleTTS 2 韵律编码器，Bradley–Terry 成对训练；发音奖励用 SenseVoice 转写的 Jyutping 音节错误率（SER）；二者调和平均为复合奖励。以 CosyVoice2-Yue 经 SFT 为策略，用带 PPO clip 的 GRPO 优化。OPRL 两阶段：Stage1 把中等奖励、低 SER 的 rollout 并入奖励集并重训；Stage2 在外部文本上按 SER 分箱与分位数赋奖励，再 GRPO。

## 实验与结果
专家数据 125 对 / 1.5 h（train 89）。客观：GRPO w/o OPRL 静音时长 11.51 s、总时长 27.62 s（GT 约 5.43 / 19.27），SER/MOS 差，显 hacking。OPRL Stage2：SER 7.54%、CER 3.86%、MOS 3.78（8 名 66–83 岁听者），优于 base / SFT / 无 OPRL；多项韵律与可懂度指标最佳或次佳，MOS 显著高于 base 与无 OPRL。

## 结论
用专家示范 + 两阶段 OPRL 的 GRPO 可在低资源偏好对齐下缓解 reward hacking，生成更受老年人偏好、可懂度更好的粤语合成语音。

## 点评
把“奖励也 on-policy 更新”对准 hacking 很有针对性，复合奖励抑制牺牲可懂度换慢速。示范仅 1.5 h、听者 8 人，风格是否覆盖真实老人偏好仍受限；发音奖励依赖 ASR/粤拼质量，跨语种移植需重设计。
