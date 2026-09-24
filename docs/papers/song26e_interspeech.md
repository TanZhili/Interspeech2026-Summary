# Speaker-Filtered Heterogeneous Graph Network: Toward Privacy-Preserving Multimodal Emotion Recognition

- 论文编号：2282
- 报告人：heying song
- 程序：Wednesday 30 September 2026 / Speaker Identity, States, and Traits in Paralinguistics
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/song26e_interspeech.pdf

## 问题
多模态对话情感识别（MDER）常用全局图聚合，易混入非目标说话人表征（隐私风险），并可能泄漏未来信息；跨模态噪声也导致负迁移。

## 方法
提出 SF-HGN：CAGI 在因果窗内用分模态 Top-K 注意力抽取跨说话人线索并注入目标话轮（含冲突/情感动态特征）；随后仅在单说话人异质子图（SS-HG）上做内外模态关系传播，从结构上隔离其他说话人节点。特征：RoBERTa 文本、DenseNet 视觉、openSMILE IS10 声学。

## 实验与结果
IEMOCAP：WA 68.76%、WF1 68.73%，总体优于所列基线。MELD：WA 66.40%、WF1 65.65%，在 Fear/Disgust/Anger/Surprise 等少数类上更强。消融去掉残差、事件注入或说话人过滤均掉点。参数约 1.19M，推理约 51.3 ms，低于 DialogueGCN/DialogueRNN。

## 结论
先因果注入上下文、再单说话人图传播，可在保护说话人级隐私边界的同时保持竞争力，并降低计算开销。

## 点评
“隐私”主要靠图拓扑隔离而非差分隐私等形式化保证，但对部署场景仍有工程意义。Angry 在 IEMOCAP 上偏弱、MELD 中性类偏大，说明隔离策略在低唤醒冲突与类别不平衡下仍需加强。
