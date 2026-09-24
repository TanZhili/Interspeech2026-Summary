# The Effect of Neck Skin Vibration on the Periauricular Acoustic Receiver

- 论文编号：170
- 报告人：Ruoyan Li
- 程序：Tuesday 29 September 2026 / Speech Production and Perception 1
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/li26b_interspeech.pdf

## 问题
自语时除口腔辐射外，颈部皮肤振动会再辐射空气声，可能污染耳周麦克风；许多自语仿真只建模口鼻辐射，忽略该路径。

## 方法
三路证据：(1) KEMAR 口模拟器扫频，耳周/额/口前麦克风同步；(2) 真人朗读，耳周麦克风 + 颈振传感；(3) 头几何 BEM（GPU 加速，球模验证）仿真。对比有无颈振耦合下耳周拾音差异。

## 实验与结果
摘要与结论导向：靠近颈部的耳周接收器测到与颈皮振动相关的显著空气声分量；假头–BEM 与真人–仿真对照支持该耦合。含义是自语声学模型需把颈振辐射纳入，而非仅口腔源。

## 结论
耳周器件设计与自他语音分离应考虑颈振空气声路径。

## 点评
把可穿戴耳周场景下的「被忽略声源」钉死，对助听器/耳机自语处理有工程意义。强在假头、真人、BEM 三角互证；脆弱点在被试少（正文写 S1–S2）与稳态朗读材料，动态语速/音高变化下耦合强度待扩展。
