# Beyond Speech Technologies in Healthcare

- 日期：2026年10月1日（星期四）
- 时间：09:00-11:00
- 形式：Oral
- Area：13
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场面向医疗与辅助沟通：电子喉（EL）语音转换的个性化与新设备、舌超声到语音合成及其信息来源检验，以及构音障碍 ASR 的零样本声克隆增广。共同约束是术前/病理数据极少、设备声学特异、以及评测需超越谱失真走向可懂度。

ELVC 线从单句术前音色保留（级联优于伪目标）、鼻部电子喉（NEL）特征选择与增广，到用合成数据做一对多时间对齐 EL→自然语音。超声线提出时空 Transformer 框架并用 WER 评测；对照实验意外发现去除舌区未必显著伤 MSE，提示基线可能利用更广图像线索，而双编码器可把激活聚焦舌区。构音障碍侧用零样本克隆绕过说话人专用采集瓶颈。

## 技术内容

### 电子喉语音转换

**Personalized Electrolaryngeal Voice Conversion with a Single Pre-operative Utterance**（论文 1942；Devin Chang）  
仅一条自然术前话语做音色保留的 one-shot ELVC。比较级联（ELVC 后再转目标音色）与伪目标（零样本模型造合成数据训监督 ELVC）。级联在说话人相似度与质量上更优且对可懂度影响很小；直接把零样本 VC 用于 ELVC 因域失配失败，确认需专用框架。

**A Preclinical Study of Electrolaryngeal Voice Conversion for a Novel Nasal Electrolarynx: Feature Choice and Data Augmentation**（论文 1882；Ming-Chi Yen）  
据称首个系统研究新型鼻部电子喉（NEL）的 ELVC（既往多针对颈部 CEL）。比较 Mel 与 WavLM 输入，并用 LLE-VC 增广合成成对 sNEL–sNL 做预训练。设备依赖：WavLM 利 CEL，Mel 更保 NEL 谱特性，NEL→NL 上可懂度相关指标与听者偏好更好。

**One-to-Many Electrolaryngeal Voice Conversion with Synthetic Data**（论文 2150；Carlos Toshinori Ishi）  
面向时间对齐 EL→NL，数据更稀缺。用约 13 分钟 EL 微调预训练 any-to-many VC 做 NL→EL，将大规模多说话人自然语音转为合成 EL，再监督一对多 EL→NL。实验称在语调与可懂度上优于基线。

### 舌超声合成与构音障碍增广

**Tongue2Speech: Real-Time Speech Synthesis from Tongue Ultrasound Videos via Spatiotemporal Transformers**（论文 3023；Yash Sonkar）  
用显式 3D 时空编码 + 多层 Transformer 建模长程发音动态；以 WER 替代孤立谱失真作评测。英语 TaL：单说话人 15.93% WER、多说话人 31.64%，优于六个强基线；说话人微调可提升未见用户可懂度。

**On the Role of the Tongue Region in Ultrasound-to-Acoustic Mapping**（论文 1071；Ibrahim Ibrahimov）  
用自动舌区提取做受控输入操纵，并试双编码器交叉注意力门控映射到 80 维 mel。去除舌区未造成统计显著 MSE 变差，暗示 2D-CNN 或利用更广图像线索；双编码器在 MSE/MCD/PESQ/MOSnet 上亦无显著增益，但 Grad-CAM 显示其激活更聚焦舌区，朝可解释映射迈出一步。

**Low-Burden Data Augmentation for Dysarthric ASR via Zero-Shot Voice Cloning**（论文 1501；Satwinder Singh）  
用 Higgs Audio V2 零样本克隆 TORGO 说话人，微调 Whisper-medium。相对零样本 31.62% WER，Clone FT 26.00%，接近 Real 24.44% 与 Hybrid 25.12%；中重度说话人上 Clone/Hybrid 优于 Real；跨库 SAP-1102 上 Clone FT 相对最优（约 11.45%）。提示零样本克隆可绕过高成本采集瓶颈。

## 本场要点

- 单句术前音色可用级联零样本策略个性化 ELVC，直接零样本易域失配。
- NEL 与 CEL 声学不同，特征与增广需按设备选择。
- 合成 EL 数据可支撑一对多时间对齐 EL→NL。
- 舌超声合成宜用 WER；“舌是主信息源”假设需用可解释分析再检验。
- 零样本声克隆可为构音障碍 ASR 提供低负担训练数据。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 1071 | On the Role of the Tongue Region in Ultrasound-to-Acoustic Mapping |
| 1501 | Low-Burden Data Augmentation for Dysarthric ASR via Zero-Shot Voice Cloning |
| 1882 | A Preclinical Study of Electrolaryngeal Voice Conversion for a Novel Nasal Electrolarynx: Feature Choice and Data Augmentation |
| 1942 | Personalized Electrolaryngeal Voice Conversion with a Single Pre-operative Utterance |
| 2150 | One-to-Many Electrolaryngeal Voice Conversion with Synthetic Data |
| 3023 | Tongue2Speech: Real-Time Speech Synthesis from Tongue Ultrasound Videos via Spatiotemporal Transformers |
