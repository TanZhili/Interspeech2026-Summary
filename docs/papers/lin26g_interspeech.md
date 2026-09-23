# Silence is Golden: Mitigating Hallucinations in Large Audio-Language Models via Layer-Weighted Vector Steering

- 论文编号：1421
- 报告人：Tsung-En Lin
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/lin26g_interspeech.pdf

## 问题
LALM 常生成无音频依据的幻觉；文本式激活操控（如 VISTA）或每步对比解码（AAD）或不够模态化、或开销大。

## 方法
用等长**静音**作负实例，相对有声输入构造模态感知转向向量 \(v_l=F_l(X^+)-F_l(X^-)\)。探层：隐状态与 \(v\) 的余弦相似度 + Cohen’s \(d\)，发现后层与正确/幻觉分离更强。提出 **LWVS**：总能量守恒下加强高影响后层、削弱早层与末层；注入后做范数归一。评 Gemma-3n 与 Qwen2-Audio，Audio Hallucination QA 与 MMAU。

## 实验与结果
纯文本转向（TVS）在 Gemma 上伤性能；MAVS/LWVS 持续提升。Gemma Total Recall 53.4%→69.0%（LWVS）；Qwen MMAU 54.8%→59.2%。Gemma MMAU 大致持平，说明未明显损害一般理解。

## 结论
静音锚定的模态转向 + 层加权可免训练抑制幻觉并常保持甚至提升通用音频理解。

## 点评
把“听没听”写进激活差，并对准后层决策，比均匀操控更合机制。脆弱处：\(\lambda\)/\(\beta\)/层划分需按模型调；主要评判别式 yes/no 与多选，生成式长答未测。
