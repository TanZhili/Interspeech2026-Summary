# Learning to Rescale: On-the-Fly Sequence Length Adaptation in Non-Autoregressive Speech Synthesis

- 论文编号�?069
- 报告人：Jiawei Jin
- 程序：Monday 28 September 2026 / Scaling and Zero-Shot Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jin26b_interspeech.pdf

## 问题
非自回归（NAR）TTS 虽能并行推理、风格更稳，但对字级或全局时长预测依赖很重：字符级时长提取耗时且噪声数据下不准，固定总长度的 masked generative 方法（如 E2-TTS、F5-TTS、MaskGCT）仍需先给准全局时长。时长偏差会造成语速不自然、韵律碎裂，且无法随语义与声学自适应调长。把文本 DLM 的单 token 增删直接搬到语音域也不行——语音时序分辨率高、冗余大，单点操作梯度弱，序列又极长�?

## 方法
提出 **ElasticDLM**（弹性长�?Diffusion Language Model）：级联 DLM 中，Elastic Semantic DLM 先把音素+音色 prompt 映射为语�?token，再�?MaskGCT 式声�?DLM / decoder / vocoder�?
1. **功能 token**：`[EXPAND]` / `[DELETE]`，分别触发插�?mask 或删除片段，实现变长�?
2. **DLTS（Differentiated Length-Scaling Training�?*：先内容 mask，再做块级随机合并（非重叠块大小 \(n\)、概�?\(p\)）或在序列末插入 \(k\sim\mathrm{Uniform}(1,\lfloor\alpha(t)L\rfloor)\) �?`[DELETE]`；功�?token �?remask。损�?= masked NLL + \(\lambda\) 长度变化绝对误差（期�?\(\Delta\hat L_i=(n-1)p([\mathrm{EXPAND}])-p([\mathrm{DELETE}])\)）�?
3. **HCGI 推理**：每步先采置信度 \(>\tau\) 的功�?token 做长短调整，再对 content logits �?top-k，并按正弦调�?remask 最低置信位置；`[EXPAND]` 扩成 \(n\) �?`[MASK]`�?

训练：MaskGCT Text-to-Semantic 16 �?Transformer�?536 hidden, 16 heads）初始化，Emilia-large 英中�?100k 小时；EXPAND/DELETE �?0.5 概率独立施加，\(n=5\)�?4×A100，AdamW 1e-4�?2K warmup。默�?50 步、\(\tau=0.8\)、top-k=20，温�?1.5�?�?

## 实验与结�?
Seed-TTS �?seed-test-zh / seed-test-en，主对比 MaskGCT �?GT / Fix / Normal�?
- **Ours-Normal**（zh）：WER 2.387%，Len-L1 0.7091s，N-MOS 4.20，Sim 0.772；en：WER 3.534%，Len-L1 0.5283s，N-MOS 4.44。Len-L1 �?N-MOS 优于 MaskGCT-Normal，质量接�?GT�?
- **Fix 初长**（中 4s / �?4.5s）：Ours 几乎不掉；MaskGCT-Fix 严重恶化（zh WER 4.182%，en 13.341%）�?
- 消融（Fix）：去掉 Length-Loss �?zh Len-L1 0.8752�?.1129s；去�?HCGI �?zh WER 4.005%，en 5.652%�?
- 初长 1�?6s：Ours WER 稳定�?2.4�?.5%；E2-TTS / F5-TTS / MaskGCT 在极端长度崩溃。\(n=5\) �?WER �?U 形曲线上最优。表达性单说话人微调后 AB 偏好亦优�?MaskGCT�?

## 结论
ElasticDLM 用可学习功能 token + DLTS + HCGI，在不依赖准时长预测的情况下实现变长 NAR 合成，并在长度校准与自然度上优于固定长度范式；边界是仍依�?MaskGCT 级联后端，且块大�?\(n\) 对性能敏感�?

## 点评
核心抓的�?NAR TTS「时长先�?= 刚性瓶颈」：�?DreamOn 式增删改成语音友好的块级缩放，并用辅助长度损失与粗到细采样把变长和学习内容拆开。强�?Fix / 极端初长实验把「摆脱时长器」说清楚；脆弱处是对 \(n\)、\(\tau\)、调度的依赖，以及图中部分抽取乱码不影响主表数字，但表达�?AB 图细节需以正文文字为准�?
