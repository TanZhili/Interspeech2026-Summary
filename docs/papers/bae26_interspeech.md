# Something from Nothing: Data Augmentation for Robust Severity Level Estimation of Dysarthric Speech

- 论文编号：1390
- 报告人：Jaesung Bae
- 程序：Wednesday 30 September 2026 / Clinical and Inclusive Speech Technology
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/bae26_interspeech.pdf

## 问题
构音障碍严重度评估缺标注、难泛化；SAP 仅少量句子有 SLP 评分，直接监督受限，跨病因/语言更脆弱。

## 方法
三阶段：Whisper-large 教师在 SAP 有标子集上回归并给未标注样本伪标；用伪标 SAP + LibriSpeech（健康标为 1）做标签感知对比预训练（离散/连续/二值配对）；再在有标 SAP 上微调。评测 UASpeech、DysArinVox、EasyCall、EWA-DB、NeuroVoz 等未见集。

## 实验与结果
基线 SAP 测试 SRCC 0.719，跨域说话人级平均 SRCC 0.732；完整框架跨域平均 SRCC 0.761，并保持 SAP 内表现。消融显示弱监督与引入 LibriSpeech 对跨域稳健性关键。

## 结论
伪标 + 标签感知对比 + 健康语料扩增，可在几乎“无额外人工标注”下提升构音障碍严重度估计的跨域鲁棒性。

## 点评
充分利用 SAP 大量未标注与健康语音做表示塑形，问题抓得准。跨域标签体系（可懂度/MOS/TOM/MoCA/H-Y）异质，相关不等于临床可互换；伪标噪声仍可能固化教师偏差。
