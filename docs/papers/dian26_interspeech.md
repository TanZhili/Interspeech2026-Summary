# Reconciling Dynamic Data Analysis with Linguistic Reality: Comparing Legendre Polynomial Modelling and GAMM Applied to Prosodic Contact

- 论文编号：2585
- 报告人：Angelo Dian
- 程序：Monday 28 September 2026 / Tools and Techniques for Phonetic Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/dian26_interspeech.pdf

## 问题
接触引发的语调变异是动态轮廓问题；单点音高分析不足。Legendre 多项式与 GAMM 都能建模非线性 F0，但各自揭示的语音学信息、如何对接音系解释，需在同一接触语料上对照。

## 方法
以塞浦路斯希腊语（CYG）与雅典希腊语（ATG）年轻人延续升调为案例：在兴趣区（RoI）上分别做 **Legendre 多项式系数**（再 LMER）与 **GAMM** 平滑比较。CYG 按听感核高/核低分为 CYG-nh / CYG-nl。

## 实验与结果
- 两法一致：CYG-nh 与 CYG-nl、ATG 不同——整体斜率更小、曲率更大、更 N 形；ATG 与 CYG-nl 相近。
- 多项式：variety×tone 对 c1–c3 均显著（如 c1 \(F(2,21.41)=74.872,p<.001\)）；CYG-nh 在三维系数空间独立成簇。
- GAMM：形状差异显著、整体高度不显著；CYG-nh vs ATG 在归一化 RoI 约 **29–50%** 核高目标附近显著偏高，并与 CYG-nl 在更大区间有差异。

## 结论
多项式抓全局几何，GAMM 定位相对时间上的局部差异；互补使用更利于接触语调的语音实现与音系解释。

## 点评
方法论文色彩强：同一语言事实上展示两种动态分析各擅长什么。强在收敛结论 + 时间定位互补；样本年轻说话人、听感预分类可能影响类别边界，但作者以档案研究为先验支撑。
