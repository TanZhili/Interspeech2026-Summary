# MoDiCoL: A Modular Diagnostic Continual Learning Dataset for Robust Speech Recognition

- 论文编号：2111
- 报告人：Theresa Pekarek Rosin
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pekarekrosin26_interspeech.pdf

## 问题
现有 ASR 鲁棒性数据集/基准常孤立考察噪声、口音或障碍等因素，难以反映真实共现与随时间累积的分布漂移；也缺少用持续学习诊断预训练 ASR 在何处遗忘的可控资源。

## 方法
发布 MoDiCoL：用 Taguchi L27 正交阵与 foldover 得 108 种因子配置×75 样本=8100 条（约 18.79 h，其中合成 14.08 h）。三因子族为语言内容（域/风格）、说话人（年龄/口音/健康/停顿/不流畅）、声学环境（噪声类型/SNR/距离）。真实与 XTTS-v2 合成语音经去噪、不流畅/损伤/停顿、混响距离与噪声注入管线对齐配置。CL 课程：t0=LibriSpeech 控制设定，再依次 Acoustic、Speaker、Linguistic、Compound 漂移；评估 ER、RLR、OGD 三种策略（whisper-small.en，online/streaming）。

## 实验与结果
未适应时 t0 A-WER 7.42，t1/t2/t3 分别升至 47.62/87.28/141.73，t4 为 43.37；合成子集整体好于真实。课程上 ER-10% 最稳：A-WER 17.31±0.48，优于 JOINT（27.24）与 FT（34.14），FM 接近 0；RLR 遗忘大，OGD 的 AI-WER 最好（21.19）且任务梯度近正交。顺序引入漂移提升可塑性，但除 ER-10% 外 FM/BWT 方差大，任务顺序敏感。

## 结论
MoDiCoL 支持对多因子漂移下 ASR 适应与遗忘做诊断；适度 replay 最利于跨漂移保持鲁棒性，梯度子空间干扰是遗忘因素之一。数据与管线已放 Hugging Face。

## 点评
价值在“可控共现因子 + CL 课程当诊断工具”，而非再堆单一噪声/口音集。合成占比高、部分配置靠损伤仿真，外推到真实共现分布时需谨慎；ER 优于 JOINT 的结果有启发，但强依赖缓冲与任务顺序。
