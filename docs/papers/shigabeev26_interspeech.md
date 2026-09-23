# Dialogs: a studio-quality expressive conversational Russian speech corpus for dialog assistants

- 论文编号：809
- 报告人：Ilya Shigabeev
- 程序：Tuesday 29 September 2026 / Datasets
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shigabeev26_interspeech.pdf

## 问题
俄语缺同时具备棚录质量、对话风格与句级情感/风格标注的公开语料；现有资源多为单人朗读或非受控网络数据，难训对话向表达 TTS。

## 方法
Dialogs：3 名演员面对面棚录 20.6 小时、11796 句、44.1 kHz 立体声；脚本作提示可即兴；12 类风格/情感众包标注；划分 19.9/0.30/0.37 小时。众包 MOS 对标 Ruslan、Natasha。用 VITS2 在训练集上训 615k 步作可行性验证。OpenRAIL 许可。

## 实验与结果
语料 MOS：Overall 4.15，表达力 4.11、对话自然度 4.08，显著高于 Ruslan/Natasha 的表达与对话维，音质/可懂度相当。VITS2 合成 Overall 2.83、表达 2.56、对话 2.59、UTMOS 3.36；单人时长不均（4.4–9.9 h）限制绝对质量，适合与更大数据混合。

## 结论
填补俄语棚录对话表达语料空白，可支撑表达/对话式 TTS 训练与评测；局限为表演式非完全自发、无叠语与噪声、说话人时长不平衡。

## 点评
定位清晰：用专业表演对话换可控标注与棚录质量。众包 MOS 维度设计贴合对话助手；单语料 VITS2 分数偏低符合数据量预期，价值在风格分布而非单独刷榜。
