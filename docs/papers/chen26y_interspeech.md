# Improving Flow Matching based Text-to-Speech with Dual-Model Preference Optimization and Classifier-Free Guidance

- 论文编号：2412
- 报告人：Minchuan Chen
- 程序：Thursday 1 October 2026 / Flow Matching for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/chen26y_interspeech.pdf

## 问题
流匹配零样本 TTS 常用 CFG，但常规训练/推理难以有效融入人类反馈，训练目标与评测指标（可懂度、说话人相似、自然度）存在错配；同输入不同采样质量波动大。单模型同时编码偏好/非偏好易产生参数冲突，CFG 也未利用偏好信号。

## 方法
基于 F5-TTS Small，提出 **PA-Dual** 统一框架：
1. **双模型偏好优化**：从同一参考模型初始化 preferred / dispreferred 两个模型；用统一 DPO 式目标分别拟合 win/lose 分布，避免单模型权衡。偏好对用 WER、SSIM 等代理指标构造（GT vs 生成、模型多样本 Pareto 排序；含常规与舌尖/重复等困难文本）。
2. **采样引导**：将两模型速度场与代理 prompt \(\hat{c}=-\alpha c+(1+\alpha)\phi\) 结合，用三项目标推向偏好、排斥非偏好，并减少前向次数。
3. **改进 CFG**：引入优化尺度因子 \(s\)（条件速度在无条件方向上的投影）与 early-step zero-init，稳定早期 ODE 步。

## 实验与结果
预训练：WenetSpeech4TTS Premium（945h 普通话）+ LibriTTS（约 585h）。偏好集 DT1/DT2/DT3 各 2000 对。Seed-TTS test-zh/en：PA-Dual(w/ DT3) 中文 WER 2.87、SSIM 0.634、UTMOS 2.728；英文 WER 2.38、SSIM 0.625，全面优于 Baseline 与单模型 PA-Base。数据效率：约 250 对即可让 WER 趋稳，SSIM 约 500 对趋稳。CFG \(\omega=2.5\) 较优；消融显示 zero-init 对 TTS 增益更明显。主观 CMOS/SMOS 与客观趋势一致。

## 结论
双模型分别建模偏好与非偏好，并与改进 CFG 协同，可用少量偏好数据提升流匹配零样本 TTS 的可懂度、说话人相似与自然度。后续拟用蒸馏/LoRA 降低双模型开销。

## 点评
把图像领域里「正/负偏好分模」迁到语音，并用 WER/SSIM 作可扩展代理，抓住了 FM-TTS 训练目标与听感指标错配。强在数据效率与困难文本对构造；脆弱点是推理需维护两套权重、代理指标可能与真实听感不完全一致，以及偏好对质量高度依赖排序策略。
