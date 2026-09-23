# Clinical and Inclusive Speech Technology

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Long Oral
- Area：（跨领域长文 Oral；程序未单列 Area 编号）
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program ；https://www.isca-archive.org/interspeech_2026/index.html）。不补写摘要未给出的数字与细节。

## 技术趋势

本场为临床与包容性语音技术长文 oral：构音障碍严重度估计的数据扩充、病理语音隐私保护变声、口吃研究与终端用户需求对齐、儿童语音发育自动测量、神经多样性话语的五十年回顾，以及 EEG 引导目标语音提取中的捷径学习。线索是技术必须对非典型语音稳健，并与临床与社区真实需求对齐。

数据稀缺推动伪标签教师、弱监督对比预训练与大规模典型语音迁移；纯数据驱动谱包络估计在病理模式上脆弱，物理知情声道共振模型被引入以增强可懂度与临床属性保留。社会与方法论层面，范围综述与利益相关方调查揭示研究议程与口吃者/言语治疗师需求的错位；神经多样性相关论文的话语分析批评医疗化、缺位参与与能力歧视语言。儿童侧 TinyVox/BabAR 把音素识别接到发育指标；脑机接口侧则指出试次内捷径导致跨试次泛化失败。

## 技术内容

### 构音障碍评估与隐私变声

**Something from Nothing: Data Augmentation for Robust Severity Level Estimation of Dysarthric Speech**（论文 1390；Jaesung Bae）  
三阶段框架：教师为未标注构音障碍样本生成伪标签，标签感知对比学习弱监督预训练，再微调 DSQA。在五个未见、跨病因与语言的数据集上摘要称稳健；Whisper 基线显著优于 SpICE 等，完整框架未见测试集平均 SRCC 达 0.761。

**Phy-VC: Physics-Informed Voice Conversion for Privacy-Preserving Pathological Speech**（论文 378；Suhita Ghosh）  
通过可微声道共振模型施加发音–声学耦合作为归纳偏置。在标准语音上训练后，摘要称在口吃、痴呆、老年与情感等多样模式上相对基线改善可懂度、韵律与自然度并有效匿名；专家评估确认临床相关属性显著保留，发音表示还可解释地控制系统性说话人变化。

### 需求对齐、儿童发育与包容话语

**Aligning Stuttered-Speech Research with End-User Needs: Scoping Review, Survey, and Guidelines**（论文 1704；Hawau Olamide Toyin）  
结合口吃相关论文范围综述与 70 名利益相关方（口吃成人与言语治疗师）调查，提出口吃语音研究分类法，指出研究方向与用户需求的分歧，并给出面向真实需求的指南。

**BabAR: from phoneme recognition to developmental measures of young children's speech production**（论文 1132；Marvin Lavechin）  
构建 TinyVox（英/法/葡/德/西儿童发声音素转写，逾五十万条），训练跨语儿童音素识别 BabAR。摘要称在多语儿童日长录音上预训练显著更优，微调时提供约 20 秒周围音频上下文进一步提升；替换多落在同一宽语音范畴，适合粗粒度发育分析；自动言语成熟度指标与文献发育估计一致。

**Making Room for Speech Diversity: A 50 Year Retrospective of Speech Science and Technology through a Neurodivergent Lens**（论文 2962；Shaomei Wu）  
以神经多样性语音为案例，范围综述 1976–2025 年 Interspeech/ICASSP 相关论文。归纳三类问题：医疗化/干预主义把神经多样性特质视为待纠正缺陷；研究过程极少纳入当事人；能力歧视语言加剧边缘化。并提出 Interspeech 践行“所有声音”的路径。

### EEG 引导提取中的捷径学习

**Breaking Shortcut Learning for Cross-Trial EEG-Guided Target Speech Extraction via Two-Stage Training**（论文 595；Wonchul Shin）  
分析显示高试次内性能可由试次特异 EEG 结构作为目标选择捷径驱动，导致未见试次泛化差。提出 TRUST-TSE：对比预训练（attended-speaker 负采样）抑制试次身份线索，并用基于 EEG–源相似度的置信加权提取目标。在 KUL 与 DTU 上摘要称严格跨试次协议下优于端到端基线。

## 本场要点

- 伪标签 + 对比预训练显著提升未见构音障碍严重度估计（平均 SRCC 0.761）。
- Phy-VC 用物理声道约束改善病理语音匿名与临床属性保留。
- 口吃研究议程需与成人口吃者及治疗师需求系统对齐。
- BabAR/TinyVox 将儿童音素识别接到可验证的发育测量。
- 五十年综述警示医疗化框架与当事人缺位。
- EEG-TSE 必须打破试次捷径，否则跨试次不可靠。

## 覆盖核对

| id | title |
|---|---|
| 1390 | Something from Nothing: Data Augmentation for Robust Severity Level Estimation of Dysarthric Speech |
| 378 | Phy-VC: Physics-Informed Voice Conversion for Privacy-Preserving Pathological Speech |
| 1704 | Aligning Stuttered-Speech Research with End-User Needs: Scoping Review, Survey, and Guidelines |
| 1132 | BabAR: from phoneme recognition to developmental measures of young children's speech production |
| 2962 | Making Room for Speech Diversity: A 50 Year Retrospective of Speech Science and Technology through a Neurodivergent Lens |
| 595 | Breaking Shortcut Learning for Cross-Trial EEG-Guided Target Speech Extraction via Two-Stage Training |
