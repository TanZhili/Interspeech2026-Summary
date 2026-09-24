# ZeroSyl: Simple Zero-Resource Syllable Tokenization for Spoken Language Modeling

- 论文编号：315
- 报告人：Nicol Visser
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/visser26_interspeech.pdf

## 问题
纯语音语言模型需把 SSL 特征离散成单元，但帧级 token 序列过长，长程句法建模困难。Sylber、SyllableLM 等音节单元有效，却依赖多阶段微调与专用目标，管线复杂。

## 方法
**ZeroSyl** 训练免费：
1. 取冻结 WavLM Large 第 13 层特征的 L2 范数，平滑后做突出度峰值检测（\(\delta=0.45\sigma\)）得音节边界。
2. 在边界内对第 22 层特征均值池化，球面 K-means（K=10k，LibriSpeech 100h）离散化；层次聚类把静音质心合并，词表约 9116。
3. 用 OPT-125M 在发现单元上做因果 LM（对比实验 6k h / 扩展 60k h Libri-Light）。

## 实验与结果
边界：R-value 75%、token F1 54%，优于 Sylber，接近 SyllableLM 5Hz。发现质量：SNMI 88.9%、bitrate 52 bps，优于对比音节系统。6k h LM：sWUGGY 68.0、sBLIMP 60.5、tSC 68.1，全面高于 Sylber/SyllableLM。扩展：词汇任务仍逊帧级 SpidR，但句法随数据量上升更陡，60k h 叙事接近 SpidR。

## 结论
作者认为高质量音节发现不必复杂多阶段训练；L2 范数已含可用音节位置信号。局限：音节压缩可能伤稀有/未见词的词汇细节；L2 为何编码音节位置仍待解释。

## 点评
工作价值在「极简有效」：用冻结模型的范数峰值替代专门蒸馏边界网络，却在多项口语 LM 基准超过更重的音节管线。扩展实验也诚实标出与细粒度单元的任务分工（词 vs 句）。脆弱点：强依赖 WavLM Large 特定层；静音合并启发式；对非英语/嘈杂语料是否成立未充分验证。
