# Spoofing, Deepfake Detection and Watermarking

- **日期**：Tuesday 29 September 2026
- **时间**：16:30-18:30
- **形式**：Long Oral（跨领域长文口头）
- **Area**：程序标注为 Cross-area long papers（本场 JSON 中 area 字段为空）
- **论文数**：6
- **材料说明**：依据官方程序与 ISCA 归档中的题名、作者、报告人、时段与摘要整理；未补充摘要未给出的指标、数据或机制。来源：[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)、[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)。

## 技术趋势

本场覆盖音频水印攻防、歌声/语音深度伪造检测、部分伪造定位、合成语音溯源与大规模检测工具链。水印侧一方面暴露现有方案对自适应攻击的脆弱性，另一方面提出面向神经编解码压缩的潜空间零比特水印，强调在编解码不变潜空间中嵌入方向性偏移。

检测侧从“全段真假”走向高分辨率歌声伪迹、部分篡改的转移方向建模，以及无需训练的残差统计指纹归因。工程化方面出现统一可扩展的深度伪造检测工具包，并揭示前端特征提取器与训练数据偏置对跨域泛化与公平性的支配作用。

攻防与评测闭环更明显：攻击要绕过基于消息概率分布的检测器，防御要面对神经压缩与野外条件；归因与定位则把“谁生成的/哪一段被改”作为可部署能力。

## 技术内容

### 水印：自适应攻击与神经编解码鲁棒嵌入

**Learning to Evade: Adaptive Attacks on Audio Watermarking**（论文 814；Qiben Yan）  
生成音频加剧版权关切，但现有水印易受对抗攻击；解码消息概率近似正态，被防御用于检测篡改。提出自适应攻击 AWM：两阶段优化先保证攻击成功再提升音质，并从有限目标音频样本估计正态参数，自适应把解码概率推回估计范围以规避检测。在两种水印、三套语音数据上评估，摘要称高成功率且检测率在替换/创建上低于 10%、移除上为 0%。

**Latent-Mark: An Audio Watermark Robust to Neural Codec Compression**（论文 1979；Yen-Shan Chen）  
既有水印对传统 DSP 攻击较鲁棒，但对神经压缩脆弱，因神经编解码充当噪声滤波器并丢弃不可感知波形起伏。Latent-Mark 为零比特水印框架：在编解码不变潜空间嵌入可检测方向偏移，并约束扰动贴近自然音频流形；引入跨编解码优化，在多代理编解码上联合优化以瞄准共享潜不变式。摘要称对未见神经编解码有稳健零样本迁移，并对传统 DSP 攻击保持竞争力，同时维持感知不可察觉性。

### 高分辨率与部分伪造：检测与定位

**Joint Fullband-Subband Modeling for High-Resolution SingFake Detection**（论文 1614；Chia-Yu Hu）  
歌声合成带来未授权模仿风险；相对语音，歌声音高、动态与音色更复杂，16 kHz 检测器会丢失高频信息。首次系统分析 44.1 kHz 高分辨率音频用于 SingFake/SVDD，提出全频带—子带联合建模：全频带抓全局语境，子带专家隔离频谱上不均匀分布的合成伪迹。在 WildSVDD 上摘要称高频子带提供必要互补线索，框架显著优于 16 kHz 采样模型。

**Temporal Transition-Aware Multi-Head Modeling for Partially Spoofed Audio Detection and Localization**（论文 474；Yunsu Kim）  
部分伪造定位旨在检出话语中的短篡改片段；既有工作多做帧级真假或边界检测，忽略邻帧如何跨篡改演化。提出转移感知框架，分类 Real→Fake 与 Fake→Real；多尺度 GRU 捕捉局部连续与长程流动，多头目标含帧真实性头、邻帧转移头与融合精炼头。在 PartialSpoof 与 PartialEdit-E1/E2 上摘要称达 SOTA，并强调 20 ms 分辨率下时序顺序建模的有效性。

### 残差指纹归因与统一检测工具

**Lightweight Detection and Model Attribution of Synthetic Speech via Residual Statistical Fingerprints**（论文 1361；Matías Pizarro）  
提出轻量、免训练的合成语音检测与源模型归因：以音频与其滤波版本之差的平均作为残差指纹；用给定音频残差到模型指纹的马氏距离识别源模型并区分真假。摘要称跨多种合成系统与语言，在开放世界单模型归因、封闭世界多模型归因、真假分类与域外检测四项任务上表现突出。

**DeepFense: A Unified, Modular, and Extensible Framework for Robust Audio Deepfake Detection**（论文 1366；Yassine El Kheir）  
领域缺标准化实现与评测协议，限制复现与比较。DeepFense 为开源 PyTorch 工具包，整合最新架构、损失与增强管线及逾 100 条 recipe；用其对 400 余模型大规模评估。摘要称精选训练数据可改善跨域泛化，但预训练前端特征提取器主导整体性能方差；高性能模型在音质、说话人性别与语言上存在严重偏置，工具包旨在支持更公平的数据选择与前端微调。

## 本场要点

- 自适应水印攻击可利用解码概率分布估计规避检测，暴露现有防御脆弱性。
- 对抗神经编解码需把水印嵌入编解码不变潜空间，并做跨编解码联合优化。
- 歌声深伪检测受益于高采样率与全频带—子带联合建模。
- 部分伪造定位强调 Real/Fake 转移方向与多头时序建模。
- 残差统计指纹可免训练完成检测与源模型归因。
- 统一工具链评估显示前端提取器与数据偏置强烈影响泛化与公平性。

## 覆盖核对

| id | title |
|---|---|
| 814 | Learning to Evade: Adaptive Attacks on Audio Watermarking |
| 1614 | Joint Fullband-Subband Modeling for High-Resolution SingFake Detection |
| 1979 | Latent-Mark: An Audio Watermark Robust to Neural Codec Compression |
| 474 | Temporal Transition-Aware Multi-Head Modeling for Partially Spoofed Audio Detection and Localization |
| 1361 | Lightweight Detection and Model Attribution of Synthetic Speech via Residual Statistical Fingerprints |
| 1366 | DeepFense: A Unified, Modular, and Extensible Framework for Robust Audio Deepfake Detection |
