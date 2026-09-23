# How Attention Shapes Emotion: A Comparative Study of Attention Mechanisms for Speech Emotion Recognition

- 论文编号：1907
- 报告人：Federico Costa
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/casalssalvador26_interspeech.pdf

## 问题
SER 中自注意力能抓长程依赖，但 softmax 注意力相对序列长度二次复杂度，长语音代价高；高效注意力（RetNet、LightNet、GSA、FoX、KDA）在 SER 上缺少统一准确率–效率对标。

## 方法
固定架构：冻结 SSL 语音特征（WavLM / Wav2Vec2 / HuBERT / Wav2Vec2XLSR）与 BERT-large 文本特征，拼接后经可替换 seq2seq 模块，再 attention pooling + 分类头；八类情绪。仅训 seq2seq/池化/分类器（约 20M 可训、总参约 655M）。在 MSP-Podcast v1.0 Dev 与 v2.0 Test1/Test2 上比 Macro F-score；效率只测 seq2seq 的推理延迟与峰值 GPU 显存随序列长度变化。

## 实验与结果
Dev 上 LightNet 均值最高（36.62%），略超 SA（36.39%）；Test1/Test2 上 SA 最稳且最好（均值 36.42% / 27.19%），FoX 次之；GSA 在 T2 最弱（21.73%）。效率：SA 在 400s 延迟 48.59 ms、显存 12.35 GB；KDA 延迟 5.96 ms（约 8.15×）；FoX 显存 0.328 GB（约 37.6× 少于 SA）。全体在 T2 相对 T1 明显掉点。

## 结论
峰值准确率仍偏向标准自注意力（尤其短输入），高效变体提供近线性扩展；T1→T2 掉点显示真实分布与类别不平衡仍是瓶颈。

## 点评
工作把 SER 评测从刷分扩到延迟/显存，设计干净（只换融合层）。强处是多 backbone 与长度扫描；脆弱处是特征提取器冻结且效率只测子模块，端到端系统中 SSL 成本可能淹没 seq2seq 差异，且 T2 弱表现提示架构换注意力 alone 不够鲁棒。
