# A Hierarchical Feature Engineering Framework for Automated Classification of Phonotraumatic and Non-Phonotraumatic Vocal Hyperfunction

- 论文编号：3437
- 报告人：June-Woo Kim
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kim26x_interspeech.pdf

## 问题
颈表加速度计可监测日常嗓音过度功能（VH），但多依赖单特征时间平均，忽略动态与源–滤波生理耦合；PVH 与 NPVH 子类型在自然场景下仍难稳健区分。

## 方法
在 NeckVibe 上分层构造特征：(i) 静态分布（mean/SD/P5/P95/偏度/峰度/IQR 等，含 vocal dose）；(ii) 一/二阶差分动态描述；(iii) 相对变异比率（如 ΔSD/mean）；(iv) 生理动机耦合项（如 CPP/spectral tilt、CPP/H1–H2、CPP/ΔSD、IBIF naq/ΔSD 等）。仅 voiced 帧聚合到受试者级；缺失 IBIF 在 ML 中按折内中位数填补。用 Welch t + BH-FDR 做单变量检验；RFECV（XGBoost）选特征后比较 LR/SVM/RF/XGBoost/LightGBM；分层 10-fold 按受试者分组。

## 实验与结果
CV：PVH 最佳 AUC 0.891±0.04（耦合+逻辑回归）；NPVH 最佳 0.728±0.10（耦合+LightGBM）。PVH 大量特征 FDR 显著且效应大；NPVH 无特征通过 FDR。官方测试：PVH AUC 0.917，NPVH 仅 0.579。SHAP 显示 PVH 多特征分布式贡献，NPVH 更依赖高阶动态且不稳定。

## 结论
PVH 近乎可用线性/多变量结构分离，耦合特征有增益；NPVH 与对照分布重叠大，当前手工特征不足。作者建议未来用原始波形 SSL 捕捉非平稳微颤等线索。

## 点评
把“特征层次是否带来增量”做成可消融对照，并用统计显著与 ML 对照解释 PVH/NPVH 不对称，方法清晰。弱点是测试集 NPVH 崩塌暴露日级汇总对功能失调类不够；任务表述在文中多为 vs 匹配对照，与挑战“vs 全部非目标”不完全一致时需注意解读。
