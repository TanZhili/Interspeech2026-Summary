# Beyond Standard Greek: Adapting Whisper for Greek Dialects through Curriculum Multitask Learning

- 论文编号：2567
- 报告人：Vassilis Katsouros
- 程序：Tuesday 29 September 2026 / Multilingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/klimi26_interspeech.pdf

## 问题
希腊方言相对标准现代希腊语（SMG）存在明显“方言税”：零样本 WER 常极高，普通微调仍大幅落后 SMG；多任务与课程学习各自有效，但少有按监督类型做跨任务/跨域递进的适配。

## 方法
四阶段 staged multitask curriculum：Stage0 仅希腊→英语音译（G_ST）；Stage1 以 α 混 SMG ASR 与方言 ST；Stage2 以 β 混方言 ASR 与方言 ST；Stage3 纯方言 ASR。任务提示动态注入 decoder。实验方言为 Cypriot、Cretan、Messenian；donor 用 GPC-5h；英译由 Llama-Krikri 生成并人工校对。评测 Whisper-small/medium/large-v3，encoder 冻结、卷积特征可训。

## 实验与结果
Curriculum 在各方言与规模上均优于零样本与常规 FT。例如 Cypriot small：ZS 81.27 → FT 52.38 → Curr. 35.61；large-v3 Curr. 24.89。Cretan/Messenian 同样有一致降幅。α/β 比例模型相关：small 上 0.5/0.5 最好（33.56）。去掉翻译监督的 ASR-only 课程全面变差（small 上可差超 12 点 WER）；极低资源 Messenian 上缺少 GPC donor 也更易受损。

## 结论
沿任务（翻译→ASR）与领域（SMG→方言）递进可减轻分布失配、稳定低资源方言适配，一致优于朴素微调。后续拟考察语言距离、参数高效适配与更难接触方言。

## 点评
把 donor 语、音译辅助与课程调度串成对角线路径，对“有近亲高资源语但方言标注极少”的场景很实用。强在三方言多尺度与消融完整；弱在部分方言时长极短（如 Messenian 预处理后约 37 分钟）、英译依赖 LLM+人工，推广到接触型北方方言仍待验证。
