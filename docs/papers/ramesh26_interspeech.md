# Duration-Aware Soft Targets for Text-Independent Supervised Phone Segmentation

- 论文编号：2568
- 报告人：Raghavan Ramesh
- 程序：Thursday 1 October 2026 / Speech signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ramesh26_interspeech.pdf

## 问题
文本无关监督音素切分惯用单帧硬边界，无法刻画渐变过渡的不确定性；既有工作多改特征或结构损失，较少改进监督目标本身。

## 方法
在硬边界两侧放置时长感知的半高斯软标签：左右 σ 与邻段时长成比例（spread ratio K=0.2），仅替换边界附近零值。基线为 39 维 MFCC + 双层 BiGRU + 加权 BCE；推理用 prominence 峰检测。强调正确实现 R-value（已访问真值边界不重复匹配）。

## 实验与结果
TIMIT：Soft R-val 91.53% vs Hard 89.50%，优于 SEGFEAT、SuperSeg（Non-AR）；Buckeye 86.23 vs 84.47。跨集与德/泰卢固/印地语上 Soft 多提升精度与 R-val。80% TIMIT 测试句伪峰减少，每句约少 40%。均匀/三角/高斯核表现接近，增益主要来自平滑。同源不同滤过渡相对 Hard +3.4%。

## 结论
更好设计的软监督可在不改架构下提升音素切分；未来可自适应 K 并扩展到发音数据。

## 点评
把问题焦点移到“目标质量”，改动轻、可复现。R-value 实现纠错对公平对比有贡献；多语对齐来自 Kaldi，标签噪声会与软标签效应纠缠。
