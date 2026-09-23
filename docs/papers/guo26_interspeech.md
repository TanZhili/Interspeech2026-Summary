# GLAD: Global-Local Aware Dynamic Mixture-of-Experts for Multi-Talker ASR

- 论文编号：1022
- 报告人：Yujie Guo
- 程序：Monday 28 September 2026 / Multi-Talker ASR & Speaker Diarization
- 技术分类键：asr-multitalker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/guo26_interspeech.pdf

## 问题
SOT 式 MTASR 在深层中说话人相关声学线索易被稀释，标准 MoE 仅靠局部层输入路由，难以按说话人分配专家；SIMO/外部 diarization 条件方案又受限或开销大。

## 方法
GLAD-SOT：在 Conformer 编码器所有线性层换成 Mixture of Low-rank Experts（MoLE，N=3，r=8）。全局路由：卷积前端浅层特征经线性编码器得 \(X_{global}\)，KeepTopK+softmax 得 \(P_{global}\)；局部路由由层输入得 \(P_{local}\)；动态融合 \(\beta=\mathrm{softmax}(X_{in}W_{fusion})\) 按帧加权二者得到专家权重。训练损失为 ASR + Switch Transformer 式负载均衡（\(\gamma=0.01\)）。输出为带 `<sc>` 的序列化转写。

## 实验与结果
LibriSpeechMix：GLAD-SOT（35.31M）2mix OA-WER 7.4、3mix OA-WER 21.5，优于 SOT、CSE-SOT、SOT+SACTC；高重叠与 3mix 零样本仍领先。消融：去掉全局路由或改为静态求和均变差；FFN 与 Attention 同时替换最好。CH109（CH11-mix 微调 5 epoch）：平均 40.7，优于各基线。可视化：全局融合权重 \(\beta_g\) 随重叠升高，浅层与最深层更高。

## 结论
全局–局部动态融合 MoE 可提升 SOT-MTASR，尤其在高重叠与多说话人泛化场景；作者称这是首次将全局–局部融合 MoE 用于 MTASR。

## 点评
用浅层说话人线索补深网路由，直接针对“重叠越重越需要身份锚点”的瓶颈，与可视化一致。专家为低秩、规模偏学术小模型；主训仍是模拟混合，真实通话依赖短微调，跨域鲁棒性边界仍待更大规模验证。
