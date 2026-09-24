# RT-ASDNet: Unified, Real-Time Active Speaker Detection

- 论文编号：448
- 报告人：Okan Köpüklü
- 程序：Wednesday 30 September 2026 / Speaker Diarization 1
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kopuklu26_interspeech.pdf

## 问题
现有音视频主动说话人检测多为多阶段：外部门脸检测 → 每人提特征 → 分类，计算随人数线性增长，难实时，且无法端到端。需单次前向、与人数无关的统一检测。

## 方法
RT-ASDNet：音频流 SincDSNet（原始波形 sinc 卷积 + DSConv）；视频流 3D-CNN + FPN/MSF（可变形卷积融合多尺度），在滑窗关键帧（最后一帧）上做无锚框检测。音频嵌入空间广播后与视觉特征拼接；CenterNet 式热图（说/不说两类）+ 尺寸 + 偏移头。端到端训练于 AVA-ActiveSpeaker；损失 focal + L1。

## 实验与结果
验证集 IoU≥0.5 mAP：3D-ResNet-18 在 16 帧 288² 达 75.8，RTF 0.009（RTX 6000）；轻量 MobileNet/ShuffleNet mAP 75.3/70.9。32 帧约 77.3，64 帧 77.3 饱和；分辨率升至 352² 达 77.5。与 SOTA 离线/因果方法（mAP 90+，但用真值人脸只做分类）不可直接比；本文作为联合检测+分类的实时基线。人脸更大、人数更少时更好。

## 结论
首次将 ASD 做成单阶段联合人脸定位与说话分类，推理代价与场景人数无关，适合实时；精度与强离线分类器仍有差距，但协议更难。

## 点评
问题定义清楚：常数时间/帧比刷分类 mAP 更贴部署。与“给真值框再分类”的文献比分不公，作者已说明，作为新任务设定基线合理。分类仍受益于更长时上下文而定位不依赖，设计与损失分工一致。
