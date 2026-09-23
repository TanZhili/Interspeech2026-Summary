# Speech Recognition, Enhancement and Real-Time Systems

- 日期：2026年10月1日（星期四）
- 时间：09:00-11:00
- 形式：Show And Tell
- Area：展示与演示
- 论文数：4
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场 Show and Tell 面向可落地的实时通信与联络中心：连续说话人验证防冒用、边缘时域神经 AGC、手机端十亿级模型编排的实时转写+日志+自定义词表，以及人在回路多代理实体抽取把坐席修正回流 ASR。共性是低 RTF/低算力、跨设备与无需声学重训的反馈闭环。

安全与前端侧强调通话全程比对声纹并告警，以及内容感知增益映射替代规则 AGC。识别侧则把前沿精度搬到移动端，并与上下文偏置、流式日志研究结合。联络中心用 UI 确认实体驱动上下文偏置条目或后 ASR 替换规则，缩小与“提前给出实体表”的 oracle 差距。

## 技术内容

### 实时验证、边缘 AGC 与移动端前沿识别

**A light weight Continuous Speaker Verification System for Real time Monitoring**（论文 3584；Harish Rajamani）  
两阶段 ReDimNet-B1 + 三元组投影网络持续比对注册声纹，跨语/噪声/混响增强；RTF 0.05、318M MACs，TidyVoice EER 2.08%，不匹配时向坐席界面告警以防敏感信息泄露。

**WaveNorm: A Low-Complexity Time-Domain Neural Adaptive Gain Control for Real-Time Speech Applications**（论文 3588；Harish Rajamani）  
时域内容感知、电平不变增益映射，避免固定参数与手工包络跟踪；动态范围至约 −70 dB，响度符合 ITU-T P.56/P.79，约 6 dB 降噪，49M MACs、55 KB，适边缘实时。

**Argmax Pro: Frontier-level Real-time Speech-to-text with Speakers and Custom Vocabulary on Mobile Devices**（论文 3602；Atila Orhon）  
统一实时推理编排三个十亿级 Transformer，做转写、说话人日志与自定义词表；优化 iOS/Android，减少与其他应用争用并控制耗电散热，目标对标云端功能丰富识别；基于上下文偏置与流式日志相关研究。

### 人在回路实体纠错

**A Human-in-the-Loop Multi-Agent Companion for Real-Time Entity Extraction and SLU-Driven ASR Error Correction**（论文 3610；Shiva Shankar Arumugam）  
MACE 实时伴侣叠加提取命名实体供坐席确认，修正回流为上下文偏置条目 B 或复发后的后 ASR 替换规则 R，无需声学重训与先验实体表。ContextASR-Bench + Whisper-large-v3 上 NE-WER 降 17.1%、EditRate 降 18.6%，弥合与 oracle 实体表差距的 23.6%。

## 本场要点

- 轻量连续说话人验证可在通话中实时防冒用。
- 神经时域 AGC 以极低算力满足响度标准与噪声稳健。
- 移动端可编排多十亿级模型做转写、日志与自定义词表。
- 坐席确认实体可闭环驱动偏置/替换规则，无需重训声学模型。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 3584 | A light weight Continuous Speaker Verification System for Real time Monitoring |
| 3588 | WaveNorm: A Low-Complexity Time-Domain Neural Adaptive Gain Control for Real-Time Speech Applications |
| 3602 | Argmax Pro: Frontier-level Real-time Speech-to-text with Speakers and Custom Vocabulary on Mobile Devices |
| 3610 | A Human-in-the-Loop Multi-Agent Companion for Real-Time Entity Extraction and SLU-Driven ASR Error Correction |
