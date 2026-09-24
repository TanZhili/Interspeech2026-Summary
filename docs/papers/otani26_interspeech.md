# Speaker-Independent Speech Synthesis from Real-time MRI Articulatory Data

- 论文编号：3379
- 报告人：Yuto Otani
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/otani26_interspeech.pdf

## 问题
rtMRI 语音合成多依赖说话人相关模型，未见说话人难以合成；TTS 式管线虽可泛化，但时长/韵律/音色不直接来自 rtMRI。

## 方法
EfficientNetV2-B0 抽帧特征 + E-Branchformer 时序建模，经 FiLM 注入说话人信息后回归 mel，BigVGAN-v2 声码。训练双路径：音频 X-vector 与 MRI 注意力池化说话人表征共享 FiLM；MRI 侧用 stop-grad 余弦损失对齐音频侧。另加 log-F0 Pearson 相关损失（高周期帧）以学习跨说话人相对韵律。推理仅用 rtMRI，无需参考语音。

## 实验与结果
USC 75-Speaker Speech MRI，质控后 51 人（训/验/测 43/4/4）。rtMRI 路径 dWER/dCER 与 audio 路径接近（如 sub20 8.2/3.5）；朗读最好（dWER 约 4.5–11.1%），自发与 nonce 更高。F0 相关约 0.38–0.57（高周期帧 0.62–0.76）；SECS 0.95–0.96，但同性别区分弱。

## 结论
跨模态说话人对齐可实现未见说话人的 rtMRI→语音；相对韵律可捕，绝对 F0 与同性别区分受限于中矢面分辨率与声门不可见。

## 点评
把「说话人信息必须来自 MRI」做成可训练对齐，比接 TTS 更忠实发音信号。同性别 SECS 对角塌缩说明身份仍偏粗；朗读–自发差距也提示自然会话仍是瓶颈。
