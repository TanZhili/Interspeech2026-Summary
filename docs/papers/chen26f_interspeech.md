# Toward Multimodal Industrial Fault Analysis: A Single-Speed Chain Conveyor Dataset with Audio and Vibration Signals

- 论文编号：838
- 报告人：Xiaoxiao Miao
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26f_interspeech.pdf

## 问题
公开工业故障数据多在实验室、单模态（音频或振动）、面向轴承/电机等部件；噪声常缺失或事后合成，难评测产线级系统在真实厂噪下的多通道融合。

## 方法
发布 SSCC 单速链板输送机数据集：3 路音频（Zoom H5、iPhone 11、Xiaomi）+ 4 路振动（电机单轴 + 对端三轴，100 kHz），同步切 5 s，共 6,669 样本。覆盖正常与 lean/dry/loose/screwdrop 四类故障，速度档 20–100、负载重/中/轻，以及现场录制厂噪由扬声器回放的干净/噪声条件。协议：无监督故障检测（仅正常训练、跨速度 zero-shot 到 vel=100）与监督分类（hold-out vel=80 等）；统一通道级 kNN 探针（检测 k=1，分类 k=11），比较 BEATs、CED、DaSheng、EAT、ECHO、FISHER 等预训练编码器的 audio/vibration/融合表示。

## 实验与结果
检测 AUROC：多数编码器音频优于振动（如 FISHER 音频 0.954 vs 振动 0.546）；融合常提升振动并有时超过单模态（BEATs 融合 0.891）。分类准确率普遍较高（如 ECHO 音频 Acc 0.975，DaSheng 融合 0.967）；振动对 screwdrop 更有利，音频对 loose 更好，融合多数情况下最优。

## 结论
数据集提供可复现的多模态工业故障基准；模态贡献因任务与故障类型而异，简单距离基线已有可用表现，但仍有高级表示与融合的提升空间。

## 点评
把产线级输送机、多设备音频与真实厂噪注入放进同一评测协议，补上 MaFaulDa/HUSTmotor 类数据的缺口。强在通道级公平探针与跨工况划分；弱在仍为实验室平台回放噪声、低速仅正常干净条件，且基线冻结编码器+kNN，不能代表专用工业模型上限。
