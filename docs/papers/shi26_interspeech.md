# Distilling LLM Semantic Priors into Encoder-Only Multi-Talker ASR with Talker-Count Routing

- 论文编号：612
- 报告人：Hao Shi
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shi26_interspeech.pdf

## 问题
多说话人 ASR 若用 LLM 作自回归解码慢且在重度重叠/三说话人上不稳；编码器侧序列化 CTC 虽快，但缺语义正则、训练易崩，且多数方法假定固定说话人数。

## 方法
编码器-only MT-ASR：WavLM-Large 共享前 12 层 + 二/三说话人各 12 层分支（共享层冻结），LSTM 分离器 + 序列化 CTC。训练期用 LLaMA-3.2-1B：先 LoRA/特殊 token 适配多说话人 SOT 并反传蒸馏到编码器，再固定 LLM，用 \(\alpha L_{\text{Serialized-CTC}}+(1-\alpha)L_{\text{SOT}}\) 训分离器/CTC。Talker-Count Head（注意力池化 \(\mu,\sigma\) + MLP）预测 2 vs 3 人并路由分支。数据为 LibriMix（含噪声）。

## 实验与结果
无 LLM 蒸馏时序列化 CTC 几乎训不动。oracle 说话人数下，noisy eval 2mix/3mix WER 约 9.6/22.2，优于 SOT-Llama-1B 的 11.3/39.1。TCH+12 层时 talker-count 准确率 noisy eval 约 93.7%，2mix/3mix WER 约 9.7/24.5。RTF：CTC 约 0.0043/0.0106 vs Llama-1B 约 0.115/0.098。与更大 LLM/SOT 系对比：2 人可比，3 人显著更好。

## 结论
作者认为把 LLM 语义先验蒸馏进编码器可保留 CTC 速度并稳住重叠表示；TCH 支持可变人数。三说话人计数仍难，后续拟加强噪声/重叠下的计数鲁棒性。

## 点评
把 LLM 从“推理解码器”降级为“训练教师”，对准多说话人瓶颈很务实。强项是 3-mix 与 RTF 收益清晰；脆弱点在 TCH 三说话人准确率不足会拖累整体，且仍限在 2/3 人分支而非开放人数。
