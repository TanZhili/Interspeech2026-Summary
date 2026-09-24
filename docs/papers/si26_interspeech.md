# Explicit Context-Driven Neural Acoustic Modeling for High-Fidelity RIR Generation

- 论文编号：513
- 报告人：Chen Si
- 程序：Wednesday 30 September 2026 / Speech Enhancement and Restoration
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/si26_interspeech.pdf

## 问题
RIR 是房间声学仿真的核心；近年神经隐式方法（NAF、NACF、NeRAF 等）多用图像或隐式网格作上下文，几何信息间接且粒度粗。场景专用模型缺结构化局部几何，而 Mesh2IR 等生成式全局网格编码又偏场景泛化、细粒度物理细节易被稀释。

## 方法
提出 MiNAF（Mesh-infused Neural Acoustic Field）：在 Tx/Rx 位置用 Fibonacci 格点发射 N 条射线，查询粗糙房间网格，收集到首次命中点的距离 d、法向 n、邻域射线距离均值/标准差 μ/σ，以及按距离阈值的占用直方图 occ；各特征经非线性投影后与正弦位置编码的坐标拼接成上下文。时间索引也做位置编码并与上下文逐元素相乘，再连同 Rx 朝向 θ 与双耳通道 c 输入 MLP，分别预测 STFT 的 log-magnitude 与瞬时频率（IF），经 iSTFT 还原时域 RIR。损失为谱 L1 加 Schroeder 能量衰减曲线项。

## 实验与结果
数据为 SoundSpaces（基于 Replica），选取 6 个房间（矩形/非矩形单室与多室），80%/5%/15% 划分；另在更大、更稀疏的 GWA 公寓上评测。指标为 T60、C50、EDT；对比 Opus/AAC 插值与 INRAS、NAF、NACF、AV-NeRF、NeRAF 等。正文抽取在对比表中途截断，仅可见部分基线数值（如 NACF T60 2.36%、C50 0.50 dB、EDT 0.014 s），MiNAF 自身完整数字与结论段未出现在可用全文中。引言称在少样本条件下可优于先前 SOTA，并有项目页补充材料。

## 结论
作者主张用网格射线探测得到的显式局部几何能更好引导神经隐式声学场，从而更准地生成任意 ⟨Tx,Rx⟩ 的 RIR；因全文后半缺失，作者最终定量结论与边界表述无法从正文完整核对。

## 点评
设计抓的是“局部几何（距离分布/法向）应直接进入场景专用声学场，而不是只靠图像或隐式特征格”。射线统计特征预计算分布，减轻 MLP 自己从原始距离推断几何的负担，物理可解释性较强。当前可用全文在实验结果表中途截断且含乱码，MiNAF 相对基线的具体增益只能依据方法叙述推断，不能当作已核实数字使用。
