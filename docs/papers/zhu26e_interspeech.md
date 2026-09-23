# OmniVoice: Towards Omnilingual Zero-Shot Text-to-Speech with Diffusion Language Models

- 论文编号�?256
- 报告人：Han Zhu
- 程序：Monday 28 September 2026 / Scaling and Zero-Shot Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhu26e_interspeech.pdf

## 问题
大规模零样本 TTS 多只覆盖少数语言；离�?NAR 主流又常�?text→semantic→acoustic 两级级联，存在误差传播与语义码率瓶颈。单级直接预测声学虽更简，历史上可懂度落后两级系统。需要既能扩到数百语言、又能在单级离散 NAR 上稳住可懂度与相似度的架构�?

## 方法
**OmniVoice**：双�?Transformer + 离散 masked diffusion，直接把文本映到多码本声�?token（Higgs-audio 8 码本）�?
1. **Full-Codebook Random Masking**：对 \(T\times C\) 矩阵每个位置独立 Bernoulli(\(p_t\))，\(p_t\sim U(0,1)\)，平均约 50% 位置进损失（约为 per-layer �?\(C\) 倍），替�?SoundStorm/MaskGCT 式逐层稀�?mask�?
2. **LLM 初始�?*：骨干与 AR LLM 结构对齐，用 **Qwen3-0.6B** 权重初始化（作者称首个成功�?LLM 初始化受益的 NAR TTS）�?
3. **多语扩展**：聚合约 50 个开源集，经语音修复与规则过滤，�?**581k 小时�?00+ 语言**；语言级重采样抬低资源语；子词 tokenizer �?G2P。另支持 prompt denoising（`<|denoise|>`）、属性控声、副语言/拼音式混合输入�?

推理�?2 步迭�?unmask，时间偏移调�?\(\tau=0.1\)，层惩罚鼓励先解低层，CFG scale=2。双�?Emilia 版训 300k updates，多语版 2M updates�? GPU，packing 8192）�?

## 实验与结�?
- **中英**（Table 1）：OmniVoice-Emilia�?00k Emilia）与全量 OmniVoice（约 500k Multi.）在 LibriSpeech-PC / Seed-TTS 上与 SOTA 竞争；全量版 SIM-o / WER / UTMOS 多指标领先或接近前列（如 Libri SIM-o 0.729、WER 1.30；Seed-zh WER 0.84），CMOS/SMOS 亦优�?
- **MiniMax 24 �?*：Avg SIM-o 0.830，Avg WER 2.850，优�?ElevenLabs Multilingual v2 �?MiniMax-Speech�?
- **FLEURS-102**：Avg SIM-o 0.788，Avg CER 4.00（GT CER 5.11）；CER�?% 语言�?82（GT 75）。许多不�?10 小时训练语种仍可达低 CER�?
- 消融：full-codebook random mask 优于 SoundStorm/MaskGCT 式；仅单码本算损失则掉点。LLM 初始化相对随机初始化显著�?WER（如 Libri 1.57 vs 2.5+）�?

## 结论
单级离散 DLM + 全码本随�?mask + LLM 初始化，配合开源多语语料，使零样本 TTS 覆盖 600+ 语言并达到广泛基准上�?SOTA；边界是依赖大规模异构开源数据与 tokenizer 质量，低资源语仍受数据量制约（文中以 CER–时长曲线展示）�?

## 点评
把「多语扩展」和「单级离�?NAR 可懂度」绑在一起：�?LLM 先验补语言映射，用密集全码本损失补训练效率，避开语义瓶颈。强在开源数据规模与 102 语评测覆盖；脆弱处是多语质量高度依赖清洗与重采样，且商业对比仅在 MiniMax 子集，跨系统评测协议差异需谨慎解读�?
