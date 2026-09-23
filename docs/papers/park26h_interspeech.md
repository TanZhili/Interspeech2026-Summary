# AnimeScore: A Preference-Based Dataset and Framework for Evaluating Anime-Like Speech Style

- 论文编号：3025
- 报告人：Joonyong Park
- 程序：Monday 28 September 2026 / Evaluation of Speech and Audio Analysis
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/park26h_interspeech.pdf

## 问题

“二次元/动画感”嗓音缺乏可复现客观指标；该属性多维且无共享绝对标尺，传统 MOS 不可靠。生成系统迭代依赖昂贵主观听测。

## 方法

AnimeScore：日语偏好框架。从 Anim-400k、ReazonSpeech、Coco-Nut 经文本 LLM 筛语言线索、增强+UTMOS/时长过滤、ECAPA 说话人匹配，得 3000 句（训/测 2500/500，说话人与句不重叠）。187 名评分者提供 15000 对 A/B 判断与自由描述。声学分析与逻辑回归建立手工特征上限；再在 SSL 骨干上训成对排序模型作自动度量/奖励。

## 实验与结果

感知驱动因素偏可控共鸣塑形、韵律连续与刻意咬字，而非单纯高音高。手工特征组合 AUC 上限 69.3%；HuBERT 等 SSL 排序达 90.8% AUC，显著超手工天花板。消融显示掩码预测类表征优势；跨子集保持可比 AUC。元数据与实现已公开。

## 结论

偏好排序比绝对 MOS 更适动画感评价；SSL 排序模型可作实用自动指标与偏好优化奖励。动画感由多声学维度共同塑造，简单启发式不足。

## 点评

问题设定抓住“风格属性无绝对标尺”这一评测难点，用大规模成对数据+手工天花板对照，说服力强。范围限日语与特定语料筛选，文化与语种外推未知；评分者动漫熟悉度偏高可能影响泛化。
