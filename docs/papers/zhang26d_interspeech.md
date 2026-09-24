# Dual-Encoder Fusion with Explicit and Implicit Injection for the Interspeech 2026 Audio Encoder Capability Challenge

- 论文编号：463
- 报告人：Ming Li
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26d_interspeech.pdf

## 问题
LALM 管线里单一音频编码器难以在分类与理解任务上全面最优；Whisper（弱监督转写）与 Dasheng（掩码声学建模）表征互补，但如何注入、保留非冗余信息并控制冗余，在 AECC 统一评测下缺乏系统研究。

## 方法
融合 Whisper-Base 与 Dasheng-Base，投影到 512 维后输出 \(Z\in\mathbb{R}^{T\times512}\)。比较 concat、MoE-concat/MoE-proj 与 token 级 softmax 门控残差融合；并加轻量 STFT 对数幅度残差支路（可学习 \(\gamma\)）。注入两种：(1) 隐式——LoRA 适配 Dasheng 后冻结双编码器，只训融合；(2) 显式——从 Whisper 线性预测 Dasheng 得残差 \(R_d=H_d-\hat H_d\)，再门控融合，并加残差能量与交叉协方差去相关正则。训练跟 XARES-LLM 官方 “all” 配方。

## 实验与结果
softmax 门控 + STFT 相对 MoE 更稳：Track A overall 0.701、Track B 0.442。隐式注入 Track A 最高（0.712±0.001），在 CREMA-D、ESC-50、GTZAN 等声学分类上更强；显式注入更多子任务最佳、Track B 略优（0.446±0.002）。MoE 可在个别任务冲高但不抬总体分。

## 结论
token 级 softmax 门控残差 + STFT 支路是稳定骨干；显式残差注入任务互补更强、可扩展多编码器，隐式 LoRA 适配整体更稳健。

## 点评
在挑战统一接口下把“怎么融”和“怎么注”拆开消融，结论可操作。未改数据采样比，部分说话人/指令类任务仍可能被融合冲淡；显式残差目前线性预测偏简，作者也提示可换更强残差预测器。
