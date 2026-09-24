# Hierarchical Conditional Continuous Normalizing Flows for Creaky Voice Editing under Speaker Identity Preservation

- 论文编号：1341
- 报告人：Petra Wagner
- 程序：Thursday 1 October 2026 / Flow Matching for Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rautenberg26_interspeech.pdf

## 问题
嗓音编辑希望改 creak 等副语言品质而不动说话人身份；群体数据上 creak 与平均基频、性别强相关，单阶段条件流易学到跨说话人相关，改 creak 时连带改 pitch/身份。数据增强去相关仅针对特定属性，缺乏通用结构解耦。

## 方法
提出分层条件连续归一化流：a1=平均 f0+性别，a2=breathiness+roughness+creak。两段 ODE：先用 f1 条件 a1，再用 f2 条件 a2；中间潜变量 z(tm) 上对 f0/性别做 Domain Adversarial Training（GRL），促其中间表征对高层属性不变。编辑时前向到基分布再按目标条件反传。后端 YourTTS；在 LibriTTS-R 上训练，对比 base-flow、加条件与对抗的单阶段 base-extd.、以及 pitch 数据改造的 data-mod.-flow。

## 实验与结果
客观：跨 β∈[-1.25,1.25] 的 creak 操纵，hierarch 的 |Δf0|、性别准确率与说话人验证 EER 最稳，明显好于 base。主观（11 名嗓音质量专家）：两模型都能放大感知 creak；hierarch 的 SMOS 下降显著小于 base（尤其放大条件），MOS 无显著变差。

## 结论
作者认为分层注入条件并对抗剥离高层属性，可在无任务专用数据改造下更好保留说话人身份地编辑 creak；是否泛化到其他纠缠属性仍待验证。

## 点评
用“阶段分隔 + 中间对抗”硬切断低层编辑回流到高层身份，比单靠数据去相关更可迁移。主观上身份仍会有一定损失；creak 抑制因基线感知 creak 较低而不够显著，效果边界需更多标注与场景检验。
