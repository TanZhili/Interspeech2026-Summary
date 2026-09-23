# Controllable Accent Normalization via Discrete Diffusion

- 论文编号：1056
- 报告人：Qibing Bai
- 程序：Tuesday 29 September 2026 / Pronunciation Diversity
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bai26b_interspeech.pdf

## 问题
口音归一化（AN）把 L2 口音转为 L1，但多数系统只能一次性“全归一”，缺少口音强度旋钮；语言学习与配音等场景需要可调保留。已有连续扩散用起始时间步控强度，但固定时长、难调节奏。

## 方法
提出 DLM-AN：在 SSL 离散语音 token（WavLM）上做吸收式掩码离散扩散（扩展 LLaDA）。Token encoder 经 CTC 音素引导得到内容表示；Common Token Predictor（CTP）用源–目标 LCS 标“共同 token”并预测置信度，高置信源 token 可复用初始化反向过程——复用越多保留口音越多；Duration Ratio Predictor 用条件 flow matching 预测 dur_tgt/dur_src 以匹配母语节奏；DLM decoder 双向 Transformer 迭代去噪，CFG 可选；flow-matching 合成器 + HiFT 声码器波形。联合损失 LDLM+β1 LDP+β2 LCTP+β3 LCTC，先母语预训练再半合成并行微调。

## 实验与结果
摘要称在多口音英语上 DLM-AN 取得对比系统中最低 WER，口音减弱有竞争力，且口音强度控制平滑可解释，时长缩放稳健。正文有 CTP 可视化（中式口音样本上口音重区域置信度低）。抽取文本在采样算法处截断，完整对比表与客观/主观分数未见。

## 结论
离散扩散 + 共同 token 复用提供可解释的口音强度控制，并配合时长比预测；作者认为内容保真（低 WER）与可控归一可兼得。边界是依赖并行/半合成监督与音素对齐质量。

## 点评
关键不是再做一个全量口音转换，而是把“哪些 token 像母语、哪些该改”显式成 CTP，用复用比例当旋钮，比改扩散时间步更可解释。脆弱处是 LCS 标签对 token 音位性敏感、训练依赖伪并行，且全文截断使“最低 WER”无法与具体基线数字核对。
