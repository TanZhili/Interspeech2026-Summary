# Listening Like a Judge: A Music-Aware Framework for Automatic Singing Performance Evaluation

- 论文编号：912
- 报告人：Sourav Ghosh
- 程序：Monday 28 September 2026 / Evaluation of Speech and Audio Analysis
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/saini26_interspeech.pdf

## 问题

自动歌唱质量评估（SQA）需同时看歌词正确与音高—节奏保真，并容忍颤音、花腔、弹性速度等表现性变化。既有系统常只用声学或只用转写，难对齐人类整体评判；歌唱 ASR 也因 melisma 等难稳。

## 方法

提出 MUSICJUDGE：先源分离得人声/伴奏；用微调 ASR 得原型片段，再滑窗生成候选块，经语义嵌入、模糊词汇与语音相似度的多信号匹配选定语意/结构连贯块（节/副歌等）。块级内容分 C_k 与音乐分 M_k（音高保真、节奏保真等）加权聚合成总分。引入 Modality-Guided LoRA（MG-LoRA），把音高轮廓、时长稳定性、onset 对齐线索注入 ASR 微调以提升歌唱转写。评测 SWARALYRICS，并在 Jamendo、SingMOS-Pro 上看泛化。

## 实验与结果

在 SWARALYRICS 上与人类专家 Spearman ρ=0.683、Kendall τ=0.499（相对对比约 +32%/+41%），MSE/MAE 等亦最优。消融显示内容与音乐两支均必要，二者结合达最高相关。MG-LoRA 提升多风格转写鲁棒（如 Classical/Ghazal 等设定下指标改善）。定性例子显示 melisma/发音变异下歌词对齐更稳。

## 结论

块对齐的多模态 SQA 能在保留音乐结构的同时容忍合理表现性变化，并与专家判断较强一致；MG-LoRA 改善歌唱 ASR 是关键支撑。正文结论段抽取有截断，以上述结果部分为准。

## 点评

把“像评委一样听”落成内容块 + 音高节奏双通道，比单一音高阈值或纯 WER 更贴近真实评分。多信号歌词对齐针对歌唱 ASR 噪声设计合理。脆弱点是依赖参考歌词/曲式与分离质量，强即兴或无清晰结构演出可能难切块；相关仍非完美，文化/曲种外推需更多数据。
