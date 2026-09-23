# ImKWS: Test-Time Adaptation for Keyword Spotting with Class Imbalance

- 论文编号：258
- 报告人：Ting Dang
- 程序：Monday 28 September 2026 / Audio segmentation
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/ding26_interspeech.pdf

## 问题
关键词检测（KWS）在真实噪声与域偏移下性能下降，传统微调或域适应需要源域或标注目标数据，而测试时适应（TTA）虽只需无标注测试流，但现有方法（如 AdaKWS 的熵最小化）在“关键词极少、背景极多”的严重类别不平衡下，更新会被背景类主导，模型对背景过度自信、难检出稀有关键词。

## 方法
ImKWS 在预训练轻量 KWS 模型（BC-ResNet-3）上，仅用无标注测试流、只更新 BN 仿射参数做单遍 TTA。核心有三块：(1) **解耦熵最小化（DEM）**：将条件熵拆成 reward 分支（温度 τ 控制分布锐度）与 penalty 分支（缩放因子 α<1 削弱把非目标 logit 压向 −∞ 的梯度），减轻多数类过自信；(2) **多视角一致性**：对时间/频率 mask 增广视图用对称交叉熵约束预测一致，抑制不平衡流带来的梯度抖动；(3) **两阶段样本选择**（沿用并改造 AdaKWS）：DEM 损失与伪关键词一致性（PKC）双阈值筛选样本，再按 DEM 与 PKC 加权组合总损失。输入为 40 维 MFCC。

## 实验与结果
数据：Google Speech Commands v2 构造 4 类任务（yes/up/stop + 合并非关键词），测试端将关键词:非关键词比调到 1:4–1:8，并混入 ESC-50 与 MS-SNSD 噪声、多 SNR。对比 TBN、Tent、SAR、ETA、AdaKWS。在 1:8、宏/微 F1 下，ImKWS 全面最优；相对 AdaKWS，ESC-50 上 macro F1 在 −10/0/10 dB 提升约 +1.23/+1.43/+1.62%，MS-SNSD 上约 +2.96/+2.19/+1.50%。不平衡越严重（至 1:8）优势越大；消融显示去掉 DEM、一致性或样本选择均掉点。

## 结论
作者认为 DEM + 多视角一致性能在严重不平衡与低 SNR 下稳定做 KWS 的 TTA，尤其在 1:8 与 −10 dB 时优于标准熵最小化基线；未来拟扩展到内存受限的端侧学习。

## 点评
抓住的是流式 KWS 里“背景淹没关键词”导致 EM 塌缩这一具体机制，而不是泛泛的域偏移。把惩罚强度从 1 调到 α<1 是可解释的正则：主动限制多数类 one-hot 化，再靠一致性稳住梯度——和“只筛样本再做标准 EM”的 AdaKWS 路线形成互补。脆弱点在于依赖 BN 仿射更新与手工阈值/超参（τ、α、λ、选择阈值），且实验主要在 Speech Commands 人为重采样不平衡上，对真实连续长流、非固定关键词集的泛化仍待验证。
