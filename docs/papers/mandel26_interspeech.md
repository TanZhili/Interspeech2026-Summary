# From A to B to A: Palindromic Zero-Shot Voice Conversion with Non-Parallel Data

- 论文编号：1663
- 报告人：Moshe Mandel
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/mandel26_interspeech.pdf

## 问题
非平行 any-to-any 零样本 VC 常靠内容–说话人解耦，易泄漏身份或丢内容；纯 KNN-VC 在短参考下邻居稀疏、质量崩。需要能从非平行数据构造可监督训练信号的方案。

## 方法
回文（palindromic）训练：用 WavLM 特征上的 KNN-VC 把真实目标片段 \(a_1\) 映射成合成源 \(\hat B_1\)，再训 Transformer 把 \(\hat B_1\)（加目标参考 \(A_2\)）还原到目标，波形级用预训练说话人验证损失强化身份。三阶段：先 WavLM→波形 vocoder，再训转换器，再对转换特征重训 vocoder。推理时输入真实源、短目标参考。

## 实验与结果
仅英文 LibriSpeech 训练。英语上各 prompt 时长 Spk Sim/EER 优于 Seed-VC、KNN-VC、Vevo、OOVC，WER/CER/MOS 可比；3 s 参考仍稳健（相对 KNN-VC 优势最大）。多语 LibriSpeech 无微调下 WER 常最佳，相似度与 DNS-MOS 可比。vocoder 后训练抬高 DNS-MOS、抑制伪影。

## 结论
合成→真实回文监督 + 波形说话人损失，可在非平行数据上做强零样本 VC，并跨语泛化。

## 点评
把 KNN-VC 从“推理算法”变成“造平行对的数据工厂”，短参考场景收益最大。依赖离线 KNN 质量与额外 SV 模型；超大规模/高表现力数据与流式仍待扩展。
