# To glide or not to glide: Acoustic realization of the diphthong-hiatus contrast in Italian and Romanian

- 论文编号：2433
- 报告人：Johanna Cronenberg
- 程序：Wednesday 30 September 2026 / Diphthongs and Monophthongs
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/cronenberg26_interspeech.pdf

## 问题
/ia/ 可实现为单音节双元音 /ja/ 或异音节 hiatus /i.a/。意大利语倾向双元音、罗马尼亚语倾向 hiatus，但词汇重音与词内位置如何促进或阻断滑音化，大规模语料上的声学证据不足。

## 方法
意语约 168h、罗语约 300h 广播/电视语料，强制对齐后提取 /i,j/+ /a,ə/ 序列（最终约意 23,681、罗 17,895 token），标注重音与词首/词中。时长按发音速率归一化后 log 变换；F1/F2 转 Bark、去均值、时间归一并用 FPCA，对 PC1/PC3 得分做 LMER（语言×重音×位置）。

## 实验与结果
意大利语重音 vs 非重音时长差清晰（词首约 0.37、词中约 0.56 log 单位）；罗马尼亚各条件重叠大，但非重音序列整体长于意大利语。共振峰：意语重读时更陡、更外周；罗语仅非重音词中 /ia/ 明显更平、更像滑音。两语有大量重叠，对立呈梯度。

## 结论
重音与词位以语言特异方式调节 /ia/ 实现：意语重音可阻断滑音化，罗语更倾向在非重音词中位置滑音化；为后续感知分类研究提供生产基线。

## 点评
用大规模自然语料 + FPCA 把“范畴标签”还原为时长与轨迹形状的连续空间，比小样本实验室词表更能暴露梯度。无说话人 ID、靠 segment 随机效应是局限；感知实验需把重音/位置纳入刺激设计，否则可能低估范畴稳定性。
