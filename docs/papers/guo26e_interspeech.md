# DEBATE: A Dataset for Disentangling Textual Ambiguity in Mandarin Through Speech

- 论文编号：3146
- 报告人：Haotian Guo
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：https://www.isca-archive.org/interspeech_2026/guo26e_interspeech.pdf

## 问题
中文书面语因多音字、无显式词界与重音缺失易产生歧义，文本消歧研究较多，但“通过语音消歧”（DTS）缺乏成对的歧义文本与含发音/停顿/重音线索的口语数据。

## 方法
构建公开中文语音–文本数据集 DEBATE：从开源歧义语料、社交媒体与公考言语理解题收集句子，人工筛入三类任务——多音字（TPronu）、韵律停顿切分（TPause）、重音焦点（TStress）；标注发音、“/”停顿与“<>”重音，并由 LLM+人工审校生成语义解释。10 名母语者（年龄/性别均衡）用自备设备录音；双人协作纠错；SenseVoice-small CER 作质量对照。零样本评测 Qwen2-Audio、Qwen2.5-Omni、Gemini 2.0 Flash：听音频后在二选一释义中作答；并与三人人工听辨对比。

## 实验与结果
共 1001 条歧义文本、10010 条音频、约 9.66 小时（三类约 2000/4010/4000 条）。ASR CER：TPronu 4.75%、TPause 2.82%、TStress 1.94%。
模型最优约：TPronu Acc 65.65%（Qwen2.5-Omni）、TPause ~68%、TStress 最佳 58.83%（Gemini）；重音任务接近随机。小规模人工集上人类显著高于模型且更稳定。

## 结论
DEBATE 首次面向普通话语音消歧；现有大语音语言模型对停顿/多音字有一定能力，但对细粒度重音远弱于人。数据亦可服务 TTS 同形异音与重音渲染研究。

## 点评
把三类“文本看不见、语音看得见”的歧义拆成可评任务，填补了 DTS 数据空白。当前基准是封闭二选一零样本，开放生成与交互消歧会更难；录音设备与自备麦增强生态效度，也可能引入通道噪声，解释模型失败时需一并考虑。
