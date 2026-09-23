# Streaming T5-based Text-to-Speech Synthesis with Limited Lookahead

- 论文编号：235
- 报告人：Muyang Du
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/du26_interspeech.pdf

## 问题
级联 LLM–TTS 里多数 TTS 需整句上下文才开声，端到端响应延迟高。增量 TTS 已有研究，但多限于单/少说话人，零样本与自然度不足；T5-TTS 的 encoder–decoder 单调对齐适合稳健合成，却缺流式变体。

## 方法
提出 S5-TTS（Streaming T5-TTS）：词级流式，编码器处理已见词 + k 个前瞻词，解码器自回归生成当前词的 FSQ codec chunk；用交叉注意力 argmax 是否进入前瞻区判定词边界，chunk 间两帧重叠 + Hanning 交叉淡入。训练/推理对 encoder 自注意力与 decoder 交叉注意力施加 lookahead-causal mask；用 Conv 辅助注意力 + MAS 得到音素–codec 对齐以构造 decoder mask，并加 CTC 辅助损失。再以全上下文 T5-TTS 为教师做 Interleaved Multi-Source Distillation（IMSD）：成对语音数据与 ASR 过滤后的文本-only 软标签交错批蒸馏（隐状态 MSE + logits KL + CE）。

## 实验与结果
LibriTTS+HiFiTTS 训练（约 845h）。k=2 为自然度–可懂度折中（偏好测试 65.9% 优于 k=1）；k=3 可懂度明显变差。消融：去掉 encoder/decoder LCM 均伤 WER。IMSD 后 LibriTTS unseen：WER 2.65%、UTMOS 3.72，接近 T5-TTS；MOS 3.71 vs T5 3.75。UltraChat：蒸馏后 MOS 4.12 vs T5 4.21，E2E 延迟约 0.356s vs T5 0.868s。相对更大 AR/NAR 基线，在约 4.67K 小时数据上 STOI/PESQ 更优。

## 结论
有限前瞻下的流式 T5-TTS，配合因果 mask、辅助对齐与 IMSD，可接近全上下文质量并显著降低级联系统端到端延迟，且支持零样本说话人。

## 点评
把 T5-TTS 的单调交叉注意力优势搬到词级流式，并用 mask 对齐训练–推理分布，是务实增量路线；IMSD 用文本-only 软标签补自然度也贴合对话场景。脆弱处是依赖固定 k 前瞻（过大反而伤对齐）、词边界靠注意力启发式，以及蒸馏仍需强教师与 ASR 过滤算力。
