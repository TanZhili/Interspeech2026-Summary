# Training-Free Intelligibility-Guided Observation Addition for Noisy ASR

- 论文编号：1096
- 报告人：Haoyang Li
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26s_interspeech.pdf

## 问题
噪声下 ASR 差，语音增强（SE）可抑噪但常引入损害识别的伪影。Observation Addition（OA）用权重融合噪声与增强语音、无需改 SE/ASR，但 \(S'\) 若只看噪声侧信号质量，或依赖需标注 WER/CER 训练的神经预测器，则复杂且难泛化。

## 方法
提出无训练的可懂度引导 OA：理想情形用噪声与增强的 WER 反比归一化定 \(S'\)；实际用后端 ASR 置信度近似，\(S'=\mathrm{conf}(y)/(\mathrm{conf}(y)+\mathrm{conf}(\hat{x}))\)，再按 \(\bar{x}=S'y+(1-S')\hat{x}\) 融合后解码。Whisper 用段级平均 log-prob 的 token 加权几何均值；Parakeet/Wav2Vec2-CTC 用 Tsallis 熵（\(q=0.33\)）导出 token 置信度再取几何均值。另比较硬切换（选置信更高者）与基于帧级置信的 OA。

## 实验与结果
SE：Demucs 与 GR-KAN MP-SENet（VoiceBank-DEMAND 训练）；ASR：Whisper-large、parakeet-tdt-0.6b-v2、wav2vec2-large-960h。评测 VoiceBank+DEMAND 与 CHiME-4（Simu/Real，SE 域外）。对比 SNR-OA、DNSMOS-OA、Classifier-OA（2/3 类）。WER-OA 整体最低；实用的 Conf-OA 在多数设置上优于既有 OA 基线（如 MP-SENet+CHiME-4 Real 上 Whisper/Parakeet/Wav2Vec2 为 5.86/5.55/24.03）。误校准子集上 Conf-OA 明显优于硬切换；帧级 OA 相对句级反而变差（如 Wav2Vec2+MP-SENet Real：24.03→25.30）。

## 结论
用后端 ASR 置信度做句级 OA 权重，可在不改动 SE/ASR、无需额外训练的前提下改善噪声 ASR，并优于多种已有 OA；句级融合优于硬切换与帧级融合。

## 点评
把“该信噪声还是增强”直接交给识别器自身置信度，避开了信号质量与 ASR 目标不一致、以及再训预测器的开销。当噪声与增强差距极大时，融合可能略逊于单用更强支路；帧级变差说明时间一致性对后端 ASR 很敏感，句级标量更稳妥。
