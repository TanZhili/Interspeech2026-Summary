# Low-Resource Medical ASR for Rich Transcription in Latvian

- 论文编号：3469
- 报告人：Arturs Znotins
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/znotins26_interspeech.pdf

## 问题
拉脱维亚语医学口述需富文本转写（标点、缩写、数字、单位、术语），域数据仅数十小时；通用模型 WER 可从个位数升至 12–46%，规则 ITN 难维护。

## 方法
对比端到端富文本微调（Whisper/Canary/Gemma-3n）与“逐字 ASR + LLM 格式化”。用 Gemini 将遗留逐字稿与人工报告配对生成格式化标注，并扩 75 h LLM 校正伪标签（WER>15% 丢弃）。指标含 WER、标点/命令/数字/医学实体错误率。训练：先通用拉脱维亚再 LVMED。

## 实验与结果
通用基线极差；ft-whisper-large-v3 达 11.1% WER，加伪标签 10.6%；双阶段 Whisper+ft-gemma3-12b 约 11.2%，标点命令最好（PC-ER 2.1%）。跳过通用语适应或仅有通用数据均更差。学习曲线显示数据少时 LLM 管线更优，数据充足时两端到端接近。

## 结论
有限域数据 + LLM 策展/伪标可使低资源医学富文本 ASR 达可用质量；端到端与 ASR+LLM 在足够域数据下竞争力相当。

## 点评
实用路线是“活化遗留逐字语料 + 伪标扩量”，指标设计贴临床格式需求。临床幻觉风险作者自承；依赖已有人工报告做策展，无报告场景需更多人工核验。
