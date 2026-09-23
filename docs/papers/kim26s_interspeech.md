# Do Modern Video-LLMs Need to Listen? A Benchmark Audit and Scalable Remedy

- 论文编号：2532
- 报告人：Geewook Kim
- 程序：Monday 28 September 2026 / Audio-Visual Grounding, Synchronization & Video Understanding
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/kim26s_interspeech.pdf

## 问题
Video-LLM 常丢弃音轨，因主流基准多可用纯视觉作答；即便标榜音视频的套件也存在视觉捷径。同时原始音频 token（约 25 Hz）对长视频上下文不可承受。

## 方法
(1) 基准审计：仅用时间中心单帧、无音频喂 GPT-4o 两次，双对即剔除，得到过滤子集（如 AVQA 约 76% 可单帧解）。(2) 在 LLaVA-OneVision 上接 Qwen2-Audio 的 Whisper 编码器；比较仅视觉、非交错、时间对齐交错输入。(3) 周期 query 将音频压缩 25×（25→1 Hz）；比较 Avg Pool、Resampler、Uni/BiMamba、UniMambaMia（因果 Mamba + 门控注意，可流式）。

## 实验与结果
10 个基准上，交错+压缩在需听懂/跨模态题上明显增益；过滤后 AVSpeakerBench +3.0、WorldSense +2.7、VideoMME +2.4 等仍成立，长视频增益更大。压缩器中 UniMambaMia 最稳。最终模型在 Qwen2-7B 系统一评测中多项最优；相对未压缩 Qwen2.5-Omni 时延/显存更低（约 1.6 s vs 4.1 s）。视觉中心套件加音频收益小或略干扰。

## 结论
作者认为 Video-LLM 需要听，但前提是基准真正要求听；控制视觉捷径后音频价值清晰。时间对齐交错 + 因果轻量压缩是可扩展接音频的实用配方。

## 点评
贡献一半是评测诊断（捷径审计与过滤集），一半是工程配方（因果 25× 压缩）。用 GPT-4o 定义“可单帧解”可能过严/过松，但作为下界审计仍有说服力。与 Omni 等不同骨干/数据规模对比不宜过度解读为纯音频通路优劣。
