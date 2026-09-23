# Perceptually Weighted Minimum Mean Square Error Precoding for Acoustic Multi-User MIMO in Vehicular Personal Sound Zones

- 论文编号：1191
- 报告人：Huihui Wei
- 程序：Tuesday 29 September 2026 / Spatial Audio 3
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/wei26c_interspeech.pdf

## 问题
车舱个人声区（PSZ）中串扰与频率选择性衰落严重；传统对比控制/压力匹配常把串扰当均匀物理能量，且 bright/dark 二分难同时服务多用户。需要把听感掩蔽纳入多用户联合预编码。

## 方法
将车载扬声器–座位麦克风建模为频域声学 MU-MIMO；在 WMMSE 框架中引入感知加权矩阵 Θ_k：由目标语音的 MPEG 风格掩蔽门限与绝对听阈生成，对敏感时频区加重误差惩罚。目标最小化加权 MSE，并约束总功率与最小声对比度。预编码按 WMMSE 迭代闭式更新或凸优化求解。

## 实验与结果
实车测得 IR：7 扬声器、四座各 16 麦（共 64），ATF 测三次平均；语音来自 LibriSpeech。MU MIMO Perceptual 的 STOI 0.859、ViSQOL 4.191，高于无加权 MU-MIMO 与 ACC/PM/VAST/RACC 等基线。频带上 AC、NRE、AE 三者折中优于偏重对比或过度稳健的方法。

## 结论
感知加权 WMMSE 可在多区同时优化重建与干扰，相对传统声区控制提升客观语音质量；未来将加强 IUI 抑制与不确定条件下的鲁棒性。

## 点评
把通信域 WMMSE 迁到宽带车舱声学，并用掩蔽驱动 Θ_k，比均匀 MSE 更贴近听感。增益相对无加权基线数值不大（STOI +0.002），主要说服力在多用户联合与指标折中；实验为离线测得信道+回放指标，未报听者主观与头动/座位变化鲁棒性。
