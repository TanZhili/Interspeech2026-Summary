# Child-Centric Voice Anonymization in Single and Multi-Speaker Speech via Domain-Adapted SSL Models

- 论文编号：2191
- 报告人：Xiao Xiao Miao
- 程序：Wednesday 30 September 2026 / Speaker Privacy Preservation and Anonymization
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/tushar26_interspeech.pdf

## 问题
现有语音匿名化多在成人数据上训练，直接用于儿童会显著损害可懂度与感知质量；且常把儿童声转成成人声，并几乎只考虑单说话人，难覆盖课堂/诊疗等多说话人场景。

## 方法
基于 SSL 解耦管线（HuBERT soft content + F0 + ECAPA 说话人；选择性替换为参考嵌入后 HiFi-GAN 重建）：在 MyST 上微调 content encoder 与 vocoder，并把成人说话人池换成经筛选的 AI 儿童声池（16 说话人、44 句）。多说话人：Conformer TSE 提取目标 → 儿童目标用 FT/FT 匿名、成人用 base → 与残差非目标混合重建。单说话人评 MyST（域内）及 MPS、SpeechOcean（口音零样本）；多说话人 SparseLibriMix 风格 AA/CA/CC 混合，重叠 0–100%。

## 实验与结果
MyST 组件消融：仅改一端会变差，FT/FT 最佳（EER 45.09%、WER 16.64，相对 Base/Base 的 43.80/17.31）。跨集 SSL-FT 隐私 EER 最高，可懂度在 MyST/MPS 最优或具竞争力。13 人听感上 SSL 系自然度/流畅度优于 McAdams B2，SSL-FT 更稳地保留“听起来像儿童”。多说话人：OA EER 相对 OO 明显升高且随重叠较稳；tWER/DER 随重叠与年龄配对变差，CC 最难，瓶颈主要在儿童目标提取而非匿名本身。

## 结论
儿童域适应可改善儿童–儿童匿名的效用与年龄感知，同时保持强隐私；多说话人场景隐私相对稳健，效用受 TSE 质量制约。局限包括评测模型偏成人、多说话人伪参考转写、TSE/攻击者未儿童适应等。

## 点评
把问题从“能不能匿名儿童”转到“保持儿童声学身份的同时去身份”，并显式拆开提取误差与匿名误差，对真实对话部署很有针对性。AI 儿童声池避免用真实儿童身份作伪说话人，但引入合成音色分布；成人训练的 TSE 是 CC 高重叠下的明显短板，后续收益更可能来自儿童鲁棒分离而非继续微调声码器。
