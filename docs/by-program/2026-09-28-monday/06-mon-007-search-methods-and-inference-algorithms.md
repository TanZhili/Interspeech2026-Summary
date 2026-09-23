# Search Methods and Inference Algorithms

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Oral（Area 9）
- 论文数：6
- 材料：官方程序中该场全部论文摘要。摘要写明问题、方法与主要结论；未在摘要中出现的数字与细节不写入。

## 技术趋势

本场聚焦解码与搜索算法本身：如何在保持或提升识别质量的同时降低延迟与计算。多条线汇合于“用约束或草稿加速，而不是只堆更大模型”——阿拉伯语变音符恢复用 CTC + 字符级 diacritization lattice 硬约束做非自回归语音到文本变音；Whisper-CD 用多负例对比解码（噪声、静音、时移）抑制长音频幻觉且免训练。

投机/半自回归解码成为效率主力：SASD 在联合 CTC-attention 上对高置信 CTC token 直接采用、对难 token 用 attention 精炼；自投机方案以 CTC 编码器为草稿、LLM 一次前向校验并在失败时回退 AR。NAR-MBR 则从 NAR 输出分布采样并以期望效用最大化替代单纯最大概率，且单次前向即可多样本。

另有工作给出语音处理中自回归解码的广义形式化与纳入标准，澄清“何为 AR 搜索”以便做以搜索策略为中心的消融。整体瓶颈是长音频错误累积、NAR 不确定性与 AR 速度之间的张力；方向是约束解码、对比负例、投机草稿与风险最小化解码。

## 技术内容

### 约束 CTC 与免训练对比解码

**Constrained CTC decoding for Efficient Diacritic Restoration**（论文 3220；Rufael Marew）
针对阿拉伯语语音转写多数无变音符、难以建模细粒度音系对立，提出基于 CTC 的高效非自回归语音到文本变音方法：由无变音转写构建字符级 diacritization lattice，解码时硬约束假设落在合法变音实现上。在 ArVoice 与 ClArTTS（古典阿拉伯语与 MSA）上相对更复杂的多模态基线显著降低变音错误率，兼具性能与效率。

**Whisper-CD: Accurate Long-Form Speech Recognition using Multi-Negative Contrastive Decoding**（论文 3058；Hoseong Ahn）
针对 Whisper 类长音频幻觉、循环与漏识，且上下文传递会放大错误，提出免训练 Whisper-CD：对比干净音频 logits 与三类声学扰动负例（高斯噪声、静音、时间平移），经 log-sum-exp 聚合为多负例目标逐 token 解码。五英语长音频基准上 CORAAL WER 最高降 24.3 pp，token 吞吐比 beam search 快 48%，可即插即用。

### 投机、半自回归与 NAR-MBR

**Accelerating End-to-End ASR via Semi-Autoregressive Speculative Decoding**（论文 1953；Long Wu）
提出 SASD：在联合 CTC-attention 框架用 CTC 贪心初始化，对高置信 token 走 NAR、对低置信“更难”token 用 attention 解码器精炼。在 AISHELL-1、WenetSpeech 与工业数据上 CER 可比先进 attention-rescoring，速度提升 2.8×–3.5×。

**Self-Speculative Decoding for LLM-based ASR with CTC Encoder Drafts**（论文 2680；Avihu Dekel）
以 CTC 编码器为草稿加速语音感知 LLM 的 AR 推理：低熵帧直接接受 CTC 贪心假设；否则一次 LLM 前向按 token 似然宽松校验；失败则从已接受 CTC 前缀恢复 AR。九语料五语言实验可同时加速并降 WER；HuggingFace Open ASR 基准上 1B LLM + 440M CTC 达 5.58% WER，相对 AR 搜索 inverse RTF 提升 4.4×、相对 WER 仅增 12%。

**Non-Autoregressive Minimum Bayes' Risk Decoding for Fast Speech Recognition**（论文 2971；Hiroyuki Deguchi）
提出 NAR-MBR：最大化由 NAR 模型输出概率采样得到的期望效用，而非最大化输出概率；利用 NAR 并行性可单次前向高效多样本。在 LibriSpeech、Switchboard、AMI 与网络演讲语料上优于先前 NAR 解码，并快于 AR 解码。

### 理论形式化

**A Generalized Formalism of Auto-Regressive Decoding for Speech Processing**（论文 2768；Julia Gachot）
指出语音序列预测中 AR 策略定义隐式且多重，导致选型、比较与“是否 AR”判定不一致。工作给出 AR 搜索纳入标准与广义理论框架以归类神经模型搜索策略，并展示该形式化可简化以解码过程为中心的基准与搜索策略消融设计。

## 本场要点

- 硬约束 lattice + CTC 可在阿拉伯语变音恢复上同时提升精度与效率。
- 长音频 Whisper 幻觉可用多负例对比解码在推理期抑制，无需重训。
- 半自回归/自投机把 CTC 草稿与 attention/LLM 校验结合，是当前加速主路径。
- NAR-MBR 用期望效用替代最大概率，缓解 NAR 因缺乏左上下文的不确定性。
- 速度—精度权衡可在 2.8×–4.4× 加速区间内仍接近或优于强 AR/重打分基线（以各摘要为准）。
- 统一 AR 解码形式化有助于把搜索策略本身变成可消融对象。

## 覆盖核对

- 3220 | Constrained CTC decoding for Efficient Diacritic Restoration
- 3058 | Whisper-CD: Accurate Long-Form Speech Recognition using Multi-Negative Contrastive Decoding
- 1953 | Accelerating End-to-End ASR via Semi-Autoregressive Speculative Decoding
- 2680 | Self-Speculative Decoding for LLM-based ASR with CTC Encoder Drafts
- 2971 | Non-Autoregressive Minimum Bayes' Risk Decoding for Fast Speech Recognition
- 2768 | A Generalized Formalism of Auto-Regressive Decoding for Speech Processing
