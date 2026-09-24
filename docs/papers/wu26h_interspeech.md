# SongBench: A Fine-Grained Multi-Aspect Benchmark for Song Quality Assessment

- 论文编号：1985
- 报告人：Dapeng Wu
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/wu26h_interspeech.pdf

## 问题
Text-to-Song 评测缺专业粒度；SongEval 等维度语义重叠且分数挤在高分区间，难区分日益接近的顶尖模型。

## 方法
按作曲要素定义七维：Vocal、Instrument、Melody、Structure、Arrangement、Mixing、Musicality（1–10）。用 Hunyuan 生成歌词/提示，收集 Suno 多版本、LeVo、SongBloom、ACE-Step 与真人版权曲等约 2 万样本，经专家校准与过滤得 11717 条标注（约 683.5 小时，中英约半）。以 MuQ 为骨干训自动预测器，并建 352 条外部模型 OOD 集。

## 实验与结果
OOD 上 utterance 级各维 LCC/SRCC 多超 0.78；system 级 LCC>0.95。Musicality 相关显著高于 SongEval。模型对比能拉开 Suno v4.5→v5、MiniMax 等迭代增益，而 SongEval 近乎平台。AB 测试：同模型内判别准确率（LeVo 64%、Suno 62%）明显高于 SongEval（约 43–55%）。

## 结论
SongBench 提供更解耦、更高分辨率的歌曲质量基准与自动评估工具，有助于诊断生成短板。

## 点评
把“好听”拆成可操作的制作维度，直接针对评分压缩与维度纠缠。自动器强依赖专家标签分布；Musicality 仍偏整体审美，与其余六维的独立性需持续监控。
