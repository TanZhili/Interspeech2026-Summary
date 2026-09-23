# Mind the Gap: Detecting Cluster Exits for Robust Local Density-Based Score Normalization in Anomalous Sound Detection

- 论文编号：177
- 报告人：Kevin Wilkinghoff
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 1
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wilkinghoff26_interspeech.pdf

## 问题
嵌入空间异常声检测中，局部密度归一化（LDN）对邻域大小 K 敏感：K 增大常因越过簇边界破坏局部性而变差，固定小 K 又欠稳。

## 方法
分析排序距离与距离比 r_k=d_k/d_{k+1}，用尖锐跳变定义 cluster exit。提出训练无关的 CED：对每个参考样本根据距离比（可邻比平滑）检测退出点，自适应选取邻域大小再做 LDN（可叠加 VarMin）。即插即用替换固定 K。

## 实验与结果
五类嵌入（含 Direct-ACT、OpenL3、BEATs、EAT 等）× 多基准：相对固定小邻域，LDN+CED（及 +VarMin）在宽 K 扫描上相对性能更稳、整体增益一致（文中相对性能曲线约 1.0–1.07 量级）。目标域常更早出现簇退出，解释固定大 K 失效。

## 结论
邻域应随局部性是否保持而自适应，而非先验固定；CED 轻量且无训练，提升 LDN 对 K 的鲁棒性。

## 点评
把“大邻域不稳”归因于结构上的簇退出而非单纯统计噪声，诊断清晰。阈值固定、无标签设定适合工业监测；对极度重叠或连续流形嵌入，距离比启发式可能误触发，需场景校验。
