# MultiAPI Spoof: A Multi-API Dataset and Local-Attention Network for Speech Anti-spoofing Detection

- 论文编号：1187
- 报告人：Xueping Zhang
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26p_interspeech.pdf

## 问题

既有反欺骗基准多依赖少数公开 TTS/VC，与工业闭源 API 生态差距大，模型在真实 API 假音上是否可靠未知。同时需要更细粒度的“假音来自哪个 API”溯源能力。

## 方法

构建 MultiAPI Spoof：约 230 小时英语假音 + 等量 CommonVoice 真音，来自 30 个 API（商业 TTS、开源模型、网页 TTS），标签 A0–A29。A0–A20 内 70/10/20 划分，A21–A23 仅开发、A24–A29 仅评测未见。提出 Nes2Net-LA：在 Nes2Net 嵌套块间加滑窗局部自注意（窗口半径 K=1），增强块间局部上下文。骨干统一 XLSR-300M；另设 API tracing：对 21 个 seen API 分类，低置信度判为 unseen。训练不加增强，4 秒切段。

## 实验与结果

不加 MultiAPI 训练时，模型在 MultiAPI 测试上 EER 较高（如 XLSR+AASIST overall 7.30%）；加入训练后降至 0.70%，未见子集亦改善，且 ITW、AI4T 同步受益。Nes2Net-LA 在 Data Collection 2 上 ITW EER 1.42%、AI4T 5.64%，优于同设置 Nes2Net/AASIST。Scoreq 分布显示该集质量跨度更广。API tracing：seen F1 约 0.936，unseen 召回偏低（eval F1 0.678）；t-SNE 显示未见 API 嵌入与 seen 混叠。

## 结论

多 API 数据可缩小研究基准与真实合成生态差距，并提升跨域检测；局部注意进一步增强细粒度伪造线索。API 溯源对未见源仍难，需更强不变表征。代码与数据已发布。

## 点评

同时做“检测数据补洞”和“溯源新任务”，贴近实战取证需求。质量分布更广的假音有助于解释跨域增益。脆弱点是仅英语、未见溯源召回弱，说明当前仍偏 API 特异声学指纹而非深层生成机制不变式。
