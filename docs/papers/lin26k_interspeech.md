# BG-CRNN: Boundary-Guided Dynamic Attention for Sound Event Detection in Complex Scenarios

- 论文编号：2019
- 报告人：Zongmu Lin
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/lin26k_interspeech.pdf

## 问题

复杂噪声环境下 Sound Event Detection（SED）性能会随 SNR 下降而急剧恶化。现有系统虽可用半监督、预训练特征或外部分离模块缓解噪声，但自注意力仍易把目标事件特征与相邻背景噪声混在一起，时间定位不够稳。

## 方法

提出 BG-CRNN：前端用 CNN 与冻结预训练 ATST-Frame 提取并拼接特征，后接 Dynamic Boundary Transformer（DBT）与 Boundary-Guided Attention（BGA），再经 RNN 做帧级预测，半监督训练。

DBT 含双分支共六层 Dynamic Boundary Attention Block：边界分支由强标签差分得到边界标签，用加权边界损失预测边界概率；另一分支将预测边界二值化（阈值 τ=0.7），按类别循环分配到多头，用累积和生成 Segment ID，构造仅允许同段内注意力的动态 mask，注入 scaled dot-product attention。BGA 用边界特征经门控网络得到时域权重，以可学习标量 α（初值 0）残差增强 CNN 特征中的活跃事件区。总损失为监督 SED（BCE）+ Mean Teacher 一致性损失 + 加权边界损失。

## 实验与结果

在 DESED 与 WildDESED（16 kHz）上评估，指标为 PSDS1/PSDS2。在干净 DESED 上训练时，各 SNR 下 BG-CRNN 均优于复现的 ATST-CRNN；在噪声 WildDESED 上训练并 fine-tune 后，-5 dB 时 PSDS1 达 0.191、PSDS2 0.417，优于 EADSED 与 LLM-based 方法。DESED 消融中，完整流水线 PSDS1/PSDS2 为 0.566/0.791，高于基线 0.502/0.750。

## 结论

作者认为边界引导的段内注意力与 BGA 能抑制噪声干扰、提升低 SNR 下的检测与定位，具有实际部署潜力。边界帧稀疏需加权损失；单独加 BGA 可能过度聚焦边界，需与动态 mask 联用才最优。

## 点评

做法抓住的是“噪声与目标事件在时序上耦合、自注意力跨段泄漏”这一类问题：用显式边界把注意力硬限制在事件段内，再软增强活跃区，比单纯数据增强或外部分离更贴近 SED 的定位目标。强依赖边界预测质量与阈值设定；在极低 SNR 下边界本身难估，动态 mask 可能切错，这是设计上的脆弱点。
