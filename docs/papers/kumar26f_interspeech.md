# Who Synthesized This? Joint Deepfake Detection and Generative Source Attribution

- 论文编号：2442
- 报告人：Vishal Kumar
- 程序：Tuesday 29 September 2026 / Safeguarding Synthetic Speech: Ethical, technical and legal perspectives
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kumar26f_interspeech.pdf

## 问题
合成语音检测 alone 已不够：还需在开放世界中追溯生成源（含训练未见的零日合成器）。合成系统持续发布，静态闭集分类无法扩展；ASVspoof 5 等开放条件暴露旧基准局限。

## 方法
三阶段框架：Phase1 用 LoRA（r=8, α=16）适配 WavLM-Large，分层度量学习——条件 AAM-Softmax（可训 margin）+ EMA Center Loss；课程先分架构族（LLM-Codec、Diffusion、Flow-Matching 等）再分细粒度合成器。Phase2 对 MLAAD v9 中 2025 后 Set2 模型做 few-shot 原型注册（文中经验阈值约 K≈36 稳定质心），真实语音用 VoxCeleb2 性别条件三原型。Phase3 余弦近邻检索，无参数更新。训练/注册/评测数据严格分离，ASVspoof 5 Track1 open 仅用于评测。

## 实验与结果
ASVspoof 5 open：单系统 EER 0.49%、minDCF 0.09，优于挑战最佳单系统与多数集成；actDCF 0.97 显示度量学习分数校准偏弱。渐进注册 Set2 时族/模型准确率升至 92.0%/90.3%，加 3-way 真实原型后达 99.0%/97.0%，EER 至 0.49%。t-SNE 显示真伪宏分离与族内聚类。

## 结论
分层度量学习 + 推理时原型锚定可在开放世界同时做检测与源归属，无需为新合成器重训。后续需分数校准与对抗扰动鲁棒性。

## 点评
把“谁合成的”做成可扩展原型库，比闭集归因更贴近取证部署。强在时间划分模拟零日与真实流形多原型；弱在 actDCF 偏高、原型样本数依赖经验阈值，且超低 EER 对划分与原型完备性敏感。
