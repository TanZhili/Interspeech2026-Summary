# Lightweight Emotion Recognition with Disjoint Modality Fusion

- 论文编号：3593
- 报告人：Serkan Sulun
- 程序：Wednesday 30 September 2026 / Speech Analysis, Data Resources and Research Tools
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/sulun26_interspeech.pdf

## 问题
多模态语音情感识别常用大模型与重融合，部署成本高；真实场景中音频/文本可缺失或情绪线索冲突（如讽刺），需在轻量设定下同时支持单模态与融合预测。

## 方法
提出 Light-DMF：冻结 Distil-Whisper-large-v3 音频编码器与 MiniLM 文本编码器，用约 64k 可训参数做投影与注意力。四类 sentinel 标记模态有无；文本/音频自注意力各自出头，单向 audio→text 交叉注意力再与融合头拼接，输出 text/audio/fusion 三路预测。混合 IEMOCAP、MELD、CREMA-D、RAVDESS、TESS 与 GoEmotions，统一到 angry/excited/happy/neutral/sad；模态随机丢弃 0.1。推理复用 Whisper 一次前向得到特征与带时间戳转写，再按句并行分类。

## 实验与结果
正文未报告标准 SER 准确率表；强调可训参数 <65k，CPU（i7-5600U）上 1 分钟音频约 0.81 分钟处理（RTF<1）。提供 Colab demo 与开源代码。

## 结论
在极少可训参数与 CPU 实时下实现解耦单模态与融合情感预测，并可混训模态不全/冲突的数据，面向公众可用的轻量 SER 工具。

## 点评
“复用 ASR 内部特征 + 解耦头”对冲突线索与缺模态很务实，工程友好。作为 Show & Tell 向工作，缺系统对比与融合相对单模态的增益数字；情感标签粗映射也可能抹平细类差异。
