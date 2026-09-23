# Speech-based Digital Biomarkers can Accelerate ALS Clinical Trials: Insights from Time-to-Event and Hazard Rate Analysis

- 论文编号：2847
- 报告人：Vikram Ramanarayanan
- 程序：Monday 28 September 2026 / Clinically Useful Speech Representations 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/kothare26_interspeech.pdf

## 问题
ALS 试验主终点 ALSFRS-R 对早期球麻痹变化不够敏感且可能非线性；多数语音生物标志评估用线性混合模型，对非正态、异方差与不规则随访不够稳健。需要用 time-to-event 视角检验语音/面部数字标志能否更早检出功能下降，并据此估计试验样本量与时长。

## 方法
EverythingALS 招募、Modality 平台远程纵向采集（约每 2 周；2020-11 至 2024-04）。Praat / MFA 提语音特征，MediaPipe 提面部运动，spaCy 提图画描述语言特征；聚焦九个既往敏感指标。事件定义为达到最保守（最大）MCID；ALSFRS-R 言语题下降 1 分、球麻痹亚分下降 3 分。Kaplan–Meier + log-rank；由 KM 用指数近似估 hazard rate，再按 log-rank 公式在 HR=0.5/0.8、3–24 月下估每臂样本量，或固定 n=30 估所需时长（80% power，α=0.05）。

## 实验与结果
九个数字标志的 KM 曲线均比 ALSFRS-R 更陡：20% 患者达 MCID 最短约 14 天（阅读段落最大唇宽），最长约 100 天（阅读段落时长）；对应 ALSFRS-R 球麻痹亚分约 660 天、言语题约 208 天。数字标志相对球麻痹亚分均 log-rank p<0.001。示例：HR=0.8、12 月时球麻痹亚分约需 2551/臂，而 CTA、时长、F0、唇宽等可降至数百甚至数十；n=30/臂、HR=0.5 时球麻痹需约 137 月，最大唇宽约 4 月。

## 结论
远程语音/面部数字标志可更早检出临床有意义变化，有望缩短试验、减少样本量；宜与传统量表联用。局限：患者异质性、常数 hazard 近似、删失偏倚，泛化仍待验证。

## 点评
把“更敏感”直接翻译成试验设计数字（样本量/时长表），对产业与临床读法都很有冲击力。MCID 取最保守估计降低假事件，但 KM+指数近似仍假设风险形态，且唇宽等与 ALSFRS-R 相关弱却事件极早，需警惕测量噪声与定义阈值对“加速”幅度的放大。
