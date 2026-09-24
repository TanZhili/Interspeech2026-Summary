# Improving Model Expressivity and Speaker Matching in Low-Latency Voice Conversion

- 论文编号：796
- 报告人：Anders R. Bargum
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/bargum26_interspeech.pdf

## 问题
实时零样本 VC 在轻量因果约束下说话人相似度偏低：内容离散单元/发音合成丢失韵律，全局说话人嵌入容量不足，难以表达时变音色。

## 方法
并行编解码器：内容编码器蒸馏 HuBERT 软单元；韵律编码器估计 F0、周期性、V/UV、响度并合成 sinusoid-plus-noise 激励，在解码器各残差块注入；全局说话人编码器（VoxCeleb 预训练）+ 互补说话人编码器，用因果 MHA 将说话人 token 与内容/韵律查询融合为 S_Emb。训练时对内容输入做音高移位、加噪、参数均衡，对说话人编码器做单元级时间掩码以促解耦。推理时将源 F0 按目标均值比缩放。

## 实验与结果
LibriTTS 全 train（555 h / 2311 说话人）训练；零样本：LibriTTS test-clean 377 句 × VCTK 6 未见说话人。相对 RT-VC / StreamVC：SECS 80.83%（+4.18 / +3.02 pp），F0 PCC 0.885；WER/CER 与基线接近。主观 S-MOS 最高（3.25），Q-MOS 略低于 StreamVC；CPU 延迟 64.9 ms。消融显示扰动与互补编码器均提升 SECS。

## 结论
在保持可懂度与低延迟的前提下，激励注入 + 互补说话人融合 + 编码器特定扰动可提升零样本说话人匹配与音高一致性；作者将增益归因于表达能力增强，而非严格证明“动态音色”提取。

## 点评
针对实时瓶颈的设计很务实：用轻量旁路补回离散内容丢掉的韵律，并用因果注意力扩充说话人表征，而不是堆非因果 SSL。互补嵌入的可解释性仍弱（L2 与 F0/响度无清晰对应），扰动会略损可懂度，主观相似度优势也未达统计显著。
