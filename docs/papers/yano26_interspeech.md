# Adapting Text LLMs to Speech via Multimodal Depth Up-Scaling

- 论文编号：2099
- 报告人：Kazuki Yano
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yano26_interspeech.pdf

## 问题
把预训练文本 LLM 经语音持续预训练变成 Speech LM 时常严重损伤原文本能力；文本回放成本高且多数模型不公开预训练数据，LoRA 对跨模态容量可能不足。

## 方法
提出 Multimodal Depth Up-Scaling：扩展词表加入语义+声学离散语音 token（原 embedding 冻结），在冻结文本 LLM 中插入约 25% 新层并仅训练新层；零初始化输出投影使新层初始为恒等。放置策略：INTERLEAVED / SANDWICH / TOP / MIDDLE / BOTTOM。另用 E-Branchformer（全局 MHSA + 局部 cgMLP，\(W_{\text{Merge}}=[I;0]\) 函数保持初始化）作插入层，cgMLP 仅作用于语音 token。推理可丢弃新层完全恢复预训练。基座 SmolLM2-360M/1.7B，OWSM v3.2 英语 ASR 约 48k 小时，无文本回放。对比全参微调与参数量匹配的大秩 LoRA。

## 实验与结果
INTERLEAVED 上 ASR 接近全参（1.7B：clean/other 约 2.4/5.5 vs 2.3/5.6），文本平均降幅远小于全参/LoRA（1.7B：\(\Delta\) -8.3 vs -32.6/-35.7；TOP 文本最好 \(\Delta\) -2.7）。E-Branchformer 进一步把 1.7B WER 提到约 2.3/5.3、文本 \(\Delta\) -6.8，可训参数约少 60%。零样本语音条件翻译/简化/摘要：深度扩展仍产出连贯文本，全参微调退化为重复 token。

## 结论
作者认为插入可丢弃新层可在少伤文本的前提下学 ASR；E-Branchformer 插入层进一步提升声学适配。后续拟扩展到更多语音任务与语言。

## 点评
“冻主干 + 插层”把遗忘问题从权重更新转为容量分配，比回放/LoRA 更可恢复。强项是放置/架构消融与指令跟随定性证据；脆弱点在于推理保留新层仍有文本开销，且实验限英语 ASR、未与回放组合。
