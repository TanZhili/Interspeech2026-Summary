# BiEAR: A Human Auditory-Inspired Adaptive Binaural Front-end for Multi-Speaker Localisation and Distance Estimation

- 论文编号：1618
- 报告人：Hanyu Meng
- 程序：Monday 28 September 2026 / Spatial Audio 1
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/meng26c_interspeech.pdf

## 问题
双耳定位与测距多采用固定推理图与前馈前端，难适应非平稳场景与未见环境；且常省略人类听觉中的内侧橄榄耳蜗（MOC）传出反馈。需要可在推理期自适应调节频率选择性的双耳前端。

## 方法
BiEAR：八个 45° 扇区各自 SAD-Net，联合检测源、估方位、分距离类。STFT 后用 ERB 尺度可调 Gabor 子带；每耳用 GRU+FC 控制器，据瞬时与平滑子带 SPL 输出 δ∈[−1,1] 调制 Q 因子（绝对或相对基线 Q）；由 Z 提 ILD/IPD，波形算 CC（±3 ms→100 维），GRU 压缩后进后端。消融：无控制器 / 单控制器 / 双控制器 × Abs/Rel。评测无回声（见/未见说话人，1–3 说话人）与会议室、报告厅（未见说话人，可做环境迁移微调）。

## 实验与结果
无回声：双控制器+Rel 最优（如 1 说话人方位 MAE 约 0.36°/0.39° 见/未见；3 说话人约 8.03°/8.18°），优于 DeepEar、AuralNet 的检测与方位，距离上 AuralNet 仍更强。实房间零样本已优于基线，环境迁移后进一步提升（如会议室 1 说话人检测 93.74%、MAE 3.92°）。可视化显示近耳中高频增强 Q、低频两侧不对称调制，主动控制使时频能量更集中。

## 结论
MOC 启发的双耳自适应滤波可提升多说话人定位鲁棒性并对未见房间更易迁移；控制器是工程抽象而非完整生物模型。结论末抽取略有截断。

## 点评
把“传出反馈→Q 控制”接到扇区定位管线，双耳独立控制器是合理归纳。增益主要在检测/方位，距离仍弱于自注意基线，说明自适应前端与后端任务并不完全同构；实房间迁移仍依赖额外微调，纯零样本空间仍有限。
