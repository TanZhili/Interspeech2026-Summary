# X-OPD: Cross-Modal On-Policy Distillation for Capability Alignment in Speech LLMs

- 论文编号：861
- 报告人：Di Cao
- 程序：Monday 28 September 2026 / Multimodal Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/cao26_interspeech.pdf

## 问题
端到端 Speech LLM 相对同系文本 LLM 在复杂指令、推理与知识任务上明显掉点；标准 SFT+RL 与离线蒸馏难弥合模态差距，且常有暴露偏差与灾难性遗忘。工业上仍常退回级联系统。

## 方法
X-OPD：跨模态 on-policy 蒸馏。
- 平行数据 \((S_i,T_i)\)：语义不变的语音–文本提示对（文本改写成口语风格后 CosyVoice3 合成，SenseVoice 回译 WER>5% 过滤）；约 27k 对。
- Student（Speech LLM）在语音/文本上 on-policy 多样本 rollout（\(n=4\)）；文本 teacher 在同步文本上给 token 级优势：
  - 模态内 \(A_{\mathrm{im}}=\log\pi_\phi(y_t|T,y_{<t})-\log\pi_\theta(y_t|T,y_{<t})\)
  - 跨模态 \(A_{\mathrm{cm}}=\log\pi_\phi(y_t|T,y_{<t})-\log\pi_\theta(y_t|S,y_{<t})\)
- 目标 \(\lambda L_{\mathrm{im}}+(1-\lambda)L_{\mathrm{cm}}\)（策略梯度 + 概率比）；全参训 LLM 骨干，冻结 audio tower 与 adapter。

## 实验与结果
基座 Qwen3-Omni-A3B-Instruct，teacher 为 Qwen3-A3B-Instruct；基准 BIG Bench Audio、Audio Multi-Challenge、VoiceBench（语音/文本双模态）。
- X-OPD 将平均掉点从 11.29%（S）/5.51%（T）降至 **3.43% / 0.97%**；如 BIG Bench Audio 语音 93.41 vs 基座 85.67。
- 同数据上 SFT、Offline KD、GKD 反而扩大掉点。
- 消融：同容量 teacher（A3B）优于更大 A22B；\(\lambda=0.5\) 优于纯文本/纯语音。
- MMAR 遗忘：SFT/KD/GKD 从 71.3 跌至约 60；X-OPD 仍约 69–70.7。

## 结论
On-policy 跨模态蒸馏可在少量无标注配对数据上对齐 Speech LLM 与文本能力，并显著减轻遗忘；为低成本基础对齐提供路径。

## 点评
抓住暴露偏差：让学生在自己轨迹上被文本 teacher 打 token 级分，比静态离线轨迹更贴推理路径。强在双优势与遗忘对比完整；脆弱在依赖合成语音–文本平行性与 teacher–student 容量匹配——过大 teacher 反而变差，说明“可吸收轨迹”比绝对教师强度更关键。
