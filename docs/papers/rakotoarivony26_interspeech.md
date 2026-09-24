# Evolution Strategy-Based Calibration for Low-Bit Quantization of Speech Models

- 论文编号：119
- 报告人：Lucas RAKOTOARIVONY
- 程序：Wednesday 30 September 2026 / Acoustic Signal Analysis and Generation
- 技术分类键：signal
- 全文：https://www.isca-archive.org/interspeech_2026/rakotoarivony26_interspeech.pdf

## 问题
语音模型激活动态范围极大，Max/Percentile 等标准校准易把多数值压进同一量化档，INT4 激活量化尤其崩溃；现有语音 PTQ 多只重量化或特定结构，缺少通用权重量化+激活整型推理流水线。

## 方法
提出 ESC：先按层用 MSE 最小化 FP32 与量化层输出误差初始化激活尺度，再用 CMA-ES 全局联合优化全部尺度，目标为任务级误差。对称均匀量化（α=−β）。在 Conformer、ECAPA、MP-SENet、FastSpeech 2、AST 上做全 INT8/INT4（权+激活），校准与进化各用 100 条训练样本；并可叠 Adaround、BRECQ、SmoothQuant 等 PTQ。

## 实验与结果
- INT8：ESC 接近或达到全精度（如 Conformer WER 16.01 vs 15.94），整体优于 Max/Percentile/Entropy/MSE。
- INT4：ESC 显著优于基线（如 Conformer WER 38.49 vs MSE 41.22）；AST 相对精度仅降约 1.75%。叠 HyQ 等可进一步改善（ECAPA 等场景相对 ESC 约 +27%）。
- TensorRT INT8 部署平均加速约 2.31×（1.34×–5.07×），显存明显下降。

## 结论
局部 MSE + 全局进化策略校准可在全 INT8 近无损，并在 INT4 配合 PTQ 时接近无损。语音激活量化是关键瓶颈；跨域 PTQ 迁移效果因模型而异，仍需语音专用方法。

## 点评
问题诊断清楚：音频激活“长尾”让视觉/NLP 校准失效。把不可微尺度搜索交给 CMA-ES，工程上务实。INT4 绝对指标仍远逊全精度（ASR WER 翻倍级），“近无损”主要指相对其他校准更好；真正部署价值更在 INT8。
