# WhiSSDapt: Adaptive Fusion of Whisper Layer Embeddings for Sentence Stress Detection

- 论文编号：3236
- 报告人：Jhansi Mallela
- 程序：Tuesday 29 September 2026 / Prosody, Pronunciation and Specialized Speech Processing
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/murugaiyan26_interspeech.pdf

## 问题
句重音检测需要同时捕捉局部声学与词间相对关系，现有 Whisper 方案常固定取某一 encoder/decoder 层（如 WhiStress 选 Layer 9），默认重音信息集中在单层；而分层分析表明声学、语音、词级信息分布在多层，固定层可能次优。

## 方法
WhiSSDapt：冻结 Whisper-small（English-only），对全部 encoder/decoder 隐状态各学一组标量权重，经温度缩放 softmax 归一化后加权求和得到 ˜h_enc、˜h_dec；再经额外 decoder 块（˜h_dec 对 ˜h_enc 做交叉注意力）与两层 FFN（768→1536→2）做 token 级二分类，再对齐到词级。仅训练融合权重、额外 decoder 与分类头；加权交叉熵类别权重 [1.0, 2.33]。τ 在 GER/ITA/EmphAsses 上取 0.1，TinyStress-15k 上取 0.01。基线为固定 Layer 9 的 WhiStress，以及 ISLE 上的 SupraDoRAL。

## 实验与结果
数据：ISLE（德/意非母语英语，人工词级显著度）、TinyStress-15k（合成）、EmphAsses（Expresso TTS 强调）。词级 F1：WhiSSDapt 在 TinyStress/EmphAsses/GER/ITA 分别为 0.9131/0.9811/0.853/0.8930，优于 WhiStress（0.909/0.939/0.804/0.870），相对提升最高约自然语音 4.48%、合成 6.09%；相对 SupraDoRAL（GER 0.7817、ITA 0.8656）也有提升。层权重分析：decoder 普遍偏好 Layer 9，encoder 偏好 Layer 12、中层受抑；固定融合 E(1,12)–D9 接近全自适应，换深层 decoder（D12）明显变差。

## 结论
可学习多层融合可替代手工选层，并稳定优于固定层基线；分析给出可解释的锚点层（decoder 9、encoder 12）。未来拟扩展到其他韵律任务。

## 点评
核心贡献是把“哪一层有韵律”从离线试错变成端到端可学习融合，层权重分布与消融互相印证，比单纯刷分更有解释力。弱点是骨干仍冻结、合成数据上权重会塌到单层，说明自适应优势在自然变异更大时更明显；且与 WhiStress 同属参考转写条件下的 token 分类设定。
