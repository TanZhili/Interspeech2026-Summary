# Towards Array-Invariant Speech Enhancement via Geometry-Aware Dynamic Convolution

- 论文编号：548
- 报告人：Zhenglong Liu
- 程序：Thursday 1 October 2026 / Multi-Channel, Beamforming and Spatial Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liu26d_interspeech.pdf

## 问题
多通道语音增强依赖固定阵列几何，难跨设备复用数据与模型；现有 array-agnostic 方法可处理麦数与排列变化，但很少显式利用可用的麦克风坐标先验，空间滤波往往弱于固定阵列模型。

## 方法
提出 Geometry-Aware Dynamic Convolution（Geo-DConv）：用麦克风相对坐标的 Fourier 位置编码 + Topology-Aware Coordinate Transformer（TACT，MHSA）生成变换矩阵 M，将固定基卷积核线性组合成与输入通道数匹配的动态核，经 LN+PReLU 后接到下游固定阵列网络。TACT 对通道置换等变，保证卷积结果置换不变。将 SpatialNet、TF-GridNet 等首层卷积替换为 Geo-DConv，即可转为阵列不变系统。

## 实验与结果
在真实录制 RealMAN（32 麦子阵列、8 kHz、4 s 片段）上训练。几何不变设定下 SpatialNet-Geo-DConv：SDR/SI-SDR 9.72/4.22，优于 FaSNet-TAC 与 USES2-comp，参数约 1.3M、MACs 约 6.08 G/s。可变麦数训练进一步提升。1/2/5 麦与跨数据集 CHiME-4（未微调）上 DNSMOS OVRL 分别升至约 2.64、2.73（未处理 1.42）。

## 结论
作者认为显式几何先验可把强固定阵列算法改造成阵列不变 SE，并在真实数据上优于既有 array-agnostic 方法，为跨设备部署提供新路径。

## 点评
把“坐标→动态核”接到已有强骨干上，比纯 TAC/注意力式无几何方法更充分利用阵列结构，且置换等变性设计干净。局限是仍需设备提供坐标；训练主要在 RealMAN 子阵列抽取，极端不规则几何与仿真–真实差异下的表现需更多验证。
