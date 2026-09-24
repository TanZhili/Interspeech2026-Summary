# FlowEdit: Associative Memory for Lifelong Pronunciation Adaptation in Flow-Matching TTS

- 论文编号：2764
- 报告人：Nityanand Mathur
- 程序：Wednesday 30 September 2026 / Voice Editing
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/singh26c_interspeech.pdf

## 问题
Flow-matching TTS（如 F5-TTS）部署后对 OOV 专有名词发音错误会固化；G2P 词典难覆盖多语专名，微调易灾难性遗忘与音色漂移，权重编辑随编辑累积干扰。

## 方法
FlowEdit 冻结 DiT，在文本嵌入上对目标 token（Whisper 强制对齐定位，两侧各扩 1 token）优化扰动 δ，mel 重建 + λ∥δ∥²；用伴随灵敏度求对条件的梯度，约 50 步（N=32 Euler 约 15 s）。将 pool(c_I)→pool(δ*_I) 写入 Modern Hopfield 记忆；推理时软注意力检索并经相似度门控 σ(max sim−τ) 注入，支持模糊形态匹配。去重、LRU 限容；同形歧义用 ±3 token 上下文加权键。

## 实验与结果
骨干 F5-TTS + HiFi-GAN；基准 POLYGLOT-NOUNS（312 专名、18 语族、1560 句）。目标词 PER：zero-shot 42.5→FlowEdit 3.1（相对降 92.7%），优于微调 8.2 / LoRA 11.8；LibriTTS-R 通用 PER 保持 4.1（零遗忘），微调升至 15.3。人工评更高；跨语族一致大幅降 PER；200 次连续编辑漂移约 0.1；形态变体 PER 8.4 vs 词典 36.4；跨说话人迁移 PER 约 3.6。消融：无记忆、无门控、硬近邻、步数/λ 均变差。声调语 F0 残差较大，加 F0 损失可缓解。

## 结论
把发音纠正做成可检索的潜变量编辑而非改权重，实现近零遗忘的终身适应与约 15 秒级纠正，适合不可重训的生产 TTS。

## 点评
“言语治疗而非手术”的定位清楚：可微条件流匹配使输入侧优化可行，Hopfield 外置记忆避开权重漂移。相对 LoRA/微调，强在隔离目标 token 与保证通用 PER 不动。脆弱点在单音节/声调语与大记忆（M≫5k）稀释，且依赖参考音频与对齐质量。
