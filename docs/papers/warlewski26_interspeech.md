# Sub-Model Short-Term Memory Convolutions for Keyword Spotting Systems on Device

- 论文编号：1343
- 报告人：Szymon Klimaszewski
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/warlewski26_interspeech.pdf

## 问题
端侧 KWS 需在严格算力与内存下做高时间粒度在线推理；滑动窗 CNN 冗余计算多，原 STMC 为帧同步任务保留全部池化状态，对只需稀疏输出的分类任务存在状态冗余。

## 方法
提出 SM-STMC：将卷积骨干按池化/输出切成子模型，经内存缓冲连接；按调度式在时刻 t 只执行必要深度（池化 stride 带来的冗余状态被丢弃）。CNN 离线训练后 STMC/SM-STMC 仅作推理扩展，无额外参数；用独立子模型静态调度以兼容 TensorFlow Lite。输入 Mel 谱（窗 1024、hop 256），VGG 式嵌入 + MLP 分类器，约每 8 帧评一次分类器。

## 实验与结果
Google Speech Commands 11 类。标准 1 s 测试：SM-STMC1 recall/准确率约 93.8%，SM-STMC2 约 91.6%；两端补静音的 2 s 集上离线单窗 VGG 大幅掉点，8× 滑动窗与 SM-STMC1 达约 97.1%。ARM Cortex-M55（int8、TFLite Micro）：相对 8×/s 滑动窗，SM-STMC 总 MCPS 显著更低（如 VGG1 8× 59.36 vs SM-STMC1 11.37）；相对原 STMC 缓冲约减半至更少（如 STMC2 21632→SM-STMC2 7520）。摘要称相对等价频繁 CNN 与 vanilla STMC，MCPS 最高可降约 82% 与 46%。

## 结论
SM-STMC 在保持 CNN 识别性能的同时削减在线卷积冗余状态与算力，无需重训，适合穿戴等资源受限 KWS；分类频率降低会略增延迟，但仍在实时交互可接受范围。

## 点评
抓住 KWS“不必每帧出结果”与 STMC 帧同步设计的错位，用静态子模型调度换部署友好性。效果强依赖池化深度与评测频率；与 LSTM 比算力更省但延迟粒度更粗，边界对齐场景才显出相对离线窗的优势。
