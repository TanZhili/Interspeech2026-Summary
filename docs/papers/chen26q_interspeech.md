# Streaming Open-Vocabulary Keyword Spotting via Role Swapping in Cross-Attention

- 论文编号：1676
- 报告人：Liming Song
- 程序：Monday 28 September 2026 / Information Extraction and Retrieval
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/chen26q_interspeech.pdf

## 问题
跨注意力开放词表 KWS 多在整段语音上工作；流式时若仍把语音作 Key/Value，只能见局部帧却需全局上下文，与注册文本作 Query 的数据流不匹配。

## 方法
角色互换：流式语音作 Query，注册文本嵌入作 Key/Value，帧级更新亲和矩阵并做决策。约 0.8M 文本注册模型；因果卷积+GRU 音频编码器。两阶段训练：先用注意力输出对齐文本语义，再用亲和矩阵+音频嵌入训练帧级判别。辅以 InfoNCE、PhoneMatch、在线时域掩码硬负样本。

## 实验与结果
LibriPhrase：LPE EER/AUC 6.82%/97.95%，LPH 28.21%/79.19%；LPH 优于 SYNASPOT-AT 与 CTCAT。相对 CTCAT 在简单负例略弱，但困难负例更稳。单线程 RTF 0.065（float32）。消融显示硬负样本对 LPH 有益。

## 结论
作者认为角色互换使跨注意力可流式部署，并以端到端网络决策替代 CTC/启发式后处理，在困难负例上更鲁棒。

## 点评
关键洞察是流式场景下 Q/K/V 角色与信息粒度的匹配，工程上去掉 CTC 对齐降低部署复杂度。LPE 上未全面领先说明简单场景对齐法仍强；文本注册实例化，语音注册泛化需另证。
