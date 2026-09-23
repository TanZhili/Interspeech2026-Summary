# Improving Generalization in Speech Deepfake Detection via Orthogonality-Constrained Common-Specific Feature Decorrelation

- 论文编号：1483
- 报告人：Donghee Kim
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kim26l_interspeech.pdf

## 问题
端到端 deepfake 检测（RawNet2/AASIST 等）在域内 EER 极低，但 ERM 训练易过拟合数据集伪迹，跨未见攻击、噪声与编解码时性能骤降。需要把“真伪共性线索”与“攻击/域特异线索”拆开，避免分类器依赖捷径。

## 方法
在 SSL-AASIST（wav2vec2.0 + AASIST）上，将谱/时图表示投影为 common 与 specific 两支：common 做 bonafide/spoof 主任务，specific 做 bonafide/TTS/VC 辅助分类；用余弦相似度平方作正交损失压低两支相关。总损失 L_main+L_aux+L_ortho。训练用 ASVspoof 2019 LA；评测含 19LA、21LA、21DF、ASV5、ITW；可叠加 RawBoost（LnL+ISD）。

## 实验与结果
RawBoost 下，Proposed（三损失）相对 baseline：21DF 6.64%→3.67%，ASV5 16.25%→14.39%，ITW 11.22%→8.84%；19LA/21LA 接近或略差。无增强时跨库平均 EER 约 12.83%→10.60%。消融显示仅加 aux 不够，ortho 对 OOD 关键。t-SNE 上 common/specific 聚类分离。

## 结论
作者认为正交约束的共性–特异性解耦可促使模型依赖更一致的真伪线索，从而提升未见域与攻击上的稳健性，且改动相对轻量。

## 点评
把域泛化里的 common/specific 正交直接接到 AASIST 图特征上，动机清楚：把静音时长等语料捷径赶到 specific 支。19LA 上偶有小幅回退说明解耦有代价；辅助标签粒度仍粗（仅 TTS/VC），更细攻击类型是否进一步帮助仍开放。
