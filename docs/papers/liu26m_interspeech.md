# MultiEmoVec: Learning Generalised Multimodal Emotion Representation by Momentum Contrast and Multi-task Reconstruction

- 论文编号：1563
- 报告人：Junchen Liu
- 程序：Thursday 1 October 2026 / Multimodal Speech Processing and Speech LLM Systems
- 技术分类键：audio-llm
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liu26m_interspeech.pdf

## 问题
多模态情感识别缺大规模标注，且情感库常有噪声与模态缺失；聚类或文本锚定对比在文本不可靠时脆弱，图融合计算重。需无情感标签的可迁移表征。

## 方法
MultiEmoVec 无监督预训练：Wav2Vec/MA-Net/DeBERTa 提语音/视频/文本特征；双重建含随机掩蔽单模态 20% 维的 masked reconstruction，与 mixup+掩蔽+高斯噪声的 denoising reconstruction；9 嵌入（3 单模态 + 6 交叉注意力）经 transformer 融合；MoCo 对比；ALS 按 EMA 平衡对比与重建损失。预训练后冻结编码器，轻量分类器微调下游。

## 实验与结果
CMU-MOSEI 预训练：Acc-7 55.31%、Acc-2 84.10%、BF1 89.08%，优于 MGAFR（52.24%）等，参数 16.28M（少约 6.8M）。模态消融显示文本贡献最大。模块消融：仅监督 42.91% Acc-7，MoCo 51.68%，完整模型最佳。跨库：MOSI Acc-7 38.78%（全训基线 39.19%）；IEMOCAP 4/6 类 WF1 74.54%/55.70%，接近全监督 78.36%/58.64%。

## 结论
掩蔽+去噪重建与 MoCo、ALS 结合，可学到跨库可迁移的多模态情感表征，并降低参数量。

## 点评
用重建显式应对缺失/噪声，比纯对比更贴情感数据现实；文本主导结果也提示“无监督”仍高度依赖转录语义。跨库成功部分因 MOSEI–MOSI 同 YouTube 分布，IEMOCAP 差距虽小但设定仍靠相同前端特征。
