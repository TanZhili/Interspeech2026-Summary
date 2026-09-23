# WazobiaSpeech: A Large-Scale Multilingual Speech Corpus for Robust and Fair ASR in Four Nigerian Languages

- 论文编号：3519
- 报告人：Ife Adebara
- 程序：Tuesday 29 September 2026 / Multilingual Speech 1
- 技术分类键：multilingual
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/adebara26_interspeech.pdf

## 问题
非洲语言在大规模语音资源中系统缺位；现有语料多为朗读/脚本、人口统计标注弱、治理不足，自发语音（韵律、不流畅、方言、语码转换）尤其稀缺，限制真实场景 ASR 鲁棒性与公平性评估。

## 方法
发布 WazobiaSpeech：豪萨语、伊博语、Naijá（尼日利亚皮钦）、约鲁巴语共约 2540.8 小时、2865 说话人；约 4% 为脚本朗读以补词汇/领域，其余以自发为主。领域覆盖农业、医疗、商业、日常会话；用文本/图像/视听多模态提示诱发；Yorùbá/Igbo 全自发，Hausa/Naijá 各约 50 小时朗读。元数据含年龄段、性别、教育、领域、模态。双层音质控制（约 40 dB SNR、48 kHz 等 + 母语人工审）；母语者按规范转写，标记 [um]/[?]/[cs]。说话人级分层划分 train≈85%、dev/dev-test/test 各≈5%。另描述多语种音系与伦理知情同意、本地转写治理。

## 实验与结果
正文宣称提供跨语基线 ASR、错误分析与约鲁巴声调敏感性细粒度评估，但抽取文本在质量保障“words-per-second”自动化检查处截断，具体 WER/CER、跨语对比与声调实验结果未能读到。规模对比表中 WazobiaSpeech 约 2500 小时、4 语、2500+ 说话人，相对 NaijaVoices（1867h/3 语）等强调多领域多风格自发。

## 结论
作者将 WazobiaSpeech 定位为以自发语音与丰富元数据支撑稳健、公平非洲语 ASR/TTS 的公开资源，并强调伦理与参与式采集。后续实验结论因文本截断无法确认。

## 点评
工作重心在“真实非洲语境下的自发多语语料+治理”，而不只是再堆小时数；领域 taxonomy、说话人分层防泄漏与转写标签设计都指向可做公平与声调分析。主要风险是抽取截断导致基线数字缺失，点评只能基于数据设计：脚本比例低有利于鲁棒性，但录音设备与场景变异大，质量与标注一致性将决定下游是否真能支撑 fair ASR 结论。
