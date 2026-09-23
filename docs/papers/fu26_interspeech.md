# Acoustic and Semantic Feature Fusion Mapping for Lyric Intelligibility Prediction

- 论文编号：1014
- 报告人：Yuxiang Fu
- 程序：Tuesday 29 September 2026 / Quality, Intelligibility and Evaluation of Speech and Codecs
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/fu26_interspeech.pdf

## 问题

歌词可懂度受演唱、伴奏、旋律与语义等影响，难于口语 intelligibility。手工声学特征缺高层语音/语义信息；ASR 词正确率与人对歌词的主观可懂度存在系统性偏差，尤其在歌唱场景。

## 方法

提出声学 + 预训练编码器特征融合再回归：声学侧含能量、RMS、过零率、谱质心/带宽/rolloff、时长、源分离 SNR 等；语义/语音侧取 Whisper base.en 编码器时序嵌入。经均值/标准差/极值/偏度/峰度等时序统计，并在重要特征间构造成对交互，标准化后送入映射模块。对比神经网络（FCN、MoE FCN、CNN+GRU、Transformer）与梯度提升树（XGBoost、LightGBM、CatBoost）。侵入式 Whisper 转录正确率作基线。

## 实验与结果

数据为 Cadenza 2026 Challenge 人工标注歌词可懂度集，5 折交叉验证；指标 RMSE（×100）与 Pearson Corr。Whisper base.en 下：Baseline RMSE 29.32 / Corr 0.59；CatBoost 最优 27.367 / 0.654；无交互 CatBoost 27.532 / 0.651；树模型整体优于神经网络，Transformer 最差（34.896 / 0.461）。图示比较中 Whisper 嵌入优于 Mert、Wav2Vec2。

## 结论

作者认为融合浅层声学与 Whisper 表示、再用树模型做结构化映射，比纯 ASR 正确率更贴近主观歌词可懂度；未来可探索端到端多模态（声学–语义–语言）一体化模型。

## 点评

问题抓得准：唱歌场景下“机器听对词 ≠ 人听得懂”。特征工程 + CatBoost 在千级样本上更稳，符合数据量不足时神经网络易过拟合的常见现象。侵入式设定依赖参考歌词；交互特征与编码器选择对结果敏感，泛化到未见曲风/语言时需再验证。
