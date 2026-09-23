# Speaker Privacy Preservation and Anonymization

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Poster（Area 4 - Poster 4）
- Area：4
- 论文数：12
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。隐私指标仅出自摘要。

## 技术趋势

本场系统覆盖说话人匿名化生成、儿童域适配、残差链路削弱、流式情感保持，以及联邦属性泄漏、个体再识别风险、验证场景内容混淆、声纹对抗防护、说话人级机器遗忘与更强攻击者评估。核心矛盾仍是隐私—效用—可感知自然度三角。

生成侧从 VQ 标记+流匹配（VerAno）、可控合成说话人向量，到针孔损失细调降链路性、儿童 SSL 域适配与流式情感蒸馏。防御与威胁侧同样升级：联邦权重差分可推断口音等属性；平均 EER 掩盖个体极端风险；FAcodec 多粒度混淆保护验证；人机感知差异与生成式通用对抗音频对抗克隆；ASR 中间层说话人结构成为遗忘靶点；双流分阶段攻击者暴露转换/匿名共享变换脆弱性。

## 技术内容

### 匿名化生成、儿童域与残差/情感

**VerAno: Speaker Anonymization via Self-Supervised Tokenization and Conditional Flow Matching**（论文 497；presenter：Ngoc Hung Le）  
VQ-VAE 标记化 SSL 特征并约束码本规模以自监督解耦说话人相关/无关信息，再与预训练说话人嵌入融合，经流匹配 Transformer 合成高保真声学。VoicePrivacy Challenge 数据上显著优于基线，并显示对未见语的跨语潜力。

**Controlled Generation of Synthetic Speaker Vectors for Voice Anonymization**（论文 1464；presenter：Ekaterina Kolos）  
为 WGAN 人工向量生成加入属性标签条件，并以分类器引导的扩散模型作替代；Voice Privacy Challenge 2024 套件上属性控制强且隐私/效用具竞争力，并提出多样性/原创性/自然度度量以选最优生成配置。

**Child-Centric Voice Anonymization in Single and Multi-Speaker Speech via Domain-Adapted SSL Models**（论文 2191；presenter：Xiao Xiao Miao）  
用 MyST 儿童语音适配 SSL 匿名流水线；单说话人与双说话人混合条件下，儿童域适配提升可懂度与感知质量并保持强隐私；多说话人场景结合目标说话人提取与儿童适配匿名以保留会话结构。

**Reducing Speaker Residual by Considering Pinhole Effect in Voice Anonymization**（论文 2346；presenter：Zeyan Liu）  
对已训练匿名框架引入针孔损失细调：度量同源说话人匿名话语的链路性并最小化之。多框架、伪说话人生成与数据集上隐私提升且效用保持。

**StreamVoiceAnon+: Emotion-Preserving Streaming Speaker Anonymization via Frame-Level Acoustic Distillation**（论文 3105；presenter：Nikita Kuzmin）  
用同说话人中性情感配对监督微调，并对声学标记隐状态做帧级情感蒸馏；改动限于微调（<2 小时/4 GPU），推理无额外延迟，流式延迟约 180 ms。VoicePrivacy 2024 上情感 UAR 49.2%、WER 5.77%，相对基线 UAR 相对+24%，隐私 EER 49.0%。

### 威胁评估、验证隐私与主动防护

**Personal Attribute Leakage in Federated Speech Models**（论文 327；presenter：Hamdan Al-Ali）  
被动威胁模型下，非参数白盒攻击仅用权重差分、不访问原始语音，对 Wav2Vec2/HuBERT/Whisper 推断性别、年龄、口音、情感与受损言语等属性；预训练中欠代表/缺失属性更脆弱，口音可被可靠推断。

**A Large-Scale Per-Speaker Analysis of Re-identification Risk in Speech Anonymization**（论文 440；presenter：Orane Dufour）  
近 5000 说话人、多匿名系统/攻击者/会话长度，用最坏情形链路性指标；说话人级风险高度两极分化，且易/难再识别集合随配置大幅变化；风险来自攻击者—匿名器—可用语音量交互，而非固有个体脆弱性。

**Privacy-Preserving Speaker Verification with Multi-Granularity Feature Obfuscation**（论文 437；presenter：Hanseul Kim）  
FAcodec 去除内容信息后对非内容表示多粒度混淆，保留说话人区分并阻碍忠实波形重建；指出高 WER 仍可能部分可懂。VoxCeleb1-O 上 EER 2.35%，相对先前 SOTA 相对改进 54.7%。

**Imperceptible Voiceprint Protection via Human-Machine Perception Discrepancy Feature Disentanglement**（论文 105；presenter：Haotian Guo）  
解耦内容与说话人后，在机器敏感而人耳不敏感的说话人嵌入空间注入扰动；防御成功率 87.2%（超嵌入级 SOTA 7%），MOS 4.18，并向黑盒克隆系统迁移。

**Towards Privacy-Preserving ASR: Speaker-Level Machine Unlearning**（论文 2458；presenter：Seaone Ok）  
层间分析显示说话人身份主要在 SSL-ASR 中间编码器层；针对身份结构的特征级遗忘在 VCTK 上去除特定说话人影响并保持转写性能。

**NaVo: Natural Voice Protection against Voice Cloning Attacks via Generative Universal Adversarial Audio**（论文 2944；presenter：Seoyoung Park）  
潜扩散 TTA+按性别与雨声/音乐/嘈杂等声学类别微调的 LoRA，生成自然通用对抗音频，经简单混音实时防护；对广泛使用的商业克隆系统黑盒防御成功率 76%。

**DAST: A Dual-Stream Voice Anonymization Attacker with Staged Training**（论文 3094；presenter：Ridwan Arefeen）  
谱与 SSL 双流并行编码；三阶段训练中第二阶段利用转换与匿名共享身份变换以建跨系统鲁棒，为泛化主因；第三阶段仅用目标匿名数据 10% 微调即可在 VPAC 上按 EER 超越当前 SOTA 攻击者。

## 本场要点

- 离散标记+流匹配与可控伪说话人向量推进隐私—效用平衡与属性可控。
- 儿童域适配与针孔损失分别针对年龄错配与残差链路性。
- 流式匿名可通过帧级情感蒸馏在低延迟下显著提升情感保持。
- 联邦 ASR 权重差分可泄漏口音等属性；平均 EER 不足以描述个体再识别风险。
- 验证场景需保护内容可懂度，WER 不能单独代表感知隐私。
- 主动防护从嵌入扰动与生成式通用对抗音频两条路径对抗克隆；攻击者评估本身也在强化。

## 覆盖核对

| 论文 id | 标题 |
| --- | --- |
| 497 | VerAno: Speaker Anonymization via Self-Supervised Tokenization and Conditional Flow Matching |
| 1464 | Controlled Generation of Synthetic Speaker Vectors for Voice Anonymization |
| 2191 | Child-Centric Voice Anonymization in Single and Multi-Speaker Speech via Domain-Adapted SSL Models |
| 2346 | Reducing Speaker Residual by Considering Pinhole Effect in Voice Anonymization |
| 3105 | StreamVoiceAnon+: Emotion-Preserving Streaming Speaker Anonymization via Frame-Level Acoustic Distillation |
| 327 | Personal Attribute Leakage in Federated Speech Models |
| 440 | A Large-Scale Per-Speaker Analysis of Re-identification Risk in Speech Anonymization |
| 437 | Privacy-Preserving Speaker Verification with Multi-Granularity Feature Obfuscation |
| 105 | Imperceptible Voiceprint Protection via Human-Machine Perception Discrepancy Feature Disentanglement |
| 2458 | Towards Privacy-Preserving ASR: Speaker-Level Machine Unlearning |
| 2944 | NaVo: Natural Voice Protection against Voice Cloning Attacks via Generative Universal Adversarial Audio |
| 3094 | DAST: A Dual-Stream Voice Anonymization Attacker with Staged Training |
