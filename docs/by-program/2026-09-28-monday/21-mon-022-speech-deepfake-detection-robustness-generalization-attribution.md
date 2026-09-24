# Speech Deepfake Detection: Robustness, Generalization, Attribution

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Oral
- Area：4
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕音频深度伪造检测的泛化、神经编解码鲁棒性、词级伪造定位、开集溯源与表征解耦。生成模型迭代使未见攻击成为常态；神经编解码又可能抹掉伪造痕迹并扭曲 bona fide 嵌入分布。

提升泛化的策略包括：用扩散重建制造难样本并配合多层特征聚合与正则辅助对比学习；针对编解码后 bona fide 更易被判假的偏移设计辅助损失与边界小批量；以及用频谱专家混合与幅度/相位显式编码补足预训练表示对物理线索的忽视。

任务形态也在扩展：微调 Whisper 以 next-token 预测同时转写并检词级伪造；双分支门控融合做开集源追踪；正交解耦抑制说话人身份泄漏。共同方向是把“难样本/分布偏移”纳入训练目标，并把身份与伪造伪影分开。

## 论文技术总结

# Diffusion Reconstruction towards Generalizable Audio Deepfake Detection

- 论文编号：158
- 报告人：Bo Cheng
- 程序：Monday 28 September 2026 / Speech Deepfake Detection: Robustness, Generalization, Attribution
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/cheng26_interspeech.pdf

## 问题
ADD 对未见攻击泛化差；若能区分“重建得到的难样本”，模型更可能应付简单样本。何种重建范式最能造出有效难样本，以及如何用对比与正则提升跨域泛化？

## 方法
用 HiFi-GAN、DAC、Encodec、SemantiCodec（扩散）等重建真实/伪造语音作难样本。冻结 XLS-R 300M + 多层自适应聚合 → AASIST。训练目标含分类 CE 与 RACL：标准对比损失 + 专盯真实/重建真实的增强对比损失 + 批内方差正则促类内紧凑。

## 实验与结果
五测试集平均 EER：基线 15.789%；扩散重建 12.220%（相对降约 22.6%）；加聚合与 RACL 后最佳平均 8.247%（ITW 9.155、CodecFake 20.198 等）。扩散重建整体优于 HiFi-GAN/DAC/Encodec。

## 结论
以扩散重建构造难样本，并结合多层聚合与 RACL，可显著提升未见攻击泛化。

## 点评
“难样本分类→易样本自然变好”的思路清晰，重建选型消融有说服力。增强对比只盯真实侧，针对重建伪迹；代价是训练需多路重建数据，且 CodecFake 等仍偏高，泛化未彻底解决。


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


# Deepfake Word Detection by Next-token Prediction using Fine-tuned Whisper

- 论文编号：628
- 报告人：Xin Wang
- 程序：Monday 28 September 2026 / Speech Deepfake Detection: Robustness, Generalization, Attribution
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/tran26_interspeech.pdf

## 问题
部分篡改（用合成词替换真实词）需定位哪一段是假的；专用序列检测器开发与部署成本高。能否只微调预训练 Whisper，在转写同时标记假词？

## 方法
在训练转写中于假词两侧插入复用词表已有标记（如 `!!!!!!` / `~~~~` 作 TOF/EOF），仍用标准 next-token 训练，推理时夹在标记间的 token 判为合成。数据可用声码器对 1–5 个词做 copy-synthesis（Ft.Voc）或真实 TTS 部分伪造（Ft.TTS / 混合），降低造数成本。

## 实验与结果
域内 E.Voc/E.TTS：微调 Whisper 检测 FAR/FRR 与专用 ResNet 接近（如 E.Voc FAR 7.22%、FRR 0.52%），且转写 WER 相对预训练显著下降。域外 AV-Deepfake1M、PartialEdit（如 VoiceCraft）上检测与转写均程度不一地退化，与 ResNet 相当量级但整体需更好泛化。

## 结论
最小改动即可把 Whisper 变成“转写+假词定位”一体模型；声码器模拟可降低训练成本，但跨生成器泛化仍是瓶颈。

## 点评
工程价值高：不改结构、不加重头，就把反欺骗嵌进 ASR 流水线。标记复用词表 token 可能与真实文本冲突；域外退化说明 vocoder 伪迹与现代 LLM 编辑伪迹仍有鸿沟。


# Dual-Branch Gated Fusion for Open-Set Audio Deepfake Source Tracing

- 论文编号：3008
- 报告人：Khalid Malik
- 程序：Monday 28 September 2026 / Speech Deepfake Detection: Robustness, Generalization, Attribution
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/khan26_interspeech.pdf

## 问题
开集源追踪需识别未见合成系统并拒绝过自信；纯 SSL 在域内强但 OOD 过承诺，手工特征更稳但不够判别；朴素拼接会被高维 SSL 淹没。

## 方法
双分支：冻结 XLSR-53（1024-d）与 66-d CORES（MFCC+Δ/ΔΔ、chroma、ZCR、RMS、谱质心/带宽/滚降/对比/平坦度）。各投影到 256-d，输入条件门控软加权融合。联合训练：标签平滑 CE + 能量间隔损失促 ID/OOD 分离 + 门控多样性防单支塌缩。

## 实验与结果
MLAAD：ID Acc 97.6%、EERc 4.9%、FPR95 10.4%（相对文中参考基线 FPR95 相对降约 83.5%），约 0.9M 参数。消融显示固定拼接/单支难以兼顾 ID 与开集拒绝。

## 结论
输入条件门控融合 SSL 与多维手工描述子，可在保持高域内归因准确率的同时改善未见合成器的开集拒绝。

## 点评
明确针对“SSL 过拟合训练分布”与“手工特征保守”的互补性，门控比固定融合更对症。CORES 组合本身不新，价值在开集目标下的自适应加权与能量间隔；对极端未见管线仍依赖能量分数标定。


# Mixture of Spectral Experts for Audio Deepfake Detection

- 论文编号：661
- 报告人：Zhe Li
- 程序：Monday 28 September 2026 / Speech Deepfake Detection: Robustness, Generalization, Attribution
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/qiu26_interspeech.pdf

## 问题
神经语音合成越来越自然，伪造痕迹更难察觉；SSL 预训练模型虽有强表征，但对幅度不规则、相位失真等低层物理线索利用不足；现有频域特征或波形编码器与 PTM 融合时，相位建模不够，且与高层上下文存在表征鸿沟；全量微调成本高，常规 PEFT 也未显式控制预训练奇异方向的贡献。

## 方法
框架由 Frequency Audio Encoder（FAE）与 Mixture of Spectral Experts（MoSE）组成，骨干为冻结的 WavLM-Large。FAE 对 STFT 取对数幅度，并以 sin/cos 表示相位（训练时加随机相位扰动），经 1D 卷积与 depthwise separable convolution 得到与 PTM 同维的谱表征 P。MoSE 作用于 Transformer FFN 权重：对 W_l 做 SVD 后冻结奇异基 U、V，仅用 K 个专家对中间矩阵 Σ 做低秩更新（I+BA），组内共享可训参数（G=2，K=4）；路由按时间平均池化后的门控加权专家输出。各层输出可学习加权得到 Z_final，再与 P 做 cross-attention 融合后分类。训练用加权交叉熵（bonafide 0.9 / spoof 0.1），约 4.8M 可训参数。

## 实验与结果
在 ASVspoof 2019 LA 训练，评测含 2019 LA 与跨集 2021 LA/DF、In-the-Wild。2019 LA：EER 0.29%、min t-DCF 0.0081，优于表中对比系统。跨集 EER：2021 LA 2.68%、2021 DF 3.89%、ITW 9.25%。消融：去掉 FAE→0.51%，去掉 MoSE→0.45%，两者都去→0.72%，纯 WavLM 基线 1.46%。K=4、G=2 最优；可学习路由温度约 0.9831 时 21 LA EER 最低。

## 结论
FAE 提供显式幅度–相位线索，MoSE 在 SVD 域对冻结 WavLM 的 FFN 做专家化低秩适配，在 ASVspoof 2019/2021 与 In-the-Wild 上取得有竞争力的表现与较强跨集泛化；在对比系统中于 2021 LA 与 ITW 上 EER 最优，2021 DF 上仍具竞争力。

## 点评
抓的是“合成/声码器留下的谱与相位物理痕迹 + 如何在不破坏 SSL 先验下把骨干拧向这些痕迹”两类问题。相对只堆 LFCC/CQT 或普通 LoRA/MoE，把 PEFT 放进 SVD 中间矩阵并按组共享，更直接对准频谱奇异方向上的伪造偏移。强依赖 ASVspoof 类分布与固定 4 秒裁剪；跨集 DF 上略逊于 MoLEx，说明对压缩/深度伪造变体仍可能脆弱。


# Dual-Granularity Orthogonal Disentanglement for Generalizable Audio Deepfake Detection

- 论文编号：836
- 报告人：Zhuodong Liu
- 程序：Monday 28 September 2026 / Speech Deepfake Detection: Robustness, Generalization, Attribution
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/liu26g_interspeech.pdf

## 问题
检测器常学到说话人身份而非合成伪迹（隐式身份泄漏），跨说话人/跨域 EER 暴涨；对抗解缠复杂且训练不稳。

## 方法
共享浅层 CNN 后分内容支（卷积+MHSA→伪迹）与身份支（统计池化→说话人）。双粒度正交：样本级余弦正交 + 批级交叉协方差 Frobenius 惩罚。课程调度逐步加大解缠权重 β(t)；身份损失仅在真实样本上。总参约 2.1M。

## 实验与结果
ASVspoof 2019 LA EER 1.35%、2021 DF 7.88%、In-the-Wild 21.58%；跨数据集迁移相对梯度反转解缠绝对改进约 2.60%。以小模型达到接近更大 SSL 系统的量级表现（文中对比）。

## 结论
无需辅助网络或对抗动力学，双粒度正交 + 课程即可抑制身份泄漏并提升跨域泛化。

## 点评
把身份—伪迹独立性写成可微几何约束，比 GRL 更稳、overhead 更低。身份监督依赖训练说话人标签；ITW 仍 20%+ EER，说明真实域失配未完全消除，正交只是必要非充分。

