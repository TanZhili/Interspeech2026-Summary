# Listening or Reading? Evaluating Speech Awareness in Chain-of-Thought Speech-to-Text Translation

- 论文编号：800
- 报告人：Federico Costa
- 程序：Wednesday 30 September 2026 / Translation
- 技术分类键：translation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/romerodiaz26_interspeech.pdf

## 问题
CoT/多轮 S2TT 假设翻译阶段同时可见语音与转写，从而抗 ASR 误差传播并利用韵律；该假设是否成立缺少系统验证。

## 方法
基于 SALAMANDRATA-7B + 冻结 mHuBERT 离散单元；对比 CoT 与 self-cascade。训练变体：BASE（纯 CoT）、DUAL（25% CoT + 75% Direct）、NOISY（25% CoT 样本注入损坏转写且不对转写算损失）。用 Value Zeroing 做模态归因；控制替换转写片段测鲁棒性；CONTRAPROST 测韵律敏感；FLEURS 测通用翻译质量。英→六种欧洲语言。

## 实验与结果
BASE 的语音贡献近零，行为接近 cascade；DUAL/NOISY 语音归因升至约 1.54×/2.24×。转写噪声下 BASE 的 CoT 与 cascade 掉速几乎相同；NOISY 在高至 30% 损坏下下降明显更缓。CONTRAPROST Global：NOISY-COT 最高（AVG 17.65）。FLEURS 上干预不伤质量，DUAL 整体最好，NOISY-COT 可反超 cascade。

## 结论
默认 CoT  largely 在“读转写”而非“听语音”；混合 Direct 与注入噪声转写可提高语音依赖、抗错与韵律利用。未来可组合 DUAL+NOISY。

## 点评
用归因、噪声鲁棒、韵律三维拆穿 CoT 叙事，比只报 BLEU/xCOMET 更有解释力。NOISY 仍主要依赖转写却能纠错，说明“语音作纠错信号”而非替代文本。局限：仅英→欧语、DSU 表示可能已损韵律细节；CONTRAPROST 绝对分仍低，语音整合仍有很大空间。
