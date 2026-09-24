# Unified Gradient Projection: Language-Balanced Continual Learning for Multilingual Low-Resource ASR

- 论文编号：1915
- 报告人：Wei-Qiang Zhang
- 程序：Tuesday 29 September 2026 / Multilingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ren26g_interspeech.pdf

## 问题
对 Whisper 等做低资源多语序贯微调易灾难性遗忘；A-GEM 等梯度投影在重放缓冲语言不平衡时会被主导语言偏置，低资源语言更易被覆盖。

## 方法
提出 Unified Gradient Projection（UGP）：每步从各历史语言均匀采样构造语言均衡参考梯度 g_ref；若当前梯度与 g_ref 内积为负则投影到其正交补。同时与 Experience Replay 结合，混合 batch 上做 L_cur + λ L_replay（λ=1）。中大型 Whisper 冻结 encoder 只训 decoder/embedding；small 全参微调。

## 实验与结果
主场景（FLEURS）：目标 Malay/Indonesian/Filipino/Javanese/Māori，重放 Thai/Vietnamese/English/French。Whisper-large-v3 上 UGP：TWER 12.91、RWER 6.68、AWER 9.80、FWER 0.04（近零遗忘）；FT 的 FWER 在 medium 可达 89.80。消融显示投影与 ER 互补：单独投影 FWER 4.20，完整 UGP 达 0.04。扩展语组与 50h→5h 数据尺度上，UGP 持续压低遗忘并保持较好 AWER。收敛后梯度余弦更近正交，冲突弱于 FT。

## 结论
语言均衡梯度投影加 ER 可在多语低资源持续学习中兼顾可塑性与稳定性，大模型上遗忘近零。作者认为这为通用语音识别的持续适配提供高效路径。

## 点评
抓住多语重放里“参考梯度被大语绑架”这一具体失效点，比笼统加正则更对准问题。强在跨尺度与稀缺数据验证；弱在主实验语言组与缓冲语言固定、数据尺度分析仅在 small，对更长任务序列是否仍稳需另证。
