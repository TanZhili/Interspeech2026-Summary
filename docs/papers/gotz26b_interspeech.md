# Scalable Audio Scene Generation with the Treble SDK

- 论文编号：3609
- 报告人：Georg Götz
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gotz26b_interspeech.pdf

## 问题
真实共享空间录音难控、难扩展；仅有孤立 RIR 不足以支撑增强/分离等需要混音、目标轨、标签与背景噪声的任务。需要把声学仿真资产变成可复现、可规模化的完整场景数据集。

## 方法
Treble SDK Scene Generator：输入 RIR 集合、干净音频与场景/设备规则。场景以轻量 recipe 表示（轨道、源–IR 映射、听者配置、元数据、目标定义），卷积与混音仅按需渲染（lazy）。支持手工搭场景与规则驱动批量随机化（位置、说话人、重叠、电平、朝向、噪声等）。演示用 Jupyter：多说话人对话 + HVAC 噪声、时间线与 3D 房间视图、渲染混音/分轨/转录/JSON 元数据，再批量生成 SceneCollection。

## 实验与结果
演示系统描述，无独立下游 ASR/分离基准数字；强调 recipe 可序列化、共享、过滤与对齐监督信号。

## 结论
把物理接地仿真接到 ML 友好的场景配方与按需渲染，填补 RIR/干净音频与训练脚本之间的工程缺口，便于共享环境语音系统的数据生成与评估。

## 点评
贡献是工作流与数据工程抽象，而非新仿真算法。lazy recipe 对大规模数据集生成实用；可复现性依赖 SDK/仿真引擎与规则设计，本文未给出与真实录音下游性能的直接对比。
