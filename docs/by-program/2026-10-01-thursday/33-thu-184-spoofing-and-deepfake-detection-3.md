# Spoofing and Deepfake Detection 3

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：4
- 论文数：10
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。仅依据摘要陈述，不补写未出现的数字与细节。

## 技术趋势

本场反欺骗与深度伪造检测强调对 LLM 时代合成器的泛化、可微自适应增强、编解码器量化层级取证，以及可解释频带注意力。遗留基准与现代 TTS/VC 失配被反复指出；VoxENES 2026、ArFake 等新基准把多语、多方言与后处理条件纳入评测。

训练侧关注多增强梯度冲突（GradHarmony）与可微噪声参数（DAR-Boost）；系统侧有软门控分数融合服务欺骗感知说话人确认（SASV）。应用边界扩展到心音编解码伪造与深度伪造源验证中的说话人因素解耦；生成侧亦出现训练无关的伪造引导推理以提升离散合成真实感。

## 技术内容

### 增强、编解码器层级与现代基准

**DAR-Boost: A Differentiable and Adaptive Raw Data Augmentation Framework for Robust Anti-Spoofing**（论文 643；Yingdong Li）将卷积、脉冲与平稳噪声注入改为由轻量辅助网络预测参数的可微层，按输入波形自适应。语音域与 RawBoost 相当，环境声域更优，拓宽适用面。

**Quantizer-Aware Hierarchical Neural Codec Modeling for Speech Deepfake Detection**（论文 3212；Jinyang Wu）用可学习全局权重建模 RVQ 各量化层贡献，冻结语音编码器骨干、仅更新约 4.4% 额外参数。相对强基线，ASVspoof 2019/ASVspoof5 上相对 EER 降幅 46.2%/13.9%。

**VoxENES 2026: Benchmarking Generalization of Speech Spoofing Detectors Against LLM-Era TTS and Voice Conversion**（论文 2712；Aastha Sharma）发布英西双语、53,628 条、10 种当代合成方法与 10 种标准化后处理条件的基准。八个预训练检测器无微调评测：最佳整体 EER 28.98%，多数接近或低于随机，凸显对脆弱伪影的依赖。

### SASV 融合、稳定训练与跨域任务

**Soft-Gating Score-Level Fusion for Spoofing-Aware Speaker Verification**（论文 2294；Seongkyu Han）按置信度动态软门控融合 ASV 与对抗（CM）子系统分数，无需额外训练。两基准多配置下 a-DCF 相对改进最高约 90%，并分析最有效条件。

**GradHarmony: A Gradient Alignment and Magnitude Normalization Strategy for Audio Deepfake Detection**（论文 2216；Inho Kim）对干净与各类增强分别求梯度，以干净梯度为参考对齐冲突增强梯度，并用 EMA 统计自适应归一化幅度。多样模型上域外平均 EER 降约 22%。

**Towards Detecting Neural Audio Codec Synthesized Heart Sounds**（论文 2116；Orchid Chetia Phukan）提出 SHAC 任务与 CARDIOFAKE 数据集，基准 MFCC/LFCC 与 WavLM 等 SSL，并用 GROOT 融合频谱与 SSL；MFCC+WavLM 达所述 SOTA。

**Disentangling Speaker Traits for Deepfake Source Verification via Chebyshev Polynomial and Riemannian Metric Learning**（论文 36；Xi Xuan）提出 SDML：切比雪夫多项式损失稳定解耦优化，并将源/说话人嵌入投到双曲空间用黎曼度量降说话人信息。在 MLAAD 与四项新协议上验证有效。

**Interpretable Frequency-Band Attention with Gated SSL Fusion for Audio Deepfake Detection**（论文 2250；Abeer Alhammad）BandMIL 将窗切为八频带谱图，结合手工频带特征与 WavLM 门控融合，MIL 聚合到话语级。ASVspoof 2019 LA 上 EER 1.28%、min t-DCF 0.0331（SSL-only 为 1.73% EER）。

**ArFake: A Robust Framework for Multi-Dialect Arabic Speech Spoofing Detection Benchmark**（论文 2665；Mohamed Elsetohy）覆盖八方言的阿拉伯语欺骗生成与检测端到端框架，四 TTS 生成并以分类器、下游 ASR 与 MOS 评估质量；混合语料训练检测器，域内与 LOGO 达 96%/97%，并以 LODO 考察未见方言。

**MSpoofTTS: Multi-Resolution Spoof-Guided Inference for Discrete Speech Synthesis**（论文 2159；Junchuan Zhao）训练无关推理框架：多分辨率 token 欺骗检测在不同时间粒度找局部不自然模式，并层次剪枝与重排假设以提升零样本编解码合成稳健性。

## 本场要点

- LLM 时代合成器与后处理使遗留检测器泛化显著下降，需要新双语/多方言基准。
- 可微自适应增强与梯度和谐化提升多增强训练稳定性。
- 编解码器量化层级与频带 MIL 提供结构/频谱可解释取证线索。
- 软门控分数融合可即插即用地强化 SASV。
- 伪造检测边界扩展到心音与源生成器验证中的说话人解耦。
- 合成侧可用欺骗引导推理在不改参数下提升离散 TTS 真实感。

## 覆盖核对

| id | title |
|---|---|
| 643 | DAR-Boost: A Differentiable and Adaptive Raw Data Augmentation Framework for Robust Anti-Spoofing |
| 3212 | Quantizer-Aware Hierarchical Neural Codec Modeling for Speech Deepfake Detection |
| 2712 | VoxENES 2026: Benchmarking Generalization of Speech Spoofing Detectors Against LLM-Era TTS and Voice Conversion |
| 2294 | Soft-Gating Score-Level Fusion for Spoofing-Aware Speaker Verification |
| 2216 | GradHarmony: A Gradient Alignment and Magnitude Normalization Strategy for Audio Deepfake Detection |
| 2116 | Towards Detecting Neural Audio Codec Synthesized Heart Sounds |
| 36 | Disentangling Speaker Traits for Deepfake Source Verification via Chebyshev Polynomial and Riemannian Metric Learning |
| 2250 | Interpretable Frequency-Band Attention with Gated SSL Fusion for Audio Deepfake Detection |
| 2665 | ArFake: A Robust Framework for Multi-Dialect Arabic Speech Spoofing Detection Benchmark |
| 2159 | MSpoofTTS: Multi-Resolution Spoof-Guided Inference for Discrete Speech Synthesis |
