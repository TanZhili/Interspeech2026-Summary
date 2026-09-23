# Phoneme Error and Uncertainty Features for Interpretable Dysarthric Speech Assessment

- 论文编号：1138
- 报告人：Zihan Zhong
- 程序：Tuesday 29 September 2026 / Speech and Language Technologies in Healthcare
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhong26c_interspeech.pdf

## 问题
构音障碍多维感知评估耗时主观；SSL 嵌入强但不透明，WER 过粗且受语言模型偏置，对齐式 GoP 依赖规范音素目标、在病理失配下易偏。需要语句级、可解释、少依赖强制对齐的评估特征。

## 方法
冻结 CTC 音素识别器（wav2vec2-xls-r-300m-timit-phoneme）自由解码，构建 PED（11 维）：6 个相对规范音素（G2P）的错误率（PER、sub/del/ins、PFER、长度比）+ 5 个后验不确定度（EDL 的 evidence/aleatoric/epistemic，及 softmax margin/entropy 均值）。另提训练免费 ME=0.5(1−m)+0.5H。在 SAP 语句级 DAB 评分上做逻辑回归筛查与 Lasso 序次回归；并训深度≤4 决策树做可检查流水线。对比 GoP-maxlogit、Whisper WER、HuBERT Large、Acoustic12。

## 实验与结果
SAP 说话人分层划分（约 11k 有标注样本）。单特征：ME 在四主维平均 AUROC/ρ 约 0.79/0.543，优于 EDL、GoP、PER、WER。全 PED 四主维平均筛查 AUROC 0.80，接近 HuBERT 0.81；PED+Ac12 达 0.83。序次相关上 HuBERT 仍略优（ρ 0.62 vs PED+Ac12 0.59）。去掉不确定度特征 AUROC 从约 0.764 降至 0.694。决策树平均 AUROC 约 0.78，接近逻辑回归。次要嗓音维上 PED alone 较弱，加声学特征后 Harsh Voice 可超 HuBERT。

## 结论
CTC 后验不确定度可作构音失真代理，PED 在筛查上逼近 SSL 且可解释；浅树提供可人工检查路径。更细严重度排序仍受益于高维嵌入。

## 点评
把“过度自信的 CTC 后验”转成临床可用的不确定度探针，并与错误分解并列，解释性与性能的折中设计清楚。依赖 TIMIT 微调音素器与英语 G2P，跨病因/跨语言外推及次要嗓音维仍弱；树深度人为限制以保证可读，非最优精度。
