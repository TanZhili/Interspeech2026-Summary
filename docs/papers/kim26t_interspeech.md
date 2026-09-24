# Fast Speech Foundation Model Distillation Using Interleaved Stacking

- 论文编号：3071
- 报告人：Eungbeom Kim
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/kim26t_interspeech.pdf

## 问题
将大型语音基础模型（SFM）蒸馏为高效学生可降低推理成本，但学生训练本身仍耗时。Stacking 式阶段性加深可加速训练，而现有 gradual stacking、MIDAS 在各阶段会改变层位置；SFM 具有层特异知识，位置不一致易导致下游性能下降，也难稳定接入中间层 KD。

## 方法
提出 interleaved stacking：每阶段复制每隔 b 层选出的 K 层，并把复制层插在原层之后，使早/晚层在后续阶段仍保持相对前后位置。与输出级 MSE KD 及中间层 MSE KD 结合：中间层监督在初始浅模型上设定后全程保持，教师侧目标层索引固定。总损失为 L + w L_inter。教师为 HuBERT base（94.68M），学生为 12 层、宽 384 的 Transformer（26.87M），在 LibriSpeech 960h 上训练；B=4 阶段（每阶段加 3 层），比较 equal 与 prop-1 调度。

## 实验与结果
在 SUPERB 的 PR、ASR、SF、SID 上评估。InterleaveStack 在两种调度下均大幅优于 GradStack / MIDAS；prop-1 约 ×1.16 加速，PER=8.88、WER=9.99、SF F1=85.70、SID Acc=73.60，相对无 stacking 的 Full / Full L2L 在多项指标上持平或更好。中间层损失权重消融显示 w=0.5 较优；即便 w=0，方法在 ASR/SID 仍优于现有 stacking。Gradual stacking 难直接做层对层中间 KD（易发散），改用 prediction-style 中间损失整体仍不如 interleaved。层相似度分析显示复制层与原层保持高相似，并呈现更清晰的块状结构。

## 结论
作者认为 interleaved stacking 通过保持层位置一致性，在加速 SFM 蒸馏的同时减轻性能损失，并自然兼容中间层 KD；在 SUPERB 上显著优于现有 stacking 基线。

## 点评
核心洞察是蒸馏 SFM 时“层位一致性”比单纯堆深度更重要，把复制层邻接插入既利用相邻层相似，又稳住中间监督。方法简单、与现有 KD 配方兼容，实用价值高。边界在于实验主要围绕 HuBERT→固定 12 层学生与 SUPERB 子集任务；对更大规模教师、浅宽学生或非 MSE 蒸馏目标是否同样有效，正文未充分展开。
