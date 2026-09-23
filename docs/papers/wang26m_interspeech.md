# Position-Aware Target Speaker Extraction for Long-Form Multi-Party Conversations: A Diarization-Free Framework for ASR

- 论文编号：787
- 报告人：Yichi Wang
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26m_interspeech.pdf

## 问题
长时多方会话说话人活动极不均衡且重叠多；滑窗 CSS 有跨窗身份不一致与串扰，常需额外 diarization；基于注册嵌入的 TSE 又可遇不可得或不稳。

## 方法
PATSE：以目标 DOA 为先验。TIGER 骨干 + TAC 多通道融合；空间编码器由麦克风对 IPD 与 DOA 理论相位差构造 PSF，自注意细化后经 FiLM 调制分离特征。活动感知损失：静音区残差能量 + 有声区 SNR。每目标独立抽取后 VAD 切句送 Whisper Large-v3，无需显式 diarization。发布真实房间回放数据集 LibriReplay-DOA。

## 实验与结果
LibriReplay-DOA（约 7 h，15°–120°、多种重叠比）：PATSE PT+FT 总体 WER 14.0%，优于 CSS(TIGER) oracle 分配（32.8%）与 Sortformer+GSS（38.4%）等。真实三方 TEIDAN：WER 20.50%、DER 13.83%，均优于 DSB/FastMNMF/CSS/GSS 管线。

## 结论
会议场景说话人方位相对稳定时，DOA 条件 TSE 可直接产出说话人归因流并简化下游 ASR，无需 diarization；在真实与回放数据上均优于 CSS 与级联基线。

## 点评
抓住 CSS“跨窗置换+串扰”与 diarization 边界不可靠的耦合痛点，用稳定空间先验换身份一致性，工程路径清晰。依赖 DOA 可得与说话人基本静止；极近角与极高重叠仍难，真实移动场景需另验。
