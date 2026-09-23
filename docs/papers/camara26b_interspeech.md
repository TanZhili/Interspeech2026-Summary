# Word Lengthening as a Function of Utterance Position: A Multi-Corpus Study

- 论文编号：1379
- 报告人：Mateo Cámara
- 程序：Monday 28 September 2026 / Tools and Techniques for Phonetic Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/camara26b_interspeech.pdf

## 问题
话轮转换需在数百毫秒内预测话轮结束；边界前延长是重要韵律线索。需检验：话轮末词是否更长、是否仅为词汇选择、延长集中在词内何处，以及跨语体/语言是否稳健。

## 方法
四语料、英西双语（Switchboard、Columbia Games、BU Radio、Glissando）：>500 说话人，约 **39,470** 话轮末 + **206,268** 句中词。比较话轮末 vs 句中时长；同说话人–同词配对；音节定位；对照 ToBI 式 break index。

## 实验与结果
- 基线：话轮末均长约 0.44 s vs 句中 0.24 s（差约 203 ms；\(d\approx1.22\)）；摘要池化约 **+91 ms**（\(d=1.14\)）。
- 严格配对：约 **+80 ms**（\(p<0.001\)；77% 配对为正）；约 92.8% 词型呈正效应。
- 效应主要在 **末音节**（话轮位置对比末音节 \(d=0.09\)，非末音节 ≈0）；高 break 词更长（高 vs 低约 +215 ms）。
- 朗读语料英西均见一致方向。

## 结论
话轮末延长是稳健、局部（末音节）的地板移交线索，与韵律边界强度并行，而非单纯选更长词。

## 点评
多样本、配对与音节定位把“话轮末更长”钉成边界 contr ol 而非词汇混杂，对对话系统与转写对齐都有用。强在跨语料一致；少数反转集中在截短的 backchannel 类词，提示范畴边界仍需小心定义。
