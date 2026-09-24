# Stabilizing Short Duration Speaker Verification through Neural Re-scoring with Hybrid Enrollment

- 论文编号：228
- 报告人：Zhiqi Ai
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ai26_interspeech.pdf

## 问题
自定义唤醒词后的短时说话人验证（常 <3 s）嵌入不稳、对噪声与音素敏感；纯 TD 注册内容一致但时长短，纯 TI 信息更丰但与短语测试内容失配。

## 方法
构建 VoxPhrase（ASR+强制对齐从 VoxCeleb 切 0.8–3 s 短语，硬负例挖掘评测）。冻结 ECAPA/CAM++/ERes2Net-L，提取帧级与句级嵌入；混合 TI+TD 注册，计算句级余弦 S_ti、S_td，并用双向并行 cross-attention 做 TD 注册–查询帧级匹配，MLP 融合得最终分数，BCE 训练轻量 verifier。

## 实验与结果
Eval-1 上 TI（3/10 s）普遍优于短 TD；加 verifier 与混合注册再降 EER（如 CAM++ TD Avg 9.15→8.31，10 s TI+verifier 至约 5.35）。TI 时长从 1 s 增至 10 s EER 持续下降，混合神经重打分在 10 s 达约 1.6%（Eval-1 random）。Deepmine OOD（Eval-3/4）上混合亦最优（如 ERes2Net-L 4.88/2.38）。

## 结论
作者认为实用注册时长（≥3 s）下 TI 稳定性常优于短 TD，而混合注册 + 帧级神经重打分可互补二者，尤其在难例与分布外短语上更稳。

## 点评
把 UDKWS 场景的短时验证从“固定短语微调”拉到可自定义短语语料与混合注册，工程贴合度高。短语切分依赖 ASR/对齐质量；冻结骨干使收益主要来自后端重打分，而非端到端短时表征学习。
