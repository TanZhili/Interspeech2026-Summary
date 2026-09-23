# CoSTALA: Compositional Spatio-Temporal Audio-Language Alignment via Multi-Grain Hierarchical Contrastive Learning

- 论文编号：1110
- 报告人：Peiwei Ren
- 程序：Tuesday 29 September 2026 / Spatial Audio 3
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/ren26b_interspeech.pdf

## 问题
常规 ALM/CLAP 多为全局粗粒度对齐，难处理多事件空间音频序列，易出现上下文漂移、局部语义被平均掉。需要从全局对齐迈向可分辨时序与方位组合的细粒度时空对齐。

## 方法
基于 Clotho 合成 FOA（SRIR 卷积），用 Qwen3-8B 把方位离散到八方向并改写描述；正样本为两段不重叠事件拼接，负样本含时间反转与空间互换。架构：RoBERTa 文本编码 + HTSAT 语义/空间双分支音频编码 + RoPE Transformer 时序编码；产出 hard/soft/global/spatio-temporal 多级嵌入。层次损失：对比 Lcl、三路时空 Lst、局部对齐 Llocal、特征一致性 Lconsist（soft 对齐 stop-grad hard）。

## 实验与结果
约 375 小时、3 万训练 / 9k 评估。完整 CoSTALA 全局时空检索 Text→Audio R@1/5/10 为 8.10/19.86/27.68，优于 SALM、T-CLAP 及仅部分损失配置；Audio→Text 亦最优。仅用语义音频嵌入对接时空文本时检索崩塌，说明空间通路必要。消融显示 Llocal 与 Lconsist 需联用才达峰值。

## 结论
多粒度层次对比与显式时空负样本可缓解长序列全局塌缩，为多事件空间音频–语言理解提供更细粒度基础框架。

## 点评
硬负样本设计（时间 vs 空间错误）把“顺序”和“方位”拆开监督，针对性强。数据全为两事件无重叠拼接的合成 FOA，真实重叠、混响与自然叙述复杂度仍未覆盖；语义-only 崩塌结果有说服力，但评估仍以检索为主，未展示下游生成/QA。
