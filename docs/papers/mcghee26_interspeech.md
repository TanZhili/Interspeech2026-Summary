# Feature Design and Generative Modelling in Deep Articulatory Synthesis

- 论文编号：694
- 报告人：Charles McGhee
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/mcghee26_interspeech.pdf

## 问题
用合成评估发音反演时，常把反演丢失的信息（F0/能量/说话人等）显式或隐式加回；结果可能不再代表反演得到的发音，却很少系统分析特征与建模类型对语音内容的影响。

## 方法
基于 ArtVVN（舌/唇/颌 6×2D + 鼻音/浊音 2D，共 14 维）训级联合成器（Conformer→mel→冻结 BigVGAN）。对比加 WavLM 说话人嵌入、F0+STE 源特征，以及 Conditional Flow Matching（DiT，Euler，主结果 NFE=2）。对照 SPARC 声码器与更大容量 Conformer（12 层、hidden 768）。

## 实验与结果
训于 LibriTTS-R clean-100（Large 另加 360）；测 test-clean 与平行 noisy/clean VCTK。源特征降低 in-domain PER，但 noisy 条件下 PER/MSE 恶化更明显，说明小模型会依赖源特征重建音素。Large+Spk 可接近「+Src」的音素一致性。FM 在低 NFE 与非生成模型音素一致性相近；提高 NFE 使 PER 升、UTMOS 升（约 NFE≥10 趋于平稳）。最小对特征替换：替换源特征显著伤辅音准确率（约 84.9%→75%），并引入大跨度混淆（如 /E/–/u/、/b/–/n/）。

## 结论
附加说话人尤其是源特征会扭曲发音合成的音素内容；CFM 可在低 NFE 保持一致性、用更高 NFE 换质量。用合成结果对反演下结论时必须谨慎设计输入与模型。

## 点评
把「评估用合成」本身当研究对象，直接挑战领域常见做法；特征替换实验把依赖关系做成可测证据。对想用 ASR-PER 闭环评估反演的工作，这是很实用的警示。
