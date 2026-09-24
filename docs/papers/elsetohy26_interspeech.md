# ArFake: A Robust Framework for Multi-Dialect Arabic Speech Spoofing Detection Benchmark

- 论文编号：2665
- 报告人：Mohamed Elsetohy
- 程序：Thursday 1 October 2026 / Spoofing and Deepfake Detection 3
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/elsetohy26_interspeech.pdf

## 问题
英语等资源丰富语言已有 ASVspoof 等反欺骗基准，阿拉伯语尤其是方言覆盖不足；低资源、形态复杂与非标准正字法使合成与检测都更难，方言社区面临合成语音滥用风险却缺乏系统评测资源。

## 方法
ARFAKE 五阶段流水线：（1）基于 Casablanca 八方言语料，用 XTTS-v2、FishSpeech、ArTST、VITS 生成伪造语音；（2）用分类器可分性、Whisper-Large WER、12 名母语者 MOS 评估可懂度/真实感；（3）混合真实与 FishSpeech/XTTS/ArTST 伪造构建约 54k 条语料（VITS 留作未见生成器），训练/测集约 31k/23k；（4）在 HuBERT、Whisper、wav2vec2 嵌入上接两层前馈分类头，并设 MFCC-SVM 等传统基线；（5）In-domain、Leave-One-Generator-Out（LOGO，留出 VITS）、Leave-One-Dialect-Out（LODO）协议评测鲁棒性。

## 实验与结果
单生成器上 FishSpeech 最难（Whisper-large EER 6.92%），ArTST/VITS 近乎完美可分；MOS 与难度一致（FishSpeech 均值 3.72，VITS 1.70）。组合测试集 Whisper-large EER 4.88%、ACC 96.86%；未见 VITS 上 Whisper-small ACC 98.30%。LODO：摩洛哥方言最高约 93.51%，巴勒斯坦最低约 88.45%。摘要称域内与 LOGO 分别约 96%/97%。

## 结论
作者认为 ARFAKE 是首个面向多方言阿拉伯语伪造语音生成与检测的端到端基准，为跨生成器/方言鲁棒评测提供可复现路径。

## 点评
贡献主要在资源与协议：把方言偏移、生成器偏移纳入同一流水线，并用 MOS/WER 解释“近完美 EER”可能只是低质量伪迹。检测侧偏嵌入+浅分类头，未见更强图网络反欺骗骨干；近完美可分的生成器会抬高表观鲁棒性，解读 LOGO/LODO 数字时需对照各 TTS 真实感。
