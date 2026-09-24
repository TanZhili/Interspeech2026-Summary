# MAC-SLU: Multi-Intent Automotive Cabin Spoken Language Understanding Benchmark

- 论文编号：1055
- 报告人：Yuezhang Peng
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：https://www.isca-archive.org/interspeech_2026/peng26d_interspeech.pdf

## 问题
现有 SLU 数据意图/槽类别少、多为单意图，模型已接近饱和；且对最新 LLM/LALM 缺少统一格式与评测协议，难公平比较 ICL、SFT、流水线与端到端。

## 方法
构建中文车舱多意图数据集 MAC-SLU：真实车载指令文本脱敏后，用 CosyVoice-2 + AIShell-1 说话人模板 TTS；8 域、81 意图、192 槽，含 0–5 意图与拒识。统一评测零样本/少样本 ICL、LoRA SFT，以及 ASR+NLU 流水线与 E2E LALM。指标：IC Acc、SF F1、Overall Acc（IC+SF 同时正确）。

## 实验与结果
约 20539 条（train/dev/test 17997/1391/1151）；多意图约 15.46%，拒识 28%。
- ICL：Overall Acc 普遍 <15%；Qwen3-32B 10-shot SF F1 55.09%，OA 14.42%；Qwen2.5-Omni-7B 可略超同规模 Whisper+Qwen3-8B 流水线。
- SFT：Qwen3-8B 文本 OA 60.73%；流水线因 ASR 误差降至 47.18%（Paraformer CER 3.64%）或 35.45%（Whisper CER 10.40%）；Qwen2.5-Omni-7B OA 55.60%，接近或优于流水线。
- 案例分析：不少错误是语义对但用词与标签不完全一致，严格字符串匹配可能低估能力。

## 结论
MAC-SLU 提高任务难度；ICL 有潜力但远逊域内 SFT；E2E LALM 可规避 ASR 传播并接近流水线。未来需语义对齐评测、更复杂声学与口音。

## 点评
把“车舱多意图 + 统一 LLM/LALM 基准”做实，填补了中文复杂 SLU 评测空白。TTS 语音保护隐私但弱化真实舱内噪声/口音；标签措辞敏感也提示标准 SLU 指标与下游可执行性之间仍有缝隙。
