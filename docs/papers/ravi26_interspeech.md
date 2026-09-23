# Rank-Distance Based Confidence Estimation for ASR

- 论文编号：1355
- 报告人：Nagarathna Ravi
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ravi26_interspeech.pdf

## 问题
ASR 解码器最大类概率常过自信，无法反映正确性；二值目标的辅助置信度模型（CEM）把部分正确词也标成 0；基于强制对齐的连续目标易受时间戳误差影响；真类概率型连续目标在大词表下又塌缩成近似二值，校准变差。

## 方法
提出 RanD 连续目标：对预测–参考词做编辑对齐，再对 token 对齐；用参考 token 在后验中的归一化秩分数 \(s_{rank}\) 与后验相对 one-hot 的归一化欧氏距离 \(s_{dis}\) 加权（\(\alpha=0.5\)），词级取 token 平均。再按架构从 ASR 抽取词级嵌入训 CEM（shrinkage loss）：CTC 用编码器/解码器隐藏与后验平均；RNN-T/TDT 用预测网络状态与后验；AED 用注意力上下文、解码状态与嵌入。CEM 结构因架构而异（全连接 / BiLSTM / 小 FFN）。

## 实验与结果
在 NeMo 预训练模型上评估：Hindi Conformer-CTC（KB 训练 CEM，PB 作域外）、Conformer RNN-T、Parakeet-TDT、Canary-Flash AED（LibriSpeech 训 CEM，NPTEL/Svarah 域外）。对比 MCP、熵、二值 CEM（M/T/S-CEM 等）及 TeLeS、TruCLeS。RanD 在多数 MAE/KLD/JSD/NCE/ECE/AUROC/AUPRC 上优于或持平 SOTA；例如 CTC 在 KB 上 MAE 0.0570、AUROC 0.8669；RNN-T/TDT/AED 在 LibriSpeech 与域外集上也整体更优，并显示对错配域有更好泛化。

## 结论
用秩与分布距离构造连续置信目标，可避免二值粗糙、对齐不准与真类概率塌缩等问题，在四种 ASR 架构及域内/域外数据上优于文中对比的 SOTA CEM。未来拟覆盖删除错误与低资源场景。

## 点评
RanD 用排序位置代替易塌缩的真类概率，同时用分布距离刻画不确定度，对大词表过自信问题针对性强。方法依赖编辑对齐与架构特定特征抽取，实现成本随 ASR 类型变化；域外结果整体更好，但部分指标并非全面最优，实用时仍需按指标与任务权衡。
