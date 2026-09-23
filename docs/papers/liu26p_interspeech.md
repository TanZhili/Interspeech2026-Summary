# audiobook-cc: Controllable Long-context Speech Generation for Multicast Audiobook

- 论文编号：2125
- 报告人：Min Liu
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/liu26p_interspeech.pdf

## 问题
现有 TTS 偏单句，有声书多角色长篇缺少句间上下文建模与细粒度情感/音量/语速控制；提示音易把韵律绑定到 prompt，损害语义–韵律对齐与角色一致性。

## 方法
Audiobook-CC 基于 cosyvoice2（改用 BigVGAN）：AR 语音 LM 输入说话人嵌入 \(V\)（Cam++，来自同说话人但语义无关句）、前后文文本序列 seqC、离散属性控制 seqE（九类情感×四级强度、音量、语速）、文本与语音 token。解耦训练：timbre/persona 来自 \(V\)，韵律由当前文本与上下文决定。控制标签由 LLM 解析后规则归一；用自蒸馏合成高强度情感数据（PER<2%、SS>0.7 等过滤）缓解稀缺。三阶段微调（约 100 万→15 万上下文+指令→自蒸馏增强小时量级数据）。

## 实验与结果
章节级 M-MOS 4.25（Infer-ctx&inst），相对最强基线约 14% 相对提升；对话 S-MOS 4.11。ABX 上 Infer-ctx&inst 章节偏好 73.0%。解耦相对非解耦显著提高 S-MOS（约 3.45→3.93）；高强度–低强度情感区分在 Text-Unrelated 上明显强于 cosyvoice2；自蒸馏降低 PER 并恢复情感 F1。

## 结论
作者认为上下文机制、风格–提示解耦与自蒸馏共同提升多角色有声书的连贯性、语义对齐与情感可控性。

## 点评
针对有声书特有的“角色稳定 + 语义驱动韵律 + 长文连贯”三角，用无关内容说话人嵌入解耦是关键设计。控制离散化便于组合指令。依赖大规模内部有声书/剧集数据与章节标注，复现门槛高；后文上下文在推理时依赖已知剧本，对开放式生成需另想办法。
