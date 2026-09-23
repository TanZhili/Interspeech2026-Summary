# Automated Gradient-Driven Parameter Sharing for Low-Resource Multilingual Speech-to-Text Translation

- 论文编号：1292
- 报告人：Ruiyan Sun
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/sun26d_interspeech.pdf

## 问题
多语 S2T（如 SeamlessM4T）均匀共享参数，在低资源下易出现梯度冲突与负迁移；共享–私有结构多靠人工或昂贵 NAS，配置搜索难扩展。

## 方法
提出 GDPS：从梯度行为自动定共享配置。(A) 语言间梯度余弦 + 聚类得分组；(B) 自任务/跨任务梯度相似度差 δ 映射共享比例；(C) Joint SVD + 正则 CCA 得子空间与能量比例，用于私有支路初始化。实例化：只特化 Encoder Layer 11 的 FFN2，分成共享与组私有分支（分析得 Group1=Bem，Group2=Aeb/Est/Gle，约 50% 共享），再分组微调。

## 实验与结果
IWSLT 2025 低资源四语→英（aeb/bem/est 各 20k，gle 7k）。相对 Unified FT：如 Gle BLEU 43.59→46.20、COMET 0.7257→0.7473；Aeb BLEU 7.64→8.74。相对提升最高约 BLEU 14.4%、BERTScore 11.9%、COMET 3.26%。消融显示 A/B/C 缺一则降；50% 共享优于 75%/25%；换到低冲突模块（L10 FFN2、Adapter）增益变小或变差。

## 结论
用训练动态直接导出共享配置，可在低资源多语 S2T 上稳定优于统一微调，无需手工架构搜索。

## 点评
把“哪一层冲突、哪些语该一组、共享多少”从经验变成可测的梯度统计，再只动冲突瓶颈 FFN，改动面可控。Purity Paradox（更深更自相似却更不纯）解释选层有说服力。脆弱处是阈值与 k=2 分组偏数据依赖，四语规模小，换骨干或语对需重跑分析；且相对吃外部大数据的 IWSLT SOTA 仍有差距。
