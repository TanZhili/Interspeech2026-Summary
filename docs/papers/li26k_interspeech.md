# POTSA: A Cross-Lingual Speech Alignment Framework for Speech-to-Text Translation

- 论文编号：695
- 报告人：Xuanchen Li
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/li26k_interspeech.pdf

## 问题
SpeechLLM 的 S2TT 在高资源语对强、低资源弱。Whisper 等编码表示常按语言成簇而非按语义，翻译映射难跨语言复用；现有对齐多走 speech→text，易压扁声学细节，且各源语言独立，忽视跨语言共享表示。

## 方法
提出 POTSA：冻结语音编码器与 LLM，只训 Q-Former。(1) Bias Compensation：按语言估计全局偏置并减去，粗对齐。(2) 用语义相同的跨语言并行语音对，在选中的 Q-Former 层上对 token 序列做 Sinkhorn OT 损失，与翻译 CE 联合。(3) 基于 UCB 的在线 reward-guided 层调度，把 OT 集中在更有效的（偏底层）层。并行对采用随机语对双向对齐，而非英语锚点。

## 实验与结果
CoVoST2 先 ASR 再 En→Zh，再在 FLEURS 上五语→中文混合微调（每语约 10h）。相对 WhisperV3+Qwen2.5 基线，五语平均 BLEU +1.29（31.84 vs 30.55），零样本六语平均 +2.93（20.84 vs 17.91）。消融：去 Bias/OT 均降；英语可训锚点最差。OT 优于 MSE/余弦；调度仅在较低层优于全层对齐。R@1 与 1−JSD 显示跨语言一致性提升。

## 结论
少量并行语音 + OT 对齐即可增强跨语言表示一致性，缩小高低资源与零样本差距；机制可接入更大 SpeechLLM。

## 点评
把问题从“再堆数据”转到“源语言表示是否可比”，用粗偏置消除 + 细 OT 软匹配，比强制点对点更贴合未对齐的语音 token。层调度避免高层 CE 与对齐目标打架是实用细节。脆弱处是依赖并行语音对质量、OT 权重与层选择超参，以及英文锚点失败暗示对齐图结构敏感。
