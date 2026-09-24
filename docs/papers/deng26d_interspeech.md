# Joint Learning of Covariance Estimation and White Noise Gain for Robust MVDR Beamforming

- 论文编号：2212
- 报告人：yongyi deng
- 程序：Thursday 1 October 2026 / Multi-Channel, Beamforming and Spatial Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/deng26d_interspeech.pdf

## 问题
MVDR 对麦克风自噪声与阵列失配敏感，常用固定 WNG 阈值或对角加载，在未知/时变声学与器件条件下次优；学习型波束形成多改进协方差估计，却很少把 WNG 本身纳入端到端优化。

## 方法
双分支网络（多线索融合 JNF 骨干）：一支预测复 T–F 掩码估计噪声协方差，一支预测逐频 WNG 阈值；嵌入可微的 QEP 形式 WNG 约束稳健 MVDR 层。训练用增强输出与 early-reference 波束形成信号的 MAE，无需显式 WNG 监督，由重建损失隐式驱动稳健性–指向性折中。

## 实验与结果
VCTK、8 麦 ULA（2 cm）、端射目标、多干扰与扩散/白噪声。相对 FullSubNet 掩码 + 最优固定 WNG（−6 dB）及提出模型的最优固定 WNG（−8 dB），自适应 WNG 在 SNR/STOI/SDR/PESQ 分布上更好。已见阵列（δ=2.0±ϵ cm）上提出方法 SNR gain/ΔSDR 为 11.940/11.474，高于最优固定 W0 的 10.543/9.510 与最优对角加载。未见阵列间距设定下亦有对比（正文表格后续行因抽取截断，定性结论为自适应仍更优）。

## 结论
作者认为把 WNG 当作可学习物理控制量并与掩码协方差联合优化，可在失配条件下稳定优于固定稳健性设定。

## 点评
把稳健性旋钮从经验超参拉进可微 MVDR，问题抓得准。实验以仿真 ULA 为主；正文部分图表抽取有乱码，未见阵列定量细节需对照 PDF。early-reference 目标与真实失配分布的匹配程度决定可迁移性。
