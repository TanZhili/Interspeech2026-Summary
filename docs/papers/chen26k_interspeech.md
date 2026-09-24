# Causal Tracing of Audio-Text Fusion in Large Audio Language Models

- 论文编号：1118
- 报告人：Wei-Chih Chen
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/chen26k_interspeech.pdf

## 问题
LALM 任务表现强，但声学特征与文本上下文何时、在何处融合仍是黑盒；多数评测只看最终输出，无法定位跨模态因果通路。

## 方法
将 ROME 式因果追踪适配到 LALM：clean（原音频）、corrupted（静音替换音频）、patched（把 clean 的选定隐状态写入 corrupted 继续前向）。用 Recovery Rate RR=(P_patched−P_corrupted)/(P_clean−P_corrupted) 量化因果贡献。层向：整层文本 token 隐状态整体替换；词向：单 token 位置替换，并把 prompt 分为 early / object / late / last token。在 SAKURA 四属性（animal/emotion/gender/language）上评 DeSTA2/2.5、Qwen/Qwen2、Voxtral。

## 实验与结果
层向：DeSTA 呈渐进融合（约层 15 后稳定）；Qwen 族早期 RR≈0、约在层 18–31 陡升（晚融合）；Voxtral 更早达到高 RR（早融合）。词向：所有模型最高 RR 集中在生成前最后一 token（信息瓶颈）；中间层 object token 出现次级因果峰，类似“查询触发”拉取任务相关音频。

## 结论
不同 LALM 族采用 progressive / late / early 等不同融合策略；最后 token 是跨模态检索瓶颈，object token 触发类注意力查询。这些定位可为效率优化与幻觉监测提供线索。

## 点评
用静音 corrupted 干净消融声学、再用 RR 做因果度量，比纯 logit-lens 观察更强。发现与 VLM 末 token 瓶颈类似，暗示 transformer 通用机制。局限是分类式约束生成设定与选定模型族；开放生成或更复杂推理任务是否同构仍待验。
