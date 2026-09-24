# QuadVAD: Fine-Grained Speech Detection with a Compact Architecture

- 论文编号：2009
- 报告人：Nivedita Chennupati
- 程序：Wednesday 30 September 2026 / Acoustic Event Detection 3
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rachumallu26_interspeech.pdf

## 问题
常开设备与对话 AI 需要低延迟、精确边界的 VAD；现有神经 VAD 多为 16–40 ms 帧，边界偏移大，难以服务唤醒词等精细场景。

## 方法
QuadVAD：约 6k 参数，对每 4 ms 非重叠帧拼接前 3 ms 上下文（7 ms@16 kHz）做轻量卷积分类。多阶段训练：先用 MFA 对齐监督，再在 TIMIT 上精调时间精度；噪声/增益增强。目标 4 ms 分辨率。

## 实验与结果
相对 Silero/TenVAD 等，开源集 AUC 更高。电平 [−40,−15] dBFS：QuadVAD F1 0.95，与 Silero 相当并优于 TenVAD；更低电平 [−60,−40]：F1 0.96、AUC 0.99 最优。模型约 25 kB、25 MFLOPs，i7 上 RTF 0.0014。结论称跨语趋势稳健，适合唤醒词集成。

## 结论
超轻量 4 ms VAD 在精度与算力间取得平衡，可部署于资源受限常开设备。

## 点评
把帧率推到 4 ms 并配套对齐训练，切中唤醒/端点场景。与商用/开源基线比边界质量比单纯帧分类更有意义。极端噪声与远场会议是否仍稳，正文侧重增强 TIMIT 类设置。
