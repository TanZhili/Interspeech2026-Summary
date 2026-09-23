# Speech Benchmarks, Evaluation, and Resources

- 日期：2026年10月1日（星期四）
- 时间：09:00-11:00
- 形式：Poster
- Area：12
- 论文数：8
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场资源与基准海报强调可复现、多条件、任务对齐的评测基础设施：无监督音素发现、巴西葡语自发语音、俄语韵律感知标注流水线、印度语统一 ASR/TTS 框架、偏好指令感知 ASR、开放排行榜，以及真实 ASR 幻觉与语码转换语义错误率。共同点是单数据集单指标无法刻画系统真实行为。

低资源与多语方面，DiscoPhon 用离散单元映射预定义音素清单；Spashta Audio-Bench 插件化注册模型/数据并引入 TTS-ASR 退化作可复现可懂度。领域资源上 Tarsila 聚合 70+ 小时自发巴西葡语；Balalaika 以语义 VAD、多 ASR ROVER 与重音/标点等丰富标注支撑去噪与 TTS。

新一代评测维度包括：Preference-ASR 测自然语言输出风格偏好；Open ASR Leaderboard 统一 WER/RTFx；HALAS 在真实财报电话上标幻觉跨度；CSER 量化语码转换中语言误识等对意图的影响，并与词汇指标互补。

## 技术内容

### 音素发现、语种域基准与标注流水线

**DiscoPhon: Benchmarking the Unsupervised Discovery of Phoneme Inventories With Discrete Speech Units**（论文 2791；Maxime Poli）  
6 开发 + 6 测试语，未见语言仅 10 小时语音，将离散单元 many-to-one 或 one-to-one 映射到预定义音素清单，评单元质量、识别与切分。提供四套多语 HuBERT/SpidR 基线，显示现有模型含足够音素信息但跨语差异明显。

**Tarsila-ASR: A Multi-Domain Test Suite for Benchmarking Brazilian Portuguese Speech Recognition**（论文 450；Sidney Leal）  
聚合多公开集超 70 小时自发巴西葡语基准；系统评开源 ASR 并在多样对话数据微调得新 SOTA，强调领域适应，资源公开。

**Balalaika: Data-Centric, Prosody-Aware Annotation Pipeline for Russian Speech**（论文 83；Vasiliy Kudryavtsev）  
开源数据中心流水线：语义 VAD、多 ASR ROVER（保留词级时间戳）、质量与说话人纯度过滤，并补标点、词重音、е/ё 与 IPA。建 5.1k 小时俄语多源语料；等预算下对去噪与 TTS 一致增益。

**Spashta Audio-Bench: Unified ASR and TTS Evaluation Framework across Indian Languages**（论文 1777；Bikash Dutta）  
类 HuggingFace Evaluate 的插件框架；评 10 个开源 ASR/TTS、7 语料、22 印度语及印度口音英语。揭示参数放大≠跨语鲁棒、TTS 自然度与可懂度可分离、ASR 域敏感；引入 TTS-ASR 退化作客观可懂度。

### 偏好、排行榜、幻觉与语码转换语义

**Preference-ASR: A Preference-Aware Test Set for Benchmarking ASR in the Era of Speech LLMs**（论文 728；Nithin Rao Koluguri）  
覆盖归一化、实体、不流畅、大小写四类自然语言偏好指令；两阶段 LLM 辅助 + 人工核验，偏好感知归一化器按指令跳过步骤。四模型排名随偏好类型变化，揭示传统评测掩盖的差异。

**Open ASR Leaderboard: Towards Reproducible and Transparent Multilingual and Long-Form Speech Recognition Evaluation**（论文 1902；Eric Bezzam）  
社区贡献平台对比 85+ 系统、11 数据集（英短/长、多语短），统一 WER 与 RTFx。观察 Conformer+LLM 解码平均 WER 最佳，CTC/TDT 更利 RTFx；代码与加载器开源。

**HALAS: A Human-Annotated Dataset of Hallucinations of Modern ASR Systems**（论文 337；Mateusz Barański）  
七个 SOTA ASR 在真实未处理财报电话上的人工幻觉跨度标注。跨模型词表重叠强，低 WER 也可幻觉；字符/语义代理约 81% ROC-AUC，既有检测方法 F1 仅 53.1%。

**CSER: Semantic Evaluation of LLM Auto-Repair for Code-Switching ASR**（论文 3390；Tien Dat Bui）  
CSER 量化语言误识、少数语替换等对语义/意图的影响，并评 LLM 自动修复；含越—英多条件基准。显示词汇与语义指标互补，对流水线意图保持均必要。

## 本场要点

- 无监督音素发现与插件化印地语系评测推动可比、多指标基础设施。
- 自发域语料与韵律感知标注流水线直接提升巴西葡语 ASR 与俄语 TTS/去噪。
- 偏好指令、开放排行榜与真实幻觉基准暴露传统 WER 盲区。
- 语码转换需语义级错误率与 LLM 修复评测，不能只看词错误。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 2791 | DiscoPhon: Benchmarking the Unsupervised Discovery of Phoneme Inventories With Discrete Speech Units |
| 450 | Tarsila-ASR: A Multi-Domain Test Suite for Benchmarking Brazilian Portuguese Speech Recognition |
| 83 | Balalaika: Data-Centric, Prosody-Aware Annotation Pipeline for Russian Speech |
| 1777 | Spashta Audio-Bench: Unified ASR and TTS Evaluation Framework across Indian Languages |
| 728 | Preference-ASR: A Preference-Aware Test Set for Benchmarking ASR in the Era of Speech LLMs |
| 1902 | Open ASR Leaderboard: Towards Reproducible and Transparent Multilingual and Long-Form Speech Recognition Evaluation |
| 337 | HALAS: A Human-Annotated Dataset of Hallucinations of Modern ASR Systems |
| 3390 | CSER: Semantic Evaluation of LLM Auto-Repair for Code-Switching ASR |
