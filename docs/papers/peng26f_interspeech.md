# Cross-Lingual Speaker Verification with Self-Supervised Pre-Trained Models

- 论文编号：1799
- 报告人：Jinghan Peng
- 程序：Thursday 1 October 2026 / TidyVoice2026 Challenge: Cross-Lingual Speaker Verification
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/peng26f_interspeech.pdf

## 问题
说话人确认在语言失配时性能下降：身份线索与语言相关声学特性纠缠。相对在有限、偏语种数据上从头训 SV，利用大规模多语 SSL 预训练模型学到的泛化声学/语音表示，有望得到更语言无关的说话人嵌入；但如何聚合多层、如何稳定训练仍需系统验证。

## 方法
主系统：w2v-BERT 2.0 前端，每层经两层 MLP Adapter 投到 256 维，再做 Multi-scale Feature Aggregation（比较 Mean、层/通道加权、通道/时间拼接、Hierarchical Cross-Attention 等六种），Attentive Statistics Pooling 后投影为 256 维嵌入，AAM-Softmax 训练。三阶段训练：Stage1 冻骨干训下游（全数据、2s、margin 0→0.2）；Stage2 解冻全模型微调；Stage3 仅在 TidyVoiceX Train 上做大间隔微调（6s、margin 0.5）。辅系统：轻量 ReDimNet-B5/B6，SphereFace2-C，两阶段预训练+LM-FT。训练数据含 TidyVoiceX Train、VoxCeleb2、VoxBlink2、CN-Celeb、WenetSpeech 清洗子集、3D-Speaker，及 RIR/MUSAN 等在线增广。开发集做选模与 QMF 校准，分数级平均融合。

## 实验与结果
指标 EER / minDCF（P_target=0.01）。主系统 w2v-BERT 2.0：Dev 1.03%、eval-A 3.34%、eval-U 4.59%；+QMF 后 eval-A/U 为 2.73%/2.84%。ReDimNet-B6+QMF：2.52%/3.43%。融合+QMF：eval-A 2.21%、eval-U 2.99%。PTM 对比（仅 TidyVoiceX Train 微调）：w2v-BERT 2.0 Dev EER 2.09% 优于 Whisper Large-v3、XLS-R、MMS 等。聚合消融：Channel Concatenation EER 最低（2.09%），HCAF minDCF 最好；最终提交选 CC。训练阶段消融：冻前端 1.54% → 全微调 1.14% → +LM-FT 1.03%。

## 结论
作者认为用 w2v-BERT 2.0 作前端加多层聚合与三阶段适配，可构建更可泛化、偏语言无关的 SV；同数据下 PTM 系统在未见语种 eval-U 上强于轻量 ReDimNet；最终融合在 TidyVoice2026 达 2.21%/2.99% EER。

## 点评
路线偏“强 SSL 前端 + 工程化训练课表”，贡献更在系统对比（PTM 选型、聚合策略、三阶段）而非新解耦机制。Channel Concatenation 无额外参数却 EER 最好，说明有时简单融合够用。脆弱点在于 580M+ 骨干算力与大规模多源数据门槛；未见语种仍明显高于开发集，语言纠缠问题主要靠预训练覆盖而非显式对抗压制。
