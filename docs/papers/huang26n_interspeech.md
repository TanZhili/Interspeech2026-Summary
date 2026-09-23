# EmoEUS: Uncertainty Supervision for Multimodal Emotion Recognition in Conversation

- 论文编号：1996
- 报告人：Zilong Huang
- 程序：Monday 28 September 2026 / Multimodal Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/huang26n_interspeech.pdf

## 问题
多模态对话情感识别（MERC）常用 Transformer 融合，但往往默认各模态在所有话语上同等可靠，忽视噪声、缺失与冲突线索带来的模态不确定。已有不确定性建模多靠分类损失隐式学习，缺少对方差的显式监督与自适应加权。

## 方法
EmoEUS 含三块：
1. **ContextDEM**：模态特征经 Bi-GRU 后，用 Transformer + 残差与双 MLP 输出高斯均值 \(\mu\) 与方差 \(\sigma\)；
2. **UAMF**：按相对方差算模态置信度并 softmax，置信加权 \(\mu\) 后做多头注意力与 Transformer 融合，残差接回拼接均值；
3. **ESL**：按情感×模态维护分布簇中心（均值+方差，每 epoch 更新、不反传），用 2-Wasserstein 距离度量话语分布与簇中心偏差，监督预测方差与 \(\sqrt{D_{2W}}\) 对齐；总损失 \(L_{\mathrm{CE}}+\kappa\sum L_{\mathrm{ESL}}\)，\(\kappa\) 在 \(ep_{\mathrm{start}}\) 后打开。
特征：RoBERTa（文本）、Wav2vec2.0（音频）、CLIP（视觉）。

## 实验与结果
IEMOCAP（LOSO）与 MELD（官方划分），指标 Acc / w-F1。
- EmoEUS：IEMOCAP Acc 74.33、w-F1 74.36；MELD Acc 68.32、w-F1 67.53，整体优于所列基线（如 FEMI、CFN-ESA 等）。
- 消融：去掉 ESL 或 UAMF 均下降；相对 Concat/Attention/Transformer 融合亦更优。
- 模糊情感对误分率下降；分布表示 + 2W 优于点估计 + MSE；残差连接有益。

## 结论
显式不确定性监督使模型按话语自适应抑高不确定模态、强化可靠模态，在两基准上达文中报告的 SOTA，并改善易混情感对。未来计划加强跨说话人实时动态下的不确定性估计。

## 点评
关键是把“方差”从隐式正则拉成可监督信号，并用 Wasserstein 对齐情感簇，使融合权重有可解释的可靠性依据。强在组件消融完整、融合与监督耦合清晰；脆弱在簇中心依赖标签与 epoch 统计、ESL 权重调度敏感，以及 Sad/Angry 等个别类上仍可能不及部分基线——整体提升不保证每类最优。
