# Cross-Modal Robustness Transfer (CMRT): Training Robust Speech Translation Models Using Adversarial Text

- 论文编号：2278
- 报告人：Gerasimos Spanakis
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/issam26_interspeech.pdf

## 问题
E2E-ST 多在干净语料上训练，对非母语/方言中常见的屈折形态变异脆弱；文本侧可用 MORPHEUS 对抗微调，但合成对抗语音昂贵，且 TTS 攻击需滤掉同音异形。

## 方法
CMRT 两阶段：先用词级强制对齐上的 WACO 对比学习 + 语音/文本 mixup + 对称 KL，拉齐语音与文本语义空间（CMRT-TR）；再冻结语音编码器，把对抗文本嵌入注入对齐后的语音流形做对抗 mixup 微调（CMRT-FN）。Speech-MORPHEUS：对转写做同 POS 屈折扰动，经 TTS 合成，并排除同音候选。骨干为 HuBERT/mHuBERT + Transformer，数据 CoVoST 2（En-De/Ca/Ar、Fr-En）。

## 实验与结果
相对 HuBERT-Transformer，CMRT-FN 在对抗测试上平均约 +3.4 BLEU，且优于未做对抗微调的 CMRT-TR；相对在 50k 对抗语音上微调的 TTS-Morpheus-FN，干净集掉点更小（约 0.6 vs 3.6 BLEU）。干净 TTS 回放分数不低于原测试，说明掉分来自屈折攻击而非 TTS 音质。

## 结论
在强跨模态对齐前提下，仅用对抗文本即可把屈折鲁棒性迁到语音模态，接近真对抗语音微调且更好保住干净性能。

## 点评
核心洞见是“对齐好了就能在嵌入空间换文本扰动”，避开造对抗语音。同音过滤对法语等尤其关键。脆弱处依赖强制对齐质量与 TTS 评测链，攻击覆盖的是形态屈折而非更广声学噪声。
