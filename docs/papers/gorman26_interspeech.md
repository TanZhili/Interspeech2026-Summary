# Shifting Relational Paradigms for Affective Computing: Affective Resonance, Vitality Affects, and Vocal Interaction Fields

- 论文编号：2829
- 报告人：Cy Gorman
- 程序：Monday 28 September 2026 / Paralinguistics
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/gorman26_interspeech.pdf

## 问题

情感计算主流把情感当作孤立说话人的离散类别或唤醒/效价状态；作者认为这对互动不完整。借鉴情感共鸣（affective resonance）与活力情感/轮廓（vitality affects/contours），主张分析单元应是由嗓音动态共同构成的互动场，而非个体内状态。既有声学entrainment多测特征趋同，少见方向性、互动体制分解与场级涌现检验。

## 方法

概念上提出 Affective Resonance Dynamic Ontologies（ARDO）与 Artificial Affective Resonance Intelligence（AARI）：系统应参与并调制关系动态，而非只分类个体情感。实证为概念验证：AMI Meeting Corpus 四说话人近讲话筒，60 s 窗；用 WavLM-Base+ 连续隐状态（不做量化聚类）提取跨层“expressiveness”等代理，并对能量残差化。按 VAD 定义 Tier A（重叠共现）、Tier B（汇合的非重叠单人活动）、Tier C（按谁在说话拆开的非重叠，作语料内负对照）。在体制连续片段上做双变量与四说话人条件 VAR 的 Granger 方向性检验；用循环移位空模型校准短序列假阳性，并以 DSS∈{−1,0,+1} 汇总窗级方向性（微尺度 ≤1 s，宏尺度 >1 s）。

## 实验与结果

方向性耦合在亚秒滞后、互向共现体制下更可检：Tier A 微尺度非零 DSS 质量最高且近对称；Tier B/C 更偏向零支持。移位空模型显示短序列显著性膨胀（如 Tier A 微尺度名义 p<.05 拒绝率约 11.9%，膨胀约 2.4×）。校准后 q=5% 时 Tier A 微尺度相对空模型约有 +6.6pp（双变量）与 +7.4pp（能量控制条件模型）超额拒绝；更严 q=1% 时效应减弱但仍呈体制特异：A 最强、B 弱、C 近空。作者称耦合不能只还原为能量同步，且跨特征有小而结构化效应。

## 结论

互动配置本身构成可测的表达耦合痕迹，个体状态管线难以利用；这支持把 ARDO/AARI 作为面向场级活力动态的设计约束。局限：expressiveness 非效价/离散情感；Granger 仅线性预测依赖；结果目前仅 AMI；Tier B 宏尺度样本不足；跨语料完整结果留待后续。

## 点评

这篇主要是范式转移论文：用体制分解 + 空校准方向性耦合，证明“关系结构在，个体独占说话时耦合塌缩”，从而反对只做说话人情感标签。对社交机器人/共情对话设计有启发。脆弱点是实证仍 prelim、特征代理抽象、统计管线复杂（FDR、窗门控、滞后网格），效应幅度不大且依赖 AMI 会议场景；从可测耦合到真正 AARI 生成闭环仍有很长距离。正文末尾抽取截断，以上述可读部分为准。
