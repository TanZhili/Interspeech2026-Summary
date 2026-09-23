# Probing the Layer-wise Geometry of Chinese Dialect Representations in Wav2Vec 2.0

- 论文编号：975
- 报告人：Zhen Peng
- 程序：Tuesday 29 September 2026 / Language and Dialect Recognition
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/peng26c_interspeech.pdf

## 问题
Wav2Vec 2.0 层间如何编码方言特征不清楚；现有探测多面向标准语，中文方言工程应用常默认用顶层或简单聚合，可能丢掉中间层细粒度语音信息。

## 方法
MagicHub 五方言：西南官话（四川、武汉）、中原官话（郑州）、吴语（上海）、粤语（广州）；Azure TTS（zh-CN-XiaoxiaoNeural）生成对应标准普通话作参考锚点；VAD 去静音，16 kHz。冻结 Wav2Vec 2.0 XLSR-53 的 24 层 Transformer，提取隐状态。几何探针：与锚点的归一化 DTW 距离；方言质心两两欧氏距离 + MDS；凝聚层次聚类建谱系树。

## 实验与结果
几何指标呈三阶段：L1–8 声学主导、距离高且与物理差异一致；L9–19 距离平台、保留细粒度可分性；L20–24 距离骤降（流形收缩）。MDS：L1 无序；L12 非官话靠近、官话分离且空间分散；L24 整体向中心收缩。层次聚类 L12 对郑州等局部音系敏感，L24 自发呈现与传统分类一致的宏观分支（吴/粤 vs 官话）。

## 结论
中文方言表征经历声学→语音分化→空间收敛；深层收缩可视为特征过滤器，突出宏观分类。建议口音等细粒度任务优先中间层，宽泛方言分类可用深层。

## 点评
用无参几何探针把“层该怎么用”落到可操作建议，比只报分类准确率更有解释力。合成普通话锚点便于控内容，但也可能引入 TTS 声学偏置；五方言规模有限，谱系对齐是否稳健需更大说话人池验证。
