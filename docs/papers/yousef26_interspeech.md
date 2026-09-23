# Modeling Lombard Effects in Voice Disorders Using Daily-Life Monitoring of Ambient Noise and Voice Acoustics

- 论文编号：2777
- 报告人：Ahmed M. Yousef
- 程序：Wednesday 30 September 2026 / Speech, Voice and Language Disorders
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/yousef26_interspeech.pdf

## 问题
Lombard 效应多在实验室噪声回放中研究；嗓音障碍患者在真实环境噪声下的多维度发声调节（含音质）了解不足，既往日常监测多只看 SPL/F0 与分箱噪声均值。

## 方法
14 名 PVH（双侧小结）、10 名 NPVH（肌紧张性发声障碍为主）、18 名健康对照，2–4 天、≥10 h/天佩戴颈表 ACC（估 SPL、F0、CPP、H1H2）与肩麦噪声剂量计（Leq，说话段剔除）。3 分钟窗汇总噪声（均值、SD）与嗓音统计，用相关与线性/二次 Ridge·Lasso/GBR 预测嗓音指标，报告 PDP 斜率。

## 实验与结果
噪声升高时 SPL、F0、CPP 升、H1H2 降；CPP 与 Leq 相关最强（r=0.36–0.53）。非线性模型最优，CPP 最大 test r²=0.32。PVH 在高噪声环境时间占比最高（>70 dBA：26.1%）。相对 NPVH，PVH 的 SPL–Leq mean 斜率更陡（0.65 vs 0.47 dB/dB），CPP–Leq mean 斜率更大（0.18 vs 0.11）；Leq SD 对 SPL 的斜率在 PVH 达 0.86。F0 对噪声均值的响应对照最大。

## 结论
日常 Lombard 呈多维、子类型特异：PVH 在 SPL/CPP 上调节更强，NPVH 相对受限；CPP 可捕捉超出 SPL/F0 的音质效应，噪声变异与均值同等重要。局限含组间年龄差异与噪声 alone 解释力有限。

## 点评
把 Leq 均值与变异同时建模，并用 CPP/H1H2 补足既往「只看响度/音高」的盲区，能区分 PVH 与 NPVH。窗口级 train/test 分割不声称说话人泛化，斜率更适合作组内解释。预测 r² 不高说明还需环境、距离等上下文特征。
