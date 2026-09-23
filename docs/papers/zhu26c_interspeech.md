# Token-Independent Language Representations for Low-Latency Configurable Multilingual Speech Recognition

- 论文编号：2455
- 报告人：Hongxu Zhu
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/zhu26c_interspeech.pdf

## 问题

可配置多语 ASR（CMM）用语言特定模块（LSM）支持任意语种子集，但解码器 LSM 每步重算，延迟随输出长度线性增长，长句开销大。

## 方法

保留编码器一次计算的神经 LSM；解码器改为 token 无关语言表示：CMM-S 用静态语言向量做加性调制；CMM-D 再融合顶层编码器 LSM 的句级池化动态线索与可缓存静态矩阵扩展，门控合成一次后整句复用。每步 LSM 复杂度从 O(d²) 降到 O(d)。

## 实验与结果

MLS 8 语：CMM-D allhot/onehot 平均 WER 8.70/8.67，与原 CMM 持平，优于多语基线 9.26。平衡 4 语（含粤/普/英/马，含语码转换）同样 parity。长输出（110–130 token）上原 CMM 额外延迟 +107.88 s，CMM-S/D 仅约 +2.23/+7.34 s，峰值额外延迟降逾 90%。

## 结论

作者认为语言身份是全局属性，不必绑在自回归逐步环上；编码器告知的 token 无关表示可在精度相当下大幅降延迟。

## 点评

把“可配置多语”的延迟瓶颈拆开：编码器保留动态语言声学，解码器只做常向量/句向量加法，工程洞察清晰。CMM-S 略损精度、CMM-D 补回，消融逻辑完整。依赖用户/提示给出语种子集；极端语码切换仍靠编码器侧 LSM。
