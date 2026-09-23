# Streaming Speech Synthesis

- 日期：2026年9月30日（周三）
- 时间：14:00-16:00
- 形式：Poster
- Area：7
- 论文数：9
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。仅依据摘要表述，不补写未给出的实验细节。

## 技术趋势

本场围绕流式/低时延语音生成：神经网络编解码器与单码本语音语言模型、流式零样本音色转换、以及面向增量文本的 LLM-TTS。共性目标是在有限前瞻条件下保持韵律自然、说话人一致与可懂度。

编解码与表征侧，HybridCodec 融合双流解耦与 SSL 蒸馏；WavSLM 把 WavLM 量化蒸馏为单码本自回归流。流式 VC 则批评 ASV 说话人嵌入对帧级生成不友好，并改进分块扩散与音色编码器鲁棒性。

流式 TTS 侧，FlashTTS、CTC-TTS、S5-TTS 与韵律边界感知后训练分别从多 token 预测/均值流蒸馏、CTC 对齐与交错策略、有限前瞻掩码、以及边界早停+滑动窗上下文等角度压低首包时延并抑制长文崩溃。另有一篇舞蹈到音乐扩散生成，扩展到多舞者与非人类舞者场景。

整体趋势是：把语义—声学解耦、原生双流输入输出与对齐/边界控制组合起来，服务实时对话系统。

## 技术内容

### 编解码器与单流语音语言模型

**HybridCodec: Fast Dual-Stream, Semantically Enhanced Neural Audio Codec**（论文 3393；Arjun Gangwar）  
针对向编解码器注入语义信息的两条路线（蒸馏到首层 RVQ vs. 语义/声学分流通），HybridCodec 同时保留双分支并在语义流蒸馏 SSL，推理时无需 SSL。摘要称域内测试集上 RVQ-1 语义特化更优、全 RVQ 重建有竞争力，并在域外与零样本跨语设置稳健，相对既有双流模型约 3× 加速。

**WavSLM: Single-Stream Speech Language Modeling via WavLM Distillation**（论文 2803；Luca Della Libera）  
将 WavLM 表征量化蒸馏为单一码本，并以自回归 next-chunk 目标训练，无需文本监督或文本预训练即可在单 token 流中联合建模语义与声学。摘要称在一致性基准与语音生成上有竞争力，参数与数据更少，并支持流式推理。

### 流式音色转换与说话人表征

**VOSSA: Voiceprint Optimization for Streaming Speech Architectures**（论文 2763；Mu-Ruei Tseng）  
指出 ASV 预训练说话人嵌入为判别稳定性而抑制音段内变化，可能与流式帧级生成冲突。VOSSA 从内容编码器中间层提取说话人信息并以注意力统计池化聚合，与 VC 目标联合训练、无需独立说话人编码器。摘要称在六个数据集上改善 F0 动态与元音区分线索，同时保持相近 NISQA-MOS、WER 与说话人相似度，听感亦有提升。

**MeanVC 2: Robust Low-Latency Streaming Zero-Shot Voice Conversion**（论文 1961；Guobin Ma）  
针对 MeanVC 的块级自回归去噪、小块质量下降与参考 mel 敏感等问题，提出未来感受野分块（FRC）与通用音色 token 编码器。摘要称可在 40 ms 块大小下稳定转换，并把时延从 211 ms 降至 110 ms，显著优于 MeanVC。

### 流式 TTS、对齐与跨模态生成

**FlashTTS: Fast Streaming TTS with MTP Acceleration and X-pred Mean Flow Distillation**（论文 1692；Hanke Xie）  
面向流式文本/语音输入的对话 TTS，采用滞后多轨架构消除句级缓冲，并以并行多 token 预测与 X-pred 均值流匹配解码器实现恰好 2-NFE 的 token→mel 生成。摘要称首包时延降至 325 ms，同时保持较强零样本克隆与跨语可懂度。

**Prosodic Boundary-Aware Streaming Generation for LLM-Based TTS with Streaming Text Input**（论文 1192；Changsong Liu）  
针对流式文本缺少前瞻导致韵律不自然、以及无界上下文导致长文崩溃，提出韵律边界感知后训练：在有限未来文本下学习在内容边界早停，推理用滑动窗提示携带历史文本与语音 token。摘要称长短文均优于 CosyVoice-Style 交错基线；长文 WER 由 71.0% 绝对降至 4.8%，说话人与情感相似度相对提升 16.1% 与 1.5%。

**CTC-TTS: LLM-Based Dual-Streaming Text-to-Speech with CTC Alignment**（论文 653；Zhijian Ou）  
用 CTC 对齐器替代 MFA，并引入基于双词的交错策略；CTC-TTS-L（长度维拼接）偏质量，CTC-TTS-F（特征维堆叠）偏低时延。摘要称在流式合成与零样本任务上优于固定比例交错与 MFA 基线。

**Streaming T5-based Text-to-Speech Synthesis with Limited Lookahead**（论文 235；Muyang Du）  
S5-TTS 通过编码器—解码器语言建模与单调对齐，在收到前几个词后即开始生成；以 lookahead-causal 掩码与卷积辅助注意力，并配合交错多源蒸馏恢复自然度。摘要称质量可比全上下文 T5-TTS，支持高说话人相似度零样本，并显著降低对话端到端时延。

**PF-D2M: A Pose-free Diffusion Model for Universal Dance-to-Music Generation**（论文 248；Jaekwon Im）  
提出无需姿态、直接利用舞蹈视频视觉特征的通用扩散舞蹈到音乐模型，并用渐进训练缓解数据稀缺与泛化问题。摘要称在舞蹈—音乐对齐与音乐质量上达 SOTA，覆盖多舞者与非人类舞者等更真实场景。

## 本场要点

- 编解码器走向“双流+SSL 蒸馏”统一，或进一步压成单码本流式 SLM。
- 流式 VC 强调与 VC 联合学习的说话人表征，以及对小块与低质参考的鲁棒性。
- 流式 TTS 用边界早停、CTC 对齐、有限前瞻掩码与 MTP/均值流蒸馏共同压低时延。
- 长文流式合成需显式有界上下文，否则易出现崩溃与极高 WER。
- 场内亦出现舞蹈到音乐的位姿无关扩散扩展。

## 覆盖核对

- 3393 | HybridCodec: Fast Dual-Stream, Semantically Enhanced Neural Audio Codec
- 2803 | WavSLM: Single-Stream Speech Language Modeling via WavLM Distillation
- 2763 | VOSSA: Voiceprint Optimization for Streaming Speech Architectures
- 1961 | MeanVC 2: Robust Low-Latency Streaming Zero-Shot Voice Conversion
- 1692 | FlashTTS: Fast Streaming TTS with MTP Acceleration and X-pred Mean Flow Distillation
- 1192 | Prosodic Boundary-Aware Streaming Generation for LLM-Based TTS with Streaming Text Input
- 653 | CTC-TTS: LLM-Based Dual-Streaming Text-to-Speech with CTC Alignment
- 248 | PF-D2M: A Pose-free Diffusion Model for Universal Dance-to-Music Generation
- 235 | Streaming T5-based Text-to-Speech Synthesis with Limited Lookahead
