# TriageSim: A Conversational Emergency Triage Simulation Framework from Structured Electronic Health Records

- 论文编号：819
- 报告人：Dipankar Srirag
- 程序：Tuesday 29 September 2026 / Speech and Language Technologies in Healthcare
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/srirag26_interspeech.pdf

## 问题
急诊分诊依赖短时口语互动，但隐私与监管使真实护患多轮对话与音频难以公开；现有临床数据多为结构化结果或事后笔记，诊断向模拟也缺少音频、声学变异与明确分诊决策框架。

## 方法
TriageSim：以 MIMIC-IV-ED 与 ESI Handbook、ETEK 教学案例为种子临床状态；用 Gemini/GPT 等生成患者与护士 persona（口音、不流畅率、风险容忍、指南遵守等）。多智能体：dialogue master 持有真值并响应生命体征查询；护士 agent 按 ATS 或 ESI 算法提问/查体征/做分诊并记录红旗；患者 agent 仅知主诉与疼痛等。对话后做短语边界标注，按国籍/性别从声库取样，用 Qwen-3-TTS 零样本克隆，再混入 ESC-50 环境音（固定相对增益）。代码已公开。

## 实验与结果
生成约 814 段对话（~26 小时，四级口音）。患者不流畅可控：意图与实测 Spearman ρ=0.57。护士行为：经验与信心单调相关；低风险容忍略增过度分诊（0.40）；严格指南遵守平均查体征 2.88 次。声学：整体 WER=10.8（Whisper-Large-V3-Turbo），护士 5.7、患者 16.0；说话人一致性 99.98；UTMOSv2≈3.42。医学保真：专家盲评 50 段，主诉嵌入余弦相似 0.83，红旗检测 P/R=0.94/0.96。分诊分类二次加权 κ：合成文本/ASR/音频上均仅 fair（如 ATS 文本均值约 0.33），模态间差距小。

## 结论
框架能从结构化 EHR 生成临床连贯、交互稳定且带可控语言/行为/声学变异的分诊对话；下游分诊分类难，瓶颈更在会话临床推理而非转写噪声。

## 点评
贡献在于把分诊协议写进 agent 策略并同时交付文本+音频，评测覆盖语言、行为、声学与医学保真，比纯文本角色扮演更贴近语音研究需求。合成数据上的高红旗一致性可能偏乐观；分类 κ 偏低也提醒：有了对齐语料仍不等于自动分诊已可部署。
