# NaturalFlow: Reducing Disruptive Pauses for Natural Speech Flow in Simultaneous Speech-to-Speech Translation

- 论文编号：540
- 报告人：Dongwook Lee
- 程序：Tuesday 29 September 2026 / Multilingual Speech 1
- 技术分类键：multilingual
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26c_interspeech.pdf

## 问题
同声 speech-to-speech translation（Simul-S2ST）为压低延迟常按块释放译文，造成频繁停顿与破碎语流，增加听者认知负荷；现有研究多优化质量–延迟（BLEU vs lag），较少直接优化停顿驱动的声学流畅度。

## 方法
在 Hibiki（Mimi codec、同步预测目标语音与对齐文本）上引入 NaturalFlow：用 Direct Preference Optimization（DPO）对齐流畅偏好。偏好数据：CVSS-C 短句 1 万条 + mTEDx Fr→En 拼接长段 6 千条；每源采样 k=32 候选；用 Whisper-medium ASR+BLEU 量翻译质量，Silero VAD 算 silence ratio（静音时长/起止间总时长）。Silver-Medal Preference：按静音比五等分，取第二档（20–40%）为 chosen，避免最上档过激降静音导致语义崩坏；chosen 相对 rejected 需满足 BLEU 差≥5、静音比差≥组内归一化 15%。DPO 只优化声学条件下的文本流策略（直接优化音频 token 不稳定）。

## 实验与结果
Fr→En：CVSS-C / VoxPopuli / Audio-NTREX / mTEDx。NaturalFlow 相对 Hibiki 降低静音比（如长表 Audio-NTREX SR 0.17→0.13，mTEDx 0.26→0.21；短表 VoxPopuli 0.12→0.10），同时保持接近的 LAAL/起止偏移与 ASR-BLEU/COMET（如 mTEDx ASR-BLEU 33.27 vs Hibiki 32.94）。相对 StreamSpeech/Seamless，在长音频上静音与延迟更可控。正文称人工偏好听感更自然；抽取文本在 text-guided DPO 公式处截断，训练细节与人评完整表未见。

## 结论
通过银牌档偏好与大间隔约束，可在不明显牺牲翻译质量与延迟的前提下压低块间静音，使同声 S2ST 更接近连贯语流。边界是优化绕开直接音频 token、且依赖 ASR-BLEU 代理质量。

## 点评
问题抓的是同声系统“为等上下文而停”的用户体验，而不是再压 LAAL。Silver-Medal 有意避开最优静音档，是对 DPO 过优化的工程防护。脆弱处：静音比依赖 VAD 阈值、质量用 ASR-BLEU 代理可能误伤韵律/专名，且全文截断使人评与消融证据不完整。
