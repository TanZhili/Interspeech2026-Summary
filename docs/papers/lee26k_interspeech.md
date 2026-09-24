# Spatial-Magnifier: Spatial upsampling for multichannel speech enhancement

- 论文编号：1477
- 报告人：Dongheon Lee
- 程序：Thursday 1 October 2026 / Multi-Channel, Beamforming and Spatial Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26k_interspeech.pdf

## 问题
边缘设备麦数受物理限制，多通道增强的空间自由度不足；已有 Neural-VME 多把增强网络挪用来估虚拟麦，且缺少把 VM 信号/特征系统接入下游 SE 与波束形成的通用框架。

## 方法
提出 Spatial-Magnifier（GAN，DBPN 风格）：频域把麦通道当卷积通道，交替 up/down block，加入 Selection Module（点卷积门控）与 Dynamic Channel Allocation（动态卷积通道注意力压缩）。并提出 SARL：SARL-S 将估计 VM 波形与真实麦拼接后送 MC-SE；SARL-F 将 VM 潜特征与编码器特征相加再分离–解码。可服务 VM-BF（MCWF/MVDR）与端到端 VM-SE；训练联合 Neural-VME、波束形成与对抗损失。

## 实验与结果
DNS 语料 + 六麦仿真（圆阵+高低麦），含 omni-SE 与 FoV-SE。2ch RM/4ch VM 上 SARL-S 的 VM-BF SI-SDR/PESQ/STOI 达 7.10/2.40/82.1，接近 6ch 物理阵 8.35/2.41/84.6；相对 MC Conv-TasNet 等基线更优且算力更低。换 MVDR、MC-RNN、智能眼镜 ATF/HRTF、2→8 VM 等设定仍有效；VM-SE 使 SpatialNet-small 质量超过更大的 2ch SpatialNet-large。

## 结论
作者认为专用空间上采样网络加 SARL 条件化，可在少物理麦下接近全阵 oracle，并跨波束形成与端到端增强通用。

## 点评
把“估虚拟麦”从复用 SE 骨干改为面向通道维超分，并用信号/特征双路径条件化下游，工程完整。VM 位置绑定训练阵列几何，任意点生成仍难；复杂 2RM/4–8VM 相对全物理阵仍有差距。
