# Towards Digital Preservation of Efik: TTS for a Low-Resource African Language

- 论文编号：1868
- 报告人：Offiong Bassey Edet
- 程序：Tuesday 29 September 2026 / Safeguarding Synthetic Speech: Ethical, technical and legal perspectives
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/edet26_interspeech.pdf

## 问题
Efik 为尼日利亚东南部下克罗斯语系声调语言（约 150 万母语者），缺乏公开可训 TTS 语料，数字保存与可用语音技术严重滞后；声调错误会改变词义。

## 方法
自建单说话人语料约 3.08 小时、2632 句（无线麦、安静室内；训/验/测 1975/264/393），材料来自小说、民间故事与教材；因 Whisper/XLS-R 强制对齐不可靠，全文人工转写并由母语者与语言学家校验。微调 VITS、MMS-TTS、SpeechT5、Orpheus-TTS；MMS 从约鲁巴 checkpoint 扩词表/嵌入以覆盖 ọ、ñ 等字符。5 名母语者评 MOS、Nat-MOS、A-MOS。

## 实验与结果
MMS-TTS 最高：MOS 3.80±0.63，Nat-MOS 3.60，A-MOS 3.04，且可生成约 3 分钟连贯长音频无明显幻觉；Orpheus 3.08、SpeechT5 2.48、VITS 仅 1.08。各模型对 ñ 等稀有音素仍困难；Orpheus/SpeechT5 长序列易崩溃并带外来口音，声调与文化韵律保留不足。

## 结论
给出 Efik 首个可复现端到端 TTS 基线；多语预训练的 MMS 在极低资源单说话人设定下最稳，但要自然、声调准确仍需更大、多说话人、声调感知建模。

## 点评
贡献以语料与系统性对照为主，切中数字不平等。强在人工标注质量与长音频对比；弱在单说话人 3 小时、评测人少，且会话主题落在“合成语音防护”下更偏保存/伦理语境而非深度架构创新。
