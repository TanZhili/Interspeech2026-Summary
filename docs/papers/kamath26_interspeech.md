# Sensitivity Analysis of Generative Spatial Audio Metrics : A Study on Responsiveness, Smoothness, and Symmetry

- 论文编号：252
- 报告人：Purnima Kamath
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kamath26_interspeech.pdf

## 问题
生成式 First-Order Ambisonics（FOA）缺少对评价度量如何随方位角/仰角等空间控制参数变化的系统认识，难以判断哪些 metric 真正反映空间可控性。

## 方法
提出沿连续空间轨迹做 meta-evaluation：定义 Responsiveness（拟合距离—角位移“帐篷”曲线的平均绝对斜率×R²）、Smoothness（邻域距离抖动的逆标准差）与 Symmetry（正反轨迹距离 RMSE 的指数映射）。用 SoundSpaces RIR + SpatialScaper + FSD50K 合成单源（SS）、多源反向旋转（MS）、同类别多实例（SSMI）及加噪版本，共约 68,400 条 10 s FOA；评估 FAD（M-VGG / S-CRW / F-GRAM / F-PSELD）与样本度量（IV、LSD、IPD、GCCPHAT、MVDR-AM+LPIPS）。

## 实验与结果
F-PSELD 与 MVDR-AM 在 Responsiveness 与 Smoothness 折中上 consistently 居高，且对噪声与场景复杂度更稳；IV 在 SS/MS 尚可，SSMI 对称多源下曲线塌缩。LSD/IPD/GCCPHAT Responsiveness 低，噪声下响应更平坦。多数度量 Symmetry 都高，单独作敏感指标不够。

## 结论
定位导向嵌入与声学图类度量更适合刻画生成空间音频的参数敏感性；研究限于合成 FOA 与有限度量集，后续需真实数据与感知验证。

## 点评
把“度量是否跟得上空间控制”做成可量化的三条曲线性质，比单纯报 FAD 数字更有诊断力。合成轨迹与 20° 步进清晰可控，但对真实生成模型误差分布的迁移仍待检验；IV 在对称多源失效说明空间 cue 选择要看场景结构。
