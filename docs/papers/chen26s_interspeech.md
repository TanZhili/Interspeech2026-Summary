# LLM-Guided Reinforcement Learning for Audio-Visual Speech Enhancement

- 论文编号：1816
- 报告人：Chih-Ning Chen
- 程序：Wednesday 30 September 2026 / Audio-Visual and Generative Target Speaker Extraction
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26s_interspeech.pdf

## 问题
现有 Audio-Visual Speech Enhancement (AVSE) 多用 SI-SNR、MSE 等目标，与主观听感对齐不足，且可解释性弱。数值指标提升不一定对应更少伪影或更自然的增强结果。

## 方法
提出 LR-AVSE：在 AVSEC-4 官方预训练的 encoder–separator–decoder（TCN 融合音视频）上做 RL 微调。将预测 mask 加高斯噪声视为随机策略；用冻结的 SALMONN 生成语音质量自然语言描述，再经 BERT 情感分析得到 1–5 分；以相对奖励 R = r(ŷ_RL) − r(ŷ_base) 配合简化 PPO（无 critic）与 SI-SNR 联合优化。对比基线用 DNSMOS 标量作为奖励。

## 实验与结果
数据为 AVSEC-4（训练 34,524 场景等）。测试集：LR-AVSE PESQ 1.25、STOI 0.58、NISQA 1.29、VQscore 0.62、S-BERT 0.57，优于 Pretrained Baseline（1.20 / 0.48 / 0.99）与 RL-DNSMOS（1.24 / 0.57 / 1.15）。21 人 A/B：对 Baseline 偏好 96.7%，对 RL-DNSMOS 偏好 67.6%。示例中奖励、PESQ、STOI 同向提升。

## 结论
据作者称，这是首个把 LLM 描述性反馈转为 AVSE 奖励的框架；相对监督与 DNSMOS-RL 在客观与主观上均更好，并提供可解释反馈。局限是当前 LLM 描述模式较固定，细粒度差异难刻画。

## 点评
把“语义丰富的自然语言评估”接到 PPO，比直接优化标量 MOS 更贴近听感维度（清晰度、噪声、失真），相对奖励也稳住了预训练策略。脆弱点在奖励链：SALMONN 句式重复 + BERT 映射可能压缩细微质量差；且 Baseline 的 STOI 低于 Noisy，说明 SI-SNR 预训练本身与可懂度目标存在张力，LLM 奖励能否系统性纠正仍需更广场景验证。
