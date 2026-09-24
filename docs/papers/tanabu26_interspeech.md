# SSL-GMMVC: Interpretable Voice Conversion via Locally Linear GMM Transforms in Self-Supervised Representation Space

- 论文编号：1688
- 报告人：Tomoya Tanabu
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/tanabu26_interspeech.pdf

## 问题
LinearVC 等在 SSL 空间做全局线性映射简单有效，但无法适配不同音素簇的局部结构；深度 VC 又难解释。需要在可分析前提下提升表达力。

## 方法
SSL-GMMVC：WavLM-Large 第 6 层特征经双向最近邻对齐成源–目标对，对联合向量拟合 \(K\) 分量 GMM；转换时用源侧后验加权各分量仿射映射 \(\hat y=\sum_k p(k|x)\{\mu_k^y+\Sigma_k^{yx}(\Sigma_k^{xx})^{-1}(x-\mu_k^x)\}\)。\(K=1\) 退化为 LinearVC。协方差分 Full 与 Cross-Diag；HiFi-GAN 合成。

## 实验与结果
CMU ARCTIC 六说话人。数据充足时 Full+\(K>1\) 说话人 EER/主观相似度可超过 LinearVC NC，并常优于 FreeVC；可懂度与 UTMOS 总体可比。Cross-Diag 随 \(K\) 增大也可超过 FreeVC 相似度（参数更省）。分量选择与响音/阻音纯度相关；单分量变换矩阵呈收缩旋转，跨性别角度更大。

## 结论
SSL 空间局部线性 GMM 变换在保持可解释性下提升说话人相似度，并揭示分量与语音学结构、变换几何的联系。

## 点评
“简单可分析 VC”路线上把全局线性换成混合局部仿射，分析扎实。高维 SSL 下 \(K\) 难做大、跨分量旋转平面难对齐，扩展性仍受估计稳定性限制。
