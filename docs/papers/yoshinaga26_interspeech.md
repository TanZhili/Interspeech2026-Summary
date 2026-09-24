# Noise Scaling Factor for the One-Dimensional Voice Production Model

- 论文编号：559
- 报告人：Tsukasa Yoshinaga
- 程序：Tuesday 29 September 2026 / Speech Production and Perception 1
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/yoshinaga26_interspeech.pdf

## 问题
气声等嗓音含声门湍流噪声；1D 声学模型常用 Fant 型噪声公式及任意缩放因子，该因子相对显式湍流的 3D 流声仿真是否普适，少有系统检验。

## 方法
对元音 /a/、/u/ 做 3D 可压 Navier–Stokes 流声仿真（正常与不完全闭合气声），与嵌入 Fant 噪声项的 1D 模型对比频谱；扫描缩放因子使谱差最小，考察常规值何时成立。

## 实验与结果
/a/ 正常发声、声门可完全闭合时，传统缩放因子与 3D 吻合较好。气声（声门不完全闭合）及 /u/ 存在声门上收缩时，最优缩放偏离常规值；谱差随因子变化有明确谷值。结论：湍流噪声建模需随声道流场构型调整。

## 结论
1D 噪声缩放并非全局常数；应按声门闭合与声门上几何调节，以兼顾精度与远低于 3D CFD 的计算成本。

## 点评
用 3D 真值标定 1D 经验参数，对气声病理与合成功用直接。强在正常 vs 气声、/a/ vs /u/ 对照；脆弱点在仅两元音与有限构型，外推到动态协同发音需更多验证。
