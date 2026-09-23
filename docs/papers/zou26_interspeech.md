# Less is More: Boosting Bimodal Music Emotion Recognition with Adaptive Audio Sequence Compression

- 论文编号：1552
- 报告人：Dinghao Zou
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zou26_interspeech.pdf

## 问题
音频+MIDI 双模态音乐情绪分类中，预训练音频特征序列远长于紧凑 MIDI（信息密度失衡），全局池化抹掉瞬态，重训低帧率 tokenizer 又太贵。

## 方法
PoolingVQ：冻结 MERT-95M / MIDI-BERT；K-means 初始化 VQ 码本量化音频帧；滑窗（5 帧、步长 3，约压到 25 Hz）按窗内唯一码数 U 选 Avg / 加权 Avg / Max 池化，约压短 2/3。融合用简单拼接（MIDI 插值对齐）或两阶段交叉注意力；损失 CE+VQ commitment。EMOPIA（≤60s）与 VGMIDI（≤130s）四象限分类。

## 实验与结果
Cross-Attention+PoolingVQ：EMOPIA Acc/F1 0.8953/0.8955，VGMIDI 0.600/0.6018；macro-F1 超 BFAM 约 12.5%（EMOPIA）与 5.48%（VGMIDI）。简单拼接在 EMOPIA 亦已很强（0.8837/0.8844）。

## 结论
码本引导的自适应池化可在不重训骨干下压缩冗余音频序列并提升双模态融合，达到所述 SOTA。

## 点评
问题抓的是序列长度不对称而非再设计大融合器；“变化大 max、平稳 avg”贴近音乐动态。脆弱处是规则阈值启发式、强依赖 MIDI 可用性，以及 VGMIDI 绝对分数仍偏低显示域难度。
