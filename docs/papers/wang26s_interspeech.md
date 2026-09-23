# FlowTTS-GRPO: Online Reinforcement Learning with Multi-Objective Reward Optimization for Flow-Matching Based Text-to-Speech

- 论文编号：1102
- 报告人：Haoxu Wang
- 程序：Monday 28 September 2026 / Text-to-Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/wang26s_interspeech.pdf

## 问题
TTS 的 RL 后训练多集中在 LLM 侧；Flow Matching 因 ODE 确定性难直接做在线 RL，且零样本克隆需同时兼顾说话人相似、可懂度与感知质量，多奖励易冲突。

## 方法
FlowTTS-GRPO：将 FM 的 ODE 采样转为等价 SDE 引入随机性，用 GRPO 在线优化开源 FM（CosyVoice 3.0 的 FM 部分、F5-TTS），无需额外随机生成器/价值网。奖励含说话人相似、ASR/CER、DNSMOS 等；对比概率式单奖励分配与按 batch 标准差归一化后的加权和。训练省略 CFG 加速收敛；对 F5 引入硬文本增广（词/句重复）。LoRA 微调 FM。

## 实验与结果
Seed-TTS-Eval：F5 经 FM-GRPO 后中英 CER/WER 与 SS、DNSMOS 提升（如 test-zh CER 1.81→1.55，SS1 0.760→0.777）；CosyVoice 3.0-0.5B 主要抬升 SS 与 MOS（SS1 0.777→0.804），CER 基本持平——符合“LM 管可懂度、FM 管声学细节”观察。加权归一化奖励收敛更稳。

## 结论
作者认为 ODE→SDE + GRPO 可直接后训练开源 FM TTS，多目标加权与硬样本策略有效，且 FM-RL 与 LLM-RL 作用互补。

## 点评
把 Flow-GRPO 从图像/增强迁到零样本 TTS，并点明混合系统中应 RL 哪一模块，实用。代理奖励仍可能 reward hacking；主观偏好相对客观表较简。硬样本仅中文侧为主。
