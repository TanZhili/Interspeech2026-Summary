# Influence of Vocal Tract Curvature on Speech Acoustics: A Three-Dimensional FEM Analysis

- 论文编号：2325
- 报告人：Debasish Ray Mohapatra
- 程序：Monday 28 September 2026 / Methods and data for vocal tract and articulation analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/mohapatra26_interspeech.pdf

## 问题
许多物理声学模型把声道当直管；真实弯曲对共振的独立贡献难以从不规则截面、旁腔等中分离。

## 方法
3D FEM 波求解器，中心线长固定 17 cm，系统改变弯曲角（60°/90°/120°）与曲率强度；对比均匀截面 vs Story [A] 非均匀面积函数。分析至 14 kHz 的传递函数与声场。

## 实验与结果
均匀截面：弯曲对频率响应几乎无影响，与直管一致。非均匀截面：低于约 8 kHz 与直管接近；更高频出现曲率相关反共振/横向高阶模，位置随弯曲角变化；约 10 kHz 以上可见可辨共振偏移。压力场在非均匀弯管中显示横向模式结构。

## 结论
曲率 alone 在均匀管中可忽略；与截面非均匀耦合时主要在高频激发横向模并移动共振。直管理想化在低频尚可，宽带/高精度合成需考虑弯曲。

## 点评
受控几何消融把“弯不弯”从复杂解剖中拆出，结论对 articulatory 合成建模有直接指导。局限：简化圆柱段拼接、单一 [A] 面积函数、未含唇辐射与旁腔完整解剖。
