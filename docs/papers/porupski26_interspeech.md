# Umm... With Transformers? Insights from Filled Pause Use across Four Slavic Parliaments

- 论文编号：3262
- 报告人：Ivan Porupski
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/porupski26_interspeech.pdf

## 问题
填充停顿（FP）研究多依赖小规模单语语料；性别、年龄、语速等效应能否在大规模议会语域推广，以及情感、政治取向、执政地位等新变量是否相关，尚不清楚。

## 方法
约 4000 小时克罗地亚/捷克/波兰/塞尔维亚议会发言（ParlaSpeech），transformer 自动检 FP；用 Mundlak 校正的 GEE 负二项模型分解说话人内/间效应，预测 FP 率，纳入性别、年龄、语速、情感、左右取向与执政/在野。

## 实验与结果
复制：年龄与语速均负向关联 FP（全局每增十年 IRR≈0.86；每音节/秒 IRR≈0.65，尤以说话人内效应强）。性别：全局女性更高 FP，但主要由 HR/RS 驱动（男性 IRR≈0.40–0.53），CZ/PL 无显著差，方向与多数会话语料「男性更多」相反。情感正向关联 FP（全局 IRR≈1.06）；在野相对执政倾向更低 FP（议会特异）。取向效应因国而异。

## 结论
大规模斯拉夫议会语料显示 FP 预测因子高度语域依赖；语速的说话人内效应支持规划负荷解释，性别与年龄模式不可简单从会话语料外推。

## 点评
Mundlak 分解把「习惯」与「当下状态」分开，是相对普通回归的关键增益。情感靠自动模型（R²≈0.65），误差会渗入 FP 关联。仅议会正式语域，对日常对话概化需谨慎。
