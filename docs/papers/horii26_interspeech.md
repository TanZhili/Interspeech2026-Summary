# How does children's pronunciation develop? Capturing syllabic change with children's growth using unsupervised syllable discovery

- 论文编号：3104
- 报告人：Koharu Horii
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：https://www.isca-archive.org/interspeech_2026/horii26_interspeech.pdf

## 问题
儿童发音发展分析常依赖专家转写或成人音素 ASR（自上而下），易淹没儿童特异与中间态发音；需要可扩展、不强制成人范畴的自下而上方法。

## 方法
用 Sylber 无监督音节发现：成人版（LibriSpeech）与儿童适配版（MyST 微调）。在 OGI Kids 957 名 5–15 岁朗读英语上，度量 (1) 与 MFA 音节边界一致（Jaccard、过分割比）反映接近成人节律；(2) 活跃音节簇数反映发音库；(3) 相对目标音节的簇纯度反映稳定性。

## 实验与结果
清晰发展模式：约 5–8 岁音节模式扩展（库增大），随后逐渐稳定并向成人样组织收敛。自下而上能捕捉自上而下难见的细粒度库与稳定性变化；儿童适配模型有助于分离适应效应与真实发展。

## 结论
无监督音节发现可作为大规模儿童发音发展研究工具，揭示“先扩展再稳定”轨迹，并可能推广到构音障碍/方言等难标注数据。

## 点评
把零资源自下而上范式接到发展语音学，避开成人音素硬套。双模型（成人/儿童）设计帮助解释“像成人”与“儿童内部变化”。仍依赖 MFA/提示目标作参照，完全无监督解释边界需谨慎。
