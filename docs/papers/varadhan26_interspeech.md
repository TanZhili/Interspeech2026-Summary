# IN-F5: Adapting an English TTS Foundation Model for Multilingual and Zero-Resource Indian Speech Synthesis

- 论文编号：3366
- 报告人：Praveen Srinivasa Varadhan
- 程序：Tuesday 29 September 2026 / Low-Resource Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/varadhan26_interspeech.pdf

## 问题
英语大模型 TTS 已近人类水平，印度多语低资源场景难以从零复现；是否可用英语 F5-TTS 作先验，在严格数据预算下获得克隆、多语、语码混合等涌现能力，尚缺受控证据。

## 方法
扩展字符词表至 685 token（11 语原生脚本），比较三种策略：从零训 IN11、直接 EN→IN 微调、EN→EN+IN 混合微调。IN11 约 1417 h（IndicTTS/LIMMITS/Rasa/众包/IndicVoices-R）。再做 1/10/100 h 每语缩放；对无资源 Bhojpuri、Tulu 用相关脚本说话人合成 + 母语核验。

## 实验与结果
直接 EN→IN 总体 MUSHRA 最高（73.4），优于混合与从零（43.2）；见说话人自然度可与真人持平或略高。涌现：零样本克隆、跨语族 polyglot、语码混合与 Rasa 风格表达均较强。10 h/语已接近 100 h 多数能力；零资源 Bhojpuri 可达约 86 MUSHRA。相对既有 Indic TTS，IN-F5 MUSHRA 80.5（表 5 设定）。

## 结论
英语基础 TTS 经直接微调即可成为低资源印度多语先验，并支撑零资源跨语启动；不必持续混入英语数据。

## 点评
受控对比直接挑战“继续混高资源语更好”的直觉，实用性强。合成音有时高于真人，可能部分来自更干净、少瑕疵的生成偏置。语码混合在不自然语对上仍弱；从零失败也强调预训练不可替代。
