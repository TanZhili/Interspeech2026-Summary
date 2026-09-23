# FreqGuard: Leveraging Frequency-Domain Feature Priors for Universal Proactive Voice Defense

- 论文编号：2069
- 报告人：Yankai Wang
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/wang26ca_interspeech.pdf

## 问题

语音克隆 TTS/VC 威胁隐私，被动检测滞后。主动防御在发布前向语音嵌入不可感知扰动以破坏说话人嵌入建模，但多数方法从随机噪声出发、主要优化嵌入空间位移，跨模型泛化弱，且易被扩散净化或频域恢复削弱。需要更结构化、可迁移的频域先验引导扰动。

## 方法

FreqGuard：先在 LibriSpeech 子集上系统评估下采样、量化、频带掩蔽、编解码、混响、噪声等操作对 SRS/PESQ/STOI 的影响，构建约 2.4 万条引导样本（平衡/强破坏/参考三类）。PriorNet 以干净—引导对学习重建幅相谱，联合时域、幅度、相位、对数谱、SSIM 与说话人余弦等多损失。GradPert 在幅度谱上生成有界对抗扰动（基于可反传幅度输入的 ASV）。保护语音由扰动幅度 + PriorNet 相位经 ISTFT 得到。评测 LJSpeech、VCTK、AIShell3，对抗 YourTTS、StyleTTS2、XTTS-v2、CosyVoice 等黑盒合成，并测跨 ASV 与 De-AntiFake 净化。

## 实验与结果

相对 Attack-VC、E2E、PoP、Enkidu，FreqGuard 在质量与跨 TTS 防御间更均衡：如 VCTK 上对多系统 ASR 更低（文中多处显著低于对比法的高 ASR），大模型如 CosyVoice 上最大 ASR 约 27.50%（对比有方法近 100%）。跨 ASV（ERes2NetV2、CAM++、ECAPA 等）表现较稳。净化后仍保持相对优势（如 LJSpeech 净化后 ASR 5%、VCTK 31.75%）。PESQ/STOI 总体优于偏重强扰动却伤可懂度的方法。

## 结论

频域操作先验引导的主动防御可在保持语音质量同时抑制克隆说话人相似度，并改善跨模型与净化场景下的鲁棒性。联合多损失与 GradPert 是实现质量—防护折中的关键。

## 点评

相对“嵌入空间乱推”，先用可解释频域操作建知识库再训练 PriorNet，更对准说话人身份的频谱统计结构，也解释了为何对部分净化更稳。工程上适合作为发布前保护流水线。脆弱点：引导集与 ASV 代理选择仍可能偏置；对最强商用合成 ASR 未归零；净化同源数据时防御仍会被削弱，说明主动防御与净化仍是军备竞赛。
