# Towards Efficient Simultaneous Inverse Text Normalization with Pretrained Text-to-Text Language Model and Read-Tag-Write Policy

- 论文编号：1060
- 报告人：Kiet Anh Hoang
- 程序：Monday 28 September 2026 / Robust and Efficient ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/hoang26_interspeech.pdf

## 问题
流式 ASR 需要把口语形式即时转为书面 ITN（标点、大小写、半符号实体等）。现有流式 ITN 多为神经标注 + 手工 FST，跨域跨语难扩展；端到端 seq2seq 精度好但全局注意力不可流式。

## 方法
基于预训练文本-to-文本模型做流式端到端 ITN：
- **流式编码器**（如块注意力）+ 自回归解码器；
- **Read–Tag–Write（RTW）**：编码器边读边对 token 做 IOB 标注；标签为 O（原样）则立即写出以降延迟；遇到需归一化跨度完成后再调解码器 WRITE；
- **Prefix-based Training Augmentation**：随机截断源、目标侧加局部 `<EOS>`，让解码器在无全局 EOS 时也能结束局部跨度；
- KV cache 与推理优化；数据来自越南语新闻语料自动生成约 5M 句对（标点/大小写/半符号/语音学 OOV 等）。

## 实验与结果
摘要：越南语数据上精度可比非流式端到端基线，优于流式混合方法，并满足实时延迟要求。
（抽取主要在方法与数据构造，完整延迟/准确率表未进入可读尾部。）

## 结论
RTW 利用 ITN 多为局部、大量 token 无需改写的结构，使预训练 T2T 模型可流式化，摆脱 FST 规则依赖。

## 点评
把 SiMT 的 read/write 思想改成 ITN 友好的 Read–Tag–Write，抓住“多数 token 直通”降低延迟。强在与预训练 LM 知识结合；**定量延迟与类别 F1 因抽取不全**需回 PDF；手工 regex 造数对真实 ASR 噪声的鲁棒性仍是潜在风险。
