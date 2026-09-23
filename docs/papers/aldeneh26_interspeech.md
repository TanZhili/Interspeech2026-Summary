# Which Data Matter? Embedding-Based Data Selection for Speech Recognition

- 论文编号：3073
- 报告人：Zakaria Aldeneh
- 程序：Monday 28 September 2026 / Robust and Efficient ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/aldeneh26_interspeech.pdf

## 问题
大规模伪标注野外数据利于通才 ASR，但专科模型容量有限、无法消化全部异构数据。如何从约 **100k 小时** 源数据中选出贴合目标域的子集，仍缺系统答案。

## 方法
用互补嵌入刻画样本：说话人（MFA-Conformer）、语音/音素（WavLM Base+ 均值池化）、语义（SBERT）；再做 **batched greedy MMR**（相关–多样权衡 \(\lambda\)，相关预过滤、目标端 k-means 压缩）。在 Granary 英源上按目标域（LibriSpeech / CommonVoice / TED-LIUM）验证集选子集；训 CTC Conformer-Small（9M）与 Large（107M）。

## 实验与结果
- 全量 Granary 跨域优于仅在域内训练的专科数据（如 Conformer-Large：LS-clean 6.7 vs 仅 LS 的 3.2 但 CV/TED 更差；全量 Granary CV 25.4、TED 6.5）。
- 随机 5% 已接近全量；摘要称策略性选中的 **5% 子集相对全量最高约 36.8% 相对 WER 下降**。
（抽取在 Table 2 中途截断，MMR 主表数字不完全。）

## 结论
对专科 ASR，嵌入空间上兼顾相关与多样的数据选择可显著优于盲目用全量或随机子集；说话人/音素/语义轴需按目标域权衡。

## 点评
把信息检索里的 MMR 接到 ASR 数据策展，问题贴近工业“海量伪标→专科模型”。强在三轴嵌入与可扩展批选；**MMR 相对全量的完整对照表因截断不全**，36.8% 相对降幅以摘要为准。
