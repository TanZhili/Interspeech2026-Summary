# Preference-ASR: A Preference-Aware Test Set for Benchmarking ASR in the Era of Speech LLMs

- 论文编号：728
- 报告人：Nithin Rao Koluguri
- 程序：Thursday 1 October 2026 / Speech Benchmarks, Evaluation, and Resources
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/koluguri26_interspeech.pdf

## 问题
主流 ASR 测试集在数字、不流畅、实体与大小写等标注惯例上不一致，标准归一化又抹掉用户关心的格式差异；SpeechLLM 虽能跟自然语言偏好指令，现有基准测不到“是否按偏好输出”。

## 方法
Preference-ASR 从七个开源语料（AMI、Common Voice、Earnings-22、GigaSpeech、LibriSpeech、SPGISpeech、VoxPopuli）取约 3,545 条并人工校 GT；两阶段用 Qwen3-30B-A3B：先分类偏好类别（normalization / entities / disfluencies / case），再生成指令与偏好参考，人工复核后得 3,210 条 (audio, instruction, reference) 三元组（另 335 条无偏好基线）。提出 preference-aware normalizer：按当前指令选择性跳过 TN/ITN、保留/剥离不流畅、跳过小写化等，再算 WER。评测 Parakeet-TDT-0.6B-v3（无指令）、Canary-Qwen-2.5B、Phi-4-Multimodal、Qwen3-Omni-30B，对比 default 与 instructed。

## 实验与结果
标准归一化下 Canary-Qwen 与 Qwen3-Omni 默认总体 WER 接近（约 5.64% vs 5.66%），但对指令反应不同：Qwen3-Omni 实体 WER 从 5.12% 升至 12.85%（提示词实体幻觉）；Phi-4 不流畅默认 50.18%、指令后 10.46%，但 case 指令反而恶化（3.93%→19.76%）。偏好感知 WER 下排名重排：如 normalization 上 Qwen3-Omni (I) Pref 9.84% 优于 Canary-Qwen (I) 11.32%；实体幻觉在 Pref 下仍约 12.68%。Canary-Qwen 对指令整体几乎平坦。

## 结论
作者认为该测试集与选择性归一化能暴露传统 WER 看不见的偏好遵循差异；局限为仅英语、尚无多说话人偏好，且 LLM 生成偏好文本需人工核验（尤其 normalization）。

## 点评
对准 SpeechLLM 时代“指令跟从 vs 声学证据”的评测缺口，四类偏好与选择性归一化器设计清楚。脆弱处在实体上下文偏置与提示敏感：强指令模型可能为跟提示而幻觉，结论高度依赖人工复核后的参考质量。
