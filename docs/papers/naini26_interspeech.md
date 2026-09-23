# Comparative Reasoning: Making an Audio Language Model Better at Comparing Emotions

- 论文编号：2935
- 报告人：Abinay Reddy Naini
- 程序：Wednesday 30 September 2026 / Multimodal Emotion Recognition
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/naini26_interspeech.pdf

## 问题
大音频语言模型（LALM）多做单音频推理，跨两段语音的比较判断（如谁 arousal/valence/dominance 更高）较弱，且现有序数 SER 偏好学习很少显式建模可解释的比较推理。

## 方法
提出 reasoning-guided ordinal SER：输入成对语音与属性定义提示，预测哪一段属性更高。用 Qwen3-Omni-Captioner 语义描述 + 18 维 GeMAPS LLD 的均值/标准差（归一化后离散为 low/medium/high）喂给 Qwen3-Next-80B，生成 <5 句的比较推理轨迹；错答则条件于正确标签重生成。骨干 Qwen2.5-Omni-3B + LoRA，对比标签-only 的 SFT/DPO 与带推理的 SFT-CoT/DPO-CoT（DPO 对正确/错误推理–答案对）。MSP-Podcast v2.0 上用约 5% 话语构造每属性 10k 训练对（共识分差 >1）。

## 实验与结果
MSP-Podcast 测试：零样本平均偏好准确率 0.637；SFT 0.875、DPO 0.879、DPO-CoT 0.881，均超过 WavLM/HuBERT+RankNet 与 RankList（后两者用 240k 对，平均约 0.76–0.80）。跨域 BIIC/WHiSER 上 LALM 变体总体优于 SSL 基线，DPO-CoT 在 BIIC 平均 0.770。仅训 arousal 时 DPO-CoT 跨情绪平均 0.785，对 valence 退化小于标签-only。推理轨迹可给出音高、响度、犹豫等可解释依据。

## 结论
适当适配的 LALM 能以远少于传统序数系统的数据做好情绪偏好比较；DPO 对照正确/错误推理可提升利用推理并抑制幻觉，增强可解释性与跨域/跨维迁移。

## 点评
把成对比较、声学可感知证据与偏好优化绑在一起，切中 LALM 的多音频短板，数据效率对比（10k vs 240k）很有说服力。SFT-CoT 有时略逊于纯标签 SFT，说明推理监督质量与长度约束关键；依赖外部大模型造轨迹，部署成本与轨迹忠实度仍是实际瓶颈。
