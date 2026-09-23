# Stuttering Classification and Segmentation with Attention-Based Multiple Instance Learning

- 论文编号：1091
- 报告人：Petar Sušac
- 程序：Tuesday 29 September 2026 / Speech and Language Technologies in Healthcare
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/susac26_interspeech.pdf

## 问题
口吃严重度评估（如 SSI-4、SES）需要不流畅段时长，但多数数据集只有 clip 级多标签，不便帧级分割。现有 MIL 口吃方法多为 instance+max pooling，且常依赖合成不流畅预训练；embedding+注意力 MIL 尚未用于多标签口吃分类。

## 方法
以 wav2vec2-large / wavlm-large / whisper-medium 为骨干，HConv 聚合多层，经 BiLSTM（4×512）与投影后：(1) instance 头 + max pooling；(2) Ilse 式 MIL 注意力池化 + bag 分类头。训练仅用 clip 标签（加权 BCE，含标注者一致性权重）；帧级推理时 instance 模型去掉 max pooling，embedding 模型对正例用 softmax 前注意力权重+sigmoid。先冻骨干再解冻微调。

## 实验与结果
训练 SEP-28k-E；clip 级 FluencyBank 交叉评测；帧级用 FluencyBank CASA gold（732 段不流畅）。SEP-28k-E 多标签上 Whisper/WavLM 变体在 Block/Sound/Word/Interjection 等达 SOTA 级 F1（如表 1 Whisper+attn：Bl 0.35、Wd 0.78、Int 0.82）。FluencyBank 单标签：Whisper+attn F1 0.90，优于 Shih 等 0.85。帧级：Whisper+attn F1 0.70，相对 YOLO-Stutter 0.47、StutterCut 0.45 约提升 23%+（摘要所述）；注意力变体优于同骨干 max pool。长时 block 因 3s 窗仍困难。

## 结论
仅用 clip 级弱监督即可做零样本式帧级分割，且注意力 embedding MIL 在帧级召回上更有利。作者称在 SEP-28k-E clip 与 CASA 帧级达 SOTA。

## 点评
把弱监督 MIL 接到多标签口吃并引入注意力可解释权重，切合临床“要时长”需求。评测与基线设定不完全对等（基线常假设 clip 必含不流畅），跨标签体系（SEP-28k vs CASA）只能做单标签聚合；3s 上下文是长 block 的结构性瓶颈。
