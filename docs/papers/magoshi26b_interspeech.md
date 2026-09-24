# Improving Zero-Shot Phonetic Classification through Language-Agnostic Articulatory Features

- 论文编号：2246
- 报告人：Ryo Magoshi
- 程序：Tuesday 29 September 2026 / Low-Resource & Endangered Language Speech Processing
- 技术分类键：multilingual
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/magoshi26b_interspeech.pdf

## 问题
Speech-to-IPA 的 Phonetic Foundation Model 多靠 G2P 标签，本质偏音位且跨语记法不一致；仅靠多语离散 IPA 覆盖不足以在零样本下区分未见语音学对立。

## 方法
排除中文与日语后，在 IPAPack++ 的 Common Voice/FLEURS 部分（78 语约 3000h）训练：POWSM（CTC/Attention）与 XLS-R+AFCM（帧级预测 24 维 PanPhon 发音特征并联合 CTC）。分类时先定位目标段，再比较三种读出方式：Decoder 对齐、CTC 峰值帧 argmax、以及 AF 向量与候选模板的 L1 距离。并对比 single-frame 与 segmental 时间聚合。

## 实验与结果
零样本任务：中文送气对立（FLEURS）与日语音拍鼻音（CSJ，人工核验 IPA）。POWSM 平衡准确率差（送气约 53–58%，鼻音约 47–49%）。XLS-R+AFCM 的 CTC 送气达 94.5%；AF single-frame 进一步到 95.4%，但 AF segmental 因冲淡送气爆发几乎崩溃（约 50.8%）。鼻音上 AF segmental 最好（72.6%），稀有 [ñ] 召回 38.5%，远高于非 AF 方法（<7%）。

## 结论
连续发音特征比离散 IPA 更利于零样本语音学分类，尤其稀有音；最优时间聚合取决于线索是瞬态（送气宜单帧）还是持续（鼻音部位宜段平均）。

## 点评
把“符号覆盖了”与“声学对立学会了”拆开验证，对 G2P 训练范式是尖锐压力测试。强在两类对立与聚合消融清楚；弱在任务仅两语两类对立、训练仍依赖 G2P 派生 AF 标签，完全开放词表零样本 ASR 仍有距离。
