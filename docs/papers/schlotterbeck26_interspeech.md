# Content–Speaker Trade-offs in Continued Self-Supervised Pre-Training Across SSL Paradigms for Multilingual Speech

- 论文编号：2946
- 报告人：Danner Schlotterbeck
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/schlotterbeck26_interspeech.pdf

## 问题
Continued Pre-Training（CPT）常用在域适应，但既有工作偏对比学习架构；离散单元模型（HuBERT/WavLM）的伪标签来自源域，直接续训是否有效、以及 CPT 是否在内容与说话人信息间造成灾难性遗忘，缺少跨范式对照。

## 方法
从 UPS 用 VAD 密度与语言稀缺评分策展 100h/500h 子集。对 HuBERT、WavLM（含帧内混叠去噪）在目标数据上重算 k-means 伪标签并接新投影头续训掩码预测；对 OmniASR（wav2vec 2.0 对比）直接恢复原生对比目标。共享 span masking（约 57% 帧）、AdamW、5 epoch。另消融伪标签：MFCC（第一轮式）vs 中间层 embedding（不同层与 K）。下游用 UPS 官方探针：LID Macro-F1、说话人 diarization ARI、ASR CER；并用 LibriSpeech 线性 CTC 探针看遗忘。

## 实验与结果
内容指标常有提升但不稳：如 HuBERT-base 100h 上 F1 .56→.67、CER .72→.65，但三随机种子 CER 方差大（.55–.74）。离散单元模型 ARI 系统性崩溃（HuBERT .76→.32，WavLM-base+ .59→.31，WavLM-large .76→.38），OmniASR ARI 略升 .37→.42。MFCC 伪标签损害内容（F1/CER）却大致保住 ARI；embedding 伪标签则相反。LibriSpeech 探针上离散单元有不同程度遗忘，OmniASR WER 反而改善。全文末尾抽取略有截断。

## 结论
CPT 可使表示偏向语言内容，离散单元模型上说话人信息稳定受损，内容增益高方差；伪标签性质（MFCC vs embedding、聚类层）决定内容–说话人权衡。局限为算力下的短日程、子集策展，未扩到全量 UPS。

## 点评
核心贡献是在相同数据与探针下把“续训离散单元是否可行”做成跨范式对照，并钉住伪标签类型这一旋钮。强在揭示可复现的说话人退化；弱在多数配置单次运行、内容增益解释需谨慎，且尚未给出显式保说话人（如 adapter）的解法。
