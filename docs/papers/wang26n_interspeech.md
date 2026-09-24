# Towards Interpretable Framework for Neural Audio Codecs via Sparse Autoencoders: A Case Study on Accent Information

- 论文编号：811
- 报告人：Shih-Heng Wang
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/wang26n_interspeech.pdf

## 问题
Neural Audio Codec（NAC）广泛用于语音系统，但离散表征如何编码语言与副语言信息仍不清晰；尤其口音这类纠缠因素，缺少可量化的任务级可解释性框架。

## 方法
对 utterance 级 NAC 表征 u（时间均值池化）训练 TopK Sparse Autoencoder 得到稀疏激活 z；再用 logistic regression 做口音二分类。将 z 分解为 position（激活位置二值）与 magnitude（top-k 幅值排序）两路分别探针。用相对指标 ΔF1=F1_SAE−F1_ref（相对各 NAC 在 u 上的参考 F1）比较可解释性，避免原始口音信息量不同导致的不公。

## 实验与结果
数据来自 Vox-Profile：US vs. UK 与 US vs. Non-US-UK。覆盖 EnCodec（1.5/6/12 kbps）、DAC、Mimi、SpeechTokenizer，共 16 组 (latent ratio q×相对稀疏 s) SAE。参考 F1 上 SpeechTokenizer/Mimi 更高，但可解释性上 DAC（US vs. UK 16 配置中 13 次第一）与 SpeechTokenizer（Non-US-UK 14/16 第一）更强。声学导向 NAC 口音信息更偏激活幅值；语音学导向更偏激活位置。EnCodec 低码率（1.5 kbps）ΔF1 掉幅更小，可解释性高于高码率变体。

## 结论
提出以 SAE+ΔF1 量化 NAC 任务级可解释性的框架，并以口音为案例表明：原始口音信息多≠可稀疏分解；编码方式随 NAC 目标（声学/语音学）与码率而异。

## 点评
用相对性能而非绝对 F1 比较可解释性，避免“信息多就显得可解释”的混淆；position/magnitude 分解给出可操作的编码差异。局限是任务级代理、口音二分类，且低维 NAC（如 EnCodec）的绝对稀疏容量可能影响公平性，正文亦有说明。
