# Similarity as Evidence: An Explainable Siamese Framework for Snore Sound Classification

- 论文编号：2153
- 报告人：Mengkai Sun
- 程序：Tuesday 29 September 2026 / Audio Coding and Signal Analysis
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/meng26f_interspeech.pdf

## 问题
鼾声音频可反映上气道阻塞部位（VOTE：Velum/Oropharyngeal/Tongue base/Epiglottis），但临床数据小、类别极不平衡、噪声与设备变异大；softmax 黑盒分类既难解释“为何判为某类”，也对扰动敏感。需要把相似度本身变成可检验的决策证据，并做忠实性/稳定性验证。

## 方法
对 4 s、16 kHz 窗计算 80-bin log-Mel（20–2400 Hz）并做 CMVN；轻量 3 块 Conv-BN-ReLU-MaxPool CNN 得到 D=256 的 ℓ₂ 归一化嵌入。联合 semi-hard triplet 与 effective-number 加权 class-balanced CE（λ=1），P×M 批采样（4×8）。推理主规则为非参数 Class Centroid（欧氏距离最近类原型），另报告 softmax 头作对照。解释：每类固定靠近质心的 support 样本，用末层卷积通道平均激活上采样为时频证据图，并与 query–support 相似度对照；另做 deletion 与扰动稳定性检验。数据为 MPSSC 官方四类划分（Train/Val/Test 共 282/283/263，T 类极少）。

## 实验与结果
摘要与已读实验设置：干净条件 macro-recall 由 wav2vec2 基线 0.401 提升至 0.638，中等加性噪声下仍具竞争力；deletion/扰动分析支持解释区域对置信度贡献与结构稳定性。全文在 baselines/推理头细节处截断，完整表与噪声档位数字未全部保留。

## 结论
作者认为在小样本、长尾鼾声分类上，度量学习嵌入 + 质心推理可提升少数类召回，并用 support 级时频证据把“像谁”变成可审计解释，而非仅后验可视化。

## 点评
把 Siamese 相似度从“更好的表征”推进到“可定量检验的证据”，对临床可解释性诉求是对症的；质心规则与 support 可视化一致，比纯 CAM 更易沟通。T 类样本极少、域偏移与设备噪声仍可能使嵌入几何塌缩；正文结果表截断，噪声鲁棒与各推理头差距需对照 PDF。
