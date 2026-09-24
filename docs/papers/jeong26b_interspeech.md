# Cross-lingual Retrieval-Augmented Classification for Dysarthria Severity Assessment

- 论文编号：2697
- 报告人：Taeyoung Jeong
- 程序：Thursday 1 October 2026 / Pathological Speech Assessment 4
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jeong26b_interspeech.pdf

## 问题
自动构音障碍严重度评估受病理标注稀缺制约；直接跨语种拼数据易过拟合语言声学线索而非严重度。需要在低资源条件下有效借用另一语言的临床语音。

## 方法
提出 CRAC（align–retrieve–fuse）：冻结 Whisper-small 取均值池化内容向量 e（768-d），可训投影头得到搜索向量 z（128-d），用 SupCon 在韩/意混合批上按严重度拉近、跨语言/任务推远。用对方语言训练集建 FAISS 向量库（key=z，value=e）。目标语查询检索 top-k，以 e_q 为 query、检索 e 为 key/value 做多头 cross-attention，拼接 f=[e_q;c] 经 MLP 做三分类（HC / Mild-to-Moderate / Severe）。被试级对 6 个任务（MPT /a,i,u/ 与 DDK /pa,ta,ka/）softmax 软投票。

## 实验与结果
韩语卒中后与意大利语 ALS 数据、说话人无关划分。相对单语基线，CRAC 在韩语 balanced accuracy 78.9%→87.3%（+8.4 pp），意大利语 66.7%→86.7%（+20.0 pp）；朴素双语池化在韩语甚至降到 76.4%。消融显示仅对齐或仅检索均不足，二者互补；k=5 总体最佳，k=10 噪声增多。t-SNE 显示融合后类分离最清晰。

## 结论
结构化跨语种检索增强优于简单拼数据；对齐保证检索按严重度相关，检索再稳住决策边界，适合低资源病理严重度评估。

## 点评
临床“对照既往病例”的类比落到检索增强上很自然，消融也干净。局限是病因与任务高度特定（MPT/DDK、三分类），库语言与目标病因不对齐时检索质量仍可能漂；top-k 在韩语有非单调波动，说明邻域组成敏感。
