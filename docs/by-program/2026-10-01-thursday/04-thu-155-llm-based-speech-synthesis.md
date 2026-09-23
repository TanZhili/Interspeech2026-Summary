# LLM Based Speech Synthesis

- 日期：2026年10月1日（星期四）
- 时间：09:00-11:00
- 形式：Oral
- Area：7
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场围绕基于语言模型的语音合成：解码顺序、束搜索效率、稳定性幻觉、混合骨干加速、块离散扩散并行生成，以及自然语言意图驱动的通用合成。主线是在保持可懂度与表现力的同时，纠正自回归 TTS 的顺序偏见、退化与算力瓶颈，并拓宽输入接口。

解码与对齐方面，掩码扩散框架显示从左到右并非最优，反向与置信度自适应顺序更优；注意力引导与 OAS 指标抑制重复/漏读等稳定性幻觉；SaVE-Beam 拆开搜索与评估以实用化最大化解码。架构方面，MamTra 交织 Mamba 与 Transformer 并知识蒸馏；DLLM-TTS 在块内并行掩码扩散；Bagpiper-TTS 先推理用户意图得到富说明再合成，覆盖多说话人、意图到语音、角色扮演与歌声等。

## 技术内容

### 解码顺序、束搜索与稳定性

**Decoding Order Matters in Autoregressive Speech Synthesis**（论文 1339；Minghui Zhao）  
用掩码扩散在推理时支持任意解码顺序，并在标量量化 Mel 上隔离离散编码器归纳偏置。结果显示从左到右次优，从右到左 consistently 更优，自适应置信度 top1 在模型输出中 MOS 最高；有效顺序保持局部连续帧簇以平衡长程依赖与局部连贯。

**Decoupling Search and Evaluation: Efficient Beam Decoding for Language Model-Based Text-to-Speech Synthesis**（论文 1531；Chenlin Liu）  
分析束搜索成本在搜索与评估间严重失衡，提出 SaVE-Beam：轻量学生做块级假设扩展，教师 LM 保留精确打分，并加硬重复约束抑退化。相对常规束搜索最高约 5.1× 加速且不降质量，相对采样 WER 最高降约 50%。

**Eliminating Stability Hallucinations in LLM-based TTS models via Attention Guidance**（论文 1345；Shiming Wang）  
分析文本—语音 token 对齐，提出用 Viterbi 的 Optimal Alignment Score（OAS）评估对齐质量，并纳入 CosyVoice2 训练以学习连续稳定对齐；再用预训练注意力经 CoT 指导学生，进一步降低稳定性幻觉。Seed-TTS-Eval 与 CV3-Eval 显示有效且无额外负面效应。

### 高效骨干、块扩散与自然语言接口

**MamTra: A Hybrid Mamba-Transformer Backbone for Speech Synthesis**（论文 1031；Tan Dat Nguyen）  
交织 Mamba 与 Transformer，并从预训练 Transformer 蒸馏知识以避免从头训练成本。最优混合配置下推理显存最高降约 34% 且不损保真，即便仅用原训练数据约 2%。

**DLLM-TTS: Block Discrete Diffusion Language Model for Text-to-Speech Synthesis**（论文 788；Wasim Madha）  
将 TTS 表述为对 X-Codec2 token 的条件块离散扩散：块间顺序、块内掩码并行，兼顾局部声学连贯与全局音文对齐。0.6B 模型、20K 小时训练，推理 RTF 0.15，Seed-TTS-eval 上具竞争力。

**Bagpiper-TTS: Natural Language Guided Universal Speech Synthesis**（论文 873；Haoran Wang）  
对自然语言请求先推理意图得到含转写与细粒度元数据的富说明（caption），再据此合成。除经典 TTS 外支持多说话人、意图到语音、角色扮演、歌声等。Seed-TTS-Eval WER 1.7%，多应用上 LLM 评判与主观评测匹配专用模型。

## 本场要点

- 自回归 TTS 解码顺序是关键建模选择，局部成簇顺序更优。
- 束搜索可通过搜索/评估解耦实用化，并抑制退化。
- 注意力对齐度量与引导可降低重复/漏读等稳定性幻觉。
- Mamba–Transformer 混合与块离散扩散分别攻克显存与串行瓶颈。
- 自然语言意图→富说明→合成扩展通用 TTS 任务覆盖。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 788 | DLLM-TTS: Block Discrete Diffusion Language Model for Text-to-Speech Synthesis |
| 873 | Bagpiper-TTS: Natural Language Guided Universal Speech Synthesis |
| 1031 | MamTra: A Hybrid Mamba-Transformer Backbone for Speech Synthesis |
| 1339 | Decoding Order Matters in Autoregressive Speech Synthesis |
| 1345 | Eliminating Stability Hallucinations in LLM-based TTS models via Attention Guidance |
| 1531 | Decoupling Search and Evaluation: Efficient Beam Decoding for Language Model-Based Text-to-Speech Synthesis |
