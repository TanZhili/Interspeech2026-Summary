# Online Audiovisual Speaker Separation Using Efficient Visual Knowledge Distillation

- 论文编号：1999
- 报告人：Cheng Yu
- 程序：Tuesday 29 September 2026 / Source Separation 1
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/yu26e_interspeech.pdf

## 问题
因果音视频说话人分离（AVSS）相对离线掉点明显：缺少未来上下文，且常用非因果、参数沉重的视觉前端难接入在线系统。需要在严格因果下压缩视觉前端并保住说话人判别力。

## 方法
对预训练 DeepAVSR 用非对称时间 padding 做因果推断；接入 online AV-CrossNet（可选 Mamba narrow-band），按说话人通道对齐音视频特征。再提出 Visual Knowledge Distillation（VKD）：学生保留教师结构但残差通道缩小 16 倍；训练前期教师/学生嵌入加权和（初值约 99%/1%），权重线性过渡，到第 K=50 epoch 完全切到学生，再与分离器联合训至收敛。数据为 LRS2/LRS3/VoxCeleb2 的 2mix，损失为 SI-SDR + 谱幅度。

## 实验与结果
在线系统中，oAV-CrossNet-Mamba-VKD 在 LRS2/LRS3 上 PESQ/SI-SDRi/SDRi 优于既有在线基线（相对最强基线约 +0.3 PESQ、+0.8 dB SI-SDRi 量级）；VoxCeleb2 上 PESQ 优于 Swift-Net-12，SI-SDRi 具竞争力。相对全尺寸因果 DeepAVSR，VKD 将视觉前端压到约 0.23 MB / 1.7 G/s MACs（约 48× 参数、7.5× 算力压缩），LRS2 上甚至 SI-SDRi 14.7 vs 教师 14.1。从零训学生或直接蒸馏后微调均不收敛；相对 Dolphin 的非因果压缩前端，VKD 压缩率更高且在因果设定下提升更大。

## 结论
VKD 用任务导向的渐进蒸馏得到轻量全因果视觉前端，配合强在线分离器达到在线 AVSS 的 SOTA，并显著缩小与非因果系统的差距。

## 点评
贡献在“因果化大视觉前端 + 渐进切学生”的工程配方：单独证明从零训/硬蒸馏不够，动态权重才稳住 AVSS。表格把因果掉点量化得很清楚。脆弱处是依赖教师质量与固定切换日程；VoxCeleb2 上压缩版相对全尺寸教师仍有 SI-SDRi 回退，说明压缩收益与最难数据上的上限仍需权衡。
