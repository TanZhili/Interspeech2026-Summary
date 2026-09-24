# Vimarsha: Faithful ASR Evaluation for Indian Languages with Demographic Diversity, In-the-Wild Audio and Spelling Variations

- 论文编号：3348
- 报告人：Kaushal Bhogale
- 程序：Tuesday 29 September 2026 / Multilingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bhogale26b_interspeech.pdf

## 问题
印度语 ASR 评测存在双向失真：干净受控语料带来乐观偏差；单一刚性参考又因拼写/语码混写变体惩罚合法输出，带来悲观偏差。缺少同时覆盖真实声学难度与多合法转写的基准。

## 方法
构建约 100 小时 Vimarsha，覆盖 22 种法定印度语言：Controlled On-Field（COF，43.3h，356 区、约 5099 说话人，朗读/即兴/电话对话）与 In-the-Wild（IW，56.1h）。IW 经多模型 CER 分歧与 BEATs 声学标签筛选难样本。用多 ASR 假设对齐并经 133 名标注员校验，构建 lattice of variations；以 OIWER（相对 lattice 最优路径）评测 10 个系统（IndicConformer、Saaras、Sarvam Audio、AWS/Azure/AssemblyAI/ElevenLabs/GPT-4o/Deepgram/Gemini 等）。

## 实验与结果
各模型在 IW 上均退化：领先系统由约 10–15% 升至 27–34% 平均 WER；AWS 相对增幅最大，GPT-4o 在 IW 近崩溃（约 89，个别语可达 150+）。I-Conf 两 split 领先且人口统计敏感度低（<2 点）；对话场景整体最难。地区 WER 跨度大（如 Bharuch 4.6 vs Koppal 54.9）。短句与极慢语速显著抬高 OIWER；Mantra/Choir 等事件普遍难，儿童喊叫等事件模型间分歧极大。

## 结论
真实声学与拼写容差会改变模型排名与部署判断；COF 不足以代表上线就绪。作者开源基准、协议与结果，以推动更贴近印度语言可变性的 ASR。

## 点评
同时纠正“测太易”与“判太严”，用 COF/IW 与 lattice/OIWER 形成完整评测叙事，对 Indic 选型很有用。强在覆盖 22 语与地理切片；弱在 IW 难样本筛选依赖现有 ASR/标签器，可能偏向特定失败模式，且部分语言时长偏短。
