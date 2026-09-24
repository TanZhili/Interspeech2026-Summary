# Adding Robust Code-Switching Capabilities to High Performance Multilingual ASR

- 论文编号：1099
- 报告人：Enes Yavuz Ugan
- 程序：Thursday 1 October 2026 / Code-Switching ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ugan26_interspeech.pdf

## 问题
在已很强的多语 ASR（如 Whisper）上加码切换能力时，标准合成数据微调常严重破坏单语表现；文献多评弱基线或域内设定，强模型保真场景研究不足。

## 方法
场景定位为“强模型保真”。用 GPT-4o 按等价约束与德英形态整合规则生成 CS 文本（§§…§§ 标出切换点），xTTS-v2 按段分语合成再拼接。适配采用 BLoRA（贝叶斯低秩，μ/σ 先验推向稀疏 ΔW，λ_KL=0.5）而非标准 LoRA。评 CSFleurs 的 WER 与切换词 PIER，并用 CommonVoice 做单语回退测试。

## 实验与结果
基线 Whisper：DE/EN/CSFleurs WER 8.53/13.56/11.49，PIER 26.59。标准 LoRA 在任意数据量上单语与 CS 均大幅恶化；复杂 MT+对齐拼接同类。BLoRA + 全量合成：CSFleurs WER 10.88（相对改善约 5.31%），PIER 20.84（相对约 −21.6%），单语接近基线。严过滤 CER≤5% 时，仅 1k 样本即可将 PIER 降约 32.87%（文中最佳约 17.85）。文本多样性比说话人多样性对 PIER 略更有利。定性：基线把 matter 误成 meta，BLoRA 可保留英文插入。

## 结论
对强多语模型，瓶颈在知识整合而非合成数据复杂度；稀疏不确定性感知的 BLoRA 可用少量合成数据提升 CS 且保住单语能力。

## 点评
刻意选 Whisper 已很强的德英，否定“更好合成必更好”的假设。BLoRA 稀疏更新是关键机制；过滤在小数据时极重要。依赖手工 PIER 标注与特定语言对规则，向更远语对迁移仍需验证。
