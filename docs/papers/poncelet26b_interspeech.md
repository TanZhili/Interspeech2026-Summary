# Towards Deep Contextual Reasoning from Broad Descriptions for ASR with Speech-LLM via Metadata-Driven Reasoning Chains

- 论文编号：1041
- 报告人：Jakob Poncelet
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/poncelet26b_interspeech.pdf

## 问题
ASR 在稀有词、领域专名上脆弱；现有上下文偏置多为关键词列表，难扩展，也不能像文本 LLM 那样对宽泛主题描述做深层推理。级联文本后编辑又无法核对声学可行性。

## 方法
两阶段：用 YouTube 元数据（标题/清洗描述/标签）+ Whisper 伪标签（及 LLM 注入的声学合理错误）生成约 400 小时推理增强数据——LLM 写出从错误假说到参考的上下文理由。微调 speech-LLM 输出 `<initial-text>-<reasoning>-<final-text>`；与纯 ASR 数据 50/50 混合，初始转录损失掩码。评 Qwen2-Audio、Qwen2.5-Omni、Audio-Flamingo-3、Ultravox 等，测试侧重 M³AV 命名实体子集及 SlideSpeech/SlideAVSR。

## 实验与结果
基座模型直接喂大上下文会严重幻觉。微调后相对纯转写与“带上下文转写”，两阶段显式推理进一步降 WER，稀有词/NE 更明显（如 Qwen2-Audio 在 M 集上 All/Rare/NE 到约 9.3/23.1/23.3）。相对初始假说，推理修正多为正/中性；纯文本 LLM 后编辑反而抬 WER。多底座上趋势一致。

## 结论
用元数据驱动的 CoT 监督，可让 speech-LLM 在保持声学接地的前提下，从宽泛描述做上下文纠错，尤其改善稀有词与命名实体。

## 点评
把“关键词偏置”升级为“主题级理由监督”，且坚持音频条件化以避免文本乱改，方向正确。脆弱处：推理链由文本 LLM 生成可能有牵强样本（虽有过滤）、依赖视频元数据可用性、训练成本与推理长度增加。
