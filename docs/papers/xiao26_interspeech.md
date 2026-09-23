# Continual Adaptation for Pacific Indigenous Speech Recognition

- 论文编号：2215
- 报告人：Ting Dang
- 程序：Tuesday 29 September 2026 / Pacific Voices: Speech Science and Technology for the Languages of the Pacific Ocean
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xiao26_interspeech.pdf

## 问题
太平洋原住民语言低资源且与预训练分布远；全量微调可能灾难性遗忘。多数低资源 ASR 只报最终 WER，不问适应是否引发大规模表征漂移与顺序学习中的稳定–塑性困境。

## 方法
新整理 PARADISEC 语料：Bislama（13.75h）、Nafsan（14.83h）、Lelepa（3.55h），共约 32h。以 Whisper-Small 做：(1) 不同数据量下 Full FT vs LoRA（encoder+decoder）跨语适应；(2) 层间余弦距离测适应前后表征漂移；(3) 顺序学习 Nafsan→Lelepa，并比较 DoRA、O-LoRA；另测仅编码器/仅解码器 LoRA 对目标准确与英语遗忘的权衡。扩展词表字符并用预训练词嵌入均值初始化。

## 实验与结果
Bislama 随数据增加明显改善（Full FT 10h WER 19.64）；Nafsan 低数据不稳定，约 5h 才明显提升；Lelepa 极低资源下 2h 时 LoRA WER 75.66 优于 Full FT 84.10。漂移：Bislama/Nafsan 偏后层，Lelepa 早期编码器即大漂移。适应 Lelepa 后英语 WER：基线 15.68 → LoRA 18.89 → Full FT 26.24。仅解码器保英语更好但目标差；仅编码器目标好但英语遗忘更重。顺序学习：Full FT 保 Nafsan 更好但学不好 Lelepa；LoRA/DoRA/O-LoRA 对新任务更好却严重遗忘前语（Nafsan WER 飙至 84+）。

## 结论
对语言距离大的太平洋语言，适应常伴随深层表征改写与遗忘；现有参数高效法无法同时解决顺序适应中的塑性–稳定矛盾。亟需面向低资源、结构远语言的稳健适应策略。

## 点评
把“能不能认出”升级为“适应改写了什么、忘了什么”，对太平洋场景很有政策与工程含义。语料规模与语言数仍有限，英语遗忘用 LibriSpeech 等代理，未必等同多语能力全面退化；结论偏警示性，未给出可部署解法。
