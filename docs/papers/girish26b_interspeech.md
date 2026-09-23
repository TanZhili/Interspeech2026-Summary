# Synergizing Zero-Shot Cross-Lingual Alzheimer Detection with Language-Invariant Multimodal Bi-Geometric Adversarial Learning

- 论文编号：2756
- 报告人：Muskaan Singh
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/girish26b_interspeech.pdf

## 问题
基于语音的阿尔茨海默检测（SADD）需跨语言零样本迁移；单模态预训练表征易泄漏语言身份，简单拼接融合难以抑制语言特异伪线索。

## 方法
提出 ORBIT：冻结/浅层解冻多语语音与文本 PTM，注意力池化后双向交叉注意融合；在融合表征、球/双曲几何投影与聚类责任上施加多点 GRL 语言对抗；球空间与 Poincaré 球上做共识聚类与原型 PoE 投票分类。数据：Pitt（英）、Ivanova（西）、NCMMSC（中）、Dem@Care（希，Whisper-large-v3 转写），二分类 AD vs HC。协议含 LTLO 与 LOLO。

## 实验与结果
合并语种上 CNN 通常优于 FCN；单模态最强为 mHuBERT 与 BERT。零样本下 ORBIT+交叉注意优于单模态与拼接：LOLO 最佳 mHuBERT+Qwen3 达 86.98 Acc / 85.29 F1；LTLO 最佳 Acc 为 mHuBERT+E5（85.49），最佳 F1 为 Whisper+E5（83.34）。消融：去掉 GRL 或仅单几何均下降，完整球+双曲+对抗最好。

## 结论
多模态融合加语言不变约束能提升零样本跨语 SADD；交叉注意与双几何+多点对抗是关键。作者称相对既往 Whisper 迁移等单模态 SOTA 有提升。

## 点评
把「模态互补」与「去语言泄漏」拆成交叉注意、多点对抗与双流形共识，针对零样本跨语设定合理。异构语料（任务、录音条件、希语 ASR 转写）可能仍残留域差，语言对抗未必消尽任务混杂；合并集上单模态 Acc 已很高，跨语跌落更说明迁移难度在语言/域偏移而非可分性本身。
