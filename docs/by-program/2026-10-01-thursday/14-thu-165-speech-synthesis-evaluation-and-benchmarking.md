# Speech Synthesis Evaluation and Benchmarking

- 日期：2026年10月1日（星期四）
- 时间：09:00-11:00
- 形式：Poster
- Area：7
- 论文数：12
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场集中质疑并重建 TTS/歌声/笑声合成的评测范式：多音字、音系忠实度、嗓音重建、笑声音素、日语 G2P、情绪嵌入相似度、短语停顿多参考、野外离散 token TTS 的客观 MOS，以及歌曲细粒度维度与自然多语速 STSM、GSLM 码率与带不确定性的 MOS。主线是“好听”不等于音系/任务成功，且许多客观代理在分布外失效。

语言与音系侧，PolyBench 暴露 LLM-TTS 多音准确率天花板；音系分类器审计 ATR 和谐；日语 G2P 显示解析模式优于直出，并惠及假名输入 TTS。任务对齐评测用 BWS 情境框架与双参考分布度量服务嗓音重建；笑声合成比较自动/人工音素标注与 SPSS vs audio-LLM。

客观指标批判贯穿：情绪嵌入相似度易奖励声学模仿；野外离散 TTS 上 UT-MOSv2 等相关性崩塌；DNSMOS 对加性噪声与生成伪影的惩罚与听感矛盾。SongBench、GRATS、GSLM 码率消融与 ConformalMOS 分别补细粒度诊断、真实语速参考、低码率可行性与区间覆盖保证。

## 技术内容

### 语言、音系、G2P 与嗓音/笑声任务评测

**PolyBench: Benchmarking LLM-based TTS Systems for Chinese Polyphone Disambiguation**（论文 998；Feifan Chen）  
覆盖 494 多音字与 88 多音词的三类测试集，并探索 LALM 自动标音；评测 17 个开源系统，最佳多音字准确率仅 82.02%，方言/口语/文学类别差距显著。

**Towards a Phonology-Informed Evaluation of Multilingual TTS**（论文 3311；Neeraj Kumar Sharma）  
用人声训练的分类器审计合成是否保持语言特异音系模式；阿萨姆语 ATR 元音和谐上，[+ATR] 中元音约 1/3 被实现为 [-ATR]，人声无此偏置；词级预测标签比转写标签更能刻画和谐。

**An Evaluation Framework for Text-to-Speech Voice Reconstruction**（论文 2600；Ariadna Sanchez）  
主观用情境化 BWS 评可懂与说话人身份；客观引入双参考分布度量刻画可懂—身份权衡。对 193 说话人、17 个零样本 TTS 显示框架更贴嗓音重建任务。

**Evaluating Automatic Laughter Phone Annotation for Socially-Situated Laughter Synthesis**（论文 2141；Hiroki Mori）  
十一说话人新标注集训练改进笑声音素识别器，并分别用人工/自动标签建 SPSS 与 audio-LLM 合成器。听测：audio-LLM 自然度更高，SPSS 笑声方式可复现更好；自动标签系统未达人工标签水平。

**Benchmarking Large Language Models for Grapheme-to-Phoneme Conversion: A Japanese Case Study**（论文 1800；Tomoki Koriyama）  
超 30 个 LLM 在 3000 人工句上对比传统形态分析：最佳 LLM 假名 CER <0.52%（传统最佳 1.03%）；parse 模式通常优于 direct；LLM 假名再进 TTS 发音优于端到端 TTS。

### 客观指标失效、多参考与领域基准

**The False Resonance: A Critical Examination of Emotion Embedding Similarity for Speech Generation Evaluation**（论文 39；Yun-Shao Tsai）  
对抗任务与人类对齐显示，尽管分类准，情绪嵌入余弦相似度不适合零样本情感评测：语言/说话人干扰淹没情感特征，指标与感知错位并奖励声学模仿。

**LLM-Based Multi-Reference Evaluation for Efficient and Robust Assessment of Phrase Break Annotations**（论文 2225；Hoyeon Lee）  
LMRE 由少量示范生成多种合法韵律切分，建模一对多短语边界。韩语 1356 标注、五策略上相对单参考与人类判断更一致。

**Investigating the Relationship between Objective AI-driven Metrics and Subjective MOS for In-the-Wild Speech**（论文 2203；Shekhar Nayak）  
768 条头戴筛选自然度评分：UT-MOSv2 在连续干净 TTS 上 r=0.51，在离散野外 MQTTS 上崩至 r≈−0.01；DNSMOS 对加性噪声惩罚重于生成伪影，与听感矛盾。

**SongBench: A Fine-Grained Multi-Aspect Benchmark for Song Quality Assessment**（论文 1985；Dapeng Wu）  
七维（人声、乐器、旋律、结构、编曲、混音、乐感）专家标注 11717 样本；与专家评分高相关，作诊断基准暴露 SOTA 细粒度差距。

**GRATS : A Natural Multi-Speed Mandarin Dataset for Speech Time-Scale Modification Benchmarking**（论文 1842；Yu Tsao）  
25 说话人、五语速（0.5×–1.5×）自然平行普通话数据，可对照真实目标语速录音；基准显示可懂—感知质量权衡及极端语速下时序/音高一致性劣化。

**On the Effect of Segmentation Width and Cluster Size on Speech Resynthesis and Continuation in Generative Spoken Language Models**（论文 999；Shunsuke Kando）  
固定宽切分与多种 K-means 码率下，较低码率仍可清晰自然重合成且续写质量稳定，提示常规 GSLM 设置可能冗余；LLM 指标与主观相关仍偏低。

**ConformalMOS: Uncertainty-Aware MOS Prediction with Conformal Intervals and Ordinal Modeling**（论文 572；Tashfain Ahmed）  
共形预测给出有覆盖保证的 MOS 区间，训练上将 one-hot 高斯平滑为序感知目标。BVCC 上 MSE=0.08 且经验覆盖有效。

## 本场要点

- 多音、音系忠实与 G2P 暴露“自然度”之外的语言学短板。
- 嗓音重建与笑声合成需要任务对齐的主观/客观框架，自动标注仍不及人工。
- 情绪嵌入相似度与野外客观 MOS 常与人类感知脱节。
- 歌曲细粒度、自然多语速 STSM、GSLM 码率与共形 MOS 区间补齐诊断与可靠性工具。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 998 | PolyBench: Benchmarking LLM-based TTS Systems for Chinese Polyphone Disambiguation |
| 3311 | Towards a Phonology-Informed Evaluation of Multilingual TTS |
| 2600 | An Evaluation Framework for Text-to-Speech Voice Reconstruction |
| 2141 | Evaluating Automatic Laughter Phone Annotation for Socially-Situated Laughter Synthesis |
| 1800 | Benchmarking Large Language Models for Grapheme-to-Phoneme Conversion: A Japanese Case Study |
| 39 | The False Resonance: A Critical Examination of Emotion Embedding Similarity for Speech Generation Evaluation |
| 2225 | LLM-Based Multi-Reference Evaluation for Efficient and Robust Assessment of Phrase Break Annotations |
| 2203 | Investigating the Relationship between Objective AI-driven Metrics and Subjective MOS for In-the-Wild Speech |
| 1985 | SongBench: A Fine-Grained Multi-Aspect Benchmark for Song Quality Assessment |
| 1842 | GRATS : A Natural Multi-Speed Mandarin Dataset for Speech Time-Scale Modification Benchmarking |
| 999 | On the Effect of Segmentation Width and Cluster Size on Speech Resynthesis and Continuation in Generative Spoken Language Models |
| 572 | ConformalMOS: Uncertainty-Aware MOS Prediction with Conformal Intervals and Ordinal Modeling |
