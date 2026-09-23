# Geometry-Informed Distributed Acoustic Scene Understanding

- 论文编号：821
- 报告人：Yiyuan Yang
- 程序：Tuesday 29 September 2026 / Spatial Audio 3
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/yang26f_interspeech.pdf

## 问题
多房间场景中墙门遮挡使单点集中阵列易漏听；分布式麦克风若忽略拓扑，难以判断哪路可靠，也无法按物理邻接补全缺失转移，叙事易出现非物理跳跃。

## 方法
输入为多节点 log-Mel、麦克风坐标与几何 Ω（边界、门洞、材料）。建拓扑图，边权按距离与墙衰减。共享 AST 提节点特征并加位置编码，经图卷积空间融合 + GRU 时序建模；查询式解码器输出每帧语义三元组 ⟨subject, relation, object⟩；将几何与三元组线性化为提示，冻结 Llama-3-8B-Instruct 生成连贯叙事并补全遮挡缺口。

## 实验与结果
基于 pyroomacoustics 的定制多房间仿真（2–4 室，N=6 麦，LibriSpeech+ESC-50）。完整系统 Triplet F1 0.87、BLEU-4 0.55、ROUGE-L 0.62、BERTScore 0.77、SCS 88.2%，优于集中式（F1 0.51、SCS 35%）与仅声学分布式。消融去掉几何先验 SCS 降至 66.5%；去掉时空图融合 Triplet F1 降至 0.81。

## 结论
分布式感知 + 拓扑感知融合 + 几何约束 LLM 推理可提升遮挡下检测与叙事空间一致性；未来需真实测试床验证并优化推理速度。

## 点评
把场景理解写成“感知→符号三元组→几何提示 LLM”流水线，对多房间逻辑接地很有针对性。全部结果来自受控仿真，材料/遮挡参数理想化；冻结 LLM 的补全能力依赖提示质量，真实噪声与标注误差下 SCS 未必同样稳健。
