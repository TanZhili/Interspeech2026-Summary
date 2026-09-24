# The First Environmental Sound Deepfake Detection Challenge: Benchmarking Robustness, Evaluation, and Insights

- 论文编号：1599
- 报告人：Yang Xiao
- 程序：Wednesday 30 September 2026 / Evaluation, Benchmarking, and Reliability of Audio Systems
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yin26_interspeech.pdf

## 问题
环境声生成（TTA/ATA/VTA）可伪造警报、枪声等，威胁公共安全；相对语音/歌声 deepfake，环境声 deepfake 检测（ESDD）缺乏统一基准与挑战。

## 方法
介绍首届 ESDD Challenge：两赛道—(1) 未见生成器检测（EnvSDD），(2) 黑盒低资源；(EER 为指标；基线 AASIST 与 BEATs+AASIST。汇总 97 队、约 1700+ 有效提交，并分析顶尖系统架构与训练策略。

## 实验与结果
Track 1 基线 BEATs+AASIST EER 13.20%；榜首 AHU EAT+AASIST 集成达 0.30%。Track 2 基线 12.48%，顶尖约 0.25%。常见有效策略：大规模 SSL/EAT 表征、增广、跨层融合、集成；未见/黑盒生成器仍显著拉垮朴素系统。

## 结论
高保真生成器挑战大，但 SSL+增广+集成可获强泛化；挑战为后续 ESDD 提供基准与方向。

## 点评
把环境声反欺骗从语音反欺骗邻域单独立题，数据与赛道设计对安全评测很及时。论文偏挑战综述，具体系统细节依赖各队报告；真实野外部署噪声与复合伪造仍待 ESDD-2 等跟进。
