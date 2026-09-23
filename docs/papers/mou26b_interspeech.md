# Dynamic Prosody Prediction in LLM-based TTS for Improving Speaker Similarity

- 论文编号：2312
- 报告人：Zhenwei Mou
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/mou26b_interspeech.pdf

## 问题
个性化 LLM-TTS 常整体建模参考语音属性；显式韵律多为整句静态预计算（如 CoT），忽略已生成语音中的风格信息，限制说话人相似。

## 方法
在 CosyVoice LLM 上按音节动态预测韵律：音节韵律向量（时长、能量均值、基频均值与范围）经 k-means（512）量化；每音节先用 PQ 嵌入在已生成韵律/语音 token 条件下预测韵律 token，再条件生成该音节语音 token。训练 CE 损失加权 \(\alpha=0.5\)。约 50k 小时中文数据。

## 实验与结果
相对 CosyVoice(50k) 与静态 CoT：MOS 自然度相当或略好；偏好测试在 ESD/内部集上更偏好提出方法（约 48–52% vs 对方约 29–33%）。客观：三测试集 CER 更低；ESD 情绪 SIM/ACC 与能量 RMSE 等多项更好。作者还观察到动态预测有助于缩小小规模与大规模训练间的韵律学习差距。

## 结论
作者认为把已生成语音纳入音节级韵律预测可增强风格学习，从而提升说话人相似且不损自然度。

## 点评
相对“先整句韵律再语音”的 CoT，闭环利用自生成历史更贴合说话风格的时序依赖。实现绑定 CosyVoice 与音节级中文设定；韵律离散化粒度（512）与采样超参对风格保真仍敏感。
