# Temporal Transition-Aware Multi-Head Modeling for Partially Spoofed Audio Detection and Localization

- 论文编号：474
- 报告人：Yunsu Kim
- 程序：Tuesday 29 September 2026 / Spoofing, Deepfake Detection and Watermarking
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/kim26e_interspeech.pdf

## 问题
局部伪造（Partial Spoof）只替换句中短片段即可改语义；既有方法多做帧级真伪或边界二分类，未显式建模邻帧如何演化，多段伪造或平滑拼接时边界线索弱。

## 方法
过渡感知多头框架：SSL 前端抽 20 ms 帧特征 → multi-scale GRU（扩张卷积路径捕获约 ±60 ms 局部 + 长程流）→ 三头——frame head（帧真伪）、transition head（相邻帧 Real→Fake / Fake→Real / None）、refinement head（融合帧分与过渡概率得时序一致输出）。总损失为帧损失 + λ_tran 过渡损失 + λ_ref 精炼损失，边界帧加权。

## 实验与结果
数据：PartialSpoof（Train 2580/22800 bona/fake 等官方划分）与 PartialEdit-E1/E2（说话人不相交，bona 来自 VCTK）。摘要称在三套数据、20 ms 分辨率上达 SOTA。全文在实验设定处截断（「resolution of 2…」），具体指标表未能读到。

## 结论
作者认为方向性帧间过渡是比单纯帧标签更可靠的定位线索；精炼头负责时序连贯。定量细节需回查 PDF。

## 点评
把 PSAL 从点分类推进到「邻帧状态机」监督，与多段 PartialEdit 场景匹配。强在多头分工清楚；脆弱点在过渡标签噪声与 λ 敏感，以及 20 ms 分辨率对极短音素级篡改的下限。抽取截断已注明。
