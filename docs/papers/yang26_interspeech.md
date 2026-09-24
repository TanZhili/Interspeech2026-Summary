# Multi-Channel Differential ASR for Robust Wearer Speech Recognition on Smart Glasses

- 论文编号：127
- 报告人：Yiteng Huang
- 程序：Wednesday 30 September 2026 / Robust and Real-World ASR Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/yang26_interspeech.pdf

## 问题
智能眼镜佩戴者语音识别（WSR）在开放场易受旁人 side-talk 干扰；仅靠波束成形难完全抑制，且增强/分离/抽取前端常引入不可接受延迟或隐私敏感说话人建模。

## 方法
多通道 differential ASR：并行融合互补前端——朝向嘴部的 MVDR 波束成形、最低延迟的麦克风选择（高 SNR 通道）、轻量流式 side-talk detection（区分佩戴者/旁人、不建模身份）。不同帧率前端嵌入对齐后送入低延迟流式 RNN-T。在 Ray-Ban Meta 实测 RIR 模拟与 HATS 实采数据上评测。

## 实验与结果
模拟与真实 LibriSpeech 多通道集：相对仅波束成形基线，组合系统一致更优；真实噪声侧谈上相对 WERR 最高约 18.0%（平均约 14.4%）。实采覆盖 72 个旁人位置（角度/高度/距离）；50% 重叠时角度依赖性更明显。干净条件亦保持竞争力。

## 结论
多前端差分输入能量著提升眼镜 WSR 对 side-talk 的鲁棒性，且兼顾流式延迟与隐私约束。

## 点评
问题定义贴产品：延迟与隐私排除重前端，改用轻量互补线索喂 ASR。实采角度网格使评测可信。仍偏 LibriSpeech 读音；极强旁人主导或多人侧谈场景未充分覆盖。
