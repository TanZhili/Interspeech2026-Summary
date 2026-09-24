# Robust Audio-Visual Speech Recognition

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：10
- 论文数：5

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场聚焦噪声与复杂环境下的音视频语音识别（AVSR），尤其是 LLM 骨干接入后的稳健表示、跨模态对齐与压缩 token 多任务能力。共同问题是：干净条件优化的 LLM-AVSR 在噪声下表示不稳；独立投影或浅融合限制互补交换并加重 LLM 计算负担。

技术路径包括：向 Whisper 类骨干注入说话人与噪声场景嵌入；在 LLM 内部关键位置加入变分信息瓶颈以正则化表示；稀疏模态对齐与视觉单元引导细化；以及压缩多模态语音 token 同时支撑识别与翻译，并用对比对齐保留语言容量。场次以 Survey Talk 开场，但程序单未给出技术摘要，正式方法贡献集中在后续四篇 Oral。

## 论文技术总结

# To be announced (Survey Talk, 40 mins)

- 论文编号：
- 报告人：
- 程序：Thursday 1 October 2026 / Robust Audio-Visual Speech Recognition
- 技术分类键：multimodal
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
官方程序未提供摘要。仅能从标题与会场信息判断主题方向：「To be announced (Survey Talk, 40 mins)」，安排在「Thursday 1 October 2026 / Robust Audio-Visual Speech Recognition」。

## 方法
官方程序无摘要，无法概括具体方法、模型结构或训练流程；此处不作推断。

## 实验与结果
官方程序无摘要，未给出数据集、对比设置或定量结果。

## 结论
官方程序无摘要，无法归纳作者结论与适用边界。

## 点评
该条目目前只有标题与程序位置可参考，后续若有讲义、幻灯片或正式论文，再据此补充问题设定、方法细节与可核验结果。


# Adaptive AVSR: Integrating Speaker and Environmental Embeddings for Robust Audio-Visual Speech Recognition

- 论文编号：2081
- 报告人：Tobias Bocklet
- 程序：Thursday 1 October 2026 / Robust Audio-Visual Speech Recognition
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/simic26_interspeech.pdf

## 问题
AVSR 虽在噪声下优于纯 ASR，但大规模泛化训练未必充分用上「当前说话人」与「当前环境噪声」信息；说话人嵌入用于 ASR 个性化较成熟，环境嵌入在 AVSR 中探索较少。

## 方法
以 Whisper 为骨干，上游自注意力 AV 融合（音视频拼接后分块）。从音频提取：
- **噪声嵌入**：四层注意力编码器联合回归 SNR + 四类噪声分类（babble/music/natural/sidespeaker），取编码器输出作嵌入，注入融合模块；
- **说话人嵌入**：X-Vector（优于 ECAPA），注入解码器前级。

比较三种注入：前缀拼接、额外交叉注意力、门控通道加权。噪声用门控最好，说话人用前缀最好。

## 实验与结果
LRS3 + VoxCeleb2 预训练/微调。相对无自适应基线，噪声门控平均相对降 WER 约 3.5%（∅ 4.42→4.26），说话人前缀约 3.2%；-5 dB 收益更大。联合噪声+说话人无额外收益——X-Vector 本身可约 90% 准确分类噪声，与专用噪声嵌入冗余。相对 AV-HuBERT base 平均相对降约 13.4%（∅ 4.92→4.26），多数噪声类优于 AV-Fusion / Whisper-Flamingo。

## 结论
噪声与说话人嵌入可显著提升 Whisper 系 AVSR，且最佳注入策略依嵌入类型而异；二者信息有重叠，简单叠加未必更强。

## 点评
系统比较三种注入位点/方式很实用，门控「按噪声调音视频权重」直觉清晰。有趣发现是 X-Vector 携带噪声线索，解释了说话人自适应在重噪也有效。局限：增益绝对值不大、依赖外部噪声/说话人嵌入质量，以及与 AV-HuBERT 的训练 SNR/目标差异可能影响公平性。


# VIB-AVSR: Variational Information Bottleneck for Noise-Robust LLM-Based Audio-Visual Speech Recognition

- 论文编号：1903
- 报告人：Umberto Cappellazzo
- 程序：Thursday 1 October 2026 / Robust Audio-Visual Speech Recognition
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/arora26b_interspeech.pdf

## 问题
LLM 系 AVSR（如 Llama-AVSR）多在干净声学上优化，LoRA 微调无法让文本预训练 LLM 骨干学会对噪声音频隐状态稳定表征；噪声鲁棒压力几乎全压在编码器上，噪声下性能下降明显。

## 方法
**VIB-AVSR**：在 LLM 中间层对**音频**隐状态插入变分信息瓶颈（视频/文本不压）。位置相关两层 MLP 参数化对角高斯后验，相对可学习先验做 KL；重参数采样后与原表示插值 \(\hat{Z}=\alpha H+(1-\alpha)\tilde{Z}\)（\(\alpha=0.5\)）再传入下层。推理用均值。骨干：Whisper-medium + AV-HuBERT + Llama-3.2-1B（LoRA）。最优配置：层 4 与 8 双瓶颈，\(\beta=0.1/H\)。

## 实验与结果
LRS2；MUSAN babble/speech 噪声。噪声训练与干净训练两种范式下，相对 Llama-AVSR 在多数 SNR 降 WER，极端噪声 Avg(N>S) 收益更大；干净训练时瓶颈仍能泛化到未见噪声。干净语音（∞）基本持平或略优。消融：单层不足，双层 (4,8) 最佳，三层过正则；\(\alpha=0\) 过损，固定 0.5 优于日程调度。

## 结论
对 LLM 骨干音频表示做轻量 VIB 正则，无需改架构或加数据，即可在多 SNR/噪声类型上提升鲁棒性，且与噪声增强机制不同，干净训练也可受益。

## 点评
把噪声鲁棒从「编码器/数据增强」推到「LLM 内部表征压缩」，问题定位清楚。强在开销小、消融完整；脆弱点在仅压音频通道、\(\beta/\alpha\)/层位敏感，以及实验集中在 LRS2 + 特定噪声，跨域外推仍待验证。


# Robust LLM-based Audio-Visual Speech Recognition with Sparse Modality Alignment and Visual Unit-Guided Refinement

- 论文编号：1277
- 报告人：Fei Su
- 程序：Thursday 1 October 2026 / Robust Audio-Visual Speech Recognition
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/su26_interspeech.pdf

## 问题
LLM 系 AVSR 常独立投影音视频或浅融合，跨模态对齐弱、互补交换不足，且把连续特征喂给 LLM 增加计算与噪声敏感。需要可控的跨模态交互与更稳的 LLM 精炼。

## 方法
提出 **AVUR-LLM** 两阶段：
1. **Sparse Modality Alignment (SMA)**：在 Whisper 音频编码器上层稀疏插入块，视觉作 query、音频作 stop-gradient key/value，校准视觉而不扰动预训练音频通路。
2. **Adaptive Modulated Fusion (AMF)**：解码器中用声学探针注意力熵估计 token 级可靠性，门控视觉注入幅度与方向（tanh）。
3. **Visual Unit-Guided Refinement (VUR)**：对 AV-HuBERT 中层特征 K-means 离散化并 run-length 压缩，作视觉 token 提示；LoRA 微调 LLaMA2-7B 对 N-best 列表打分重排。

## 实验与结果
LRS3（30h/433h）及 +VoxCeleb2（1759h）。AV 干净：433h WER 0.75%，1759h 0.68%，优于 Whisper-Flamingo、Llama-AVSR、MMS-LLaMA 等。0 dB babble 相对 MMS-LLaMA 约 37% 相对降（1.7% vs 2.7%）。消融：AMF+VUR 是噪声鲁棒主因，SMA 再补一截；视觉离散取第 12 层、K=2000 最佳。

## 结论
稀疏对齐 + 置信门控融合 + 视觉离散单元引导的 LLM 重打分，可在干净与噪声下全面提升 LLM-AVSR，并控制对 LLM 的负担。

## 点评
三条线分工清楚：编码器侧稳对齐、解码侧按声学不确定性调视觉、LLM 侧用紧凑视觉单元重排。强在干净 SOTA 与重噪收益；脆弱点在两阶段管线与离线码本、N-best 依赖，以及文中注明各工作 babble 来源不一，跨文绝对数字需谨慎对比。


# MTC-AVSR: Compressed-Token-based Audio-Visual Speech Recognition and Translation with Contrastive Language Alignment

- 论文编号：266
- 报告人：Lusi A
- 程序：Thursday 1 October 2026 / Robust Audio-Visual Speech Recognition
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/a26_interspeech.pdf

## 问题
LLM 系 AVSR 依赖高分辨率多模态 token，计算与延迟高。MMS 等压缩虽有效，但多仅服务识别，未验证压缩 token 能否同时支撑识别与语音翻译，也少有把源语对齐 token 映射到多语言空间而不扩大 LLM 参数。

## 方法
**MTC-AVSR** 三阶段：
1. **多模态压缩**：音视频前端 + AV-QFormer，按约 3.5 token/s 动态分配 query（MMS 式）。
2. **Language Adaptation Module (LAM)**：共享多语言词表 + 两层门控交叉注意力，把压缩 token 重编码为多语言表示；**TCAL** 对比损失把 adapter 输出对齐到词表条目。
3. **任务条件解码**：冻结 LLM（QLoRA）前缀 `<recognize><En>` 或 `<translate><lang>` 切换 ASR/翻译。

分阶段训练：先源语对齐锁定编码器，再在冻结缓存上做跨语适配（\(\lambda\) 从 1.0 anneal 到 0.3）。

## 实验与结果
LRS3+VoxCeleb2（1759h）+ MuAViC En-X。LRS3 干净 WER 0.74%（与 MMS-LLaMA 持平），0 dB babble 2.0%。MuAViC 干净：Es 28.1、Fr 26.3、Pt 21.8 等达文中所称 SOTA；噪声下平均仍强于 Whisper-Flamingo 变体。消融：LAM→词表→TCAL 逐步抬 BLEU/降 WER；3B 较 1B/8B 在干净上更优权衡。LAM 比全量 CMT 更省显存且效果更好。

## 结论
同一超压缩 MMS token 流可同时做 AVSR 与 En-X 翻译；轻量 LAM+TCAL 在冻结编码器下实现多语言切换，说明压缩表示仍保留跨任务语言容量。

## 点评
核心问题「压缩后还剩多少跨任务语义」问得很准，用多任务提示 + 对比词表对齐给出可操作答案。强在单模型多任务与效率；脆弱点在噪声翻译对比因对方噪声文件未公开而不完全对等，以及依赖 Whisper 伪标签 VoxCeleb2。

