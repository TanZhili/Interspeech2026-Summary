# Variation and change in dynamicity of Australian English diphthongs in Sydney

- 论文编号：3206
- 报告人：Benjamin Purser
- 程序：Wednesday 30 September 2026 / Diphthongs and Monophthongs
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/purser26_interspeech.pdf

## 问题
澳大利亚英语双元音是音变热点，但既有研究多静用点测或把 F1/F2 分开建模，难以同时抓住两共振峰随时间的协同动态。

## 方法
ANU Corpus of Sydney Speech 中 119 人自发口语，约 57,269 token（FACE、FLEECE、NEAR、GOAT、MOUTH、PRICE）。10%–90% 九点提取 F1/F2，修正 Lobanov 归一后对各元音做 multivariate FPCA（MFPCA）；对 PC1/PC2 得分拟合混合效应模型，预测项含年龄组、性别、社会阶层、音系语境、时长、语速、词频及年龄×性别交互。

## 实验与结果
前两 PC 解释各元音约 75%–85% 方差。社会模式与既有音变方向一致：青年与女性更靠前（如 FACE 更高更前、GOAT 更高更后、MOUTH/PRICE 更开等）。MOUTH、PRICE 还见中产相对工人阶层的差异。语言语境（尤其鼻音前、词末）系统塑造动态性；部分 PC 主要反映语言而非社会条件。

## 结论
联合建模 F1×F2 轨迹可更整体地刻画双元音动态与社会/语言驱动；社会分层方向与静态研究一致，但揭示了高度与前后维度如何共变。

## 点评
相对分通道 GAMM/DCT，MFPCA 把“形状”压成可回归的分数，适合同时看多类双元音。未展开族裔、且过滤较严；大样本下需靠效应量门槛避免琐碎显著，文中已有意识地只报实质影响。
