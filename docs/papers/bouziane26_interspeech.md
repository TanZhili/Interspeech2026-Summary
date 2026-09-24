# Learning Multiple Utterance-Level Attribute Representations with a Unified Speech Encoder

- 论文编号：3350
- 报告人：Maryem Bouziane
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bouziane26_interspeech.pdf

## 问题
SAMU-XLSR/SONAR/SENSE 等后训练把语音对齐到句级语义空间，利于多语检索，但易压制说话人等副语言信息；缺少单一编码器同时产出多种 utterance 级属性表示的统一框架。

## 方法
在 SENSE 式教师–学生对齐上扩展多任务分支：共享 w2v-BERT 2.0 编码器，每属性 \(\tau\) 有层投影、可学习层插值权重 \(\lambda_{\tau,\ell}\)、注意力池化与可选线性头，与冻结教师余弦对齐。语义教师为 BGE-M3，说话人教师为 VoxCeleb 上预训练的 ECAPA-TDNN。在 Common Voice 19（BGE-M3 支持的 83 语，约 8250 小时）加权采样训练 350K 步（8×H100）。评测：VoxPopuli/MTEDx/FLEURS 多语 speech→speech / speech→text 检索 R@1；VoxCeleb1-O 说话人验证 EER/minDCF。

## 实验与结果
Att(sem+spk) 在 VoxPopuli 等对上 R@1 略低于纯语义 Att(sem)、明显优于 SONAR；FLEURS 低资源对（如 my-en）甚至略升。说话人验证：Att(sem+spk) EER 0.91%，接近 ECAPA 教师 0.90%，略好于单任务 Att(spk) 0.93%。层权重分析：语义集中在约 13–14 层，说话人更偏高层（约 23–24）且分布更广。

## 结论
作者认为统一编码器可经多分支联合学习语义与说话人表示而互不严重拖累；层选择自动互补。后续拟加入情感、语言、口音等更多属性。

## 点评
做法把“一句一语义向量”推广为多属性分支，用层插值缓解任务干扰，工程上贴合 SENSE。强项是检索与验证双线证据加层可视化；脆弱处在于两教师空间是否正交依赖训练权衡，扩展到更多属性时分支干涉与算力成本仍未知。
