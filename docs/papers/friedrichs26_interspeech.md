# Acoustic Pharyngometry as an Auditable Anchor for Cross-Speaker EMA Normalization

- 论文编号：1883
- 报告人：Valeriia Vyshnevetska
- 程序：Monday 28 September 2026 / Methods and data for vocal tract and articulation analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/friedrichs26_interspeech.pdf

## 问题
跨说话人 EMA 比较受声道形态混淆；全局相似变换可解释但弱，灵活非刚体配准又难审计。需要低负担、可检查的解剖锚。

## 方法
在腭参照坐标系下：用腭包络长做均匀缩放；从声学咽测量面积函数提取口腔扩张峰相对 OPJ 的比例 \(u_{peak}\)，锚定分段单调前后（A–P）翘曲。德语 14 人（有 EMA+咽测量）DDK 与持续元音：评说话人间轨迹离散度、LOSO 岭回归 F1/F2 预测、说话人识别。

## 实验与结果
多传感器舌轨迹离散度从 31.28 mm → 26.36 mm（仅缩放）→ 26.13 mm（缩放+翘曲，总降约 16.5%，主来自缩放）。LOSO 对 F1/F2（Hz/Bark/VTLN）预测未改善。绝对位置说话人识别高；去静态偏移后下降，说明仍有残余说话人结构。

## 结论
腭长缩放+咽测量锚定翘曲可提升几何可比性与可审计性，但不自动改善说话人无关的发音–声学映射。

## 点评
强调“改什么、能查什么”的规范化设计，对实验语音学很务实。结果显示几何对齐≠声学映射统一，提醒技术应用勿过度解读归一化收益。
