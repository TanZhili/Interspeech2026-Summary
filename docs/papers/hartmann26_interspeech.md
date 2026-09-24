# Towards a Stochastic DNN Approximation of Cochlear Implant Auditory Models

- 论文编号：1872
- 报告人：Theresa Hartmann
- 程序：Wednesday 30 September 2026 / Assistive Technologies 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/hartmann26_interspeech.pdf

## 问题
CI 听神经模型可仿真电刺激诱发响应，但计算重；现有 DNN 近似多为确定性、忽略放电随机性，可能削弱时间编码与不同刺激模式比较的可信度。

## 方法
用层次 VQ-VAE-2（约 2.37M 参数）将 Greenwood 谱图映射到每时频 bin 的 Gamma 分布参数（形状 k、尺度 θ），采样近似平均发放率神经图。训练数据含语音/噪声/音乐共 9000 段（每段 10 个随机神经图）；参考模型为 SpecRes 16 电极 + 40 CF×50 纤维。损失为 Gamma NLL + 指数 MSE + VQ commitment。用 JSD 与 NSIM 评分布与结构相似度。

## 实验与结果
DNN 能再现神经图整体时频谱结构与关键随机特性，低频与中频更好；示例显示近似神经图略更噪。客观 JSD/NSIM 表明全局结构与随机性捕获有效，相对全听觉模型更省时，适合大规模仿真。

## 结论
随机 DNN 近似是高效逼近电刺激听神经模型的可行一步，尤其利于保留变异性而非仅平均响应。

## 点评
用可微 Gamma 替代泊松采样，把“随机性”真正写进近似目标，比纯均值回归更贴合 CI 生理。VQ 层次结构利于粗细尺度；高/极高频与噪声细节仍可能是短板，且评测以客观相似度为主、未接下游听感/算法优化闭环。
