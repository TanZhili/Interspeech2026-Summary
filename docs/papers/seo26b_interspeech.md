# Hard Positive-targeted Training for Robust Audio Deepfake Detection under Neural Codec Processing

- 论文编号：2167
- 报告人：Jiwon Seo
- 程序：Monday 28 September 2026 / Speech Deepfake Detection: Robustness, Generalization, Attribution
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/seo26b_interspeech.pdf

## 问题
神经编解码器（NC）重建会扭曲判别线索并引入类声码器伪迹，使 ADD 鲁棒性下降。嵌入分析显示主因是 NC 处理后的真实语音向伪造区漂移，而非伪造侧大幅漂移。

## 方法
以干净真实为锚，批内加入不同编解码器的 NC-真实作正样本、干净/NC 伪造作负样本；选距锚最远的 hard positive。联合优化：引导损失（拉远 hard positive 与负样本）+ triplet（锚—正近、锚—负远）+ 分类 CE。在 LA19 等协议上评 SSL-Conformer / SSL-AASIST，原声与 BigCodec/SpeechTokenizer 等 NC 条件。

## 实验与结果
基线在 NC 下真实准确率骤降（如 SSL-Conformer 77.10%→49.27%；AASIST 66.28%→34.11%），伪造侧降幅较小。提出的 hard-positive 训练在 NC 条件下降低 EER、减少真实侧虚警，同时保持伪造检测能力（正文以 EER/准确率报告）。

## 结论
针对边界邻近的 NC-真实 vs 伪造对做批构造与辅助分离损失，可缓解 NC 主导的真实侧误判，提升编解码处理下的 ADD 鲁棒性。

## 点评
把失败模式从“整体变差”精确到“真实侧漂移”，训练目标与诊断一致。依赖特定编解码器入训练分布，对新 NC 族系的外推仍开放；批构造固定锚—正—负比例，可扩展性与算力开销需权衡。
