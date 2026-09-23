# CAL-MOS: Bridging Layers with Adapters for Robust MOS Prediction Across Speech Foundation Models

- 论文编号：2960
- 报告人：Alef Iury Ferreira
- 程序：Monday 28 September 2026 / Evaluation of Speech and Audio Analysis
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/ferreira26_interspeech.pdf

## 问题

非侵入 MOS 预测广泛依赖语音基础模型（SFM），但哪一层最有用、如何跨层融合，随骨干与数据集强变化；朴素加权求和跨设置不稳定，全量微调又贵。

## 方法

在统一协议下评测 10 个 SFM（wav2vec2 Large、XLS-R/MMS 300M 与 1B、WavLM/HuBERT/data2vec Large、Wav2BERT、Whisper Large-v3）于 BRSpeech、BVCC、SingMOS、TMHINT-QI。策略含 Last Layer、Best Layer、Weighted Sum、Full Fine-Tuning，以及 Adapter+Mean（A+M）：每层独立适配器（线性—LN—ReLU—线性）后再拼接均值池化，骨干冻结。报告 utterance/system 级 MSE 与 SRCC。

## 实验与结果

层间热图显示最佳深度高度依赖骨干与数据集，早期到中层常优于末层。朴素 WS 不稳定；A+M 在多骨干上显著提升冻结方案鲁棒性，缩小与 FT 差距（如 WavLM/XLS-R/HuBERT 等 A+M 在多集上 SRCC 接近或可比强微调）。更大参数未必带来清晰平均 SRCC 优势。

## 结论

MOS 预测的层选择无通用答案；在冻结骨干前提下，先做逐层校准再聚合比直接加权更稳，可作为全量微调的实用折中，并给出跨模型层利用指南。

## 点评

把“用哪一层”做成可复现扫描，并给出适配器校准这一可落地补丁，对工程选型很有用。A+M 仍增加可训参数与实现复杂度；未覆盖全部新 SFM，结论外推需再验证。
