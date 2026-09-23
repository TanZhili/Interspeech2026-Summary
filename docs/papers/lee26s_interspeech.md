# Comparing Self-Supervised and Domain-Invariant Features for Cross-Domain Voice Phishing Detection

- 论文编号：1975
- 报告人：Jeongmin Lee
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/lee26s_interspeech.pdf

## 问题

语音钓鱼（vishing）检测面临真实犯罪录音因隐私难获、即使有也极少、且需轻量声学端侧方案。作者比较：用场景化演员录音训练、在真实犯罪通话上测试时，域不变韵律特征与冻结 SSL（HuBERT、wav2vec2.0）谁更能跨域泛化，以及零样本/少样本下的部署权衡。

## 方法

韩语音料：场景 VP（406）、真实犯罪 VP（测试 406 + 独立 holdout 50）、场景金融咨询与真实电话咨询作非 VP；统一 8 kHz、说话人独立。eGeMAPS 88 维经 RF 重要性 + Cohen’s d<0.5 选出 4 个域稳定特征（logRelF0-H1-A3、mfcc1V、mfcc4、F2bandwidth）。SSL 用 LibriSpeech 预训练 Base 模型末层均值池化 768 维、权重冻结。分类器统一 Logistic Regression；k∈{0,1,5} 真实 VP 样本并入场景训练集。报告 F1、Recall、Precision。

## 实验与结果

零样本：精选 4 特征 F1=69.5%，全 88 特征仅 3.8%；HuBERT 58.3%、wav2vec2.0 36.2%。5-shot：HuBERT 94.2%（Recall 99.3%）、wav2vec2.0 90.2%（Precision 99.4%）、4 特征仅升至 71.0%，全 88 特征升至 85.2%。消融显示 mfcc1V 是主要检测驱动，4 特征在少样本下更利于抑制误报。部署建议：冷启动用轻量 4 特征；有少量真实样本与算力时用 SSL，并按召回/精确需求在 HuBERT 与 wav2vec2.0 间选择。

## 结论

跨域 vishing 检测存在由目标域样本量决定的体制：域不变韵律适合零样本冷启动，SSL 在 5-shot 后显著更强但精度—召回形态不同。Cohen’s d 过滤是冷启动前提；该体制是否跨语种成立仍待验证。

## 点评

贡献是把“演练数据→真实犯罪”写成可复现的零/少样本协议，并显式对比轻量特征与冻结 SSL 的部署剖面，而不是再堆一个检测网络。特征选择需用真实 VP 做离线统计这一点要诚实看待：严格意义上的“零真实数据”仍部分依赖目标域分布信息。脆弱点包括仅韩语、非 VP 类与 VP 场景未必对称，以及线性分类器可能低估微调 SSL 上限。
