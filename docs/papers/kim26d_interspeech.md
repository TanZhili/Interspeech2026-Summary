# Privacy-Preserving Speaker Verification with Multi-Granularity Feature Obfuscation

- 论文编号：437
- 报告人：Hanseul Kim
- 程序：Wednesday 30 September 2026 / Speaker Privacy Preservation and Anonymization
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/kim26d_interspeech.pdf

## 问题
说话人验证若传输原始音频/高分辨谱，会泄漏对话内容并助长深度伪造；仅丢语义 token 或全局打乱（如 SafeEar）要么仍可被人听懂，要么破坏文本无关 SV 所需的全局时序。

## 方法
客户端用 FAcodec 解耦 content/prosody/timbre/acoustic detail，丢弃 Fcon；对 Fpro 做多粒度混淆：全局时序聚合（GTA）、局部块均值（LTA）、块内置换（LTP），三路拼接线性融合后与 Faco、Ftim 拼接，经 ECAPA-TDNN（AAM-Softmax）提嵌入。用混淆特征重建语音评 WER/CER/STOI。训练 VoxCeleb2-dev，评 VoxCeleb1-O/E/H；LibriSpeech test-clean 测语言隐私；块长默认 L=50。

## 实验与结果
FA+MG：Vox1-O EER 2.35%、WER 98.83%、CER 89.60%、STOI 0.341；相对 SafeEar+GS（EER 5.19%）相对改进约 54.7%。仅丢 content 已使 WER 达 95.56% 但听感仍可能可懂；GTA alone CER 最高但 EER 升至 2.98%；GTA+LTA+LTP 将 EER 拉回约 2.35% 且保持高 CER。块长敏感实验中 L=50 平衡最佳。

## 结论
显式解耦加层次混淆可在强语言隐私下保持可用 SV；作者认为适用于金融认证等需鉴权且忌内容泄漏的场景。补充音频用于支撑感知不可懂。

## 点评
明确区分 ASR 指标隐私与人类感知隐私，并设计“先砸时序再局部恢复说话人线索”的层次策略，比一刀切打乱更贴 SV。FAcodec 解耦质量是前提；STOI 中等并不等于听不懂，正文也承认需听感样本佐证。威胁面是传输混淆特征而非波形匿名化，应用边界应限定为鉴权特征通道。
