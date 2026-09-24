# Phy-VC: Physics-Informed Voice Conversion for Privacy-Preserving Pathological Speech

- 论文编号：378
- 报告人：Suhita Ghosh
- 程序：Wednesday 30 September 2026 / Clinical and Inclusive Speech Technology
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/ghosh26_interspeech.pdf

## 问题
病理/老年语音匿名化需去身份又保留诊断线索；纯数据驱动谱包络估计对口吃重复、不稳发声等 OOD 模式脆弱，黑盒声码器常抹平临床属性。

## 方法
Phy-VC 在 DDSP-QbE 上加入物理声道瓶颈：预测可微 articulatory 参数→面积函数→Webster 代理求共振峰/带宽→Lorentzian 滤波；目标池韵律映射减轻源说话人泄漏；可用 α6（喉高/有效声道长）可控改说话人大小。标准语音训练，评测口吃、痴呆、老年、情感等。

## 实验与结果
相对 Emo-StarGAN、KNN-VC、DDSP-QbE，正文报告在多数据集上可懂度、韵律与自然度更优并保持有效匿名；SLP 专家评估确认临床相关属性显著保留。

## 结论
把 articulatory–acoustic 耦合作为归纳偏置，可提升病理语音匿名 VC 的稳健性与可解释可控性。

## 点评
物理约束对准“非典型发声 OOD”很有说服力，且给出临床专家验证路径。实现与损失项较多，依赖 Praat 等伪标签监督；匿名–效用权衡的攻击面细节需结合全文表格细读。
