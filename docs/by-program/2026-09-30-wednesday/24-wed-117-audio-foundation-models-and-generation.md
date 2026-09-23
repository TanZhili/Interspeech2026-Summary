# Audio Foundation Models and Generation

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Oral（Area 5 - Oral 5）
- Area：5
- 论文数：6
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。仅转述摘要中的方法与数字。

## 技术趋势

本场横跨音频—语言模型骨干、端侧小模型、文本到音频生成/编辑，以及对语音基础模型微调评价方法的反思。状态空间模型（Mamba-2）被用作音频—语言骨干，强调与音频编码器联合微调、紧凑信息丰富的 token，以及指令跟随监督对推理能力的提升；同时出现面向端侧推理的开源小型音频语言模型族。

生成侧，无训练精确音频编辑（FreeSonic）用解耦注意力与反演—反向流程在 Rectified Flow TTA 上编辑；在线 GRPO 与大音频语言模型奖励把强化学习引入 TTA（Resonate）；舞蹈到音乐则用体裁自适应节奏与上下文对齐的扩散 Transformer。

最后一篇警示：监督微调上的小幅增益往往高度依赖具体预训练检查点与随机种子，未必抬高“可达成性能天花板”，促使社区重新审视“更好的 SFT”与“更好的匹配”之别。

## 技术内容

### 音频—语言基础模型与端侧缩放

**SAM: A Mamba-2 State-Space Audio-Language Model**（论文 639；presenter：Taehan Lee）  
SAM 将音频编码器与 Mamba-2 骨干结合；SAM-2.7B 在 AudioSet 上 21.1 mAP、AudioCaps 上 17.6 SPICE，以更少参数匹配或超过更大的 7B Transformer 模型。表征分析指出：（1）联合微调音频编码器必要；（2）尽管线性扩展，SSM 更受益于紧凑信息丰富的音频 token 而非过长序列；（3）指令跟随监督使 MMAU-Sound 准确率从 22.8 升至 56.8。

**Samsone: A Family of Open Small Audio Language Models for On-Device Inference**（论文 763；presenter：Michal K. Grzeszczyk）  
面向隐私与低延迟的端侧 Small Audio Language Models；核心 Samsone-134M 在其规模档建立多项基准新 SOTA，并给出 99M/356M 以探索缩放规律。模型在公开数据上训练，并开源训练代码、权重、移动优化检查点与 Android 实时推理应用。

**Rethinking Speech Foundation Model Fine-tuning: Better SFT or Better Match?**（论文 2436；presenter：Wangjin Zhou）  
在三项 SUPERB 分类任务上，对 wav2vec 2.0、HuBERT、WavLM 的九个预训练检查点评估八种 SFT 变体（代表 base 规模多种子重复）。统计上不可区分的“最优 SFT 配方”身份常随检查点变化，跨实例迁移有限；许多下游增益更像实例/种子依赖的诱发匹配，而非普遍抬高性能上限。

### 文本到音频编辑、强化与舞蹈配乐

**FreeSonic: Training-Free Temporal-Aware Decoupled Attention for Precise Audio Editing**（论文 1121；presenter：Yuxuan Jiang）  
无训练框架基于 Rectified Flow 的 TangoFlux：优化反演—反向与联合文本—音频注意力图做目标段提取；调度注意力解耦把修改限制在目标区并保留原声学上下文；任务导向噪声注入支持移除与非刚性替换等。摘要称在保真与效率上取得更优平衡。

**Resonate: Reinforcing Text-to-Audio Generation via Online Feedback from Large Audio Language Models**（论文 1823；presenter：Xiquan Li）  
将在线 GRPO 适配到基于 Flow Matching 的音频模型，显示相对离线 DPO/CLAP 奖励的优势；并用 LALM 提供更细粒度、更贴近人类感知的奖励。最终约 470M 参数的 Resonate 在 TTA-Bench 音频质量与语义对齐上建立新 SOTA。

**GACA-DiT: Diffusion-based Dance-to-Music Generation with Genre-Adaptive Rhythm and Context-Aware Alignment**（论文 2348；presenter：Jinting Wang）  
针对粗粒度节奏嵌入与下采样时间错位，提出扩散 Transformer 框架：体裁自适应节奏模块做多尺度时空分析与自适应关节加权；上下文感知时间对齐用可学习查询对齐音乐潜变量与相关舞蹈节奏。AIST++ 与 TikTok 上客观与人工评价均相对 SOTA 一致提升。

## 本场要点

- Mamba-2 音频—语言模型强调联合编码器微调、紧凑 token 与指令监督。
- 开源 SALM 族推动端侧实时推理与公开可复现训练。
- 无训练精确编辑与在线 RL+LALM 奖励分别推进 TTA 编辑与生成质量。
- 舞蹈到音乐需细粒度体裁感知节奏与潜空间时间对齐。
- SFT 收益常与预训练实例绑定，不宜简单解读为方法天花板提升。
- 本场同时覆盖基础模型设计、生成对齐与评价方法论。

## 覆盖核对

| 论文 id | 标题 |
| --- | --- |
| 639 | SAM: A Mamba-2 State-Space Audio-Language Model |
| 763 | Samsone: A Family of Open Small Audio Language Models for On-Device Inference |
| 1121 | FreeSonic: Training-Free Temporal-Aware Decoupled Attention for Precise Audio Editing |
| 1823 | Resonate: Reinforcing Text-to-Audio Generation via Online Feedback from Large Audio Language Models |
| 2348 | GACA-DiT: Diffusion-based Dance-to-Music Generation with Genre-Adaptive Rhythm and Context-Aware Alignment |
| 2436 | Rethinking Speech Foundation Model Fine-tuning: Better SFT or Better Match? |
