# Multimodal Speech Processing and Speech LLM Systems

- 日期：2026年10月1日（星期四）
- 时间：09:00-11:00
- 形式：Poster
- Area：10
- 论文数：7
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场连接语音感知 LLM 的时间戳与领域适应、音频—语言模型提示学习泛化、多模态情绪无监督预训练、音视频“谁何时说了什么”，以及视频引导的 ASR 后修正与多说话人流式日志前端。主线是在单一 Speech-LLM/多模态骨干上模块化扩展能力，同时缩小语音—文本模态间隙与屏外说话人等现实缺口。

Speech-LLM 侧，两步生成（先转写再带时间戳重生成）与激活 LoRA 复用 KV-cache，在不损 WER 下把对齐误差压到数十毫秒量级；少量目标域语音经混合批即可逼近全量成对微调。ALM 提示学习用零样本熵正则融合 logits 缓解基类过拟合。情绪与场景理解则靠掩码/去噪重建与动量对比学通用表示，或用专用缺席 token 统一屏上/屏外说话人。

多媒体纠错与可穿戴多说话人理解方面，VLMM 捕获剧集视频上下文修正 ASR；源分离 + 统计分类器替代脆弱阈值日志，并用 Conformer 与多几何模型兼顾效率与不同智能眼镜麦克风布局。

## 技术内容

### Speech-LLM 时间戳、领域适应与 ALM 提示泛化

**Parameter-Efficient Adaptation of Speech-Aware LLMs for Timestamp Prediction**（论文 2441；Avihu Dekel）  
两步 SRWT：先转写再带时间戳重生成以保转写质量；模块化 LoRA/aLoRA 仅用 SRWT 数据训练且可复用 KV-cache。英语对齐误差 27 ms（相对最佳基线约 35%），多语 21 ms，WER 与基座相同；仅英语训练零样本多语 37 ms。

**Closing the Speech-Text Gap with Limited Audio for Effective Domain Adaptation in LLM-Based ASR**（论文 3383；Sergio Burdisso）  
比较纯文本、成对语音—文本与混合批（MB）。即使少量语音也稳定改进；MB 仅用目标域约 10% 语音（<4 小时）即可达或优于全数据常规 ASR 微调的 WER。

**ZEBRA: Zero-Shot Entropy-Regularized Prompt Learning for Base-to-Novel Generalization in Audio-Language Models**（论文 261；Asif Hanif）  
融合零样本与提示学习 logits，并以自熵正则减轻基类过拟合；多音频分类数据集上提升新类同时保持基类，显著缩小 base-to-novel 差距。

### 多模态情绪、音视频说话人与视频后修正/流式日志

**MultiEmoVec: Learning Generalised Multimodal Emotion Representation by Momentum Contrast and Multi-task Reconstruction**（论文 1563；Junchen Liu）  
无监督预训练：跨模态掩码/去噪重建、Transformer 跨模态注意力与动量对比；冻结编码器后轻量分类，消融与跨库评估显示泛化有效。

**Unified Audio-Visual Modeling to Recognize Which Face Spoke When and What in Scenarios with On- and Off-Screen Participants**（论文 1592；Naoki Makishima）  
在序列化 token 自回归框架中引入表示视频中说话人缺席的专用 token。含屏外说话人时优于传统方法与分离式组合系统；全员在屏时接近专用传统方法。

**Speech Recognition on TV Series with Video-Guided Post-ASR Correction**（论文 2970；John Hansen）  
VPC 用 VLMM 捕获视频上下文 refinement ASR 输出；剧集基准上在多说话人、重叠、领域术语与长程依赖场景一致提升转写准确率。

**Improving Streaming Speaker Diarization for LLM Based Multi-talker Speech Understanding**（论文 1403；Ruizhi Li）  
源分离后接统计分类器（如 GBDT）做说话人标记，克服简单阈值脆弱性；探索更少参数的 Conformer，并训练多几何模型以泛化不同智能眼镜麦克风布局。真实多说话人录音上提升识别与翻译准确率与效率。

## 本场要点

- Speech-LLM 可用两步时间戳与激活 LoRA 在保 WER 下做毫秒级对齐。
- 少量目标域语音经混合批即可弥合文本适应的模态间隙。
- 零样本熵正则提示学习缓解 ALM 的基类—新类权衡。
- 缺席 token、视频后修正与分离+分类器前端服务真实音视频多说话人场景。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 2441 | Parameter-Efficient Adaptation of Speech-Aware LLMs for Timestamp Prediction |
| 261 | ZEBRA: Zero-Shot Entropy-Regularized Prompt Learning for Base-to-Novel Generalization in Audio-Language Models |
| 1563 | MultiEmoVec: Learning Generalised Multimodal Emotion Representation by Momentum Contrast and Multi-task Reconstruction |
| 1592 | Unified Audio-Visual Modeling to Recognize Which Face Spoke When and What in Scenarios with On- and Off-Screen Participants |
| 2970 | Speech Recognition on TV Series with Video-Guided Post-ASR Correction |
| 3383 | Closing the Speech-Text Gap with Limited Audio for Effective Domain Adaptation in LLM-Based ASR |
| 1403 | Improving Streaming Speaker Diarization for LLM Based Multi-talker Speech Understanding |
