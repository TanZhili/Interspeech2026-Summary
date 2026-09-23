# Towards Speech Impairment Prediction in German-Speaking Individuals with Amyotrophic Lateral Sclerosis

- 论文编号：1052
- 报告人：Monica Gonzalez-Machorro
- 程序：Monday 28 September 2026 / Clinically Useful Speech Representations 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/gonzalezmachorro26_interspeech.pdf

## 问题
ALS 球麻痹致言语障碍，临床用 ALSFRS-R-speech 与 QOL-Dys 等量表；德语队列上跨说话人 vs 个体内预测、以及何种言语任务更有信息量，尚缺系统对比与采集标准化参考。

## 方法
AIMnd 2.0 中 66 名德语 pwALS、最多三访；任务含持续 /a:/、Cookie Theft、/da/-/da/、/da/-/ba/、北风与太阳朗读。特征：eGeMAPS、Whisper Large v3、Wav2vec2-de。SVM/XGB/RF 回归两量表；跨说话人分层划分与个体内时间划分；任务预测可均值融合。

## 实验与结果
跨说话人：QOL-Dys 上重复任务 /da/-/da/、/da/-/ba/ 最佳 CCC≈0.62；朗读/看图对 ALSFRS-R-speech 可达约 0.64–0.65。个体内设置可达 CCC 0.86（摘要报告）。多任务融合亦有竞争力。作者强调结果为德语 ALS 言语障碍预测的初步步骤。

## 结论
作者认为声学特征可跨人与个体内预测言语相关临床分；重复任务对 QoL 主观言语特征尤其有用，有助于标准化采集讨论。

## 点评
价值在同一队列上对照量表、任务与建模范式，服务协议标准化。样本量与访次有限；个体内高 CCC 依赖有随访的子集，监测场景外推需更大纵向数据。
