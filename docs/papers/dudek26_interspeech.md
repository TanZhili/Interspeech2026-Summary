# Phoneme-Level Mispronunciation Screening in Polish-Speaking Children with an Explainable Assistant

- 论文编号：1416
- 报告人：Milosz Dudek
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：https://www.isca-archive.org/interspeech_2026/dudek26_interspeech.pdf

## 问题
儿童语音障碍早期筛查受专科资源限制；波兰咝音系列密、易替换，通用 ASR 易被语言模型“纠正”而漏检；需可解释、偏保守的看护者筛查（非诊断）。

## 方法
专有 4–8 岁波兰儿童提示语料（201 人）。wav2vec2-large-xlsr-53-polish + 6 层 Transformer 后编码器 CTC；标签含括号化 IPA 替换证据（如 [s]）。LoRA+解冻后 6 层（约 33% 可训）。识别序列与规范序列对齐得诊断向量，再由固定模板助手生成看护者反馈，带不确定时抑制/拒答规则。

## 实验与结果
10 名未见儿童、559 句：精确序列匹配 88.7%；去掉后编码器降至 84.5%。保守筛查代理（目标位发出括号 token 即标记）：精确率 72.9%、召回 61.4%、F1=0.67，目标正确项假警 2.7%。强调非临床诊断，计划临床闭环验证。

## 结论
替换敏感的 token 识别 + 对齐筛查 + 模板助手，可在波兰儿童咝音场景提供低假警、可审计的家庭筛查原型。

## 点评
把“可解释”落成对齐痕迹+模板+拒答，适合看护者产品边界。括号 token 把替换显式化，避开 ASR 过度规范化。仍缺真实看护者/临床验证；召回中等意味着漏检需人工兜底。
