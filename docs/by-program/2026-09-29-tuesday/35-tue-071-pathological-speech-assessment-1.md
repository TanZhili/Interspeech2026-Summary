# Pathological Speech Assessment 1

- 日期：Tuesday 29 September 2026；时间：14:00-16:00；形式：Poster；Area：13；论文数：8
- 材料：官方程序摘要。仅依据摘要归纳，不补写摘要未给出的数字或机制。

## 技术趋势

本场从心衰、呼吸音、感冒到抑郁与帕金森构音障碍、痴呆预测，共同主题是：生理/病理状态如何改变语音或呼吸声学，以及模型是否学到疾病线索还是说话人身份等捷径。

自监督对比时间邻近、无缓冲持续学习、听诊部位特异相关，以及感冒语料上的说话人嵌入位移，强调生态有效数据与跨中心/跨域泛化。抑郁检测则同时出现免训练辩证推理引擎与严格说话人独立评测的警示。

跨语帕金森构音障碍检测用表征级语言平移削弱语言身份；多语痴呆预测评估基础模型零样本能力。趋势是：数字生物标志物必须经受说话人泄漏、域偏移与跨语混淆的压力测试。

## 技术内容

### 心肺声学与感冒域偏移

**Contrastive Time-Proximity Pre-Training for Speech-Based Heart Failure Monitoring**（论文 424；Nicholas Cummins）提出 CTP：用片段注意力 LSTM 使 <3 天录音嵌入靠近、>100 天录音推远。双中心 68 名 ADHF 患者上，经典声学特征跨中心失败，CTP 特征跨中心更稳健；注意力聚焦呼吸相关片段。

**Lung-CL: Spectrum-aware Distillation and Generative Replay for Continual Learning based buffer-free Respiratory Sound Classification**（论文 1199；Qinben Lai）无缓冲域增量框架：类特异潜空间重放合成伪特征，多层谱感知蒸馏分离病理模式与域干扰。ICBHI、SPRSound、HF 上准确率与抗遗忘优于既有 CL。

**An auscultation location specific study on the relationship between expiratory-to-inspiratory acoustic patterns and spirometric airflow limitation across age and gender in asthmatic patients**（论文 2602；Dheeraj Harish Kumar）在 141 名 20–60 岁受试者上，E/I 谱功率比与 FEV₁/FVC 在 100–200 Hz、200–400 Hz 显著相关；后下部位总体更强，并呈年龄与性别分层差异。

**Common Cold Corpus: Health-aware robustness study of modern speaker embeddings under physiological domain shift**（论文 1188；Anabell Hacker）85 名德语者远程成对录音（急性上呼吸道感染 vs. 健康）。少数声学特征经多重校正仍显著；现代说话人嵌入在中等症状下于身份空间出现显著定向位移。

### 抑郁、构音障碍与痴呆

**Moot-Court: Training-Free Dialectical Reasoning for Depression Detection**（论文 3099；Yuqing Sun）冻结 LLM，结合临床转录与文本化声学特征做模拟法庭辩证推理，并以动态经验库 Codex 约束轨迹。DAIC-WOZ 上超过微调模型。

**Who is Speaking or Who is Depressed? A Controlled Study of Speaker Leakage in Speech-Based Depression Detection**（论文 1394；Hsiang-Chen Yeh）在训练规模固定下控制说话人重叠：重叠显著抬高性能，未见说话人则骤降；即便 DANN 仍有明显差距，提示抑郁线索与说话人身份高度纠缠。

**Adapting Self-Supervised Speech Representations for Cross-Lingual Dysarthria Detection in Parkinson's Disease**（论文 773；Abner Hernandez）用健康对照估计的质心向量适配做语言平移，对齐源/目标 SSL 分布。捷克/德/西口腔交替运动数据上，跨语设定敏感度与 F1 大幅提升，并降低嵌入中的语言身份。

**Foundational speech models evaluation on multilingual dementia prediction**（论文 2587；Bartłomiej Eljasiak）评估 Whisper、WavLM、HuBERT、Wav2Vec2 等下游头在单语/多语训练及未见语言零样本上的痴呆预测；合并英语集平均 F1 0.854，更具挑战的多语设定 0.761。

## 本场要点

- 心衰监测从持续元音主动采集转向自然语音自监督时间邻近表征。
- 呼吸音持续学习强调无缓冲隐私友好与谱感知蒸馏。
- 感冒语料显示神经说话人嵌入对中等生理偏移更敏感。
- 抑郁检测需警惕说话人泄漏；免训练辩证推理提供另一路径。
- 跨语构音障碍语言平移与多语痴呆基础模型评测，推动跨语临床语音 AI。

## 覆盖核对

| id | title |
|---|---|
| 424 | Contrastive Time-Proximity Pre-Training for Speech-Based Heart Failure Monitoring |
| 1199 | Lung-CL: Spectrum-aware Distillation and Generative Replay for Continual Learning based buffer-free Respiratory Sound Classification |
| 2602 | An auscultation location specific study on the relationship between expiratory-to-inspiratory acoustic patterns and spirometric airflow limitation across age and gender in asthmatic patients |
| 1188 | Common Cold Corpus: Health-aware robustness study of modern speaker embeddings under physiological domain shift |
| 3099 | Moot-Court: Training-Free Dialectical Reasoning for Depression Detection |
| 1394 | Who is Speaking or Who is Depressed? A Controlled Study of Speaker Leakage in Speech-Based Depression Detection |
| 773 | Adapting Self-Supervised Speech Representations for Cross-Lingual Dysarthria Detection in Parkinson's Disease |
| 2587 | Foundational speech models evaluation on multilingual dementia prediction |
