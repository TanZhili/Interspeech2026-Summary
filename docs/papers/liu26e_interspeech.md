# CTC-TTS: LLM-Based Dual-Streaming Text-to-Speech with CTC Alignment

- 论文编号：653
- 报告人：Zhijian Ou
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/liu26e_interspeech.pdf

## 问题
多数 LLM-based TTS 不做低延迟双流（文本边进、语音边出）。高质量双流依赖准确的文本–语音对齐与合理的交错训练序列；现有方法常用 MFA 等 GMM-HMM 强制对齐（流水线重、不够灵活），或固定比例交错文本/语音 token，难以刻画对齐规律。

## 方法
提出 CTC-TTS：用 CTC ASR（Whistle Conformer）做音素–语音对齐，经 Viterbi 得路径并将 blank 归到后续音素；NAC（WavTokenizer）帧率与 CTC 为 3:1，每音素对应三个语音 token。按词构造 bi-word 块：当前词音素 + 词间分隔符 + 下一词音素 + 当前词语音 token + ⟨eob⟩。两变体：CTC-TTS-L 沿序列长度拼接（偏质量）；CTC-TTS-F 将音素与语音 embedding 沿特征维堆叠（可从首音素起生成，降首包延迟）。单码本 NAC 上用 decoder-only Transformer，对语音 token 与 ⟨eob⟩ 做交叉熵（文本位置不计入损失）。

## 实验与结果
单说话人（VoiceAssistant400K）：相对 LLMVox，CTC-TTS-F 的 WER/CER 更低且 FPL-A 更短（约 159 ms vs 167 ms）；CTC-TTS-L 可懂度最好（WER 1.50%、CER 0.79%）但 FPL-A 约 210 ms；三者 UTMOS 均为 4.15。多说话人零样本（LibriSpeech 训练）：continuation 上 CTC-TTS-L WER 4.82%、MOS 4.33，优于 MFA+bi-word 与 ELLA-V 类序列；cross-speaker 上 CTC-TTS-L WER 6.33%、MOS 4.23。消融显示 CTC 对齐与 bi-word 交错均重要；CTC 在跨说话人域外更稳，MFA 在域内 continuation 上仍有竞争力。

## 结论
以 CTC 对齐替代 MFA，配合 bi-word 交错，可在流式与零样本任务上优于固定比例交错与 MFA 基线；L/F 两变体提供质量–延迟折中。未来可换神经 G2P 与更精细的神经强制对齐。

## 点评
核心是用“结构够用、不必帧级精确”的 CTC 对齐降低流水线成本，再用当前词+下一词的局部前瞻平衡流式条件。L 走长度拼接、F 走特征堆叠，把质量与首包延迟拆开权衡。脆弱处是依赖冻结 CTC/G2P/NAC 质量，以及 bi-word 仍需一词前瞻（L 甚至两词才出声），极短句或强共发音场景下对齐噪声可能被放大。
