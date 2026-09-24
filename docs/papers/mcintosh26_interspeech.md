# Speech Playground: An Interactive Tool for Speech Analysis and Comparison

- 论文编号：3604
- 报告人：Stephen McIntosh
- 程序：Wednesday 30 September 2026 / Speech Analysis, Data Resources and Research Tools
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/mcintosh26_interspeech.pdf

## 问题
Praat 等工具难方便接入现代深度学习表征并做句对比较；研究者常需拼编码器、对齐与临时可视化脚本。

## 方法
Speech Playground：SvelteKit 前端（Analysis 单轨 / Diff 双轨）+ FastAPI Python 后端懒加载模型。统一 encoder 接口覆盖 SSL、发音、音系特征、段级及 ZeroSyl 等可变长表征，可离散化；Diff 模式用 DTW 或段/离散对齐，可切换距离与全局/半全局匹配。支持 TextGrid、可选 MFA 强制对齐、录制与同步听对比。IndexedDB 管理本地样本库。

## 实验与结果
本文为工具介绍与 UI/工作流演示（含音系向量层、帧级 DTW 距离层、发音反演特征对齐等截图）；未报告独立基准实验数字。开源仓库与可选 mfa-service 已给出。

## 结论
在同一交互界面比较多种连续/离散/变长表征与对齐设定，服务语音研究、表征校验与 CAPT 向实验。

## 点评
Diff 模式把“听哪里不同、表征哪里不同”绑在一起，对 CAPT 与表征调试很贴切。扩展性依赖 encoder 插件生态；大模型加载与实时性权衡正文未量化。
