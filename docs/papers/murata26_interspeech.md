# Exploring Pre-training Benefits on Phoneme Addition through Fine-tuning in Speech Synthesis

- 论文编号：208
- 报告人：Masato Murata
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/murata26_interspeech.pdf

## 问题
低资源 TTS 常先高资源预训练再微调；目标语含未见音素时需“音素添加”（扩展嵌入并随机初始化）。预训练已见音素能力是否真正帮助学会新音素，此前多只报整体自然度，证据不足。

## 方法
两设定：(1) 仿真——用 LLM 生成 Limited（排除目标音素）与 Full（含全部）语料，同一说话人/语言 TTS 合成，隔离语种与说话人混淆；目标组为爆破音或前元音。(2) 真实跨语——VCTK 英预训练 → JSUT 日微调，添加 20 个日语特有音素。Conformer-FastSpeech2，微调 vs 同数据从头训；数据量 100–2000 句。指标：目标音素 PER（wav2vec2 识别）与 UTMOS。

## 实验与结果
仿真与跨语一致：微调 UTMOS 优于或持平从头训（尤其低资源）；但达到相近 Target PER 所需数据量 ≥ 从头训，甚至更差。低资源下从头训爆破闭合模式更清晰；微调在保住已见音素时更难学新音素。

## 结论
预训练主要提升合成自然度，对音素添加本身帮助有限——与“预训练语言知识必然利于新音素”的常见假设相反。建议更广音素库存预训练或专为新音素设计辅助损失。

## 点评
用可控仿真拆开“自然度”与“新音素习得”，结论反直觉但证据链完整，对低资源跨语 TTS 实践有直接提醒：别指望随机扩嵌入就能自动借力预训练。仿真用合成语音，声学分布可能偏乐观；跨日语结果能部分对冲这一顾虑。
