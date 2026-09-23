# Breaking Neutral Bias: Zero-Human-Annotation Fine-Grained Emotion Enrichment via Semantic Drift and Discriminative Re-ranking

- 论文编号：1925
- 报告人：Qihang Lu
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/lu26c_interspeech.pdf

## 问题
LALM/字幕数据常呈 **Neutral Bias**（安全中性描述）；纯文本扩写会声学幻觉，多模态标注又易被视觉/ASR 主导。

## 方法
零人工标注的“假设–验证”流水线：Gemini 与 Qwen3-Omni 协同标注，高一致样本训 **判别式 LALM 裁判**（硬/软负例对比）；低一致样本用 LLM **语义漂移**生成多维情绪假设；裁判用原始音频过滤并按 Drift→Refine→Origin 重排。下游用精炼数据做 SFT。

## 实验与结果
约 2.95 万音频；裁判全量训练后 Balanced Acc 96.07%，消融显示单类负例会过度拒识。下游相对基线：Gemini 偏好胜率 66.15% vs 29.23%；词表多样性（Unique Bigrams、熵）上升；t-SNE 显示情绪分布更贴近参考流形、缓解向 Neutral 塌缩。

## 结论
语义漂移 + 声学接地重排可在无人工下把中性标签炼成细粒度情绪描述，提升下游表现。

## 点评
数据中心路线抓住“中性捷径 vs 文本幻觉”双问题，用音频裁判做物理接地。风险：裁判与评测仍依赖大模型标注、偏好评测同源偏倚；过度过滤可能丢难例。
