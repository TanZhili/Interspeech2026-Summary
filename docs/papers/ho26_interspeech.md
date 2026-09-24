# An Investigation on Combining Geometry and Consistency Constraints into Phase Estimation for Speech Enhancement

- 论文编号：621
- 报告人：Chun-Wei Ho
- 程序：Thursday 1 October 2026 / Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ho26_interspeech.pdf

## 问题
加性噪声 SE 中几何相位估计可把问题化成相位差符号二分类，但符号难估且错分代价大；直接相位回归与 DNN 符号预测也常不稳定。

## 方法
提出 multi-source Griffin-Lim（MSGLA）：在语音与噪声谱之间交替做 GLA 式一致性投影，并强制加性几何。NM-MSGLA 用估计语音/噪声幅度，经几次迭代隐式落到 ±|ΔP| 候选；NP-MSGLA 首次用正弦定理，由语音幅度与噪声相位得到两候选并迭代消歧。骨干 TF-GridNet（约 1.3 M）。

## 实验与结果
Oracle 实验显示噪声幅度/相位对重建很关键。VB-DMD：NP-MSGLA PESQ 3.46、SI-SNR 19.61、CBAK 3.18，匹敌或略优于直接相位估计与符号预测。WSJ0-CHiME3 上两变体与 GLA/基线接近，背景抑制（CBAK）更稳。

## 结论
几何约束与多源一致性结合可无监督消解符号歧义；NP 路径表明噪声相位在低能区可作为互补线索。

## 点评
用一致性迭代替代脆弱的符号分类器，动机扎实。Oracle 与盲测落差说明幅度/噪声估计仍是瓶颈；相对直接回归增益多为边际，价值更在可控几何框架与 CBAK。
