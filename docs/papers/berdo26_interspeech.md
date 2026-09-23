# Post-Training Speech Enhancement Language Models with Perceptual Rewards

- 论文编号：3405
- 报告人：Antonis Asonitis
- 程序：Tuesday 29 September 2026 / Language-Model and Codec-Token Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/berdo26_interspeech.pdf

## 问题
自回归 SE 语言模型用离散音频 token 的交叉熵训练，却以 DNSMOS、WER、UTMOS 等感知指标评测，存在 train–eval 鸿沟；单指标优化易 reward hacking。NLP 的 pretrain–SFT–RL 流水线在 AR SE LM 上尚未补齐后训练阶段。

## 方法
对 UniSE 与 GenSE 的公开 SFT 权重施加 Group Sequence Policy Optimization（GSPO）：每输入采样 G=4 条完整序列，用复合奖励 R=DNSMOS+(1−WER)+UTMOS（等权）算组内相对优势，做序列级重要性比裁剪与 KL 约束，无需 critic。训练约 20k 条 5 s DNS 风格配对数据，3000 步。人类偏好消融对比 SFT 基线与单指标/复合 GSPO。

## 实验与结果
DNS2020：两基座各项 DNSMOS 均升；GenSE+GSPO 混响/无混响 OVRL 3.53/3.55，UniSE+GSPO 真实录音 OVRL 3.37，均超 MaskSR、AnyEnhance、LLaSE-G1 等。DNS5 pDNSMOS：GenSE+GSPO Track1/2 的 pOVRL 达 4.45/4.36（相对基座 +1.04/+1.40）；UniSE+GSPO Track1 最佳 4.63。21 人成对偏好：复合奖励 Elo 1571 最高；仅 DNSMOS Elo 1335 低于基线 1476，显示单指标 hacking。

## 结论
GSPO 多指标后训练可直接优化不可微感知目标，补齐 SE LM 的 RL 阶段，并在榜单与听感上优于单指标变体。后训练可作为架构与数据之外的第三条提升轴。

## 点评
把 SE LM 明确接到 LLM 式后训练范式，并用真人消融钉死“复合奖励 vs hacking”，证据扎实。强在无需替代网络与离线偏好对；弱在奖励仍是代理指标组合、采样 G 增加训练成本，且增益幅度依赖基座起点（GenSE 在 DNS5 上提升空间更大）。
