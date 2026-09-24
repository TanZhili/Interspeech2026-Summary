# Scaling and Zero-Shot Speech Synthesis

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Oral
- Area：7
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场聚焦零样本与大规模 TTS：一方面用扩散语言模型式离散 NAR 架构把文本直接映射到多码本声学 token（OmniVoice，覆盖 600+ 语言、581k 小时开源数据）；另一方面用 ElasticDLM 通过长度缩放训练与置信度引导推理摆脱对精确时长预测的强依赖。

效率与适配是第二主线。WAND 把预训练 AR-TTS 改为全局条件注意力 + 局部滑动窗，并以课程收紧窗口与知识蒸馏保持音质，降低 KV cache。VoiceTTA 在推理时用强化学习（GRPO）与 F0/能量风格奖励、说话人相似度与 Whisper WER 做 test-time adaptation，专攻相声、方言等少见风格提示。

数据稀缺个性化方面，ZeSTA 用域嵌入区分真实与零样本合成增强数据并过采样真实数据；DSC-TTS 则在说话人嵌入空间与脸—声对齐共享身份空间双重约束，缓解模块化脸部驱动零样本 TTS 的身份漂移。瓶颈从“会说”转向时长柔性、超多语覆盖、长序列算力、少见风格模仿与跨模态身份稳定。

## 论文技术总结

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


# WAND: Windowed Attention and Knowledge Distillation for Efficient Autoregressive Text-to-Speech Models

- 论文编号�?43
- 报告人：Hanna Lee
- 程序：Monday 28 September 2026 / Scaling and Zero-Shot Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26j_interspeech.pdf

## 问题
基于 LLM 骨干的自回归 TTS 质量高，但全自注意力使计算与 KV cache 随序列线性甚至更糟地膨胀，长句与实时部署受限。剪层不改注意力本质；线性注意力/Mamba 需从头训且常掉质量；投机解码仍扛不�?cache 增长。作者假设：条件前缀（文本、参考音、系�?情感标签）提供全局语义与身份，生成声学 token 只需局部时序一致性，不必全序列注意力�?

## 方法
**WAND**（Windowed Attention and Knowledge Distillation）把预训�?AR-TTS 改成常数复杂度，不改主干结构�?
1. **全局 + 滑窗注意�?*：条�?token 全程可见；已生成声学 token 只看最近窗�?\(W\)，KV cache = 固定全局�?+ 滚动窗口 �?相对总长 \(T\) �?\(O(1)\)�?
2. **知识蒸馏**：学生用滑窗，教师全注意力；损失 \(L=L_{\mathrm{CE}}+\lambda L_{\mathrm{KL}}\)（Skew KL）�?
3. **课程缩窗**：余弦调度把窗口�?\(W_{\mathrm{start}}\) 收到目标 \(W\)，并对窗�?logits 用温�?\(\tau(t)\) �?mask，由软到硬�?

�?CosyVoice 2-0.5B（\(W=32\)）、IndexTTS 1.5（\(W=32\)）、SparkTTS-0.5B（\(W=64\)�?0 Hz 码率更高）上，仅�?LibriTTS train-clean-100 �?**53.8 小时**、单 epoch、单 A100 MIG 20GB 微调�?

## 实验与结�?
Seed-TTS-eval test-en / test-zh；效率按生成 10 秒音频计�?
- **质量**（test-en）：相对原模�?UTMOS/NMOS/SSIM 几乎持平或略升；WER 不升反降（如 CosyVoice 1.94�?.72，IndexTTS 0.98�?.91）�?
- **效率**：KV cache 最高降 **66.2%**（IndexTTS 38.44�?3.01 MB）；GFLOPs 降约 35�?7%，速度�?1.51�?.89×；每步延迟近常数，而全注意力随长度上升�?
- **跨语**：仅英数微调，test-zh CER 退化约 �?.1% 绝对（主系统）�?
- 注意力统计：前缀�?48�?5% 注意力质量；decode �?57�?3% 落在最�?\(W\)；前缀+局部共�?85�?1%。消融：CE+KL 与课程缩窗均优于直接硬窗或单损失�?

## 结论
WAND �?AR-TTS 的内存与每步算力从随长度增长变为近常数，在三套异构骨干上质量损失可忽略，并用少量数据实现跨语保持；作者认为这为「硬件不绑死的长时连续合成」铺路。边界是窗口 \(W\) 需随码�?注意力分布调（如 SparkTTS �?64），且仍依赖教师全注意力蒸馏�?

## 点评
抓的�?AR-TTS 里「注意力 sink + 语音局部相干」这一结构性冗余，用适配而非换骨干换取常�?KV。强在跨架构复现与极低数据量；脆弱处是极端超长或强跨句韵律依赖时局部窗可能不够，以及蒸馏仍需跑教师前向，适配阶段有额外成本�?


# VoiceTTA: Enhancing Zero-Shot Text-to-Speech via Reinforcement Learning-Based Test-Time Adaptation

- 论文编号�?757
- 报告人：Li Liu
- 程序：Monday 28 September 2026 / Scaling and Zero-Shot Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xie26c_interspeech.pdf

## 问题
零样�?TTS 多在播客、影视、有声书等常见域上训，遇到相声、方言、含糊、儿童语音等非常�?prompt 时，音色能贴上但夸张韵律与口音难仿。微调需要大量高质量目标数据；说话人嵌入适配又依赖嵌入模型，且对多样风格泛化不足。需要在推理时用极少参考音、轻量参数做在线适配�?

## 方法
**VoiceTTA**：在 flow matching 零样�?TTS（骨�?**F5-TTS**）上做强化学习式 **test-time adaptation**�?
1. 在首�?DiT 输入前接 **可学�?prefixes**（默�?4 个）；主网冻结，只训 prefixes�?
2. 用温�?\(T\sim U(0.5,1.5)\) 采样 \(k=4\) 条候选；奖励含：F0-CV 差、Energy-CV 差、说话人相似�?S-SIM，以�?Whisper WER 可懂度奖励；归一化后加权（\(\lambda_{1}=\lambda_{2}=0.2,\lambda_{3}=1,\lambda_{4}=1.5\)）�?
3. **GRPO** 优化 prefixes：因 flow matching 不产 token 概率，用 flow matching 损失差近似概率比；无 KL 项（只动轻量前缀）。每样本 \(G=50\) 步适配后合成；下一样本前随机重�?prefixes。每人约 **16 KB** 前缀可存�?

## 实验与结�?
内部 200 条非常规风格（口�?90 / 儿童 40 / 含糊 30 / 中国相声小品 40�? KeSpeech 八方言�?20 条；对比 CosyVoice、MaskGCT、Vevo、F5-TTS�?
- **平均**：Ours WER 3.12、S-SIM 0.64、S-MOS 3.27、N-MOS 3.35；优于或接近各基线（F5-TTS�?.19 / 0.57 / 3.07 / 3.36），风格相似度最高，自然度不掉�?
- 分场景：口音、儿童、含糊、方言等上 S-SIM / S-MOS 多领先；部分场景 WER �?F5-TTS 接近�?
- 消融：仅可懂�?�?WER 最好但 S-SIM 0.43；仅风格三项 �?S-SIM 0.67 �?WER 7.04；四奖励并用才平衡。前缀数在域外升、域�?Seed-TTS 上过多则伤；过大 \(T\) 伤可懂度�?

## 结论
�?GRPO 与复合风�?可懂度奖励在测试时适配轻量前缀，可显著提升非常�?prompt 上的风格模仿，同时保持清晰度与自然度，且参数与存储开销极小，适合在线个性化。边界是适配步数带来推理时延，且奖励依赖 ASR 与说话人嵌入模型质量�?

## 点评
把「域外风格」从离线微调挪到推理�?RL 适配，奖励设计直接对准韵律动态（F0/能量 CV）而非只追 embedding。强在非常规五场景与消融把风格–可懂权衡写清；脆弱处是 GRPO 多候选采样成本、以�?reward hacking（贴 CV/SIM 却不真「像」）风险，主观自然度仍略低于大规模后训的 CosyVoice�?


# ZeSTA: Zero-Shot TTS Augmentation with Domain-Conditioned Training for Data-Efficient Personalized Speech Synthesis

- 论文编号�?269
- 报告人：Youngwon Choi
- 程序：Monday 28 September 2026 / Scaling and Zero-Shot Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/choi26b_interspeech.pdf

## 问题
个性化 TTS 在目标说话人录音极少时难适配。用零样�?TTS 合成词句丰富的增强数据再微调轻量模型看起来可行，但作者观察到：大量合成音与少量真录音简单混训，可懂度上升�?*说话人相似度却掉**——模型被拉向合成域声学。需要不改主干架构、又能稳住身份的受控增强策略�?

## 方法
**ZeSTA**�?
1. 用开�?ZS-TTS�?*Fish-Speech**�?*CosyVoice 2**）在目标参考上合成分配给训练文本的语音；低资源设定保留 **Real 10%**，其�?**Synth 90%**（最长可用真录音�?prompt）�?
2. **Domain-conditioned training (DC)**：每条样本带 \(d\in\{\mathrm{real},\mathrm{synthetic}\}\) 域嵌入；文本编码器学说话人无关语言表示，声学模块条件于 \(d\)；推理时固定 \(d=\mathrm{real}\)。在多说话人 **VITS** 上复用说话人嵌入矩阵，隐层从 256 改为 **64** 作域嵌入�?
3. **Real-data oversampling (OS)**：真录音重复�?**3 �?*，强调稀缺真实域�?

目标模型先在 VCTK 按原 VITS 设定预训练；微调 LibriTTS 8 人与内部 YoBind 6 人语音助手数据，lr \(1\times10^{-5}\)�?00 epoch，单 A100�?

## 实验与结�?
指标：ECAPA-TDNN SECS、Whisper medium CER/WER；主�?MOS �?ABX�?
- Naive Real10+Synth90：相�?Real10 明显�?CER/WER，但 SECS 大跌（如 LibriTTS Fish�?.818�?.765）�?
- **DC+OS**：SECS 回升接近 Real10 / Real100（LibriTTS Fish/CV2 均约 **0.815**），同时保留合成带来的可懂度收益；两�?ZS-TTS 趋势一致�?
- 额外扩合成（VCTK 文本 + WER 低于 5% 过滤）：SECS 略降、CER/WER 再降�?
- 主观：MOS 不降；ABX 偏好提出法相�?naive 基线（LibriTTS FS 70.8%，YoBind 66.7% 等）�?
- 消融：OS 单独不稳；域嵌入 64 折中优于 16/256�?*说话人不匹配**合成相对匹配设置 SECS 更差�?.792 vs 0.807），说明需说话人一致增强�?

## 结论
ZS-TTS 增强有效，但必须用域条件与真数据过采样抑制合成域偏置；ZeSTA 在不�?VITS 主干下提升说话人相似度并保留可懂度。作者指出可扩展到更�?TTS 架构与架构专用条件策略�?

## 点评
问题定义很准：增强的「语言学红利」与「声学域偏置」分开处理——语言走文本支路、身�?域走条件嵌入。强在双数据源、双 ZS 生成器复现与 speaker-matched 对照；脆弱处是仍依赖外部 ZS-TTS 质量与参考时长，且目标骨干限定为 VITS，换流匹�?LLM-TTS 时域注入位置可能要重设计�?


# Dual-Space Constrained Face-Based Zero-Shot Text-to-Speech Synthesis

- 论文编号�?09
- 报告人：Ju Zhang
- 程序：Monday 28 September 2026 / Scaling and Zero-Shot Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26f_interspeech.pdf

## 问题
人脸含身份线索，可做无注册语音的零样�?TTS（配音、虚拟人等）。模块化路线用脸预测说话人条件、再喂预训练多说话人 TTS，音质可借大规模语音语料，但声学模型训练时只�?*语音导出**嵌入，推理才�?*脸导�?*表示，训练–推理失配导致身份漂移、音色不稳。端到端视听联合训又受视听数据规模限制�?

## 方法
**DSC-TTS** 三阶段模块化框架�?
1. **Speech Encoder \(E_s\)**：ECAPA-TDNN �?log-Mel �?\(\ell_2\) 归一化说话人嵌入；主目标 AAM-Softmax，辅以梯度反转域对抗（抑语料依赖�? Supervised Contrastive（保可分结构）。训完冻结�?
2. **对称 Face–Voice Alignment**：每视频均匀�?\(K=5\) 帧，注意力池化得脸嵌入；�?\(v=E_s(\mathrm{audio})\) 经投影进 256 维共享空间，双向 CLIP/InfoNCE + 重建 + latent consistency；投�?解码为两层残�?MLP�?
3. **Dual-space constrained TTS**：声学骨�?**YourTTS**（LJSpeech 预训�?120K �?LibriTTS 微调 165K）。微调时固定 \(E_s\) 与语音侧投影 \(P_v\)；对合成与真音施加说话人嵌入余弦一�?\(L_{\mathrm{SCL}}\) 与共享身份空间一�?\(L_{\mathrm{SICL}}\)，总损�?\(L_{\mathrm{TTS}}+\lambda_{\mathrm{SCL}}L_{\mathrm{SCL}}+\lambda_{\mathrm{SICL}}L_{\mathrm{SICL}}\)（\(\lambda_{\mathrm{SCL}}=9,\lambda_{\mathrm{SICL}}=3\)）。脸�?AntelopeV2�?

## 实验与结�?
训练：VoxCeleb2（对齐与编码器）、LibriTTS clean-100/360、LJSpeech。评测：VoxCeleb2 未见 24 �?+ LRS2 语料失配�?
- **Table 1**：DSC-TTS �?VoxCeleb2 �?WER 0.072、CER 0.037、SECS 0.677、SEC 0.842、SED 0.748、SMOS 3.172，优�?FaceTTS / Face2Speech / SYNTHE-SEES / Face-StyleSpeech；LRS2 �?SECS 0.653、SMOS 3.416 等同理领先�?
- **消融**：域对抗+SupCon �?SCL/SICL 互补；全组件组合最优。SICL 提升 SEC；SED 基本不变�?
- 可视化：注意力池化压低姿�?模糊差帧；LRS2 上脸–声嵌入 discrepancy 分布更左偏；t-SNE 合成嵌入簇更紧、类间更清�?

## 结论
通过语料不变说话人嵌入、对称脸声对齐与双空间约束训练，DSC-TTS 缓解模块化脸条件 TTS 的训练–推理身份失配，在相似度与身份一致性上优于既有脸基 TTS，同时保持可懂度。边界是仍依赖视听预训练数据与固�?YourTTS 骨干�?

## 点评
把问题钉在「训练用声、推理用脸」的表示缝上，用共享身份空间把推理条件拉回训练约束集。强在统一骨干下重实现多模块基线、以�?SEC/SED 拆开看稳定性与可分性；脆弱处是双空间损失权重敏感，且零样本�?TTS 仍受单图姿�?光照与跨数据集域移影响，主观 SMOS 方差仍大�?

