# Enroll-on-Wakeup: A First Comparative Study of Target Speech Extraction for Seamless Interaction in Real Noisy Human-Machine Dialogue Scenarios

- 论文编号：259
- 报告人：Yiming Yang
- 程序：Tuesday 29 September 2026 / Target Speaker Extraction, Speech Separation and Audio Understanding
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yang26b_interspeech.pdf

## 问题
传统 TSE 依赖预录高质量 enrollment，打断自发人机对话；希望仅用唤醒词片段做“Enroll-on-Wakeup”（EoW），但约 1 s、含噪声与干扰的参考线索稀缺且被污染，现有模型在真实场景下的表现与 ASR 友好性尚缺系统评估。

## 方法
定义 EoW-TSE：KWS 切出 xwake 与后续 xquery，以 xwake 为条件抽取目标。评测四类模型——判别式 SEF-PNet、LExt、CIE-mDPTNet 与生成式 SoloSpeech；判别式在 Libri2Mix train-100（mix both）训练，SoloSpeech 用作者预训练。针对短噪 enrollment，用 IndexTTS2、xTTS、CosyVoice3 做 Clean Re-synthesis（CR）与 Extended Concatenation（EC）增强。测试为 Unisound 五场景真实录音（Close/Far Noise±Reverb，SNR 10/5 dB，中文唤醒词“Hi, Pandora/Hello, Cube”），指标含 SI-SDR、PESQ、STOI、DNSMOS、WER（Fun-ASR）。

## 实验与结果
Libri2Mix 2spk+noise 上 SoloSpeech SI-SDR 11.12、LExt 10.47 等，建立基线。EoW 五场景：SoloSpeech OVRL 最高，但远场/混响下 WER 急剧恶化；CIE-mDPTNet WER 最稳，然各模型均未优于直接对噪声混合物做 ASR。TTS 增强中 IndexTTS2 更常降低 enrollment 侧 WER；对 CIE-mDPTNet，CR/EC 提升 DNSMOS，却未能降低提取后 WER，EC 相对 CR 感知略好、识别相当。

## 结论
首次系统评估 EoW-TSE：生成式偏感知、判别式偏 ASR，整体存在感知–识别鸿沟；约 1 s 唤醒参考下模型远非理想，TTS 可减轻线索污染但无法自动修好可懂度与 ASR。

## 点评
问题设定贴近产品链路（唤醒即注册），价值在真实五场景对比与 TTS 增强诊断，而非提出新分离骨干。脆弱点在于线索极短且与查询同场景污染，以及生成式修谱易引入音素失真——后续更需 ASR-aware 目标或保留更多声学细节的约束，而不是只刷 DNSMOS。
