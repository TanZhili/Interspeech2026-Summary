# Speaker Privacy and Anonymization

- 日期：2026年10月1日（星期四）
- 时间：09:00-11:00
- 形式：Oral
- Area：4
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场围绕说话人隐私与匿名化：轻量时域修改对通信效用的影响、扩散模型推理时韵律可控、可证明差分隐私机制、属性视角威胁评估、声学 token 同时抹除说话人与内容标识，以及全双工对话模型隐状态泄漏与流式匿名。共同议题是在保护身份（及内容）的同时保留可懂度、韵律与下游评估可用性。

方法从启发式替换说话人嵌入，走向可连续权衡的 CFG 扩散（DiffAnon）与形式化 speaker DP（DP-VOXLET）。评测也从信号对信号扩展到属性集合唯一性与单话语攻击。监管域场景要求同时切断生物识别与语言可识别内容，并尽量保留域内声学特性；端到端全双工模型则暴露 LLM 骨干隐状态的说话人泄漏，需要波形/特征域流式匿名前端。

## 技术内容

### 效用权衡与可控韵律匿名

**Privacy vs. Performance: Assessing Communication Utility of Anonymized Voice Features**（论文 751；Shogo Okada）  
评估轻量相位声码器时标修改（PV-TSM）对声学/韵律特征与 ASR 的影响。摘要称匿名可大体保留这些特征并有效掩盖说话人身份；用匿名语音微调 ASR 可缓解识别错误并恢复下游特征精度，表明隐私与韵律保真可并存。

**DiffAnon: Diffusion-based Prosody Control for Voice Anonymization**（论文 1331；Ismail Rasim Ulgen）  
在 RVQ codec 语义嵌入上用带 CFG 的扩散细化声学细节，推理时可连续插值匿名强度与韵律保真。摘要称其为首个提供结构化、可插值推理时韵律控制的语音匿名框架，在可控工作点上兼具强效用与有竞争力的隐私。

**DP-VOXLET: Provable Speaker Anonymization for Disentangled Speech Representations**（论文 2910；Christopher Liberatore）  
引入基于差分隐私的 speaker differential privacy 形式定义，并给出可证明满足该定义的机制，从而对任意对手的再识别成功率（如 EER）给出可证下界。框架兼容现有解缠表示，相对先前说话人 DP 工作效用显著更高。

### 属性威胁、双通道匿名与全双工泄漏

**Voice Privacy from an Attribute-based Perspective**（论文 2061；Mehtab Ur Rahman）  
主张以说话人属性集合比较度量隐私，分析真实属性、原语音推断属性与标准匿名后推断属性的唯一性，并考察每说话人仅一条话语的攻击错误率。观察：尽管属性推断有误差，推断属性仍构成风险，未来需同时考虑属性相关威胁与保护机制。

**Acoustic token admixture for joint speaker and content anonymization**（论文 1949；Ali Golmakani）  
在声学 token 空间对编码器导出与音素条件 token 做逐帧混合，联合匿名说话人身份与语言可识别内容，并用 NER 触发跨度替换以保留周围韵律，避免完整重合成牺牲域内声学。VoicePrivacy 2024 上 EER 42.54%、WER 3.73%。

**Privacy-Preserving End-to-End Full-Duplex Speech Dialogue Models**（论文 3181；Nikita Kuzmin）  
按 VoicePrivacy 2024 懒惰知情攻击协议，显示 SALM-Duplex 与 Moshi 隐状态跨层泄漏大量说话人身份；SALM-Duplex 早期层更强，Moshi 较均匀，前几轮 Linkability 急升。提出 Stream-Voice-Anon 的 Anon-W2W 与 Anon-W2F：Anon-W2F 使 EER 相对离散编码器基线升逾 3.5×（11.2%→41.0%），Anon-W2W 保留基线 sBERT 的 78–93% 且首响低于 0.8 s。

## 本场要点

- 轻量时标修改可兼顾身份掩盖与通信相关特征，微调可恢复 ASR。
- 扩散 + CFG 实现推理时连续韵律—隐私权衡。
- 形式化 speaker DP 提供可证再识别下界并提升效用。
- 属性视角揭示推断属性仍是残留威胁。
- 监管域需联合抹除说话人与内容两通道，并尽量保留域声学。
- 全双工对话模型隐状态泄漏显著，流式特征域匿名接近机会水平 EER。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 751 | Privacy vs. Performance: Assessing Communication Utility of Anonymized Voice Features |
| 1331 | DiffAnon: Diffusion-based Prosody Control for Voice Anonymization |
| 1949 | Acoustic token admixture for joint speaker and content anonymization |
| 2061 | Voice Privacy from an Attribute-based Perspective |
| 2910 | DP-VOXLET: Provable Speaker Anonymization for Disentangled Speech Representations |
| 3181 | Privacy-Preserving End-to-End Full-Duplex Speech Dialogue Models |
