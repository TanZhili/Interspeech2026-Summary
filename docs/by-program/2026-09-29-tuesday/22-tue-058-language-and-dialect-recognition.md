# Language and Dialect Recognition

- 日期：2026年9月29日（周二）
- 时间：14:00-16:00
- 形式：Oral
- Area：4
- 论文数：6
- 材料说明：依据官方节目单与 ISCA 条目中的标题、作者、报告人、时间与摘要撰写；不补写摘要未给出的数字、数据集或方法细节。

## 技术趋势

本场覆盖口语语种识别（LID）的对抗鲁棒、方言表征几何、跨库泛化，以及方言 ASR 的地理条件与语义漂移校正。安全侧首次系统展示 SOTA LID 在白盒梯度攻击下的脆弱，并提出含对抗样本挖掘、无教师防御蒸馏与语言一致性正则的自防御再训练。表征侧对 Wav2Vec 2.0 中五类中国方言做几何探测，描述低层声学差异—中层高散布细粒度音系—深层收缩但仍吻合传统分类的三阶段轨迹。

跨域与方言 ASR 方面，半正对比学习用音—文双模态与“同语不同域”半正样本处理跨库泛化；Predict-Then-Adapt 在测试时从语音回归经纬度再做地理条件解码；西/法十变体方言偏见基准揭示非均匀差距与形态句法“纠正”、话语标记失败机制；DASR-CPO 以无参考对比偏好优化抑制普通话主导先验造成的语义漂移。整体上，方言/语种问题从分类准确率扩展到鲁棒、可解释几何、地理条件与语义正确性。

## 技术内容

### LID 对抗鲁棒、层几何与跨库对比学习

**Improving Adversarial Robustness in Spoken Language Identification through Self-Defensive Distillation**（论文 3091；Spandan Dey）展示主流 LID 在白盒梯度攻击下的脆弱，并提出 Self-Defensive Adversarial Re-Training（SDART）：扩展对抗再训练，加入对抗样本挖掘、动态在线标签平滑的无教师防御蒸馏与语言一致性正则，跨多库与架构评测。

**Probing the Layer-wise Geometry of Chinese Dialect Representations in Wav2Vec 2.0**（论文 975；Zhen Peng）对五种中国方言表征做几何探测，归纳三阶段轨迹，并建议口音识别等需细粒度音系信息的任务关注中层高散布表征。

**Robust Language Identification Using Semi-positive Contrastive Learning**（论文 2502；Shubham Sharma）提出 Semi-positive Contrastive Learning（SpCL），以双模态音—文编码器将波形与基于音素的文本描述映射到共享空间，用可控权重区分强正样本（同语同域）与半正样本（同语异域），在无需显式域自适应的情况下应对跨库偏移。

### 地理条件方言 ASR、偏见诊断与语义漂移校正

**Predict-Then-Adapt: Inferring Coordinates from Speech for Continuous Geo-Conditioned Dialectal ASR**（论文 3333；Pouya Mehralian）在冻结编码器上附加轻量 Coordinate Regression Head，两遍推理先预测坐标再地理条件解码；摘要称参数增量 <0.1%、时延增量 <3%，荷兰方言上 10–30 秒语音平均大圆误差 15–25 km，且 GLoRIA 对该误差范围稳健。

**Dialect Bias in Speech Recognition Across 10 Spanish and French Varieties**（论文 458；Rodrigo Nieto）构建约 20 小时、性别平衡、国家级分层并保留方言特征人工转写的语料，评测七个模型：法语偏欧洲变体，西班牙语出现多米尼加优于半岛、智利错误率最高等非均匀模式；词汇分析关联形态句法“纠正”与区域话语标记，声学分析显示说话人嵌入编码方言信息。

**DASR-CPO: Reference-Free Contrastive Preference Optimization for Correcting Mandarin Semantic Drift in Low-Resource Chinese Dialect ASR**（论文 1228；Tao Zhang）针对 Whisper-Large-v3 等普通话主导先验导致的同音异义语义漂移，用数据驱动混淆挖掘构造无人工标注偏好对，并以跨度级对比目标相对 LoRA 监督微调更直接抑制竞争候选。

## 本场要点

- LID 安全研究起步：白盒攻击脆弱性与 SDART 自防御蒸馏。
- 方言 SSL 表征呈层间几何三阶段，任务选型应匹配层特性。
- SpCL 用半正对比缓解低资源 LID 跨库泛化。
- 地理条件 ASR 可在测试时从语音推断坐标，无需先验坐标。
- 西/法方言偏见非均匀，机制涉及词汇“纠正”与嵌入中的方言信息。
- 中国方言 ASR 需专门抑制普通话语义漂移，而非只降 CER。

## 覆盖核对

| paper_id | title |
|---|---|
| 3091 | Improving Adversarial Robustness in Spoken Language Identification through Self-Defensive Distillation |
| 975 | Probing the Layer-wise Geometry of Chinese Dialect Representations in Wav2Vec 2.0 |
| 2502 | Robust Language Identification Using Semi-positive Contrastive Learning |
| 3333 | Predict-Then-Adapt: Inferring Coordinates from Speech for Continuous Geo-Conditioned Dialectal ASR |
| 458 | Dialect Bias in Speech Recognition Across 10 Spanish and French Varieties |
| 1228 | DASR-CPO: Reference-Free Contrastive Preference Optimization for Correcting Mandarin Semantic Drift in Low-Resource Chinese Dialect ASR |
