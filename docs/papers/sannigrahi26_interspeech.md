# AdaTS: Adaptive Token Sampling for Efficient Speech Language Models

- 论文编号：2753
- 报告人：Sonal Sannigrahi
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/sannigrahi26_interspeech.pdf

## 问题
SLM 将密集语音 token 塞进 LLM 上下文，序列长且冗余高，均匀卷积下采样或固定池化易在压缩与语义保留之间失衡，拖累长音频与推理成本。

## 方法
AdaTS：在预训练语音编码器输出上按成对余弦相似度做 score-and-merge——相似度高于阈值 t 的连续子组加权合并（权重 1−sim，强调更不相似单元）。两阶段训练：先冻编码器与 LLM，只训线性/MLP 模态与长度适配（ASR 对齐）；再解冻 LLM 做 ASR/SQA/ST 指令微调。编码器固定 Wav2Vec2Bert，解码器试 Qwen2.5 1.5B、Llama 3.2 1B、EuroLLM 1.7B；采样模块可只在 IT 或两阶段启用。

## 实验与结果
主结果（Qwen2.5 1.5B+AdaTS）：ASR LS Clean/Other 等显著优于 Pooling、WLQF、FLS；Spoken SQuAD F1 58.9、SLUE 37.5、LongSpeechEval 3.5，FLEURS ST COMET 82.0。t=0.85 时平均压缩约 1.65–1.85×（最高可超 4×）；加权平均合并优于简单平均与 Top-1。最佳为 MA 用全长、IT 再下采样；仅 MA 压缩会严重掉点。10 s 音频推理约 2.14 vs 卷积下采样 3.23 TFLOPS（约 34% 降算力；摘要称推理成本约降 40%）。

## 结论
无参相似度合并可在约 2× 平均压缩下保持甚至提升 ASR/ST/SQA，并降低推理算力；对齐阶段宜保留冗余，压缩宜放在指令微调。

## 点评
用内容自适应粒度替代一刀切下采样，小解码器也能压过依赖更大骨干的 CTC 融合路线。阈值对 ASR/ST 更敏感；压缩率随数据变化，部署需按任务标定 t。FLOPS 数字依赖其计算工具设定。
