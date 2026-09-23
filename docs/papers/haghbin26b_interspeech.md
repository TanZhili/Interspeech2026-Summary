# Natural Speech Encodes Early Markers of Cognitive Decline: Evidence from Clinical Conversations

- 论文编号：1860
- 报告人：Maryam Zolnoori
- 程序：Monday 28 September 2026 / Clinically Useful Speech Representations 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/haghbin26b_interspeech.pdf

## 问题
ADRD 早期症状在结构化 EHR 中记录稀疏，实验室短任务语料又偏晚期、生态效度不足；真实照护场景中的电话回访与护患对话是否能作为可扩展的早期认知障碍生物标志，增量价值尚不明确。

## 方法
175 人多模态语料（47 认知下降 / 128 健康）：约 100 维结构化临床变量 + 护理笔记；回访电话（均约 9 min）与护患口头交流（均约 29 min）。AWS Transcribe 转写与说话人分离，GPT-4o 映射患者侧；SpeechDETECT 提六类声学特征，BERT / BioMedBERT 提语言嵌入。轻量 bottleneck 融合：各模态经 adapter/encoder 成 token，用 m=8 可学习 fusion tokens 做 cross-attention + self-attention，再经 MLP 分类。分步加入模态；缺失模态用训练集均值填补；五随机种子报告均值±标准差。

## 实验与结果
EHR  alone：AUC 0.74±0.05，CI 类 F1 58.22。加首次电话：AUC 0.76，F1 61.95；加两次护患对话：AUC 0.90，F1 78.22。最佳为 EHR + 首次电话 + 两次护患对话：AUC 0.92±0.03，F1 83.08±3.59，Macro F1 88.31。Gradient×Input：首次护患对话贡献最大（34.6%），EHR 最小（17.4%）；声学与语言贡献接近（52.6% / 47.4%），声学侧以谱/倒谱为主。完整模态子集与性别/年龄分层结果大体稳定。

## 结论
真实场景自然对话相对结构化 EHR 能显著提升早期认知障碍检出；语音可作为可扩展、非侵入的功能向标志。局限包括样本规模与语言多样性不足，尚需纵向验证是否预测进展而非短期波动。

## 点评
增量消融设计清楚：先钉死 EHR 基线，再分别量化电话与护患对话的增益，结论可操作性强。瓶颈融合与归因分析也把“哪路信号在起作用”说清楚了。需注意缺失填补、小样本分层与电话标准化话术可能抬高可迁移性预期；最佳配置依赖较长护患录音，落地成本高于纯 EHR。
