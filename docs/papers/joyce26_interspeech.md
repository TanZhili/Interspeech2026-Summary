# Demonstration of Embedded Systems for Clinical Speech Analysis

- 论文编号：3592
- 报告人：Jeremiah B Joyce
- 程序：Wednesday 30 September 2026 / Speech and Language Processing for Health and Accessibility
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/joyce26_interspeech.pdf

## 问题
精神/神经科临床语音分析常依赖需上传云端或专用 GPU 的流水线，延迟与 IT/隐私障碍限制床旁决策采用。

## 方法
在 NVIDIA Jetson AGX Orin（ARM CPU + Ampere GPU，约 60 W）上本地跑端到端临床会话分析：pyannote VAD/日志、角色分配、WhisperX ASR、强制对齐、音节核检测、情绪识别等；麦克风采集，显示器展示语速、轮次、词级时间戳与频谱，可用 ELAN 人工校正后重算。演示床旁即时处理。

## 实验与结果
正文为演示与系统能力说明，称可快于实时本地处理；未报告大规模临床准确率新实验（方法细节指向既有工作）。作者称据其知是首次用嵌入式设备做临床语音分析演示。

## 结论
边缘嵌入式可集成采集–计算–显示，降低延迟与数据外传，适合 IT 薄弱门诊与低资源场景；硬件进步使变压器级模型可近实时落地。

## 点评
把“能跑起来的床旁流水线”本身作为贡献，切中临床采用瓶颈。强在隐私与离线；弱在无新的临床效度数字、单设备功耗与噪声环境鲁棒性仍需现场验证。
