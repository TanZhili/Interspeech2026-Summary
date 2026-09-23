# Easper: An Accessible ASR Pipeline for Language Documentation

- 论文编号：2781
- 报告人：Aso Mahmudi
- 程序：Tuesday 29 September 2026 / Corpus Creation, Summerisation and Understanding
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/mahmudi26_interspeech.pdf

## 问题
语言文档中转写是瓶颈；Whisper 等可微调，但田野语言学家缺工程能力。冷启动时不知应优先标哪些录音——声学干净（高 SNR、少重叠）还是语言丰富（词汇多样/重复）——缺少实证指南。

## 方法
发布 Easper：从 ELAN 导出→校验（>30s、重叠等）→云端（如 Colab）微调 Whisper-small / XLS-R→本机 diarization（SpeechBrain 或 pyannote）+ 转写写回 ELAN。优先策略实验以「整场录音 session」为不可分割单位，提取 SNR、重叠率 OVR、TyTo（type-token）、以及时长归一的 ToTy（token/type×duration）；按 Baseline 随机、SNR、最少重叠、TyTo、ToTy 五种排序逐步加入训练池，全量微调 Whisper-Small（3 epoch/步，batch 8，lr 1e-5），以 CER 衡量后期编辑成本。

## 实验与结果
三种瓦努阿图语言：Bislama（13h45m）、Nafsan（14h50m）、Nguna（1h01m）。学习曲线显示早期 ToTy 优先通常 CER 最低；SNR/最少重叠并不更优。作者认为基础模型已较抗田野噪声，缺的是目标语词汇与拼写规则，故早期喂入高词汇密度/重复会话更有效。全文在「Lexical Breadth and Depth」处抽取截断，后续定量细节与结论段不完整。

## 结论
可读部分表明：冷启动应优先语言分布（丰富度与重复）而非声学洁净度；Easper 把无代码 workflow 与该选择策略绑定，便于人在环迭代。

## 点评
同时解决工具可达性与数据选择策略，贴近真实「按场次转写」工作流。ToTy 设计针对「重复利于学习」合理；脆弱点在 session 级不可分割可能混入噪声片段，且 Nguna 极小、学习曲线有 catastrophic forgetting 尖峰。正文后半抽取截断，点评未编造未读到的数字。
