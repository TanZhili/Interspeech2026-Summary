# HASS: Hierarchical Simulation of Logopenic Aphasic Speech for Scalable PPA Detection

- 论文编号：3080
- 报告人：Harrison Li
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 2
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26ia_interspeech.pdf

## 问题
原发性进行性失语（PPA）临床数据稀缺；既有不流畅仿真多注入孤立事件，难刻画 logopenic 变异（lvPPA）跨词汇检索与音系编码的多层次表型。

## 方法
HASS：在临床专家指导下用 LLM 生成内容层（词汇检索受损）与音素层（音系错误）严重度条件缺陷，再合成为语音；同管线生成匹配对照（不注入损伤）。语料 4773 句级片段。用 Wav2Vec2+LoRA 分类，严格跨站：Baycrest/Hopkins 患者与 Delaware/Capilouto 对照。

## 实验与结果
跨站：HASS 训练模型 AUC 0.892±0.076、F1 0.800±0.072、dysfluent 召回 0.899±0.066，优于真实数据基线（AUC 0.850、召回 0.659）。纯 HASS 训练在跨语料协议上也可泛化。

## 结论
临床接地的分层仿真可为 lvPPA 检测提供可扩展增强，并改善跨站点泛化与对不流畅样本的召回。

## 点评
把疾病机制写成可控制的双层生成，比“随机插停顿”更贴近表型。合成–真实域差仍在；作者强调对照与患者同管线以隔离合成伪影，但零样本临床部署仍需标定阈值与伦理边界。
