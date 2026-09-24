# StanceBench: A Benchmark for Audio LLM-Based Interpersonal Stance Evaluation from Speech

- 论文编号：2938
- 报告人：Yuzhe Wang
- 程序：Thursday 1 October 2026 / Benchmarking Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26fa_interspeech.pdf

## 问题
语音到语音对话模型依赖韵律与互动细微差别传达社会意图，但现有评测多盯转写/自然度，缺少对人际立场（empathy、礼貌、支配等）的标准化自动评判基准。

## 方法
StanceBench 基于 Seamless Interaction Improvised 子集的角色提示，定义 9 个立场维（S0–S8），每维正/负两极（每极约 3–4 个代表角色）。Category 1 单说话人片段（温暖、同情、礼貌、自信、真诚、注意）；Category 2 带对方上下文的互动维（社交投入、权力取向、冲突调节）。用能量 VAD 抽 IPU，拼成 30–45 s 说话人段或转轮附近的 CONTEXT/TARGET 窗。法官模型在统一量规下做 P/N 二选一并输出概率与证据；评测 Qwen2.5-Omni-7B、Kimi-Audio-7B、Granite 级联转写、gpt-audio、Gemini-2.5-Flash。固定种子抽取 25% 会话共 2431 段、484 说话人；角色提示作弱标签，报告稳健性与可分性。

## 实验与结果
摘要：共情与礼貌最易；温暖与自信中等可分且有正向偏斜；诚实最难且提示顺序偏置高（需跨轮证据）；注意可分但与人类对齐弱；互动维更依赖语境，阈值间隙与方差大，冲突调节尤甚。正文抽取止于评判提示与一致性检查，完整数值表未完整可读。

## 结论
StanceBench 提供统一流水线评估音频 LLM 作为立场法官的能力与局限，并为后续评估 S2S 对话模型选定较可靠的法官候选。

## 点评
把人际立场操作成量规两极对比，比笼统“风格分”更可诊断。弱标签依赖演员角色提示，与真实自发立场仍有距离；诚实维的顺序偏置提示法官对跨轮证据敏感。结果细节因抽取截断需以摘要为准。
