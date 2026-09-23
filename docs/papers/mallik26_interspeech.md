# MAC-VAD: A Modality-Aligned Cross-Attentive Framework for Robust Voice Activity Detection

- 论文编号：384
- 报告人：Bruhanth Mallik
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mallik26_interspeech.pdf

## 问题
纯音频 VAD 在噪声、混响、重叠下脆弱；音视频融合易模态坍塌，且缺少面向多模态 VAD 的大规模野外基准。

## 方法
MAC-VAD：WavelNet（可学习小波滤波）音频编码 + BiLSTM；EfficientViT（CasiaWebface/CelebA 预训练）视觉编码 + VTN；Dynamic Audio-Visual Cross Attention（对称交叉注意 + 温度门控 + 残差）。冻结 Wav2Vec 2.0 教师经适配器蒸馏；总损失含融合/单模态 CE、蒸馏 MSE、交叉注意同步 MSE。由 AVA-Speech 整理为 MMVAD（Speech vs Non-Speech + 人脸裁剪）。

## 实验与结果
WavelNet+Eff-ViT+Distil：Acc 93.52%、F1 86.39%，优于无蒸馏与单模态。DAVCA 融合 F1 高于拼接/相加/双线性/普通交叉注意。Wav2Vec 2.0 教师优于 HuBERT/xLSR/WavLM。相对 TS-TalkNet、ACLNet、LightASD、Pyannote，AUROC 97.85% 最高。MUSAN 噪声 0–15 dB 下 Acc 仍约 92%。模型 21.4M，GPU 约 21.9 ms/帧。

## 结论
模态对齐交叉注意加自监督蒸馏可显著提升野外多模态 VAD，并在噪声下保持稳健，超过代表性主动说话人检测与音频 VAD 基线。

## 点评
视觉单模态已强于音频，融合+蒸馏主要补齐召回与噪声鲁棒；DAVCA 门控针对模态失效是合理设计。MMVAD 由电影标注重标，与通用 VAD 边界定义不完全等同，跨域部署需再测。
