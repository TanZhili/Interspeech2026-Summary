# Beyond Short Segments : Expanding Speaker Embeddings with Vector Archives

- 论文编号：3192
- 报告人：Hyunku Kang
- 程序：Monday 28 September 2026 / Speaker Verification: Advances in Speaker Embeddings
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kang26_interspeech.pdf

## 问题
即便强 SSL 骨干（如 WavLM）在说话人验证上表现好，短于约 3 秒的话语因缺少协同发音与韵律线索，帧级特征稀疏，EER 急剧恶化；聚合多段或元学习要么推理要多句，要么不直接充实帧特征。

## 方法
VAM-ECAPA：WavLM 层加权和 → TVAMSP → ECAPA-TDNN 得 192 维嵌入。TVAMSP 含：Transformer 建帧间上下文；可学习 Vector Archive Library（G=4 档案，每档 l₂=149 向量，约对应 3 s WavLM 特征）作固定 Key/Value，输入作 Query，温度 softmax 映射后残差加回；Attentive Statistics Pooling 得全局均值/方差广播加回各帧。在 VoxCeleb2 开发集训练、VoxCeleb1 评测（O/E/H，EER 与 MinDCF），对比 Wav2vec2/HuBERT/WavLM+ECAPA 及短段训练配方。

## 实验与结果
全长上 WavLM 基线最强（Vox1-O EER 0.973%）。短段：基线 Vox1-O 3s→1s EER 2.393%→18.437%；1s 训练配方可降到 10.346%；同配方加 VAM 到 8.342%，最终 VAM-ECAPA 1s 为 8.334%（相对常规基线降 54.8%）；Vox1-H 1s 20.449%→14.571%，Vox1-E 18.059%→8.511%。3s 上 VAM 反不如基线（作者归因于短段优化的映射扰动已充分特征）。消融：去 VAM→8.856%，去 Transformer 残差→8.529%，仅 VAM+ASP→8.352%，完整 8.334%。

## 结论
可学习档案映射能在单段推理下补偿短时信息不足；代价是长段上可能过补偿。未来拟按时长自适应调节、给档案加显式监督，并测噪声与跨语。

## 点评
把“记忆库式参考说话人特质”接到短时 SV，比单纯短段重训更对症帧稀疏。档案长度锚定 3 s 稳定区是清晰归纳偏置；脆弱点是 3 s 性能倒退、档案可解释性弱，以及增益部分仍依赖与短段训练配方的耦合，需在噪声/跨语上验证是否真是“档案补偿”而非容量红利。
