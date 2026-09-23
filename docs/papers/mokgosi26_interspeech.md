# Tone-Conditioned Curriculum Learning for Low-Resource Bantu Speech Recognition

- 论文编号：2905
- 报告人：Vukosi Marivate
- 程序：Tuesday 29 September 2026 / Indigenous Voices in Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mokgosi26_interspeech.pdf

## 问题
南部班图语（isiZulu、isiXhosa、Sesotho、Setswana、Tshivenda、Xitsonga）基础 ASR 零样本 WER 常 >100%；声调扩展与短语轮廓编码语法意义，标准正字法常省略声调，通用微调忽视形态–声调难度梯度。

## 方法
混合难度 s(u)=0.7·WER_norm + 0.3·Tonal_norm（WER 来自冻结 Whisper 基线；声调特征：F0 转移率、独特模式、簇数、标准差与范围，Parselmouth，无强制对齐）。门控声调适配器（约 2.1M）按话语声调统计调制编码器输出。三阶段课程（40%→80%→全量，各约 650 步）。在社区语料 Swivuriso 上训 Whisper、W2V-BERT、MMS，匹配测 Swivuriso、迁移测 NCHLT。

## 实验与结果
跨库平均：W2V-BERT Tone-cond. 最佳 WER 28.41%；Whisper Multilingual 29.44%。Nguni 上 W2V-BERT 优于 Whisper 约 3–4 点；Sotho-Tswana 上 Whisper 更好（如 Setswana Tone+Curr. Swivuriso 18.60%）。Xitsonga 迁移：W2V-BERT Tone-cond. 23.79%，相对稳健；Tshivenda 匹配可至 17.23% 但 NCHLT 可升约 20+ 点。课程效果因架构/语言不一；MMS 上纯 WER 课程优于混合。

## 结论
无单一模型适合全部六语；应按语族选架构并跨语料验证。声调门控对 CTC 式 W2V-BERT 更有帮助，课程收益不统一。

## 点评
把班图声调扩散写进难度与适配器，比纯 WER 课程更贴语言事实。强在架构×语族交互与跨库迁移；弱在 α/β 未敏感性分析、社区与录音棚域差仍大，课程有时反而伤个别语言。
