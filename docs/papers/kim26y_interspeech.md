# VividAC: Visually Informed and Visually Interacted Audio Captioning for Enhancing Audio-Visual Question Answering

- 论文编号：3442
- 报告人：Mingi Kim
- 程序：Monday 28 September 2026 / Multimodal Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/kim26y_interspeech.pdf

## 问题
AVQA 中希望用文本 caption 撬动 LLM 推理，但朴素音频 caption 常与视觉场景不一致、缺少问题相关细节，甚至相对“仅视频”基线掉点。端到端 AV-LLM 联合训练成本高，跨模态证据对齐仍困难。

## 方法
VividAC：训练免费的级联智能体通信。
1. **Visual Agent（VLM）**：根据视频与问题名词短语生成 query-relevant 视频描述 \(C_v\)；
2. **过滤**：从 \(C_v\) 抽名词，用 CLIP 与问题名词相似度筛保留（阈值 \(\tau=0.8\)），得关键词；
3. **Audial Agent（ALM）**：在音频、\(C_v\) 与关键词提示下生成视觉语境化音频 caption \(C_a\)；
4. **推理 LLM**：综合视频描述、音频 caption 与问题作答。
方向固定为 Vision→Audio；全程自然语言接口，无音视频联合训练。

## 实验与结果
MUSIC-AVQA 官方测试（9192 QA / 6399 样本）；答案归一化后关键词包含判定准确率。
- 12 组 LLM–VLM 组合中 11 组相对 Naive 提升，最高约 +11.01%p（Llama-3.1 + Qwen2.5-3B）；唯一下降为 Llama-3.1 + InternVL2.5（Overall −0.63%p，但 A-Avg 仍 +2.37%p）。
- VividAC + Qwen2.5 达 Overall 59.91%，相对最强端到端 Video-SALMONN 52.91% 高 7.0%p。
- 方向消融：V→A 优于 No Interaction 与 A→V；给既有 AV-LLM 附加 VividAC caption 亦优于朴素 caption。

## 结论
结构化跨模态自然语言对话可在无需联合训练下显著提升零样本 AVQA；改进主要来自智能体交互而非特定模型配对。作者视其为对端到端路线的互补路径。

## 点评
抓住“音频 caption 必须被视觉与问题锚定”这一瓶颈，用轻量 CLIP 过滤缓解级联误差传播，实用性强。强在组合泛化与相对 AV-LLM 的零训练优势；脆弱在级联仍可能传错实体、依赖 caption 质量与 \(\tau\)，且评测为字符串关键词匹配——对开放式表述可能高估/低估真实语义正确性。
