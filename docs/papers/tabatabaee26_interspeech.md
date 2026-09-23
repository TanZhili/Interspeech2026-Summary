# Towards Language-Agnostic Speech Inversion

- 论文编号：1633
- 报告人：Saba Tabatabaee
- 程序：Monday 28 September 2026 / Methods and data for vocal tract and articulation analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/tabatabaee26_interspeech.pdf

## 问题
言语反演（SI）多在英语 EMA/XRMB 上训练；声道声学跨语言共享，但跨语恢复 oral TV、腭咽 TV 与声源参数的能力验证不足。

## 方法
WavLM-Large 特征 → 多任务 SI：六种 oral TV（LA/LP/TBCL/TBCD/TTCL/TTCD）+ Per/Aper/F0，可选 VP（对标 nasalance）。英语 XRMB + 自建 YU（英/法/俄共录 EMA、nasalance、音频）训练；在未见法语、俄语上评 Pearson 相关。

## 实验与结果
跨 oral TV 与声源参数，法语 PPMC 约 0.83、俄语约 0.74。VP/nasalance：英语 0.92、法语 0.89、俄语 0.82。定性轨迹显示 TBCD/TTCD/LA 在未见语言上仍跟踪 ground-truth；可反映预期性鼻化等跨语言差异。

## 结论
仅英训 SI 可较好泛化到法/俄的 oral、VP 与声源参数，支持更接近语言无关的发音反演。

## 点评
补上跨语 SI 实证缺口，尤其含 VP。样本上法语/俄语说话人很少，俄语 VP 仅 1 人，泛化结论需更大样本复核。
