# Personal Attribute Leakage in Federated Speech Models

- 论文编号：327
- 报告人：Hamdan Al-Ali
- 程序：Wednesday 30 September 2026 / Speaker Privacy Preservation and Anonymization
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/alali26_interspeech.pdf

## 问题
联邦学习虽不上传原始语音，但 ASR 本地微调后的权重差仍可能泄漏性别、年龄、口音、情感、构音障碍等属性；既有联邦语音攻击多聚焦成员/再识别，且常需目标说话人音频。

## 方法
被动服务端白盒威胁：仅用全局模型 Wg 与单句个性化后 Ws。用公开数据建 shadow 模型，从每层参数张量抽 μ/σ/min/max 拼成向量，按类中心做归一化欧氏距离分类。在 Wav2Vec2-Base、HuBERT-Large、Whisper-Small 上测性别/年龄/口音（SAA）、情感（RAVDESS 三对二分类）、构音障碍（TORGO）。另做 Wav2Vec2 逐层攻击、十类口音细粒度分类，以及口音多样微调防御与未见口音泛化、功能更新（ℓ2/surprisal/KL）分析。

## 实验与结果
Table 1：性别最难（46–64%）；年龄与口音泄漏极强（Wav2Vec2 均达 100%；口音 HuBERT 80%、Whisper 93%）；Whisper 多数任务 >70%。情绪与构音障碍上 Whisper 更稳。十类口音攻击准确率 ≥90%；对十口音小样本微调后各口音精度骤降至 ≤0.2，但未见口音仍高 F1。功能分析：各组权重 ℓ2≈11.21 相近，但韩语口音 surprisal/KL 约为英语的 2–2.5 倍。

## 结论
联邦 ASR 更新可在无原始音频下推断敏感属性，泄漏与预训练覆盖不足相关；扩大口音等人口学覆盖可显著削弱已知属性攻击。作者强调 FL 保护并不均匀。

## 点评
威胁模型贴近真实联邦服务器，且把“覆盖不足→更大功能位移→更可分更新”串成证据链，比单纯报攻击准确率更有建设性。口音/年龄极高成功率值得警惕；性别近机会水平也说明泄漏属性相关。局限是单句个性化与二分类设定偏理想化，且影子数据需与属性分布对齐。
