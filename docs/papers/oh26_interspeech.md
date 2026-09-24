# L-Proto: Language-Aware Episodic Prototypical Training for Multilingual Speaker Verification

- 论文编号：410
- 报告人：Hyung-Seok Oh
- 程序：Thursday 1 October 2026 / TidyVoice2026 Challenge: Cross-Lingual Speaker Verification
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/oh26_interspeech.pdf

## 问题
多语说话人验证中，嵌入常把说话人与语言缠在一起，同说话人形成语言子簇；随机情节采样混语会扭曲原型估计。

## 方法
L-Proto：每情节只从单一语言采样 P 说话人 × K 句，流式缓冲按语构建情节；情节内用支持集均值原型 + 余弦温度 CE。总损失 = 全局分类 + λ·情节原型损失。在 VoxBlink2 预训练骨干上于 TidyVoiceX 微调。

## 实验与结果
TidyVoice 开发集：SimAM-ResNet34 EER 2.88→1.38，ResNet100 3.48→1.18；跨语试验（D/D、D/S）增益最大。ResNet/ECAPA/CAM++ 等多骨干均优于预训练与普通微调。质心分析：跨语同说话人相似度升、同语异说话人降。消融：单语情节优于随机/多语情节；情节采样与原型监督需同用。

## 结论
语言一致情节可稳定多语原型学习、缓解说话人–语言子聚类，在 TidyVoice 上跨骨干一致提升跨语验证。

## 点评
从任务构造而非对抗解耦入手，实现简单且效果清楚。依赖语言标签与语内足够说话人多样性，采样有额外开销；对极端低资源语改进不均匀，自适应情节仍是后续方向。
