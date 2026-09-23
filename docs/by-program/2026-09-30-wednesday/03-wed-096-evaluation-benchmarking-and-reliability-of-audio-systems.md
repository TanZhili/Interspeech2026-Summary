# Evaluation, Benchmarking, and Reliability of Audio Systems

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：5
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program ；https://www.isca-archive.org/interspeech_2026/index.html）。不补写摘要未给出的数字与细节。

## 技术趋势

本场围绕音频系统的评测、基准与可靠性展开，覆盖质量评估、深度伪造检测、无损压缩、空间表示探测以及可解释的编辑评测等方向。共同背景是生成式音频与处理算法快速迭代，静态评测模型与固定决策边界难以跟上新失真类型与域漂移。

质量评估侧出现两条互补路径：一是以持续学习应对语音与音乐等多域任务序列，用双分支与知识蒸馏在可塑性与稳定性之间权衡；二是把多模态大模型当作“评委”，用链式思维对音频编辑结果做自然语言可解释评分。真实性与安全侧则从“拟合已知伪造分布”转向建模真实流形，并推动环境声深度伪造检测挑战的数据集与评测协议建设。

压缩与表示评测方面，语言模型式无损压缩被扩展到全保真（16/24-bit）音频，字节级分词缓解词汇表爆炸；空间音频预训练表示则通过受控探测基准系统检验方位、距离与房间参数等空间因子是否可解码。整体上，评测从单一分数走向挑战赛洞察、可解释文本评测与开放基准，强调对分布漂移与跨域泛化的鲁棒性。

## 技术内容

### 质量评估与可解释评测

**CAQA-Net: Continual Audio Quality Assessment Across Speech and Music Domains**（论文 476；Naiyuan Li）  
针对生成与处理引入的新失真与新域，静态 AQA 模型难以持续更新。提出 CAQA-Net 持续学习框架：双分支多头结构结合可训练波形编码器与基于谱图的语义锚，知识蒸馏正则保留旧知识，原型门控支持任务无关推理。摘要报告该方法在可塑性与稳定性之间取得平衡，相对联合学习上界 SRCC 差距在 0.036（4.6%）以内。

**Interpretable Audio Editing Evaluation via Chain-of-Thought Difference-Commonality Reasoning with Multimodal LLMs**（论文 3176；Yuhang Jia）  
面向音频编辑评测，构建基于 Qwen2-Audio 的自然语言自动评测框架。引入两项基于 caption 的微调任务增强多音频理解，并用链式思维提示促使分步结构化推理。摘要称框架给出可解释且逻辑一致的文本评测，与人类判断对齐较好，并优于已有基线；代码与工具将发布。

### 深度伪造检测与真实流形建模

**The First Environmental Sound Deepfake Detection Challenge: Benchmarking Robustness, Evaluation, and Insights**（论文 1599；Yang Xiao）  
环境声深度伪造检测（ESDD）相对语音/歌声伪造检测仍不足。首届 ESDD 挑战吸引 97 支队伍、收到 1,748 份有效提交。论文介绍任务设定、数据构建、评测协议、基线与结果洞察，并分析顶尖系统的常见架构与训练策略，讨论后续开放问题。

**DASM: Detecting AI-Synthetic Music via Authentic Manifold Deviation Modeling**（论文 3245；Xinya Zhu）  
针对判别式方法在伪造分布非平稳漂移下的结构脆弱性，DASM 仅在真实样本上用重建损失训练可学习记忆库，刻画压缩的真实流形先验；双分支分类器结合原始特征与记忆重建特征，将伪造视为流形空间偏离。并以轻量 prompt tuning 适配冻结 MERT 编码器。摘要称在 SONICS 上达到先进性能并对声学退化具有鲁棒性。

### 压缩基准与空间表示探测

**Benchmarking Language Modeling for Lossless Compression of Full-Fidelity Audio**（论文 1748；Phillip Long）  
将原始波形上的自回归“语言模型”用于无损压缩，基准覆盖音乐、语音、生物声学及 16–48 kHz、8/16/24-bit。提出 Trilobyte 字节级分词，将词汇规模从 O(2^b) 降为 O(1)，使 24-bit LM 无损压缩变得可行。摘要指出 LM 持续优于 FLAC，在 8/16-bit 达先进压缩，但比特深度升高后增益更有限。

**Probing Spatial Structure in Pretrained Audio Representations**（论文 2506；Sivan Ding）  
提出 SARL 基准，受控探测预训练音频模型中的声源级（方位、仰角、距离、类别）与房间级（RT60、体积、形状）因素。跨多种编码器实验显示：输入配置与训练范式塑造空间编码；声源因子比房间因子更易解码；扰动下对声源与房间变化的响应异质。SARL 开源以支持可复现评测。

## 本场要点

- 持续学习 AQA（CAQA-Net）用双分支、蒸馏与原型门控应对语音/音乐任务序列。
- 首届环境声深度伪造检测挑战提供任务、数据、基线与顶尖系统洞察。
- Trilobyte 使全保真（含 24-bit）LM 无损压缩可扩展评测，高比特深度增益趋缓。
- SARL 系统探测预训练表示中的空间信息偏差与可解码性。
- 多模态 LLM + CoT 给出可解释的音频编辑自然语言评测。
- DASM 以真实流形偏离替代跟踪伪造分布，并结合 MERT prompt tuning。

## 覆盖核对

| id | title |
|---|---|
| 476 | CAQA-Net: Continual Audio Quality Assessment Across Speech and Music Domains |
| 1599 | The First Environmental Sound Deepfake Detection Challenge: Benchmarking Robustness, Evaluation, and Insights |
| 1748 | Benchmarking Language Modeling for Lossless Compression of Full-Fidelity Audio |
| 2506 | Probing Spatial Structure in Pretrained Audio Representations |
| 3176 | Interpretable Audio Editing Evaluation via Chain-of-Thought Difference-Commonality Reasoning with Multimodal LLMs |
| 3245 | DASM: Detecting AI-Synthetic Music via Authentic Manifold Deviation Modeling |
