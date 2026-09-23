# A Generalized Formalism of Auto-Regressive Decoding for Speech Processing

- 论文编号：2768
- 报告人：Julia Gachot
- 程序：Monday 28 September 2026 / Search Methods and Inference Algorithms
- 技术分类键：asr-decoding
- 全文：https://www.isca-archive.org/interspeech_2026/gachot26_interspeech.pdf

## 问题
语音处理中序列生成高度依赖自回归搜索，但“AR / next-token / MAP beam”等概念定义分散，推测解码、NAR、随机采样等常被用不同名称复述相近机制，导致难以系统比较、消融与报告。现有分类常按任务或“确定性 vs 随机”切分，跨任务迁移结论困难。

## 方法
将生成表述为 \((M, g_{\mathrm{AR}})\)，在 SIPC（随机整数规划）视角下给出 AR 纳入准则与模块化形式：
- **模型假设**：网络估计有限字母表上的条件概率，并用解码状态/先验更新；
- **解码假设**：迭代局部搜索，且至少一次用目标函数（如 MAP）更新有限候选集。
每次迭代 \(f^t_{(M,g_{\mathrm{AR}})}(Y_t,Z_t)\) 由四步组成：**Estimation**（条件 PMF）、**Decision**（目标函数选/扩候选）、**Update of prior**（维护 \(Z_t\)）、**Termination test**。报告解码策略即报告初始条件与上述设计选择。用该框架形式化 beam search 与 temperature sampling，并讨论 speculative / “NAR” 边界案例的纳入与排除。

## 实验与结果
本文以形式化与讨论为主，未报告新的 ASR/MT 数值实验。在 2018–2025 的十篇相关工作上做归类：按解码假设排除 1 篇非 SIPC；模型假设下 speculative 与部分所谓非 AR 方法可纳入。进一步说明可用“用基线步骤替换某一步”做结构消融，以隔离 estimation / decision / prior / termination 的贡献。

## 结论
作者给出统一的 AR 搜索形式与报告清单，用以跨任务比较与设计聚焦解码的消融；主张摆脱“仅是似然最大化器”的笼统描述，转向递推关系与模块设计视角。

## 点评
贡献是元方法：把解码拆成可复用的结构组件，便于把 speculative、多样性惩罚等放到同一坐标系里比较。强在澄清报告要素与消融接口；作为纯理论/分类工作，正文没有对照实验数字，实际收益取决于社区是否采用该报告约定。技术分类虽挂在 asr-decoding，内容覆盖更广的序列生成搜索。
