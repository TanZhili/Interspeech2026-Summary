# NaVo: Natural Voice Protection against Voice Cloning Attacks via Generative Universal Adversarial Audio

- 论文编号：2944
- 报告人：Seoyoung Park
- 程序：Wednesday 30 September 2026 / Speaker Privacy Preservation and Anonymization
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/park26g_interspeech.pdf

## 问题
主动防克隆常对每条语音迭代优化对抗扰动，易引入可听噪声且延迟高，难实时部署。

## 方法
NaVo 以 AudioLDM2 为骨干，对 UNet 交叉注意力 K/V 用 LoRA 按性别×环境类别（雨声、babble、办公室、音乐等）模块化微调；混合原语音与生成环境音（训练固定 SNR 17 dB）。目标用 α-散度（Bhattacharyya）把混合后说话人嵌入分布推到异性性别分布，而非单点 ℓ2；总损失 = 扩散损失 + 低噪声步上的分布目标损失。推理单次前向生成 UAA 再混合，说话人无关。评 DSR（相对 ECAPA/Resemblyzer/ResNet 等阈值）与 CLAP；对比 Enkidu；白盒 SV2TTS/CosyVoice，黑盒 Tortoise/ElevenLabs，并测 WaveGuard 等提纯攻击。

## 实验与结果
相对 Enkidu，DSR 显著更高（如 Resemblyzer 78.0% vs 25.2%）。白盒多风格 DSR 常达数十至 90%+；黑盒对 ElevenLabs 雨声风格可 >90%。摘要报告对商用系统黑盒约 76% DSR。自适应提纯后多数情形 DSR 仍 >80%。CLAP 与骨干默认生成相近。

## 结论
用自然环境音作通用对抗音频，经模块 LoRA 与分布目标可实现实时、可听自然且对未见说话人有效的主动防护。

## 点评
把“不可听噪声”换成“可听但语义合理的背景”，绕开了感知–强度权衡，并靠前向混合满足实时性。异性分布目标利用嵌入空间性别聚类，简单有效但也可能引入可察觉的性别偏移。依赖混合 SNR 与类别选择；对不接受背景音的使用场景适用性有限。
