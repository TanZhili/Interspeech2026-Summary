# Time-Unconditional Generative Speech Enhancement via Autonomous Rectified Flow

- 论文编号：1679
- 报告人：Wen Zhang
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26z_interspeech.pdf

## 问题
多数生成式增强仍用显式时间步嵌入调节向量场。线性边界锚定路径下目标速度场本应与时间无关；强制时间条件易过拟合轨迹，低 NFE 或数值偏离时恢复变差。

## 方法
Autonomous Rectified Flow（ARF）：直线路径 \(x_t=(1-t)x_0+t(y+\sigma z)\)，目标速度 \(u=y+\sigma z-x_0\) 等价于噪声本身，与 \(t\) 无关。网络 \(v_\theta(x_t,y)\) 不接收时间嵌入，直接回归 \(u\)；推理从噪声先验 \(\phi_1=y+\sigma z\) 沿自治 ODE 用 Euler 回积到干净端。基于 NCSN++，冻结时间步与噪声调度模块；\(\sigma=0.5\)。

## 实验与结果
VoiceBank+DEMAND：NFE=5 时 PESQ 3.11、eSTOI 0.88；NFE=1 时 PESQ 3.00、SI-SDR 19.91，优于同步数 FlowSE/BBED。统一 27.8M 消融中去掉时间嵌入后 NFE=1 RTF 降至 0.02（FlowSE 0.05）。跨域 DNS 上与 FlowSE 总体相当，强混响下两者均明显下降。

## 结论
作者认为线性路径增强中显式时间条件冗余；自治整流流可提升低 NFE 质量与推理效率，并保持与传统流相当的泛化。

## 点评
抓住边界锚定线性流中“目标速度恒定”这一数学结构，把去时间嵌入从工程省参提升为原则选择，对单步/少步生成特别有利。脆弱点在混响等非加性退化上仍弱；与 MeanFlowSE 等单步流的对比显示优势主要来自去掉时间调制而非更大模型。
