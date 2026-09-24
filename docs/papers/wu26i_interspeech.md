# AFG-Bias: Acoustic-Fusion-Gated Biasing for Plug-and-Play Hotword Customization in LLM-Based ASR

- 论文编号：2029
- 报告人：Long Wu
- 程序：Wednesday 30 September 2026 / Multi-Speaker Processing, Personalization, and Adaptation
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/wu26i_interspeech.pdf

## 问题
LLM-ASR 难识别稀有领域实体；浅层融合不适生成式解码，深度上下文化多为传统 E2E，提示注入易规模崩塌与幻觉。需不改 LLM 参数的可插拔热词偏置。

## 方法
AFG-Bias：Cross-Modal Acoustic Retrieval（CAR）用滑窗跨模态相似度从大规模候选中取相关热词；Acoustic-Fusion Gating 把经验证偏置注入解码并抑制无声学依据的幻觉。训练时冻结骨干 LLM；HotwordModule（内维 256、单层单向 LSTM）等轻量模块可训。推理 K=5、τ=3、偏置权重约 0.4。

## 实验与结果
AISHELL-1/KeSpeech 训，SeACo 与金融/医疗集评。三骨干 FireRedASR/OSUM/Kimi：相对直推，金融/医疗 CER 相对降最高约 74.1%（OSUM 10.93→2.83）；AISHELL 热词 F1 最高约 +5.4。无门控 CER 飙至约 20%；候选扩到上千仍较稳。纯提示注入常崩至 >30% CER。

## 结论
声学检索 + 门控融合可在冻结 LLM-ASR 上实现可扩展、低幻觉热词定制，显著优于提示注入。

## 点评
把“先声学证据再偏置”做对，直接打消提示列表淹没注意力的失败模式。可插拔性强。依赖 CAR 召回质量；极短/同音热词与跨语实体仍可能漏检或误门控。
