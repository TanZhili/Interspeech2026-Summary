# CAQA-Net: Continual Audio Quality Assessment Across Speech and Music Domains

- 论文编号：476
- 报告人：Naiyuan Li
- 程序：Wednesday 30 September 2026 / Evaluation, Benchmarking, and Reliability of Audio Systems
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26d_interspeech.pdf

## 问题
生成与处理模型不断引入新失真与新域，静态 AQA 难跟进；联合重训代价高，微调又灾难性遗忘，跨语音–音乐回归任务的持续学习几乎空白。

## 方法
CAQA-Net：可训波形支路 M2D + 冻结谱图语义锚 BEATs，特征拼接后接多任务头；训练用知识蒸馏正则保旧知识；推理用基于 BEATs 原型的门控做任务无关加权。任务序列：TCD–VOIP → NISQA–SIM → Tencent → SingMOS → MusicEval。

## 实验与结果
相对 FT/MH-FT 等，CAQA-Net（LwF）mSRCC 0.754、mPSI 0.887，接近联合学习上界 JL 的 0.790（差约 0.036 SRCC / 4.6%）。EWC/MAS 变体亦优于朴素微调。语音到音乐域移仍是主要难点。

## 结论
双分支多头 + 蒸馏与原型门控可在语音/音乐 AQA 流上平衡塑性与稳定性，接近联合学习而不必重训全数据。

## 点评
把持续学习真正落到跨域 MOS 回归，填补评测侧空白。评分标准不一致与标签噪声仍会放大切换不稳定；未来需更强处理语音–音乐鸿沟。
