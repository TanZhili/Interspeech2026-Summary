# Automatic Detection of Stress from Speech in the Trier Social Stress Test

- 论文编号：671
- 报告人：Wieland R. Cremer
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/drimalla26_interspeech.pdf

## 问题
压力多用自评与唾液生物标志，难无创高频采集；需验证语音能否在被试间设计下区分 TSST 与友好对照，并预测生理/情感反应。

## 方法
50 名健康德语大学生随机分入 TSST 或 f-TSST；收集唾液皮质醇、sAA 与 PANAS。眼动眼镜麦克录音，Sortformer 说话人分离后提 MFCC、Praat 嗓音参数与 eGeMAPS（共 144 维+性别）。嵌套交叉验证训练 LR/SVM/RF/XGB 分类与 SVR/RFR/XGB 回归。

## 实验与结果
操作检验：TSST 后皮质醇与负情绪显著升高。分类最佳 XGB 准确率 0.82±0.11、RF AUC 0.85，显著优于多数类基线。SHAP 突出浊音谱流变、极低/低频能量、浊音段速率与 shimmer 变异。全样本 SVR 可优于虚基线预测皮质醇反应性；部分模型可预测 ΔNA；sAA 与 ΔPA 较难。

## 结论
声学–韵律特征可无创区分急性格社会压力情境，并部分预测皮质醇与负情绪反应。

## 点评
被试间 TSST vs f-TSST 避免先前被试内设计的顺序污染。眼动镜麦克与分离后拼接改变停顿结构，可能影响时长类线索。n=50、大学生样本限制外推；回归效应中等，不宜替代生物标志而宜作辅助监测。
