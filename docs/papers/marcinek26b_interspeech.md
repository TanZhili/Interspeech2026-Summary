# Optimal Linguistic Complexity for Dialogue System Speech in Noise: Convergent Evidence from Automatic and Human Transcription

- 论文编号：2799
- 报告人：Lubos Marcinek
- 程序：Tuesday 29 September 2026 / Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/marcinek26b_interspeech.pdf

## 问题
嘈杂环境下对话系统合成回复应否“自适应简化”？对 ASR 与人类听者，最优语言复杂度仍缺系统证据。

## 方法
Study 1：250 句五级复杂度（电报式 L1 到复杂 L5），两 TTS×性别×12 DEMAND 噪声×7 SNR×两 ASR，共 168k 转写。Study 2 试点（N=15）：人类转写 L1/L3/L5×四噪声×三 SNR。控制词长、困惑度与韵律混淆。

## 实验与结果
ASR 与人类均呈 U 型：自然语法句（L3，约 9–16 词）优于电报式 L1——ASR WER 约优 43%，人类转录错误约优 45%；条件越好，语法优势反而更大。建议系统输出落在约 9–19 词的语法完整区间，拒绝“噪声越大越简化”。

## 结论
噪声下对话系统输出应保持自然语法完整句，而非电报式简化；ASR 与人类证据收敛。

## 点评
用大规模因子交叉把“该不该简化”钉成可检验结论，对 Listening Speaker 输出策略直接有用。人类侧仅 N=15 试点；复杂度由 LLM 改写+人工检查，真实交互中的语用简化未覆盖。
