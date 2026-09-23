# Tonal Contrasts in Different Vowel Contexts and Different Tonal Systems

- 论文编号：1215
- 报告人：Mingxing Li
- 程序：Monday 28 September 2026 / Tones
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/li26v_interspeech.pdf

## 问题
声调由 F0、时长、强度与音质等多线索实现；不同元音（含顶音）有内在音高差异，不同高度区分度的声调系统是否在线索权重上不同，尚欠系统比较。

## 方法
录两个湘方言：寿燕（SY，约三级高度 /43,33,11/）与梅花（MH，约四级 /55,44,33,21/）。各在顶音 [ɹ̩]、高前 [i]、低后 [a] 上做最小对比词；9/8 名男性说话人，载句内各 9 次。ProsodyPro 提 F0/时长/强度，VoiceSauce 提 H1*-H2*、HNR、CPP、SoE 等。LMM/生长曲线分析 + XGBoost+SHAP 估线索相对贡献。

## 实验与结果
高调总体更短、更强、更周期（HNR/CPP）。[i] 上调类 F0 跨度更大；音质差异也常在 [i] 更显著，顶音上部分模式例外（如 MH 的 t33 时长最短）。MH 的 t21 相对高度随元音变化大。XGBoost+SHAP：两方言均以 F0 类线索最重要；高度层次更多的 MH 更倾向动用更多线索。

## 结论
不同高度的调类呈多维差异；同一对立在不同元音上线索权重可变；高度区分更细的系统可能依赖更多线索。

## 点评
把元音语境与声调库存规模绑在一起比较，对“声调空间如何填满”有启发。仅男性、两方言各一、SHAP 解释仍依赖分类任务构造，外推到更大方言样本需谨慎。
