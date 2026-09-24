# SpeechBench: A Unified Speech Annotation and Analysis Tool

- 论文编号：3600
- 报告人：Zheng Nan
- 程序：Wednesday 30 September 2026 / Speech Analysis, Data Resources and Research Tools
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/nan26_interspeech.pdf

## 问题
通用语音模型预标注 + 人工精修可显著提效，但现有工具（Praat、Label Studio 等）或缺模型管线、或缺可视化串联、或强制上传公网，难满足领域数据与隐私需求。

## 方法
SpeechBench 采用 Docker 化前后端：Vue3 + WaveSurfer.js 浏览器前端；Python 后端集成 Parselmouth（类 Praat 分析）及 VAD、说话人分离、ASR、音素识别、强制对齐等预训练模块。用户在画布上拖拽模块组成有向预标注管线，输出直接映射为与波形/谱图对齐的 annotation tiers，再在工作区做人机精修与音高/共振峰/元音三角等分析。支持本地/私有服务器部署，含账号与项目管理。

## 实验与结果
本文为系统与演示描述：展示离线本地运行、会话语音预标注与 tier 编辑全流程；未报告独立定量用户实验。引用 AusKidTalk 等工作说明模型辅助标注可省时降本。

## 结论
在统一环境中接通“可视化多步预标注管线 + 交互精修 + 声学分析”，降低非技术用户门槛，并兼顾隐私敏感数据的本地部署。

## 点评
把管道编排与 tier 编辑做成一体，对准真实标注瓶颈。价值取决于内置模型质量与领域适配；正文未给出相对基线工具的效率对比数字。
