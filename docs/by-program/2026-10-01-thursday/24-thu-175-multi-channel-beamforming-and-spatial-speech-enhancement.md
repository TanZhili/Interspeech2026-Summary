# Multi-Channel, Beamforming and Spatial Speech Enhancement

- 日期：2026年10月1日（星期四）
- 时间：14:00-16:00
- 形式：Oral
- Area：6
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场多通道/波束形成口头报告面向阵列几何可变、无线传感网分布式滤波、虚拟麦空间上采样、近距源歧义、自适应白噪增益 MVDR，以及方向信息压缩传输。核心问题是：固定阵列假设与边缘物理尺寸限制，如何在有限麦数、带宽与算力下保住空间滤波增益。

几何与分布侧，Geo-DConv 把麦坐标显式注入动态卷积使固定阵列模型阵列不变；ANDFilter 用端到端神经滤波替代 DANSE 迭代协方差优化。空间上采样与轻量双通道则通过虚拟麦条件下游增强，或以空间不变单通道教师动态仲裁蒸馏，降低对脆弱空间线索的过度依赖。经典 MVDR 经可微层联合学掩码与频变 WNG 阈值；NDC 仅压缩空间信息即可在接收端配置方向模式重建。

## 技术内容

### 阵列不变、分布式滤波与空间上采样

**Towards Array-Invariant Speech Enhancement via Geometry-Aware Dynamic Convolution**（论文 548；Zhenglong Liu）  
Geo-DConv 用麦克风坐标将标准固定阵列 SE 转为阵列不变系统。RealMAN 真实多通道数据上，两款常用固定阵列模型可适应多样拓扑并一致提升。

**An All-neural Distributed Filtering Algorithm for Speech Extraction in Wireless Acoustic Sensor Networks**（论文 648；Jiawei Wang）  
ANDFilter：单节点滤波、节点选择自适应加权、多节点分布式空间滤波三阶段端到端合成，替代 DANSE 迭代优化。LibriSpeech+Freesound 仿真 WASN 上 PESQ/ESTOI/DNSMOS 在各 SNR 优于 SOTA 基线。

**Spatial-Magnifier: Spatial upsampling for multichannel speech enhancement**（论文 1477；Dongheon Lee）  
由有限真实麦生成虚拟麦信号，SARL 用估计 VM 信号/特征条件下游增强。相对既有空间上采样基线，在端到端多通道增强与神经波束形成上更优，接近全麦可用时的 oracle。

### 近距歧义、自适应 MVDR 与方向编码

**A Dynamic Knowledge Distillation Framework for Mitigating Spatial Ambiguity in Lightweight Dual-Channel Speech Enhancement**（论文 1524；Yifei Yang）  
D-SKD 引入空间不变单通道教师动态仲裁蒸馏，使双通道学生自适应调节空间依赖而无需显式角度监督。近距源上一致提升且别处质量不损，推理零额外开销。

**Joint Learning of Covariance Estimation and White Noise Gain for Robust MVDR Beamforming**（论文 2212；yongyi deng）  
DNN 联合预测时频噪声掩码与频变 WNG 阈值，经可微鲁棒 MVDR 层端到端优化，相对固定 WNG MVDR 提升语音质量与可懂度。

**Neural Directional Coding: Joint Spatial Coding and Filtering with Configurable Directivity Patterns**（论文 2234；Weilong Huang）  
NDC 联合空间编码与滤波，仅压缩空间信息；接收端由压缩空间信息与单通道参考重建可配置指向性虚拟麦。4 麦 16 kHz、1.4M 参数下空间信息可压至 0.25 kbps，匹配或超过 7.5 kbps、90.8M 参数基线。

## 本场要点

- 显式几何动态卷积使固定阵列 SE 跨拓扑泛化。
- 全神经分布式滤波与虚拟麦上采样分别服务 WASN 与边缘物理尺寸限制。
- 动态空间感知蒸馏缓解轻量双通道近距源歧义。
- 可学习 WNG 的 MVDR 与超低码率神经方向编码兼顾鲁棒性与传输带宽。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 548 | Towards Array-Invariant Speech Enhancement via Geometry-Aware Dynamic Convolution |
| 648 | An All-neural Distributed Filtering Algorithm for Speech Extraction in Wireless Acoustic Sensor Networks |
| 1477 | Spatial-Magnifier: Spatial upsampling for multichannel speech enhancement |
| 1524 | A Dynamic Knowledge Distillation Framework for Mitigating Spatial Ambiguity in Lightweight Dual-Channel Speech Enhancement |
| 2212 | Joint Learning of Covariance Estimation and White Noise Gain for Robust MVDR Beamforming |
| 2234 | Neural Directional Coding: Joint Spatial Coding and Filtering with Configurable Directivity Patterns |
