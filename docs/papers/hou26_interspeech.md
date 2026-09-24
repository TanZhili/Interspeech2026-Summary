# UGPCB: Uncertainty-Gated Phonetic Contextual Biasing for Improving Hotword Recognition in Large Speech Models

- 论文编号：1577
- 报告人：Yong-Jie Hou
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/hou26_interspeech.pdf

## 问题
热词语境偏置在 BPE 切分下脆弱；拼音/语音匹配可提召回，但易过偏置与同音误触发。需免训练、可栅控的解码期方案。

## 方法
UGPCB：参数无关 logit bridge 取声学后验熵作不确定性门控，仅在高熵步注入偏置；字素 BPE trie 与拼音（带调/不带调）双轨匹配，并用字素–拼音对比惩罚抑制纯拼音假阳性；配合 N-best 重打分。在 Dolphin 基座、SeACo 测集评估，并测至 1000 干扰项。

## 实验与结果
完整系统：召回 84.19%、F1 90.81%（基线 F1 80.85%）、CER 5.60%；相对文本浅融合召回 +4.68 pp。熵门控降误报；1000 干扰下仍有约 +14.26% 召回增益。精度下降约 0.78 pp 量级、与部分对比差异不显著。

## 结论
不确定性门控 + 双模态拼音匹配可在免训练解码中提升热词召回并抑制过偏置/同音幻觉，适合大模型热词应用。

## 点评
面向普通话同音与 BPE 截断的设计很具体，免训练部署友好。依赖拼音工具规范读音、未枚举多音字；门控阈值与惩罚强度需场景调参，过严会牺牲召回（消融 B3 已体现）。
