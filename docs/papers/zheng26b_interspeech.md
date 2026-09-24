# Balancing ASR and diarization in end-to-end LLMs for multi-talker speech recognition

- 论文编号：1124
- 报告人：Naijun Zheng
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/zheng26b_interspeech.pdf

## 问题
多人 ASR 需「谁说了什么」；流水线解耦语义与说话人，端到端 LLM 又常依赖大规模会议标注。重叠区易诱发重复幻觉，ASR 与 diarization 训练难平衡。

## 方法
双编码器：SenseVoice-small（语义，多层拼接+适配器）与冻结 Campplus（多块时长 400/200/100ms 统计后卷积对齐）。特征融合比较语义-only、特征维拼接、时间维拼接、时间交织（每 20 帧/~1.2s）。标签含 `<SC>`+说话人 ID。段长加权说话人 CE；重叠高 CE token 用自适应阈值 Tmask=max(Avg(CE),2.0) 屏蔽。多阶段：ASR→双人对话→拼接至 8 说话人→AliMeeting/Aishell4 微调。后端 Qwen2.5-0.5B-Instruct，总约 0.7B。

## 实验与结果
时间交织 + mask 最优：AliMeeting Test CER/cpCER 23.61/27.16，Aishell4 Eval 17.18/19.98；相对开源流水线约 18%/24% 相对提升（摘要）。mask 相对 cpCER 增益约 8.5%/6.9%。去掉说话人损失、mask 或 ASR 损失均变差。说话人特征可下采样至约 25% 帧仍可接受。

## 结论
有限真实会议数据下，交织融合 + 段感知说话人损失 + 重叠高损屏蔽可平衡 ASR 与归属，减轻幻觉。未来拟做说话人注册与更长时戳。

## 点评
把重叠幻觉归因于「高损 token 主导反传」并做自适应屏蔽，是很具体的训练诊断。0.7B 相对 SpeakerLM 大数据设定的可比性有测试切分差异，但结构消融本身说服力强。
