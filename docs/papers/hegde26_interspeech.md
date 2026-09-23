# Aligning Audio Captions with Human Preferences

- 论文编号：2052
- 报告人：Kartik Hegde
- 程序：Monday 28 September 2026 / Evaluation of Speech and Audio Analysis
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/hegde26_interspeech.pdf

## 问题
音频描述通常依赖成对 audio–caption 监督与 BLEU、CIDEr 等自动指标，但这些指标与人类判断相关性弱，且标注成本高。已有基于 CLAP 奖励与大语言模型的对齐方案算力开销大，不适合低资源部署；绝对评分的人工评测一致性也较差。

## 方法
提出基于 RLHF 的偏好对齐音频描述框架，无需额外成对标注即可微调基线描述模型。奖励模型用 LAION CLAP（htsat-unfused）提取 512 维音频/文本嵌入，拼接为 1024 维后经两层网络（512→128）与 sigmoid 输出 [0,1] 偏好分；按 Bradley–Terry 用成对偏好训练，并加 L2 正则。策略优化采用 SCST / REINFORCE：对采样描述 \(w_s\) 与贪心基线 \(w_g\) 用自定义奖励差分更新，且奖励不依赖 ground-truth 描述。为抑制过长等 reward hacking，引入长度惩罚 reward shaping（期望长度 \(L_e=13\)）。基线为约 15M 参数的 CNN10 PANN 编码器 + Transformer 解码器。

## 实验与结果
偏好数据来自 FENSE 的 AudioCapsEval / ClothoEval（一致标注约 1473 / 1555 对）及约 4424 条专有偏好与 880 条困难样本。在 AudioCaps 与专有集的非困难/困难划分上做人机偏好对比：困难集上 RLHF 相对基线人类胜率更高（AudioCaps Challenging 53.93% vs 46.07%；专有 Challenging 59.11% vs 40.89%）。自定义奖励与人类偏好的加权偏差最低（4.19），优于 S-BERT、FENSE、CLAPAT。扩充偏好数据可提升奖励模型与 RLHF 人类胜率；与 SFT 相比可达到相近表现且无需成对描述标注。

## 结论
作者认为该框架能在无 ground-truth 描述的情况下提升与人类偏好的对齐，在基线失败/不自然时收益更大，并与监督训练性能可比；进一步扩大偏好数据与改进 RL 有望继续提升。

## 点评
核心是把音频描述从“对齐 n-gram/CLAP 相似度”转到“对齐成对人类偏好”，并用轻量 CLAP 头 + SCST 避开大模型开销，适合嵌入式字幕系统。长度惩罚针对可见的 hacking 模式，设计务实。脆弱点在于奖励模型域覆盖：公开 AudioCaps 非困难集上人类胜率未必高于基线，且偏好数据量与困难样本定义会直接影响对齐效果。
