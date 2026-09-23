# Collection and Curation of a Spontaneous Multilingual Speech Corpus for Low-Resource Himalayan Languages

- 论文编号：2634
- 报告人：Abhijit Sinha
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sinha26_interspeech.pdf

## 问题
东喜马拉雅走廊语言多样但自发多语语料稀缺；野外采集噪声不一、转写成本高，需要在一致协议与元数据下收集可计算的验证型资源，而非仅堆数据量。

## 方法
采集 Bodo、Dzongkha、Gorkhali（Nepali）、Sherpa 共 320 名母语者（每语 80 人）、约 146 小时室内自发独白（每人 5 段，均长约 5.5 分钟），44.1 kHz 或 16 kHz 原样保存，带年龄/性别/环境元数据；不因质量剔除。用 YIN 提 F0、WebRTC VAD 估语速做声学刻画；语种识别将音频重采样 16 kHz、切 10 s，说话人独立 80/20，比较 MFCC 与 pitch/intensity/loudness 及融合，分类器为 SVM 与 CNN。无转写。

## 实验与结果
语言级均值 F0：Bodo 173.7、Dzongkha 163.4、Gorkhali 156.5、Sherpa 141.9 Hz；语速亦有系统差异。单特征 CNN：MFCC 85.95%、loudness 76.09%、pitch 仅 56.86%。融合后 MFCC+Loudness 91.97%，全特征（MFCC+Loudness+Intensity+Pitch）达 92.95% accuracy（balanced 92.41%）。性别分布不均（Sherpa 74 男/6 女）会影响音高分离解读。多语预训练表示初步实验未达竞争力。

## 结论
一致协议下的自发语料即使无转写也可支撑声学刻画与说话人独立 LID；谱特征为主、能量/韵律互补。语料可用于喜马拉雅低资源语言后续建模与文献记录。

## 点评
用“声学结构 + LID 可学性”做语料验证，比单纯发布小时数更有说服力。强在四语平衡说话人数与严格说话人分割；弱在性别失衡、无转写限制下游 ASR、设备采样率混杂，且 LID 准确率不能直接外推到其他任务。
