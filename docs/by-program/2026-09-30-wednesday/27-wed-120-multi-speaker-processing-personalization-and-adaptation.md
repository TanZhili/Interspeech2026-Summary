# Multi-Speaker Processing, Personalization, and Adaptation

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Oral（Area 9 - Oral 5）
- Area：9
- 论文数：6
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。数字仅引自摘要。

## 技术趋势

本场覆盖多说话人 ASR/日志、用户自定义关键词、LLM-ASR 的文本域适配与热词定制，以及音频问答的测试时强化学习。级联多说话人系统的说话人泄漏被用日志验证做剪枝校正；统一生成式 Speech-LLM 则用 CoT 先推断说话人数，再用约束感知 GRPO 在未知人数下联合 ASR 与日志。

个性化与适配侧：CTC 引导关键帧融合提升易混淆自定义关键词分辨；文本仅适配用多视角去噪批混合避免破坏 speech–text 投影对齐；热词定制 AFG-Bias 以声学检索+门控注入替代脆弱提示注入。部署后自适应方面，AQA-TTRL 仅用无标注测试数据做多数票伪标签与置信加权强化学习，使较小模型经测试时适应后可超过未适应的更大模型直接推理。

## 技术内容

### 多说话人 ASR、日志与泄漏校正

**Mitigating Speaker Leakage in Cascaded Multi-talker ASR with Diarization-based Transcript Correction**（论文 3191；presenter：Suresh Singh）  
级联 MT-ASR 性能常受分离阶段说话人泄漏限制。提出剪枝范式：以预训练说话人日志为多模态验证器，删除同时满足时间包含、词汇交叉验证与时间对齐三方共识的泄漏片段。LibriMix、LibriSpeechMix、AMI 上一致降低 cpWER；高泄漏子集相对 cpWER 降幅可达约 29%。

**Beyond Mimicry: Constrained Exploration with GRPO for Joint Multi-Talker ASR and Diarization under Unknown Speaker Counts**（论文 2297；presenter：Yunrui Cai）  
未知说话人数且输出结构严格时，仅 SFT 对齐在密集重叠下易幻觉与标签畸形。两阶段框架：CoT 增强 SFT 先推断全局人数；再用 MCAR 引导的 GRPO 优化排列不变准确率并强制计数/时间/结构约束。Libri3Mix 与 Dynamic-Mix(2+3) 上 cpWER 为 14.52%/9.24%、WDER 为 1.95%/1.12%；相对 SFT+CoT，GRPO 带来约 35%/54% 相对 cpWER 降幅。

### 关键词、文本域适配与热词门控

**KFC-KWS: Keyframe Fusion with CTC for User-Defined Keyword Spotting**（论文 1586；presenter：Wenbin Jiang）  
利用 CTC 尖峰后验选高置信音素帧，实现音频—音素—文本精确对齐，再经交叉注意力与整句表示融合。LibriPhrase 上取得最佳平衡表现（AUC 98.73%），困难子集 AUC 97.65%、EER 7.75%，显著优于先进基线。

**Avoiding Catastrophic Forgetting in Text-Only Adaptation of LLM-based ASR via Multi-View Text Denoising**（论文 3422；presenter：Sergio Burdisso）  
纯文本微调易破坏投影器学到的语音—文本对齐。将适配表述为去噪，并用多视角噪声驱动批混合：配对源音视频例、投影器诱导噪声转写、合成损坏源转写与损坏目标转写。无需改结构或加参，相对未适配基座相对 WER 改进可达 25.4%，并优于近期文本仅适配方法。

**AFG-Bias: Acoustic-Fusion-Gated Biasing for Plug-and-Play Hotword Customization in LLM-Based ASR**（论文 2029；presenter：Long Wu）  
跨模态声学检索以滑窗对齐从大候选集选相关热词，声学融合门控把已验证偏置注入解码并抑制幻觉，不改 LLM 参数。三套 LLM-ASR 骨干上，金融/医疗域相对 CER 降幅可达 74.1%，AISHELL-1 热词 F1 最多提升 5.4 个绝对点。

### 测试时强化学习音频理解

**AQA-TTRL: Self-Adaptation in Audio Question Answering with Test-Time Reinforcement Learning**（论文 288；presenter：Haoyu Zhang）  
仅用无标注测试数据经多数票伪标签做测试时强化学习；置信加权抑制噪声标签，多次尝试采样缓解优势塌缩。MMAU、MMAR、MMSU 上 Qwen2.5-Omni 7B/3B 平均分别提升 4.42%/11.04%；适应后的 3B 超过未适应 7B 直接推理。

## 本场要点

- 日志驱动剪枝可系统清除级联分离引入的泄漏伪影。
- 未知人数联合 ASR+日志需要 CoT 计数与约束感知 RL，而非仅模仿式 SFT。
- CTC 关键帧融合强化用户自定义关键词的易混分辨。
- 多视角文本去噪批混合实现 LLM-ASR 文本域适配且避免灾难性遗忘。
- 声学检索+门控偏置提供即插即用热词定制，避免提示尺度崩溃。
- 测试时 RL 使音频理解模型在部署后仍可无监督自进化。

## 覆盖核对

| 论文 id | 标题 |
| --- | --- |
| 3191 | Mitigating Speaker Leakage in Cascaded Multi-talker ASR with Diarization-based Transcript Correction |
| 2297 | Beyond Mimicry: Constrained Exploration with GRPO for Joint Multi-Talker ASR and Diarization under Unknown Speaker Counts |
| 1586 | KFC-KWS: Keyframe Fusion with CTC for User-Defined Keyword Spotting |
| 3422 | Avoiding Catastrophic Forgetting in Text-Only Adaptation of LLM-based ASR via Multi-View Text Denoising |
| 288 | AQA-TTRL: Self-Adaptation in Audio Question Answering with Test-Time Reinforcement Learning |
| 2029 | AFG-Bias: Acoustic-Fusion-Gated Biasing for Plug-and-Play Hotword Customization in LLM-Based ASR |
