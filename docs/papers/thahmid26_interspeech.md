# Layer-wise Probing of Whisper's Encoder Representations for Bengali Phone-like Units

- 论文编号：2199
- 报告人：Munim Thahmid
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/thahmid26_interspeech.pdf

## 问题
多语语音编码器哪一层对音位信息最线性可分，在孟加拉语与监督 ASR（Whisper）上研究不足；说话人混叠评测也偏松。

## 方法
OpenSLR53 子集 2000 句；MMS 强制对齐 uroman 转写，按规则合并为 phone-like 标签；冻结 Whisper-small/medium/large-v3 编码器，帧中心三分之一池化，说话人独立线性探测（可选 MLP）。对照组：wav2vec2-XLSR、英语 MFA+LibriSpeech；另做置信过滤、ABX、时长分层、送气/卷舌对比等。

## 实验与结果
峰值 Macro-F1：small L8/12=0.837，medium L15/24=0.858，large-v3 L26/32=0.860；相对深度约 0.63–0.81。large-v3 末层仅降约 2 pp，XLSR 末层降约 14 pp。送气塞音/塞擦音早期即可分，鼻音/咝音推动中层增益。英语 MFA 锚点亦在中后层。

## 结论
孟加拉语 phone-like 可分性在 Whisper 中后层最强；监督 ASR 预训练比 SSL 更能把音位细节保留到更深编码器层。边界是 uroman/MMS 标签非规范音位库。

## 点评
严格说话人独立 + 缩放曲线，把“中层音位峰”推广到南亚语与 Whisper。强处是鲁棒控制齐全；脆弱处是对齐噪声与罗马化坍缩音位对立，解释需限在送气/卷舌等稳定对比。
