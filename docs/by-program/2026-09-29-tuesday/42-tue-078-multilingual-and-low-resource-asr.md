# Multilingual & Low-Resource ASR

- 日期：Tuesday 29 September 2026；时间：16:30-18:30；形式：Oral；Area：8；论文数：6
- 材料：官方程序摘要。仅依据摘要归纳，不补写摘要未给出的数字或机制。

## 技术趋势

本场聚焦南亚/印度语族与方言场景下的多语低资源 ASR：专用越南语自监督预训练、南亚语错误解剖、印地/马拉雅拉姆复杂度分层基准、统一梯度投影持续学习、希腊方言课程多任务，以及印度 22 种表列语言的忠实评测基准。

共同问题是：标准微调常改善朗读却损害自发语音；主导语言偏置导致灾难遗忘；WER 被正字/Unicode 变异夸大。对策包括向量量化预训练、转写后处理、学习率时机与课程顺序、语言均衡回放投影，以及允许多合法转写的评测格。趋势是“诊断基准 + 训练动力学 + 语言均衡优化”三位一体。

## 技术内容

### 预训练、错误诊断与训练动力学

**ViP-VL: Vietnamese Self-supervised Speech Pretraining Model with Vector-Quantization Learning**（论文 1077；Kiet Anh Hoang）在 ChunkFormer 上以 BEST-RQ 预训练约 17,000 小时无标注越南语语音，结合 Acoustic Stacking、感受野对齐与掩码选择；在 ASR、情感、方言分类与说话人验证四项下游报告新 SOTA，并公开权重。

**Dissecting ASR Failures in Low-Resource South Asian Languages**（论文 1382；Agha Ali Raza）用 11 类错误分类法评五种多语 ASR。Whisper 在四种语言中三种以脚本混淆为主；SeamlessM4T 乌尔都/旁遮普 WER 约 16.3%/22.1%。跨语污染可达输出字符约 35%；标准 WER 可因正字/Unicode 高估至约 3.1 点；转写后处理可挽回至多约 25 点 WER。

**Vividh-ASR: A Complexity-Tiered Benchmark and Optimization Dynamics for Robust Indic Speech Recognition**（论文 3408；Kavya Manohar）印地/马拉雅拉姆四层级基准（棚内、广播、自发、合成噪声）。早期大切参数更新约绝对改善全局 WER 12 点，难到易课程利好自发语音；R-MFT 使 244M Whisper 匹配或超过常规微调 769M。CKA/SVD 显示有效日程把适配集中在解码器。

### 持续学习、方言适配与忠实评测

**Unified Gradient Projection: Language-Balanced Continual Learning for Multilingual Low-Resource ASR**（论文 1915；Wei-Qiang Zhang）UGP 在统一投影空间用语言均衡回放参考梯度约束更新，减轻主导语言偏置；与数据级回放互补。多样低资源语组与模型规模上有效适配并大幅减遗忘；Whisper-large-v3 上报告近零平均遗忘。

**Beyond Standard Greek: Adapting Whisper for Greek Dialects through Curriculum Multitask Learning**（论文 2567；Vassilis Katsouros）融合相邻捐赠语增强、识别+翻译多任务与分阶段课程（跨语翻译/捐赠语监督逐步过渡到方言 ASR）。塞浦路斯、克里特、麦西尼亚等低资源设定一致优于常规微调。

**Vimarsha: Faithful ASR Evaluation for Indian Languages with Demographic Diversity, In-the-Wild Audio and Spelling Variations**（论文 3348；Kaushal Bhogale）约 100 小时、覆盖 22 种表列印度语言：人口多样实地录音 + 声学困难野生音频 + 每句多合法转写格。10 个 SOTA 模型排名在真实条件下显著变动，并暴露地理/人口差距与语速、环境失败模式。

## 本场要点

- 语言专用 SSL（如越南语 ViP-VL）仍可显著抬高多下游任务上限。
- 南亚语失败常是脚本/正字问题；转写后处理与细粒度错误分类比单看 WER 更有行动价值。
- 复杂度分层基准与 R-MFT 揭示“朗读变好、自发变差”的微调错配。
- UGP 用语言均衡梯度投影对抗多语持续学习中的主导语偏置。
- 希腊方言课程多任务与 Vimarsha 忠实评测，分别服务方言适配与印度语族现实部署评估。

## 覆盖核对

| id | title |
|---|---|
| 1077 | ViP-VL: Vietnamese Self-supervised Speech Pretraining Model with Vector-Quantization Learning |
| 1382 | Dissecting ASR Failures in Low-Resource South Asian Languages |
| 3408 | Vividh-ASR: A Complexity-Tiered Benchmark and Optimization Dynamics for Robust Indic Speech Recognition |
| 1915 | Unified Gradient Projection: Language-Balanced Continual Learning for Multilingual Low-Resource ASR |
| 2567 | Beyond Standard Greek: Adapting Whisper for Greek Dialects through Curriculum Multitask Learning |
| 3348 | Vimarsha: Faithful ASR Evaluation for Indian Languages with Demographic Diversity, In-the-Wild Audio and Spelling Variations |
