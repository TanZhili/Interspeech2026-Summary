# SALT: Selective Allophone-Level Tokenization for Korean Text-to-Speech Synthesis

- 论文编号：2055
- 报告人：Kwangsung Kim
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kim26p_interspeech.pdf

## 问题

韩语 Hangul 虽偏表音，但正字法形态音位性强，字素≠实际发音；低资源下模型难靠隐式学习消歧。全量音位变体标注会膨胀词表、破坏 token 分布平衡，损害可学性。

## 方法

提出 Selective Allophone-Level Tokenization（SALT）：在 G2P 后的音素上选择性附加音位变体标签（如词首清化 i、腭化 j、韵尾 c）。用 Gini 与 Rényi 效率（α=2.5）筛选标签组合；优选仅区分鼻韵尾的 SALT-N（词表增幅小、效率高）。在预训练 F5-TTS（英/普）上，对文本嵌入与 ConvNeXt 全参微调，其余用 LoRA；数据为 KSS 12.75 h 与极低资源 1 h 子集。

## 实验与结果

12.75 h：SALT-N CER 3.30%、WER 11.24%，优于字素 4.74%/15.26% 与音素 3.74%/14.06%；NMOS 最高 3.10。全标签 SALT-VCP CER 反升至 6.03%。1 h：仅 SALT-N CER 低于 10%（8.19%），字素/音素/VCP 均≥10.78%。人类听感对发音错误更敏感，故 NMOS 更青睐低 CER 的 SALT-N，即便 UTMOS 略低于 VCP。

## 结论

作者认为不必改架构或堆数据，用选择性音位变体输入作归纳偏置即可提升韩语 TTS；关键是在声学消歧与 token 统计效率间取平衡。局限为单说话人小数据，未来将扩到多说话人与其他规则性强的语言。

## 点评

把“语言学先验要注入多少”量化成分布效率指标，再选最小有效标签集，比盲目全规则 G2P 更工程化。低资源增益最大，符合归纳偏置预期。依赖标准发音规则与 G2P 质量；方言/口语变体更自由时，选择性规则可能需重标定。
