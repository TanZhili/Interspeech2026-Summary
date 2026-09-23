# Multilingual Phonological Feature Recognition with Self-Supervised Speech Models

- 论文编号：2735
- 报告人：Abner Hernandez
- 程序：Wednesday 30 September 2026 / Phonetic Aspects of TTS and ASR Systems
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hernandez26b_interspeech.pdf

## 问题
多数系统先识别音素再映射音韵特征，未显式建模音韵结构；单语或辅助目标设定下，结构化音韵预测相对强音素基线在多语/跨域/未见语上的优势尚缺系统比较。

## 方法
PhonoQ-2.0：冻结 XLSR-ft（wav2vec 2.0 音素微调版）+ 共享投影与 2 层 Conformer，四头预测 22 维特征（manner 9、元音高低/前后 6、place 5、voicing 2）；manner 条件门控只在相容类别上激活元音/部位头。基线 CTC-Phoneme 同骨干，预测后用统一 phone→feature 表映射到同一 22 维空间。训练语：英、德、西、捷（各约 52–56 h）；MFA 对齐；段级 macro-F1 评估。

## 实验与结果
域内（CP 等）平均 macro-F1：PhonoQ-2.0 91.3% vs CTC 映射 82.5%（+8.8），英语增益最大（+11.6）。OOD（FLEURS / VoxPopuli）仍优约 +9.3 / +7.8。相对旧版 PhonoQ，在共享 12 维上德国/西语大幅提升。零样本法/意/俄：平均 73.6% vs 66.9%（+6.7），意大利语最高 +10.8。逐特征分析显示 manner/元音/部位/浊音普遍提升，非单靠某一难类。

## 结论
直接结构化音韵特征预测优于“音素优先再映射”，跨域与未见语更稳；可用于发音评估、语言学习与低资源场景。局限：22 维未覆盖法语鼻化元音、俄语腭化、意大利语长辅音等，需扩展特征清单与更远类型学迁移。

## 点评
同骨干、同特征空间的公平对照很关键，说明低 PER 并不自动等于好音韵特征。Manner 门控把语言学约束写进解码，比独立多标签更干净。未见语仍掉到七十出头，说明 articulatory grounding 有帮助但非万能；特征库存缺口会直接限制临床/跨语用途。
