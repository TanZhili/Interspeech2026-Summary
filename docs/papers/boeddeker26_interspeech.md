# Speaker Identity as Sole Supervision for Speech Separation

- 论文编号：2620
- 报告人：Christoph Boeddeker
- 程序：Thursday 1 October 2026 / Source Separation 2
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/boeddeker26_interspeech.pdf

## 问题
分离通常依赖干净参考波形/频谱、多通道空间线索或 MixIT/self-remixing 等信号级无监督目标；真实场景难获平行干净源。能否仅用说话人身份作为监督信号训练说话人无关分离器？

## 方法
Speaker-Identity Supervision (SIS)：训练时每个说话人另有辅助语句 ˜x_k；分离输出与辅助句经嵌入器得 ˆe/˜e，用温度缩放余弦相似度上的 InfoNCE（批内负样本含竞争说话人与其他混合物辅助嵌入），排列用相似度 PIT。嵌入器仅训练期使用：处理分离输出时冻结参数（梯度只回传到分离器），另一次前向更新嵌入器于辅助句，避免嵌入器适应分离伪迹。推理为常规无条件分离器，无需注册语音。骨干为轻量 STFT-magnitude BLSTMP；对比 sigmoid/softmax 掩码。

## 实验与结果
Libri2Mix max 16 kHz。干净集：波形监督 14.4 dB SDR；联合学习嵌入的 SIS 达 8.1 dB SDR、WER 19.4%；冻结预训练 ECAPA 仅 3.0 dB。噪声域：干净训练模型域移严重；用 SIS 从干净波形模型微调到含 WHAM! 噪声的混合物可达 8.7 dB SDR（N5），接近全波形噪声监督 9.7 dB。softmax 强制混合一致性但限制去噪；sigmoid 更灵活但可能引入伪迹。

## 结论
仅说话人身份即可从零训出可用分离器，并可用于无干净参考的噪声域自适应；仍弱于全波形监督，计划结合 ASR/空间约束与更强骨干。

## 点评
把 TSE 里“身份当条件”改成“身份只当损失”，推理零注册，问题设定很干净。关键在嵌入器设计：过鲁棒的验证模型反而害训练。弱监督下放松混合一致性可能生成伪内容，部署需谨慎；更适合作为适配/弱标注场景的补充监督。
