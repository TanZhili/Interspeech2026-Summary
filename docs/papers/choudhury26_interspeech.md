# Impact Analysis of Speech Representation Learning Models for Acoustic Side-Channel Attack

- 论文编号：3500
- 报告人：Orchid Chetia Phukan
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/choudhury26_interspeech.pdf

## 问题

键盘敲击声可被用于声学侧信道攻击（ASCA）推断按键，但公开评测多缺现代 VoIP 编解码失真，也少系统检验语音预训练模型（PTM）表征是否适应该任务。作者要在跨键盘与 Zoom/Teams 等传输条件下量化 PTM 表现，并改进下游适配。

## 方法

发布 KEYAC：37 键盘、37440 次敲击，均分笔记本麦、手机近场与实时 VoIP 流三通道。冻结骨干提取表征：Wav2Vec2、HuBERT、WavLM、XLS-R、X-Vectors、Whisper 编码器。下游对比 FCN、CNN 与 Kolmogorov–Arnold Network（KAN，单隐层 30 单元、样条适配）。协议含 5 折域内，以及标准录音键盘留出、VoIP 下键盘留出、仅编解码迁移（标准训 / VoIP 测）。

## 实验与结果

基线中 WavLM+CNN 最强：标准域内 Acc/mF1 约 58.34/56.92，VoIP 与编解码设定明显下降。KAN 全面抬升：WavLM+KAN 标准域内 68.47/67.12，键盘 OOD 61.73/60.34；VoIP 键盘泛化 57.82/56.41；编解码泛化 58.36/57.04。其他 PTM 在 KAN 下亦系统性优于 FCN/CNN，但绝对水平仍受未见键盘与压缩伪影制约。

## 结论

语音 PTM 可为 ASCA 提供有用特征，但在 VoIP 与未见键盘上用常规下游会明显退化；KAN 适配通过显式非线性交互建模持续改进鲁棒性，WavLM 表征整体最稳。数据集按请求向研究用途开放。

## 点评

工作价值在基准化：把 ASCA 从手搓特征小实验推进到 PTM + 多通道编解码评测。KAN 提升说明瓶颈常在适配层而非再换更大 SSL。安全含义上强调现实威胁面；脆弱点是按键分类准确率仍远非“可稳定还原密码”水平，且数据集非完全公开、场景偏受控采集。
