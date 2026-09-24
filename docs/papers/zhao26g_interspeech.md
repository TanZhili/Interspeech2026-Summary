# MSpoofTTS: Multi-Resolution Spoof-Guided Inference for Discrete Speech Synthesis

- 论文编号：2159
- 报告人：Junchuan Zhao
- 程序：Thursday 1 October 2026 / Spoofing and Deepfake Detection 3
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/zhao26g_interspeech.pdf

## 问题
神经 codec 语言模型做离散语音合成时，自回归解码易积累 token 级不一致与分布漂移，产生听感伪迹；偏好优化/重训成本高，而常规解码约束多只针对重复等局部失败，缺少对 codec 序列真实性的显式评估与引导。

## 方法
MSpoofTTS 在固定 NeuTTS 参数下做训练无关推理：先训多分辨率离散 token 伪造检测器——对 codec 序列做长度 L∈{10,25,50} 裁剪及 skip-sampling（r∈{1,2,5}），各用独立 Conformer+分类头区分真实/合成 token 段；再提出 Entropy-Aware Sampling（EAS，逆秩加权+时间衰减记忆缓冲）与分层伪造引导采样：warmup 后对多候选逐步用 M10→M25 剪枝，最后用 M50 及其采样变体加权重排选续写。不改动基座 AR 模型。

## 实验与结果
检测器在 LibriTTS 上用真实与 NeuCodec 合成配对训练；合成评测在 LibriSpeech/LibriTTS 与舌头绕口令 TwistList。HierEAS（MSpoofTTS）在多数客观指标上最优或次优：如 LibriSpeech WER 0.0532、NISQA 4.602、MOSNET 4.4158（Original 分别为 0.0694/4.462/4.3418）。TwistList 上感知质量最好而 WER 未必最低。主观 MOS-N/MOS-Q 显示分层伪造引导优于非分层对照，说话人相似度保持良好。

## 结论
多分辨率 token 伪造分数用于剪枝与重排，可在不重训 codec LM 的前提下提升感知质量与解码鲁棒性。

## 点评
把反欺骗从“事后分类”接到“解码时约束”，且工作在离散 token 而非波形上，思路新颖实用。收益主要在 NISQA/MOS 等感知侧，WER/SIM 提升有限；检测器与 tokenizer/TTS 绑定，换 codec 或生成器时需重训引导器，分层 beam 也会增加推理开销。
