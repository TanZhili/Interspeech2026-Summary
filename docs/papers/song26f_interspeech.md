# Evaluating and Preserving Lexical Stress in English-to-Chinese Speech-to-Speech Translation

- 论文编号：2321
- 报告人：Yuchen Song
- 程序：Wednesday 30 September 2026 / Translation
- 技术分类键：translation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/song26f_interspeech.pdf

## 问题
S2ST 语义与自然度已较强，但跨语言词汇重音/强调传递仍弱；汉语为声调语言，英语中心强调检测难直接迁移，且缺带重音标注的中文数据与可靠自动评测。

## 方法
自建中文重音语料（2 名普通话说话人，418 句、1883 条、2.74h）。Syl-BiLSTM：XLS-R 多层融合 + 音节级池化 + BiLSTM 做字级重音检测。CETS：EmphaClass 检英侧重音，Whisper+fa-zh 对齐中文，Syl-BiLSTM 检目标重音，SimAlign 对齐后判是否传到对应语义位置。S2ST：StressTransfer（Whisper+Qwen2.5-3B LoRA）出带 stress 标签译文，CosyVoice3 LoRA 在重音数据上微调可控合成。

## 实验与结果
Syl-BiLSTM F1 0.91，远超 Frame-Linear/Frame-BiLSTM。Proposed CETS-W/S 60.80%/58.30%，基线约 16–26%；BLEU 47.35 与 StressTransfer+Base 接近，UTMOS 最高 3.68。主观成功转移率 78.33% vs 基线约 12–25%；CETS 与人判 Pearson r=0.52，绝对一致约 79%。

## 结论
中文重音数据 + 音节级检测 + 可控 TTS 可显著提升英→中强调传递，同时保持翻译质量与自然度；CETS 可作为自动代理。未来扩展更多说话人与声调语言。

## 点评
把“评测瓶颈”和“合成可控”一起打通，CETS 的词级/句级双粒度比单纯听感更可诊断。说话人仅 2 人、TTS 用固定默认音色，强调可控性可能部分依赖说话人特异性；CETS 链路依赖 ASR/对齐/检测多模块，错误会耦合进指标，与人相关中等需谨慎解读。
