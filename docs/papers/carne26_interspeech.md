# Function words: a topic independent approach to word n-gram selection for forensic speaker comparison

- 论文编号：3166
- 报告人：Michael Carne
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/carne26_interspeech.pdf

## 问题
基于词 n-gram 的似然比法医说话人比对常用“最高频 k 项”隐式选特征，可能混入话题相关内容词，从而高估证据强度。

## 方法
对 AusEng 500+ 中 104 名澳大利亚男性各两段电话闲聊前两分钟净语音做逐字转写。特征级两层 multinomial–Dirichlet LR；基线用全词表频次选 k；提出先固定 156 个功能词显式特征集，再比较频次、MI、ANOVA F-ratio、χ²、方差阈值五种筛选。5 折划分测试/参考/校准，以 C_llr 等评估。

## 实验与结果
基线 k=450 时 C_llr=0.60，但约 35%（157/450）为话题内容词。全功能词控制 C_llr=0.83；ANOVA F-ratio 选 k=50 最佳，C_llr=0.78（C_min=0.66），维度大幅下降。Tippett 显示 DS 强证据比例与幅度有所提升。

## 结论
作者建议用显式功能词集规避话题偏置；虽弱于含内容词的基线，但对话题失配更稳健，且 F-ratio 可进一步改善。未来需检验说话风格失配与社会语言学混杂因素。

## 点评
把“话题泄漏”写成可核验的比例与词例，对法医证据解读很有价值。性能换稳健性的取舍明确；语料为同任务闲聊，风格失配场景尚未实证。
