# Role-Aware Semi-Supervised Domain Adaptation for Teacher-Student Speaker Diarization

- 论文编号：155
- 报告人：Zhen Liao
- 程序：Wednesday 30 September 2026 / Speaker Diarization 1
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liao26_interspeech.pdf

## 问题
通用说话人日志化到课堂老师–学生场景会因远场、噪声与标注稀缺而失效；教育分析需要的是角色（教师 vs 学生）而非个体 ID，学生侧是“多对一”粗标签，重叠时传统 PIT 难以解耦。

## 方法
发布 TSSD 数据集（45 场标注 26.57h + 174 段未标注 110.20h）。框架：源域复合数据预训练 DSE-CBM（冻结 WavLM + ConBiMamba），再 Mean Teacher 半监督域适应。监督支路用 Role-Aware Union Loss：C>2 通道中选一作教师，其余 max 并集拟合集体学生标签，诱导通道特化。一致性用 PIT-MSE 对齐学生/教师模型输出排列。推理 ECAPA-TDNN + AHC。

## 实验与结果
TSSD 测试：开源管线 DER 26–35%；监督微调 21.42%；Mean Teacher 基线 19.77%；加 Role-Aware Union → 17.75%（confusion 5.20→2.70）；加 PIT-MSE → 17.80%；二者结合 16.95%（0s collar；0.25s 为 12.67%）。标注/未标注比 r=1.0 最优。可视化显示 Union 损失在多学生重叠时能激活多通道而非压成单通道。

## 结论
粗角色监督 + 半监督域适应可把课堂声学解成可聚类的角色流；TSSD 与方法为教育场景角色日志化提供可扩展范式。

## 点评
把“身份区分”改成“角色并集”切中课堂标注现实，confusion 下降与通道可视化相互印证。依赖教师多为单说话人的假设；学生侧特化质量仍受粗标签上限约束。开源数据与代码对低资源课堂研究有直接价值。
