# Automating Sociophonetic Research in Under-Resourced Languages: A Case Study of Speech Rate in Cook Islands Māori

- 论文编号：3507
- 报告人：Rolando Coto-Solano
- 程序：Tuesday 29 September 2026 / Pacific Voices: Speech Science and Technology for the Languages of the Pacific Ocean
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/cotosolano26_interspeech.pdf

## 问题
社会语音学需要大量带社会标签的口语，低资源语难以手工扩展；AI（ASR、年龄识别）能否半自动扩充语料并揭示 Cook Islands Māori（CIM）语速的岛屿×年龄变异，尚缺报告。

## 方法
合并 Paradisec 田野转录与公开社媒音视频：Silero VAD 切段，ASR 助算 mora/秒语速；尝试人脸年龄估计失败后改为人工“>/<50 岁”。共 60 说话人、约 7.5 小时、8083 韵律短语，覆盖 Rarotonga、Nga Pū Toru、Aitutaki。线性回归检验年龄×岛屿交互。

## 实验与结果
人脸年龄模型在 Cook Islander 面孔上表现很差。语速（mora/s）：Aitutaki 最快（老/青约 8.4/8.7）；Rarotonga 约 6.6/6.4 无年龄差；Nga Pū Toru 年轻人显著快于年长者（7.7 vs 6.8，p<.0001）。Rarotonga 年轻人慢于 Nga Pū Toru 年轻人；Aitutaki 各年龄均快于同龄他岛。作者将无“年轻更快”的岛屿与语言转移/熟练度下降联系起来。

## 结论
自动化可加速语速测量，但年龄等社会标签对原住民面孔仍不可靠，需人工/社区众包。语速地理–年龄格局与岛屿活力差异一致。将扩更多岛与说话人。

## 点评
把 ASR 当 sociophonetic 量尺而非终点，并诚实报告年龄 AI 失败，对低资源计算社会语言学很有方法论价值。在线数据的岛屿归属与迁移史噪声大；语速–熟练度因果仍是解释性假说。
