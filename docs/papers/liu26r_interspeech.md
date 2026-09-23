# P-SED : Asymmetric Prototype Metric Learning for Weakly Supervised Speech Emotion Diarization

- 论文编号：2388
- 报告人：Nurmemet Yolwas
- 程序：Monday 28 September 2026 / Paralinguistics
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/liu26r_interspeech.pdf

## 问题

Speech Emotion Diarization（SED）要对连续语音中情感事件的起止与类别做细粒度定位，但帧级标注极稀缺（公开 ZED 仅约 17 分钟），难以全监督训练。弱监督常用 MIL：极端池化监督过稀，把句级标签铺到全帧又易在静音/过渡段引入噪声。需要在仅有句级标签时仍能定位连续情感片段。

## 方法

P-SED：WavLM 提帧特征，投影并 L2 归一化到单位超球面，与可学习情感原型（含 Neutral）做温度缩放余弦相似度得帧 logits。正交正则 L_orth 抑制“中性主导坍缩”。弱监督用非对称优化：Class-aware Prototype Contrastive Loss（CPCL）对中性袋用多类 CE，对情感袋仅对比目标情感相对中性的响应并动态伪标；Top-K ranking loss 在情感袋上对 top-p% 显著帧施 margin 约束。另有句级加权池化辅助分类。推理对各类概率序列做 Total Variation Denoising（TVD）再归一化，抑噪同时保锐利边界。

## 实验与结果

IEMOCAP（Happy/Angry/Sad/Neutral，Session 1–4 训、5 验）作弱监督训练，ZED 作帧级测试。同 WavLM 骨干下，P-SED+TVD 的 EDER 为 47.00%，优于 frame-wise CE（56.52%）、ENT/FENT（55.16%/54.37%）及 MA/GEP 后处理；无后处理 RAW 为 50.67%。消融去掉原型、正交、CPCL 或 Top-K 均升高 EDER；Top-K 比例约 0.6 较好。配对 t 检验相对基线显著（p<0.05）。

## 结论

正交原型空间 + 非对称显著实例挖掘 + TVD，可在仅句级标签下做连续情感定位，并在 ZED 上优于对比弱监督基线。局限：固定比例挖掘难适应快速多变情绪转换；测试集规模小，泛化评估受限。未来拟自适应挖掘、上下文序列建模与更大帧标注集。

## 点评

抓住 SED 的结构难点：中性背景占时长、情感局部连续、弱标签易确认偏置。把“目标情感 vs 中性”做成袋级二元对比，再用 Top-K 补局部边界，比单纯 max-pool 更贴合情感事件形态。脆弱点是依赖 IEMOCAP→ZED 的跨语料迁移与固定 p，真实对话情绪更碎时可能漏检；EDER 仍较高，说明弱监督 SED 距离可用仍远。
