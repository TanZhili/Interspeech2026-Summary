# Quality, Intelligibility and Evaluation of Speech and Codecs

- 日期：Tuesday 29 September 2026；时间：14:00-16:00；形式：Poster；Area：6；论文数：9
- 材料：官方程序摘要。仅依据摘要归纳，不补写摘要未给出的数字或机制。

## 技术趋势

本场把“听得清/听得省力/评得准”放在同一条评估链上。近端聆听增强从时频改到谱—时调制域能量重分配；个性化神经编解码用说话人聚类压缩模型与码率；歌词可懂度预测融合声学与 Whisper 表征。

主观评测方法论成为独立主题：众包 vs. 实验室、筛查手段、噪声与增强对编解码可懂度的交互，以及听力障碍听者跨数据集可懂度预测的小样本适配。声学传送编解码的探测式解耦评估，则指出交叉重建不足以发现泄漏。

另一端是用现代 ASR 评价增强系统时的陷阱：大模型噪声鲁棒与语言模型上下文可能使 WER“看起来太好”，与声学向的增强评测目标不完全一致；低帧率神经编解码的质量悬崖也被归因到训练配置而非根本物理障碍。

## 技术内容

### 增强、编解码与可懂度建模

**Energy Redistribution in the Spectro-Temporal Modulation Domain for Near-End Listening Enhancement**（论文 319；Amin Edraki）在谱—时调制域优化全局调制掩码（能量约束），联合修改谱与时调制；多种噪声上相对既有 NELE 基线在客观与主观可懂度上一致改进。

**End-to-End Model Compression for Personalized Neural Speech Codecs**（论文 878；Inseon Jang）按感知相似度聚类说话人并分组训练编解码。摘要称模型体积减 96%、码率由 2 kbps 降至 1 kbps，同时保持与 DAC 相当的感知质量，且在噪声条件下仍优于基线。

**Acoustic and Semantic Feature Fusion Mapping for Lyric Intelligibility Prediction**（论文 1014；Yuxiang Fu）融合声学特征与 Whisper 编码器表示，经特征工程后用神经网络与梯度提升树回归可懂度；人工标注集上 CatBoost 报告 RMSE 27.367、Corr 0.654，优于所试神经网络。

**Assessing the Impact of Noise and Speech Enhancement on the Intelligibility of Speech Codecs**（论文 1459；Lyonel Behringer）比较经典与神经编解码在干净/噪声下的可懂度与聆听努力，并评估编码前增强。摘要称经典编解码更抗噪；增强可显著改善否则受噪声损害的编解码；聆听努力在可懂度饱和时仍能区分差异；基于 ASR 的客观可懂度与条件平均主观可懂度高相关。

**Improving Cross-Dataset Speech Intelligibility Prediction for Hearing-Impaired Listeners with Few-Shot Adaptation**（论文 1567；Guojian Lin）提出 CFA-SIPNet：跨域小样本适配器与对比学习。跨数据集相对 SOTA 报告相对 RMSE 降 8.5%、相对 PCC 升 4.2%；用不足 20% 目标域样本可超过全量域内训练。

### 评测方法论、解耦探针与低帧率机制

**Screening Matters: A Comparative Study of Conventional and Crowdsourced Listening Tests**（论文 1387；Anika Treffehn）比较 P.808 众包与 P.800 DCR 实验室评测经典/神经语音编解码，分析锚点排序与评分跨度、陷阱题与金标准等筛查；提出成本有效、降偏的筛查组合。

**Beyond Cross-Reconstruction: Probing-Based Disentanglement Evaluation for Acoustic Teleportation Codecs**（论文 2406；Philipp Grundhuber）用探针回归混响时间、清晰度、直混比并分类说话人，以“有意/无意分区”差距衡量解耦。发现说话人身份大体限于其分区，声学却泄漏到语音嵌入；声学嵌入可盲估房间参数，误差约在监督基线 0.02 s 内。

**Too Good to Be True: A Study on Modern Automatic Speech Recognition Systems for the Evaluation of Speech Enhancement**（论文 2597；Danilo Oliveira）听辨实验显示大规模噪声训练并内嵌语言模型的现代 ASR 与人类 WER 更相关，换能器模型转录最可靠；但其噪声鲁棒与上下文利用也可能对以声学为中心的增强评测信息不充分。

**Probing Low Frame Rate Degradation in Neural Audio Codecs**（论文 3493；Alex Gichamba）复现约 6.25 Hz 质量悬崖，排除音素碰撞与码本饱和作为根本障碍；归因于训练固定片段时长导致低帧率 token 过少、解码器缺乏跨 token 上下文。纠正后 WER 随音素负载平滑退化至 3.1 Hz 与 1.6 Hz。

## 本场要点

- NELE 转向谱—时调制能量重分配；个性化 NSC 以聚类分组实现大幅压缩。
- 噪声、增强与编解码类型强交互；聆听努力补充饱和区的可懂度区分。
- 众包听测质量高度依赖筛查；HI 可懂度预测可用小样本跨域适配。
- 交叉重建不足以证明解耦；探针可揭示声学泄漏。
- 用现代 ASR 评增强与低帧率编解码“悬崖”解释，都提醒评测指标/训练配置可能误导结论。

## 覆盖核对

| id | title |
|---|---|
| 319 | Energy Redistribution in the Spectro-Temporal Modulation Domain for Near-End Listening Enhancement |
| 878 | End-to-End Model Compression for Personalized Neural Speech Codecs |
| 1014 | Acoustic and Semantic Feature Fusion Mapping for Lyric Intelligibility Prediction |
| 1387 | Screening Matters: A Comparative Study of Conventional and Crowdsourced Listening Tests |
| 1459 | Assessing the Impact of Noise and Speech Enhancement on the Intelligibility of Speech Codecs |
| 1567 | Improving Cross-Dataset Speech Intelligibility Prediction for Hearing-Impaired Listeners with Few-Shot Adaptation |
| 2406 | Beyond Cross-Reconstruction: Probing-Based Disentanglement Evaluation for Acoustic Teleportation Codecs |
| 2597 | Too Good to Be True: A Study on Modern Automatic Speech Recognition Systems for the Evaluation of Speech Enhancement |
| 3493 | Probing Low Frame Rate Degradation in Neural Audio Codecs |
