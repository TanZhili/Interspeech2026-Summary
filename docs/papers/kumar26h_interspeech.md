# VāṇīSetu: A Human-AI Collaborative Framework for Scalable Conversational Speech Corpus Creation in Low-Resource Settings

- 论文编号：2607
- 报告人：Rishabh Kumar
- 程序：Tuesday 29 September 2026 / Corpus Creation, Summerisation and Understanding
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/kumar26h_interspeech.pdf

## 问题
农村印地语等场景需领域对话语音数据，但手工校对成本约 6–8× 实时；噪声、方言与码混使通用 ASR 脆弱。需要可扩展的人机协同建库流程，并量化后处理对标注负担的影响。

## 方法
VāṇīSetu 四阶段：领域关键词引导从 YouTube 采集→VAD、PyAnnote 说话人分离、IndicWav2Vec/KVWav2Vec ASR、强制对齐→mT5/ByT5 或 LLaMA/ChatGPT 后校正→增强版 Vāgyojaka 上 Annotator→Validator→Verifier 三角色、阈值门控激励（λ=5%，δ=2%）。案例产出 KrishiVāṇī（约 100h 印地语农业对话）。ASR 上用 65h IndicVoice + 10h 领域数据训 KVWav2Vec；评测分 KV-Known / Unknown / OOD。

## 实验与结果
KVWav2Vec 在 Known/Unknown 上 WER 优于 IndicWav2Vec 与 IndicConformer（如 Known 22.38 vs 23.70/24.20）；OOD 上 IndicWav2Vec 略优。后校正中 mT5 在 Known/Unknown 上最好（22.29 / 25.70），ChatGPT ICL 在 OOD 最好（22.62）；mT5 延迟最低（0.97s）。相对全手工，验证流水线标注时间降 61.1%（95% CI [57.4%, 64.8%]，p<0.001）；协议一致性 Krippendorff’s α=0.87。

## 结论
角色分离 + 激励门控 + 小模型领域后校正，可在保持保真的前提下大幅降本；领域适配 ASR 有助 in-domain，OOD 仍宜保留通用基线。

## 点评
贡献重心在可度量的人机标注操作系统，而非单纯刷 WER。mT5 胜过更大 LLM 的 in-domain 结果对低成本流水线有直接启示；脆弱点在 YouTube 版权/代表性、激励阈值对标注行为的诱导，以及农业印地语特性对其他领域的迁移程度。
