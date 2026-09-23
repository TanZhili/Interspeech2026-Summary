# Boundaryless Speech-to-Syllable Representations with Hierarchical CNN for Linguistically Inspired Automatic Stress Detection

- 论文编号：3144
- 报告人：Namrata Mokshagundam
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mokshagundam26_interspeech.pdf

## 问题
英语音节重音检测对 CALL 关键，但既有方法依赖人工边界或强制对齐，标注贵且对齐误差会传导；部分“无边界”法仍用音素边界。

## 方法
全边界无关：自监督帧级嵌入 → 编码器抓上下文 → 分层 CNN+池化把帧序列压成固定最大音节数表示 → 非自回归或自回归解码器输出每音节重音概率。损失用 BCE 或 Post-net2.0（强制一词恰一重音）。真音节数来自 ISLE 标注用于截取输出。评德语（GER）、意大利语（ITA）L2 英语学习者。

## 实验与结果
Post-net2.0 CNN：GER 94.86%、ITA 96.24%，相对边界相关与先前无边界 SOTA 最高增益约 18.67%/16.12%。作者称持续优于 DNN、LSTM 与既有方法。

## 结论
分层时间压缩可直接学 speech-to-syllable 表示，结合语言学单重音约束，在无显式切分下达到高准确重音检测。边界是仍需已知音节个数截断输出。

## 点评
核心是用 CNN 层级下采样替代对齐，抓住 CALL 部署痛点。强处是 Post-net2.0 注入语言学先验；脆弱处是“无边界”仍依赖数据集给的音节数 n，以及表演/朗读 ISLE 与自发口语差距。
