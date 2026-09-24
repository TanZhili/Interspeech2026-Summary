# A Unified Safety Subspace Exists in Speech Language Models

- 论文编号：2797
- 报告人：Nurdaulet Mukhituly
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/mukhituly26_interspeech.pdf

## 问题
SLM 同时面临文本与音频越狱；先验常把语音安全当独立问题。不清楚音频攻击是否走模态特异失效，还是绕过与文本共享的内部安全机制。

## 方法
在中间层 last-token residual stream 上对 harmful/jailbreak 激活做 PCA，估计从拒绝簇到顺从簇的方向并回投为全维 steering 向量（Audio Vector 来自 AdvWave，Text Vector 来自 AutoDAN）。推理时在选定层对激活加减归一化方向（α 控制幅度与符号），无需再训练。在 Qwen2-Audio（层 15）与 GLM-4-Voice（层 17）上评估跨攻击、跨模态迁移；ASR 由 GPT-5 作 judge。

## 实验与结果
PCA 上 harmful 与 jailbreak 可分，jailbreak 落在 benign 与 harmful 之间。负向 steering 把五类攻击 ASR 压到大多 <7%：如 AdvWave 97.93%→0.52%（Qwen）、AutoDAN 72.69%→2.82%；音频向量对文本越狱、文本向量对音频越狱同样有效。正向 steering 使原本拒绝的有害输入 ASR 升至约 56–90%。同范数随机方向远弱于定向向量。摘要亦报告拒绝向量使文本越狱约 76.5%→2.2%、音频约 79.0%→3.1%。

## 结论
SLM 残差流中存在跨模态、跨攻击族共享的低维安全子空间；单一方向即可在推理期翻转拒绝/顺从，支持“统一几何边界”而非纯模态特异漏洞。

## 点评
把文本 LM 的 refusal-direction 叙事推进到语音-文本双通道，并用跨模态迁移做因果证据，说服力强。依赖中间层选择、α 扫描与 LLM judge；对不同对齐策略/规模的稳定性以及是否被自适应攻击绕过，仍是开放问题。
