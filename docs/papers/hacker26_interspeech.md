# Common Cold Corpus: Health-aware robustness study of modern speaker embeddings under physiological domain shift

- 论文编号：1188
- 报告人：Anabell Hacker
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 1
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hacker26_interspeech.pdf

## 问题
中度上呼吸道感染（URTI）会改变发音器官，但现代说话人嵌入在生态有效录音下对短期生理域移的稳定性仍不清楚；既往冷语音语料多为高症状、实验室条件，不利于同人健康–患病对照。

## 方法
发布 Common Cold Corpus：85 名德语者经个人设备远程采集，患病（WURSS 均值约 3.25/7）与健康各一场（≥7 天间隔），朗读 NWS 与 Butter Story，共约 431 分钟。声学：openSMILE eGeMAPS（90 参量），配对 t/Wilcoxon + BH 校正。嵌入：ECAPA-TDNN、TitaNet、ECAPA2、ReDimNet，16 kHz、截断至 15 s，文本受控闭集验证（genuine 188、imposter 15792），报告 EER/AUC、条件内距离、Zshift、身份 crossover margin。

## 实验与结果
声学：NWS 上 F0 80 百分位与 HNR 在 BH 后仍显著下降；多数特征仅名义显著；TBS 趋势同向但校正后不显著。验证：患病–健康仍高可分（TitaNet EER 1.51%，AUC 0.9893 等），相对健康–健康跨文本基线 EER 约升 1–2 个百分点。条件内距离 ill 更大；Zshift 模型依赖（TitaNet 8.826，ECAPA2 1.177）。ECAPA-TDNN 约 6.38% 样本身份 margin>0；位移方向有显著全局对齐。

## 结论
中度感冒在真实场景下即可引起说话人嵌入可测、部分有向的位移，而多数经典声学标记校正后消失；身份大体可保，但对生物特征与数字生物标志应用有双重含义。语料仍在扩大。

## 点评
用同人配对 + 生态录音把“生理域移”从通道失配里拆出来，并同时看声学显著性与嵌入几何。强在多架构对照与 Zshift/crossover 指标；弱在设备/环境等混杂难彻底排除、样本相对 ComParE 仍小，位移是否特异于感冒需更大规模与症状分层验证。
