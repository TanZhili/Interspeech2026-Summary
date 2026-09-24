# Acoustic token admixture for joint speaker and content anonymization

- 论文编号：1949
- 报告人：Ali Golmakani
- 程序：Thursday 1 October 2026 / Speaker Privacy and Anonymization
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/golmakani26_interspeech.pdf

## 问题
受监管场景需同时压制生物特征身份与文本风格/命名实体等语言再识别通道；既有方法常分治两通道且全句重合成，毁掉可作域内训练数据的原声学特质。

## 方法
统一声学 token 空间：Stream A 为 Whisper 编码 + 8 级 RVQ；Stream B 为转写→IPA/发音特征→T5 自回归预测同空间 token。按 β 逐帧随机混入两流；余弦相似度门控（τ=0.6）拒收对齐失败的音素 token。NER 敏感跨度强制用 Stream B 并局部编辑替换。BigVGAN 条件于融合 token、变换 F0（α=0.75+噪声）与 ECAPA 伪说话人嵌入。

## 实验与结果
VPC 2024：β=0.7 时 EER 42.54%、WER 3.73%、UAR 40.11%，EER 距榜首 T12-5（43.23%）约 1 点。β 升则 EER 升、WER 缓增。编辑子集：仅混入 Anon.Sim 0.123；全系统 Edit Sim 0.959、MOS 3.84、WER 11.9%。

## 结论
帧级 token 混入 + NER 跨度替换可在不改全句重合成的前提下联合匿名说话人与内容，隐私接近挑战顶尖且可懂性尚可；UAR 与情绪韵律保留仍是主要短板。

## 点评
把内容隐私嵌进同一合成栈，并保留周围帧，贴合“可复用域内录音”需求。情绪效用偏低、依赖 Whisper/NER 召回；门控与 β 的部署调参决定隐私–可懂折中。
