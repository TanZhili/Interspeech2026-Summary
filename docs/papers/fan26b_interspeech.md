# Robust Multi-Tier Infant-Centered Audio Understanding with Whisper via Structured Speaker Conditioning

- 论文编号：2746
- 报告人：Mark Hasegawa-Johnson
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：https://www.isca-archive.org/interspeech_2026/fan26b_interspeech.pdf

## 问题
婴儿中心日长家庭录音标签少、信噪比低、跨家庭域移大；需帧级多说话人层（儿童/女看护/男看护/兄弟姐妹）同时做发声分类，并处理重叠。

## 方法
LoRA 微调 Whisper-large-v2 编码器 + MLP（每 5 帧）下采样 + 两层目标说话人 Transformer + 每层分类器。说话人 token = 共享层 token + 家庭特异偏移。序列级时间平滑损失（λ=0.2）。家庭划分无重叠；输入 30s 片段。

## 实验与结果
跨层平均 Macro-F1 74.88、κ 68.14，优于 TL-TR（69.55/64.04）与多层级评测下的 W2V-LB（67.27/59.27）。去掉 LoRA、家庭偏移或平滑损失均下降。成人层（FAN/MAN）相对 W2V-LB 增益更大；儿童层差距较小，作者归因于 Whisper 成人预训练偏置 vs W2V-LB 家庭预训练。

## 结论
结构化说话人条件 + 参数高效 Whisper 适配，能高效完成婴儿中心多层级帧级音频标注，并更好处理重叠与跨家庭变异。

## 点评
把“家庭特异”与“角色层”拆开编码，直接对症跨家庭域移；多标签层设计贴合真实重叠。Whisper 对婴儿近麦发声仍偏域外，说明预训练分布与架构需一并考虑。
