# InsideSSL: Understanding Self-Supervised Speech Representations using a Model-Centric Perspective

- 论文编号：733
- 报告人：Samir Sadok
- 程序：Monday 28 September 2026 / Speech Representations and Alignment
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/sadok26_interspeech.pdf

## 问题
Wav2Vec2、HuBERT、WavLM 等 SSL 语音模型下游强，但层内动力学仍不清。既有分析多依赖预定义属性与下游相关，缺少任务无关的模型中心刻画，也难比较不同预训练目标如何塑造压缩、几何与鲁棒性。

## 方法
INSIDESSL 两块：
1. **层内三视角**：压缩（Gram 矩阵 von Neumann 熵）、几何（相邻 token 轨迹平均曲率）、鲁棒（噪声/音高/掩蔽等增强视图上的 InfoNCE）；
2. **跨层 Generative Compatibility Matrix（GCM）**：各层训练生成解码器，交叉条件于其他层表示，度量功能可迁移性（语音内容/说话人身份等）。
并辅以线性探测连接拓扑与音素、音高、说话人等任务。评估主要在 LibriSpeech；对比 BASE/PLUS/LARGE 及不同目标（对比、掩码预测、去噪、连续回归等）。

## 实验与结果
（抽取在 scale/data 小节中部截断，以下为可读结果。）
- 多数模型熵全程高（约 0.82→0.75）；**Wav2Vec2** 末层出现熵塌缩。HuBERT/WavLM/UniSpeech 熵轨迹相关约 0.86。
- 曲率：早期高（约 1.4）后降至约 1.2（流形展开）；HuBERT/WavLM/UniSpeech 曲率相关 >0.96。
- 不变性：多数前 20% 层即达低 InfoNCE 平台；Wav2Vec2 与 Data2Vec 深层 InfoNCE 再升高，与熵/曲率异常一致，形成与 HuBERT 系不同的簇。
- 综述 takeaway：先增复杂（曲率）→ 展开流形 → 深层稳定。

## 结论
不同 SSL 目标诱导不同压缩与流形展开制度；GCM 与层内指标揭示稳定语音核心、身份波动与深层语义修剪。线性探测进一步表明层拓扑制约下游编码位置。

## 点评
不绑死下游标签、用熵/曲率/不变性与跨层生成兼容性读“网络在干什么”，对选型与层选择有直接启发。强在跨模型相关矩阵分出稳定簇；**全文抽取在 3.3 节中途截断**，scale、ASR 微调与 GCM/探测的定量表可能不全，点评仅基于已读部分。
