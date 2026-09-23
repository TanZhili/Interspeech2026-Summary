# Automatic Assessment of L2 Speech Intelligibility: Segmental Error Ranking

- 论文编号：2522
- 报告人：Agnieszka Pludra
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pludra26_interspeech.pdf

## 问题
现有 CAPT 常按“靠近母语”纠一切音段偏差，忽略交际目标——可懂度。需要用音段替换信息预测可懂度，并给出对交际影响最大的音素错误排序。

## 方法
从 VoxPopuli、speechocean762（排除儿童）、Pearson 内部数据筛选 600 条 5–15 秒录音；120 名 Prolific 评分者按 5 点可懂度量表评分（每条 5 人，Krippendorff α=0.67）。Azure 音素识别对齐规范 IPA，提取各音素误读率与音素对替换率；去稀疏特征后训多种回归，最佳为 AdaBoost DTR。用特征重要性得到可懂度导向的音段错误排序。

## 实验与结果
Leave-one-out：AdaBoost MSE 0.48、Corr 0.74，优于随机/均值基线，也略优于以 Azure WER 作相关基线（0.67）。重要音素包括元音 /ɛ ə ɪ i/ 与辅音 /z s ð v k t r l/ 等，讨论中联系功能负荷与常见 L2 难点。

## 结论
音段替换特征可在一定程度上预测可懂度，并由重要性排序引导学习者优先纠正影响交际的音素，支持以可懂度而非母语性为中心的 CAPT。

## 点评
把评估目标从 nativeness 拉回 intelligibility，排序可直接进教学反馈。依赖自动音素识别会误差传播；评分者 L1 匹配带来主观性（α 不高）；样本偏中高可懂度且未建模超音段，作者也承认音段解释力有上限。
