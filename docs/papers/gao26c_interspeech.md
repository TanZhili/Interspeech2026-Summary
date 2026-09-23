# UD-ASD: A Unified Diffusion Model for Anomalous Sound Detection

- 论文编号：482
- 报告人：Pengxiang Gao
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gao26c_interspeech.pdf

## 问题
异常声音检测常为每台机器单独建模，泛化差、异常覆盖窄。扩散模型有条件生成能力，能否用统一模型跨机型监测。

## 方法
UD-ASD：log-Mel 输入；轻量模块把机器 ID 编成条件嵌入，引导扩散重构该机正常数据；用 GMM 拟合重构误差分布判异。统一模型跨机型/域学习；DDIM 采样加速推理（约 24.4M 参数，A40 上约 0.32 s/clip）。在 DCASE2022 Task 2 评测。

## 实验与结果
相对官方基线摘要称 AUC +3.44%、pAUC +2.52%。Table 2：UD-ASD-U 调和平均 AUC/pAUC 约 77.16 / 62.80，优于 Official-AE/CLS 与多种生成式方法；分机型上 Fan/Slider 等较强、Valve 等较弱。

## 结论
作者认为条件扩散统一模型可跨机型 ASD，并用重构误差分布做异常度量。

## 点评
“一小块条件模块 + 统一扩散”降低每机一模型成本，跨域共享特征是卖点。扩散推理延迟与对未见故障模式的覆盖仍是工业落地约束；分机型表现不均提示条件嵌入未必学到同等质量的机型流形。
