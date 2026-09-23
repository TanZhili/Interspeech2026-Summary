# ELSA: Acoustic Event-Level Semantic Alignment for Fine-Grained Reference-Free Text-to-Audio Evaluation

- 论文编号：914
- 报告人：Shuntaro Suzuki
- 程序：Monday 28 September 2026 / Evaluation of Speech and Audio Analysis
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/suzuki26_interspeech.pdf

## 问题

文生音频（TTA）需要与人类主观相关的自动指标。参考音频难获，参考无关的 CLAPScore 等多为粗粒度全局相似，对短暂声学事件敏感不足，与人类相关有限（如 RELATE 上 CLAP 与 REL 的 Spearman 仅约 0.280）。

## 方法

提出 ELSA：用 Human-CLAP 得全局文/音嵌入；LLM（GPT-5.2）把文本拆成简短名词—动词事件短语；LASS（SAM Audio）按事件查询分离对应音频段并嵌入。全局余弦相似作粗分，事件级精度/召回 F1 作细分，再以 λ_M（经验 0.4）自适应加权得最终分。在 AudioCaps、Clotho、MusicCaps、RELATE 上与人类 OVL/REL 及相关组合属性评测对比多种参考相关/无关基线。

## 实验与结果

四基准上 ELSA 与人类相关普遍高于 PAM/CLAP 变体与多类参考相关指标：如 AudioCaps REL Spearman ρ=46.5（相对次优约 +17.8）、Clotho REL 39.8、MusicCaps REL 36.8、RELATE REL 37.9。消融与事件数敏感性分析支持事件分解贡献；对 CompA/RELATE 的属性与顺序评测亦更好反映组合对齐。

## 结论

事件级语义对齐可在无参考音频时显著提升与人类主观（尤其相关性）的一致，适合可靠 TTA 评测。项目页已公开。

## 点评

借鉴视觉语言细粒度对齐思路，用“解析事件 + 查询分离”补全局 CLAP 对短事件的盲区，方向正确。代价是依赖外部 LLM 与 LASS，评测成本与可复现性受第三方模型影响；相关绝对值仍中等，说明 TTA 自动评测远未饱和。
