# Domain Adaptation & Accented ASR

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Oral（Area 8 - Oral 3）
- Area：8
- 论文数：6
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。主张均来自摘要。

## 技术趋势

本场围绕口音/领域变异下的 ASR 与发音评测：从测试时自适应、轻量适配器与对比正则，到模型合并、激活转向与实时口音转换。共同目标是在不大规模全量微调的前提下，把预训练骨干适配到多样口音与多领域。

MDD 侧用测试时训练让 wav2vec 2.0 块内 MLP 模块在新样本上自监督更新；口音 ASR 则出现 Mixture-of-Accent-Adapters（按需特化 Whisper）、无口音标注的监督对比正则，以及在表示空间识别“口音敏感中间层”并做无参数激活转向。

多领域方面，模型合并被系统基准化，并提出 BoostedTSV-M 缓解秩塌缩；口音转换 AccentDrift 则用稀疏语音标记与流式缓存，在约 520 ms 延迟下做内容与身份保持的口音变换。整体呈现“适配成本下沉到测试时/轻量模块/合并/转向”的路径谱系。

## 技术内容

### 测试时自适应与轻量口音适配

**SEA-MDD: Self-adapting Mispronunciation Detection and Diagnosis Models via Test-Time Training**（论文 856；presenter：Minglin Wu）  
L2 学习者水平与误读类型高度多样，全覆盖标注昂贵。SEA-MDD 在 wav2vec 2.0 的 Transformer 块中嵌入基于 MLP 的测试时训练模块，训练与测试阶段均以自监督更新 TTT 参数，使模型动态适应新输入分布，缓解多样分布下的性能退化；实验验证有效性（摘要未列具体数值）。

**Mixture-of-Accent-Adapters for Robust ASR: Injecting Accent Cues into Pretrained Whisper**（论文 1373；presenter：Mehedi Hasan Bijoy）  
MoAA 在冻结 Whisper 骨干上按需特化：池化状态控制瓶颈估计口音程度，经可学习软口音码本加权检索注入口音线索并路由轻量口音专家适配器，再与骨干门控混合；对抗性别头减泄漏，无参考幻觉抑制减稀有解码伪影。AESRC 上 WER 7.49%、CER 3.81%。

**Contrastive Regularization for Accent-Robust ASR**（论文 949；presenter：Van-Phat Thai）  
在自监督预训练+CTC 微调中加入语句级监督对比损失，不改结构、不需显式口音监督。L2-ARCTIC 上多编码器一致降 WER，未见口音评估相对降幅可达约 25–29%；句内余弦离散度分析显示表示在口音变异下更紧凑稳定。

### 多领域合并、激活转向与实时口音转换

**Exploring the potential and limitations of Model Merging for Multi-Domain Adaptation in ASR**（论文 1969；presenter：Carlos Carvalho）  
在 10 个欧洲葡萄牙语领域上基准 11 种合并算法，评估域内、分布偏移及英语/多语表现。提出基于 TSV-M 的 BoostedTSV-M，用奇异值提升缓解秩塌缩并改善数值稳定。总体在欧葡上优于全量微调，且单模型保持分布外泛化。

**Activation Steering for Accent Adaptation in Large Audio Language Models**（论文 2166；presenter：Ting Dang）  
从层间编码器激活估计口音均值偏移方向，注入各层并度量与标准嵌入对齐，得到中间层窄带集中口音信息的敏感剖面；据此提出推理期无参数口音转向。八种口音上一致降低 WER。

**AccentDrift: Real-time Streaming Accent Conversion via Sparse Speech Tokenization**（论文 710；presenter：Sang-Hoon Lee）  
从信息瓶颈视角用稀疏语音标记抽取语言信息，口音适配器注入风格后再由音色适配器分层生成说话人声学；缓存感知流式架构与并行流实现约 520 ms 延迟。摘要称优于既有并行口音转换模型，并展示 L2 说话人生成接近母语口音的可行性。

## 本场要点

- 测试时训练使 MDD 在部署后仍可对单样本分布漂移自适配。
- MoAA 与对比正则分别走“按需口音专家”与“无口音标签几何正则”两条轻量路径。
- 模型合并可把多领域检查点合成单模型，BoostedTSV-M 针对秩塌缩。
- 口音信息集中于编码器中部，支持无参数激活转向。
- 稀疏标记+流式架构把口音转换推到约半秒级实时交互。
- 目标从“全量微调口音数据”转向“控制/路由/合并/转向”的低成本适配。

## 覆盖核对

| 论文 id | 标题 |
| --- | --- |
| 856 | SEA-MDD: Self-adapting Mispronunciation Detection and Diagnosis Models via Test-Time Training |
| 1373 | Mixture-of-Accent-Adapters for Robust ASR: Injecting Accent Cues into Pretrained Whisper |
| 949 | Contrastive Regularization for Accent-Robust ASR |
| 1969 | Exploring the potential and limitations of Model Merging for Multi-Domain Adaptation in ASR |
| 2166 | Activation Steering for Accent Adaptation in Large Audio Language Models |
| 710 | AccentDrift: Real-time Streaming Accent Conversion via Sparse Speech Tokenization |
