# Lightweight Detection and Model Attribution of Synthetic Speech via Residual Statistical Fingerprints

- 论文编号：1361
- 报告人：Matías Pizarro
- 程序：Tuesday 29 September 2026 / Spoofing, Deepfake Detection and Watermarking
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/pizarro26_interspeech.pdf

## 问题
合成语音检测多为二分类，缺少生成系统归因；现有归因多封闭世界多分类，新模型出现需重训。法医场景需要轻量、免训练、可开放世界的来源识别。

## 方法
Residual Statistical Fingerprints（RSF）：对信号与滤波版本之差取平均残差作为模型指纹（类比图像 GAN 指纹）。测试残差相对各类指纹分布算 Mahalanobis 距离，统一覆盖开放世界单模型归因、封闭世界多模型归因、真假分类与 OOD。滤波在 STFT 上做（优选低通 1 kHz、带通 5–6 kHz）；细粒度 STFT（8 ms / 0.125 ms hop）略优于标准设置。

## 实验与结果
ASVspoof LA 上单模型归因：A16/A19 留出评测，Mahalanobis 明显优于相关（如低通 1 kHz 平均 AUROC 0.98 vs 相关 0.91）。摘要称跨多种合成系统与语言、在四类任务上表现突出，并对噪声等失真稳健。全文在 STFT 分辨率分析处截断，后续主表未能完整读取。

## 结论
可读部分支持：残差统计指纹 + Mahalanobis 可做免训练归因与检测；协方差建模优于简单相关。

## 点评
把图像域指纹思路迁到语音残差空间，部署成本低、适合开放世界单模型查询。强在统一距离框架；脆弱点在滤波/STFT 超参与合成器进化后指纹漂移。截断后半已标明。
