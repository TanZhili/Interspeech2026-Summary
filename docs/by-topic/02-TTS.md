# 语音合成、声音转换与歌唱生成

- 论文数：158
- 规则：每篇论文至少进入一个技术分类；这里收录该分类下的全部单篇总结。

## 技术趋势与评论

# 语音合成、声音转换与歌唱生成：技术趋势评论

本组约百五十余篇工作覆盖零样本与规模化 TTS、流匹配与 LLM-TTS、可控/情感韵律、长形式与流式合成、低资源与文本前端、评测协议、声音转换，以及歌唱与生成式音频。共同背景是：零样本克隆与多语覆盖已成默认能力底座，研究重心转向**时长与长程一致性、细粒度可控、部署延迟、前端忠实度，以及评测是否还能拉开差距、是否贴合应用语境**。

### 零样本与规模化：从“能克隆”到多语、域外与效率

大规模零样本不再满足于少数高资源语言。单级离散 masked diffusion、全码本随机掩码与 LLM 权重初始化被用来同时抬可懂度与相似度，并配合异构开源语料与语言级重采样扩展到数百语；低资源语种仍受数据量与 tokenizer/G2P 质量制约。个性化侧则出现两条互补路径：推理时用轻量可学习前缀做强化学习式测试时适配，专攻方言、儿童、含糊、非常规表演等域外 prompt；离线侧用零样本教师合成增强数据微调轻量模型时，必须用域条件嵌入与真数据过采样抑制“合成声学域拉低说话人相似”的偏置。效率缩放同样进入议程——滑窗注意力加知识蒸馏把 AR-TTS 的 KV 与每步算力压向近常数；NAR 侧用可学习功能 token 做块级变长，减轻对准时长预测的刚性依赖。人脸等非语音条件零样本仍受模块化训练–推理身份失配困扰，双空间约束对齐是代表性缓解。反复出现的边界是：多语质量高度依赖清洗与重采样，测试时适配带来延迟与奖励模型依赖，商业对比协议不一致时跨系统排名需谨慎解读。

### 流匹配与 LLM-TTS：生成骨干与后训练分工

Flow matching / rectified flow 已成为零样本 TTS、Token2Wav 与部分 VC 的主流声学骨干；离散流匹配在因子化 codec 空间上追求更紧凑、更低时延。后训练重点从纯 LLM 侧扩展到 FM：把 ODE 采样转为等价 SDE 以引入随机性，再用 GRPO/DPO 类方法在线对齐说话人相似、可懂度与感知质量；混合系统上出现“LM 管可懂度、FM 管声学细节”的经验分工。一步/少步 mean flow、潜空间压缩与块级半自回归推理继续压延迟与显存。LLM-TTS 一侧则同时处理解码稳定性（注意力引导抑制稳定性幻觉、搜索与评估解耦的 beam）与块离散扩散等非纯 AR 替代。自然语言规划–描述–生成式统一接口把多说话人、角色与歌声等任务收进同一提示协议。共同脆弱点是代理奖励的 reward hacking、对 codec/参考转写质量的依赖，以及低 NFE 时常伴随的可懂度或相似度小幅回退。

### 可控与情感韵律：对齐管线下沉到词级与轨迹级

细粒度控制已从规则调 F0/能量与整句静态韵律，转向可计算奖励驱动的偏好对齐。强调与词级强弱/语速控制普遍采用 SFT→DPO→Flow-GRPO 流水线；部分工作用 LLM 打标签加教师 TTS 的 best-of-N 构造偏好，尽量摆脱人工标注。控制接口也在分化：音素对齐的 pitch/响度/时长、Lombard 式构音–发声双轴、口音强度插值、可学习 CFG null、以及文本描述与参考语音协同的粗到细控制。情感侧从离散类别走向词级残差强度、VAD 正交 LoRA、训练期学习的中性→情绪轨迹，以及跨模态一致性引导处理“文本语义与渲染情绪冲突”。与此同时，语篇条件重音基准显示当前系统几乎不可靠；神经 TTS 的全局 F0 压缩与局部变调过量、元音空间塌缩可同时存在，且韵律偏差与音段偏差近乎不相关——“听起来平”并非唯一诊断。口音–情感纠缠、指令中多维社会线索的绑定效应，以及可控性与 CER/说话人相似之间的张力，仍是共性边界。

### 长形式：上下文解耦、推理期扩展与叙事编排

长文痛点集中在韵律漂移、说话人不一致与句界伪影。训练侧用语义无关句的说话人嵌入解耦音色/角色与语义驱动韵律，并辅以自蒸馏补高强度情感稀缺；纯推理侧用软注意力先验加跨块传递编码器状态，在不重训长文数据的情况下改善连贯与边界。长对话 flow matching 则把 Mel 压到更低帧率潜空间以换显存，代价往往是客观可懂度与相似的小幅损失。更上游的多智能体闭环把选角、分层合成与 Critic 重生成接到长篇叙事与音效混音，质量提升依赖外部 LLM/TTS/SFX 栈。分析工作提醒：MOS 无法定位偏离发生在韵律层还是音段层，需语音学可解释指标补充。内部有声书/剧本数据、已知后文上下文与拼接构造的长文评测，仍限制复现与生态效度。

### 流式：有限前瞻、边界标记与低延迟 VC

部署目标明确为流式文本输入、低首包延迟与长文不崩溃。LLM-TTS 流式后训练用弱对齐插入韵律边界标记、有限 lookahead 与滑动窗口 KV，相对朴素交错可显著稳住长文可懂度与说话人/情感相似；CTC 对齐加 bi-word 交错试图替代沉重的 MFA 流水线，并在质量–首包延迟之间提供变体折中。Flash 类系统用滞后多轨输入、多 token 预测与少步 mean flow 同时砍“等整句”与“慢解码”。VC 流式则强调短块未来感受野、参考音色编码器对低质 prompt 的稳健性，以及听者侧电话降质场景下的多教师蒸馏；风格转换流式相对离线常抬高 WER。共性权衡是：lookahead 过大伤对齐，过小伤韵律；流式几乎总在可懂度、自然度与延迟三角中取舍，并对齐模块（WhisperX/CTC/G2P）质量敏感。

### 低资源与文本前端：先验迁移仍压过从零堆数据

低资源路径高度依赖英语或高资源基础模型的直接微调，受控对比显示持续混入英语数据未必优于直接迁入目标语；约十小时量级棚录在部分拉丁文部落语与 Indic 设定上已可建立可用基线，但同脚本不保证跨语迁移，声调与变音符仍脆弱。零样本教师合成再蒸馏到轻量 NAR，配合严格过滤，可换确定输出与大幅加速。前端被重新证明是质量上限的一部分：更精确的形态/G2P 显著改善韩语等 TTS；选择性音位变体 tokenization、通用罗马化加语音 token 预测、IPA 统一方言加参数高效适配，都在减少对语言专用规则工具的依赖。多音字与开放词表、希伯来等欠规格书写、日语口语化偏好对齐，以及输入语域（对谈转写 vs 书面文本）对可听性的影响，说明“文本进声学模型之前”仍未商品化完成。综述性判断是：成百上千种语言的合成门槛已下降，真正低资源/濒危场景下的多样性、质量与可靠评估仍是缺口。

### 评测：饱和区间、应用语境与专用基准

客观指标在 SOTA 区间易饱和且与人类排序相关弱；迭代自条件退化等协议被用来拉开区分度。更重要的是评测假设本身被质疑：应用任务语境会系统依赖地改变质量与听努力度评分；合适性跨域独立于自然度，优化一域可伤另一域。大规模成对评测加多维解释显示，总体偏好常由表达与可懂度驱动，噪声/幻觉轴在强系统上易饱和。专用基准密集出现——非语言发声、多音字、语篇重音、口音 codec 重合成、歌声多流派与细粒度歌曲维度等——把“有没有事件/对不对读音/适不适合域”从笼统 MOS 中拆出。自动 MOS 的性别偏差、野外离散 TTS 上的崩溃、情感嵌入相似度不可靠，以及训练动态伪标签与元音空间几何等补充手段，共同指向：听测与域感知协议仍不可被单一自动分替代。LLM-as-judge 与听者口音/性别偏差则是新的系统性噪声源。

### 声音转换：解耦、流式与场景扩展

VC 主线仍是内容–音色–韵律解耦。韵律导向 codec 把文本/说话人前缀吃掉可知内容与身份，迫使离散瓶颈编码残差韵律，并用双话语训练抑制 prompt 风格泄漏；共享说话人空间、cycle-consistent 说话人交换、伪平行构造与 SSL 空间局部仿射，分别服务歌声 VC、免蒸馏因子化 codec、开放集与可解释轻量路径。流式/低延迟 VC 与匿名场景把未来上下文、激励/F0 旁路与时变情感控制接到同一部署约束下。电话听者侧、实时风格（而非仅音色）转换、耳语到正常等设定扩展了应用面。边界包括：对 ASR/SV/SSL 质量的依赖、开放集相似度系统性弱于闭集、短参考下检索稀疏，以及流式场景中音质–延迟–相似的三角权衡。

### 歌唱与音频生成：编辑约束、文化数据与控制失败模式

歌声工作强调硬约束：改词保总时长与旋律的掩码 infilling、免手标对齐的扩散课程与偏好优化、风格一致的 rectified flow 美化，以及歌曲生成与伴奏协同的统一 SVC。全长歌曲生成用块内 NAR、块间 AR 的 flow matching 兼顾对齐与效率，并配合多维偏好优化。数据与评测同步扩张——多语 singfake、传统器乐文本–音乐、粤剧等剧种基准、多流派与细粒度歌曲质量维度——暴露零样本控制下的流派坍塌与检测器跨生成器脆弱性。文本到音频侧，否定约束被证明是系统失败模式；综述强调文本提示只是入口，创作者更需要 MIDI、分轨、参考片段等可编辑表示，以及条件遵循与创造性主体性等超越 Fréchet/笼统感知分的评估。视频到音频与综艺音效则走组合式控制、时序对齐与智能体检索闭环，多事件与重叠声源仍弱。连续扩散口语语言模型的缩放证据偏谨慎：语言性指标可随规模改善，但未根本改写算力需求，长程连贯仍难。

### 横切结论

若用一句话概括本组趋势：**零样本与流匹配/LLM 骨干已把“像不像某人、能不能多语”推到可用底座；增量价值转向变长与长程一致、词级/情感/指令可控、流式延迟，以及前端与评测是否诚实反映域与任务。** 仍普遍脆弱的是合成增强与奖励模型引入的域偏置、可控性与保真的张力、流式前瞻–崩溃折中，以及自动指标在饱和区间与跨域合适性上的失真。

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


# audiobook-cc: Controllable Long-context Speech Generation for Multicast Audiobook

- 论文编号：2125
- 报告人：Min Liu
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/liu26p_interspeech.pdf

## 问题
现有 TTS 偏单句，有声书多角色长篇缺少句间上下文建模与细粒度情感/音量/语速控制；提示音易把韵律绑定到 prompt，损害语义–韵律对齐与角色一致性。

## 方法
Audiobook-CC 基于 cosyvoice2（改用 BigVGAN）：AR 语音 LM 输入说话人嵌入 \(V\)（Cam++，来自同说话人但语义无关句）、前后文文本序列 seqC、离散属性控制 seqE（九类情感×四级强度、音量、语速）、文本与语音 token。解耦训练：timbre/persona 来自 \(V\)，韵律由当前文本与上下文决定。控制标签由 LLM 解析后规则归一；用自蒸馏合成高强度情感数据（PER<2%、SS>0.7 等过滤）缓解稀缺。三阶段微调（约 100 万→15 万上下文+指令→自蒸馏增强小时量级数据）。

## 实验与结果
章节级 M-MOS 4.25（Infer-ctx&inst），相对最强基线约 14% 相对提升；对话 S-MOS 4.11。ABX 上 Infer-ctx&inst 章节偏好 73.0%。解耦相对非解耦显著提高 S-MOS（约 3.45→3.93）；高强度–低强度情感区分在 Text-Unrelated 上明显强于 cosyvoice2；自蒸馏降低 PER 并恢复情感 F1。

## 结论
作者认为上下文机制、风格–提示解耦与自蒸馏共同提升多角色有声书的连贯性、语义对齐与情感可控性。

## 点评
针对有声书特有的“角色稳定 + 语义驱动韵律 + 长文连贯”三角，用无关内容说话人嵌入解耦是关键设计。控制离散化便于组合指令。依赖大规模内部有声书/剧集数据与章节标注，复现门槛高；后文上下文在推理时依赖已知剧本，对开放式生成需另想办法。


# MagpieTTS-LF: Inference-Time Long-Form Speech Generation Without Training on Long-Form data

- 论文编号：1461
- 报告人：Jing Yao Li
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ghosh26f_interspeech.pdf

## 问题
神经 TTS 短句质量高，长文易韵律漂移、说话人不一致与句界伪影。压缩序列、加长上下文或朴素分句拼接各有分辨率损失、硬掩码或需改架构/重训的问题。

## 方法
MagpieTTS-LF：纯推理期扩展 MagpieTTS（Koel-TTS 式编解码器 + 神经编解码 token）。(1) 软注意力先验：在上一时刻最高注意力位置邻域赋固定权重，远处给 \(\varepsilon>0\)，以 \(\lambda\log P_t\) 加到 softmax，引导单调对齐且保留远距上下文；(2) 有状态分块：跨句传递历史文本 token、对应编码器隐状态与注意力跟踪 \(\tau\)；(3) 历史文本编码支持篇章级韵律规划。无需长文重训或改结构。

## 实验与结果
自建 Long-Form HifiTTS（约 20 段 3–4 分钟 MLS 拼接）上对比 XTTS、Qwen3-TTS、VibeVoice。WER/CER 最低（0.025/0.012）；WavLM SSIM 最高且最稳；句界能量跳变 14.04 dB，综合 PBD 最优。全程说话人相似与 UTMOSv2 更稳、方差更小。超参：\(\varepsilon=0.1\)，\(w=(0.2,0.8,1.0,0.8,0.2)\)，\(\lambda=1.0\) 等。

## 结论
作者认为推理期软先验 + 跨块状态传递即可在不训练长文数据的情况下显著改善长距可懂度、韵律连贯、说话人一致与边界自然度，并可推广到其他分块编解码 TTS。

## 点评
价值在于“部署即用”：不碰权重，专治分句拼接的边界能量不连续与上下文断裂。软先验相对二值流式掩码更温和。局限是依赖 MagpieTTS 训练期已有的 CTC/注意力先验归纳；对非编解码器或非 AR 架构需再适配；评测长文为拼接构造，真实叙事节奏多样性可能更复杂。


# AuDirector: A Self-Reflective Closed-Loop Framework for Immersive Audio Storytelling

- 论文编号：1180
- 报告人：Wen Wu
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ren26d_interspeech.pdf

## 问题
长篇音频叙事需整合语音、音效与配乐，现有智能体系统常出现角色设定与声线不匹配、缺乏缺陷自纠、以及用户难用自然语言局部改稿。

## 方法
AuDirector 闭环多智能体：(1) 身份感知前期：Director 解析剧本与角色档案，Casting 用 EmbeddingGemma 粗检索 + Director 精选（320 条多样声库），并为每句生成 7 维情感指令；(2) 协同合成与校正：Acoustic 用 IndexTTS2 / TangoFlux / MusicGen 分层生成语音与非语音，Critic（MiMo-Audio、CLAP）打分，低于阈值则改情感指令/提示/种子并最多 \(N_{\max}\) 次重生成，Mix 混合；(3) 人机精修：Interaction 解析自然语言反馈，只对受影响脚本片段做定向再生。主 LLM 为 Gemini-3-Pro。

## 实验与结果
100 场景（40 播客 + 60 广播剧）对比 WavJourney、PodAgent 及无 Critic 变体。客观上 AuDirector 在 PQ、CE、VRM 领先（VRM 4.23）；主观 MOS-M/Emo/Ali/Aes 等整体最优或接近最优，Critic 带来除 MOS-Q/M 外的普遍增益。交互指令执行准确率平均 90%（增益控制 96%，结构编辑 84%）。作者指出非语音细粒度（如呼吸紧张度）仍受限。

## 结论
作者认为身份感知选角、闭环自纠与自然语言精修共同提升长篇音频故事的结构连贯、情感表现与声学保真，并支持人机协作。

## 点评
把“编排质量”与“单模型生成质量”拆开，在后端统一时用选角 + Critic 闭环解释 MOS-M/Emo 优势，评测设计较干净。系统工程性强，依赖外部 LLM/TTS/SFX 栈。脆弱点在重叠音效时的定位歧义（结构编辑 IEA 较低），以及环境声多样性不足仍会破坏沉浸感。


# Designed Vocalizations Dataset: Sound-Designed Human and Animal Voices for Non-human Voice Conversion

- 论文编号：932
- 报告人：Seolhee Lee
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/lee26i_interspeech.pdf

## 问题
人到非人语音转换（H2NH-VC）对游戏/影视等重要，但公开数据与基准稀缺，多依赖内部语料，难以公平对比与泛化评估。

## 方法
发布 Designed Vocalizations Dataset：从 VCTK 与 Freesound 收集言语与非言语源（动物、感叹、拟声等），用 Dehumaniser 2 内置与自研预设（部分经 Cubase 后处理）生成设计音色。训练为非并行 raw/designed；测试为 (source, reference) 对，reference 为同源经预设 \(G_p\) 处理。提供预设风格与源音色的 seen/unseen 划分。用 H2NH-VC 作基线评测。

## 实验与结果
训练约 5,654 源 × 40 预设 → 226,160 设计样本；测试 120 源 × 47 预设 = 5,640。四场景：seen–seen MOS 3.81、Cos.Sim 0.667；unseen–unseen MOS 3.49、Cos.Sim 0.610；交叉约 3.66。能量相关 PCC-E/RMSE-E 跨场景几乎不变；未见源时 CER/WER 反而更低（作者推测转换较弱、输出更接近源）。

## 结论
作者认为该公开数据集与基准可支撑非人设计发声转换的可复现研究，并给出基线结果供后续对比。

## 点评
贡献在资源与评测协议而非新算法：用专业 DSP 预设把“设计音色”可复现化，并显式拆开源/风格泛化。局限是基线仅一个模型，且 ASR 指标在弱转换时可能误导；效果模块覆盖仍可扩展。


# ZipL-Dialog: Memory-Efficient Long-Form Spoken Dialog Synthesis via Latent Flow Matching

- 论文编号：185
- 报告人：Jihwan Kim
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kim26_interspeech.pdf

## 问题
零样本对话 TTS 的 flow matching 在密集 Mel 上做分钟级单次生成时显存爆炸，常被迫切块，损害长程一致性。

## 方法
ZipL-Dialog：确定性 Mel 自编码器将 100 Hz Mel 压到 25 Hz（\(r=4\)，\(D=100\)）连续潜空间；在潜空间做掩码条件 flow matching（前缀上下文干净、目标区线性插值噪声）；辅助 Mel 域重建损失 \(\lambda=0.5\)。ZipFormer 下采样改为较温和的 [1,1,2,1,1]，避免默认激进层级在压缩后损害短音素分辨率。预训练后在 OpenDialog 英语子集微调。

## 实验与结果
相对 ZipVoice-Dialog：最大峰值显存最多降 11.22×（CoVoMix2：36.21→3.23 GB），推理最多快约 2.23×。UTMOS 最优或并列最优；WER/cpSIM 略逊未压缩基线。消融：确定性 AE 优于 VAE（WER 3.634 vs 6.535）；加 \(L_{\mathrm{mel}}\) 全面提升；默认 [1,2,4,2,1] 与无下采样均严重损害质量。

## 结论
作者认为 25 Hz 潜空间 CFM + 适配层级可大幅降低长对话合成的显存与时延，并保持有竞争力的感知自然度。

## 点评
把“长序列显存”问题落到时间压缩，并用确定性瓶颈 + Mel 监督对抗 VAE 过平滑，针对性强。效率收益清晰；代价是客观可懂度与说话人相似的小幅回退，说明压缩仍损局部细节。


# Not Flat, But Dissociated: Prosodic and Segmental Divergence in Neural TTS

- 论文编号：2730
- 报告人：Rong Wang
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/wang26ea_interspeech.pdf

## 问题
MOS 与谱距离只给全局分，无法定位合成相对自然语音的偏离层级：是韵律垮了、音段垮了，还是两者独立？

## 方法
在 LJ-TTS（13,100 句配对）上分析四系统（Tacotron2-DDC、FastSpeech2、Glow-TTS、MixerTTS），共享 HiFi-GAN。韵律：21 个句级 F0/强度/时间特征 + LASSO 分类。音段：元音空间面积、按发音部位的 F2 轨迹、locus equation。人–机边界经 MFA 迁移并抽查校验。

## 实验与结果
韵律呈跨时间尺度解离：全局 F0 变异压缩（\(d=-0.55\)），局部 pitch inflection 升高（\(d=+0.82\)）；语速/浊音比等时间指标无显著差。元音三角形面积仅剩人类 9–30%；齿龈/软腭处 F2 条件运动减弱，齿龈 locus 斜率系统偏高。韵律与音段偏差 Spearman 近零。LASSO AUC≈0.851。架构上 FastSpeech2 韵律偏差小但元音塌缩最重，Glow-TTS 局部变调过量等。

## 结论
作者认为神经 TTS 并非“单调平坦”，而是全局–局部 F0 协调与音段目标/协同发音各自偏离；二者基本不相关，应作为独立质量维度，补充 MOS。

## 点评
用语音学可解释指标拆开 MOS 黑盒，结论“解离而非平坦”有说服力。局限在单说话人朗读英语、两阶段声学模型；作者也承认在更口语/端到端系统上差距可能更大。


# Refining Emphasis Control in Flow-Matching TTS via Preference Alignment and Reinforcement Learning

- 论文编号：2284
- 报告人：Jiangnan Ye
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ye26b_interspeech.pdf

## 问题
细粒度强调控制因标注稀缺与韵律复杂而难；规则调音高/能量常不自然，LLM-TTS 指令微调又数据饥渴。

## 方法
在 F5-TTS 上加 Emphasis Encoder（4 层 Transformer），融合 `<strong>` 等标签嵌入。三阶段：(1) 2.5 h 人工中文强调数据 SFT；(2) 用 SFT 采样 + WPT 突显度排序构造偏好对做 Flow-DPO；(3) Flow-CPS（FlowGRPO 变体）以 WPT 为奖励做组相对优势在线 RL。标签可由 DeepSeek 辅助生成。

## 实验与结果
突显度：F5 0.86 → SFT 1.22 → DPO 1.42 → GRPO 1.45（CosyVoice 1.32）；WER 约 1.62–1.63% 稳定，SIM≈0.71–0.72。主观：E-MOS 2.51 vs CosyVoice 2.16，N-MOS 3.47 vs 3.06。名词强调控制准确率 GRPO 63%（DPO 37%，CosyVoice 22%）。

## 结论
作者认为 SFT→DPO→Flow-CPS 流水线可在有限标注下显著提升强调强度与可控性，同时保持可懂度与说话人相似。

## 点评
把 LLM 对齐套路迁到 flow-matching TTS，并用 WPT 作可计算突显度奖励，缓解标注瓶颈。风险是奖励模型与人类感知不完全一致；主要评测在中文强调场景，跨语与更复杂话语焦点泛化未充分展开。


# CraftTTS: Fine-Grained Prosody Control for Text-to-Speech

- 论文编号：2018
- 报告人：Qihang Lu
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/yang26l_interspeech.pdf

## 问题
零样本 TTS 全局克隆强，但严格词级强度/语速控制易破坏声学先验，产生伪影、停顿或不自然情绪泄漏。

## 方法
CraftTTS 三阶段对齐 CosyVoice 2：(1) 计算驱动数据：DeepSeek-V3 打 strong/weak/fast/slow 标签，Indextts2 多轮 AR 续写 + best-of-N（音色相似/时长代理语速）构造偏好正样本，无人工标注；(2) 联合 SFT+DPO 增强局部标签敏感；(3) GRPO，奖励解耦为停顿感知 ASR CER、情绪锚定强度对比、语速方向正则，平衡局部可控与全局自然。

## 实验与结果
中文 InstructTTSEval 等评测：相对 CosyVoice 2 基线，完整 CraftTTS 提升 NMOS（3.87 vs 3.67）、STMOS/SPMOS，SMOS 略升；CER 7.01%（基线 6.36%）、Sim 略降。消融与主观表明 Stage 2/3 逐步改善细粒度表达。

## 结论
作者认为零样本偏好构造 + SFT/DPO/GRPO 对齐可使 LLM-TTS 在保持零样本能力下达到更强词级韵律可控。

## 点评
与强调控制工作同属“对齐管线迁到 TTS”，特色是无人工偏好数据与多维解耦奖励，直接针对局部控制破坏全局先验的冲突。CER/Sim 小幅回退提示可控性–保真仍有张力；依赖教师 TTS 质量与 LLM 标注可靠性。


# Dynamic Prosody Prediction in LLM-based TTS for Improving Speaker Similarity

- 论文编号：2312
- 报告人：Zhenwei Mou
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/mou26b_interspeech.pdf

## 问题
个性化 LLM-TTS 常整体建模参考语音属性；显式韵律多为整句静态预计算（如 CoT），忽略已生成语音中的风格信息，限制说话人相似。

## 方法
在 CosyVoice LLM 上按音节动态预测韵律：音节韵律向量（时长、能量均值、基频均值与范围）经 k-means（512）量化；每音节先用 PQ 嵌入在已生成韵律/语音 token 条件下预测韵律 token，再条件生成该音节语音 token。训练 CE 损失加权 \(\alpha=0.5\)。约 50k 小时中文数据。

## 实验与结果
相对 CosyVoice(50k) 与静态 CoT：MOS 自然度相当或略好；偏好测试在 ESD/内部集上更偏好提出方法（约 48–52% vs 对方约 29–33%）。客观：三测试集 CER 更低；ESD 情绪 SIM/ACC 与能量 RMSE 等多项更好。作者还观察到动态预测有助于缩小小规模与大规模训练间的韵律学习差距。

## 结论
作者认为把已生成语音纳入音节级韵律预测可增强风格学习，从而提升说话人相似且不损自然度。

## 点评
相对“先整句韵律再语音”的 CoT，闭环利用自生成历史更贴合说话风格的时序依赖。实现绑定 CosyVoice 与音节级中文设定；韵律离散化粒度（512）与采样超参对风格保真仍敏感。


# FlowTTS-GRPO: Online Reinforcement Learning with Multi-Objective Reward Optimization for Flow-Matching Based Text-to-Speech

- 论文编号：1102
- 报告人：Haoxu Wang
- 程序：Monday 28 September 2026 / Text-to-Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/wang26s_interspeech.pdf

## 问题
TTS 的 RL 后训练多集中在 LLM 侧；Flow Matching 因 ODE 确定性难直接做在线 RL，且零样本克隆需同时兼顾说话人相似、可懂度与感知质量，多奖励易冲突。

## 方法
FlowTTS-GRPO：将 FM 的 ODE 采样转为等价 SDE 引入随机性，用 GRPO 在线优化开源 FM（CosyVoice 3.0 的 FM 部分、F5-TTS），无需额外随机生成器/价值网。奖励含说话人相似、ASR/CER、DNSMOS 等；对比概率式单奖励分配与按 batch 标准差归一化后的加权和。训练省略 CFG 加速收敛；对 F5 引入硬文本增广（词/句重复）。LoRA 微调 FM。

## 实验与结果
Seed-TTS-Eval：F5 经 FM-GRPO 后中英 CER/WER 与 SS、DNSMOS 提升（如 test-zh CER 1.81→1.55，SS1 0.760→0.777）；CosyVoice 3.0-0.5B 主要抬升 SS 与 MOS（SS1 0.777→0.804），CER 基本持平——符合“LM 管可懂度、FM 管声学细节”观察。加权归一化奖励收敛更稳。

## 结论
作者认为 ODE→SDE + GRPO 可直接后训练开源 FM TTS，多目标加权与硬样本策略有效，且 FM-RL 与 LLM-RL 作用互补。

## 点评
把 Flow-GRPO 从图像/增强迁到零样本 TTS，并点明混合系统中应 RL 哪一模块，实用。代理奖励仍可能 reward hacking；主观偏好相对客观表较简。硬样本仅中文侧为主。


# DiFlow-TTS: Compact and Low-Latency Zero-Shot Text-to-Speech with Discrete Flow Matching

- 论文编号：1043
- 报告人：Son Nguyen
- 程序：Monday 28 September 2026 / Text-to-Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/nguyen26d_interspeech.pdf

## 问题
零样本 TTS 中 AR 延迟高，连续流匹配空间复杂；离散扩散训练与采样配置强耦合。需要在因子化编解码离散空间做更灵活的离散流匹配。

## 方法
DiFlow-TTS：以预训练 FACodec 得韵律/内容/声学离散码与说话人嵌入。Phoneme-Content Mapper 将音素对齐到内容码并产内容嵌入；Factorized Discrete Flow Denoiser 在离散流匹配框架下用分头同时预测韵律与声学概率速度，条件于内容嵌入与参考提示的韵律/声学/说话人。PCM 确定性，流去噪器并行生成多属性。

## 实验与结果
作者报告相对基线在自然度、内容准确与韵律保持上有竞争力，模型可小至约 11.7×，推理加速可达约 34×（摘要/贡献声明）。作为 DFM 应用于因子化语音码的首批框架之一。

## 结论
作者认为在因子化离散码上做离散流匹配是可行的紧凑低时延零样本 TTS 方向，并提供分属性速度场分解设计。

## 点评
相对连续 FM，离散有限支撑降低优化难度；分头建模韵律/声学是相对同质 DFM 的关键扩展。正文抽取后半数字表不完整，规模与对比细节以作者声明为主；强依赖 FACodec 解耦质量。


# RAF: Relativistic Adversarial Feedback For Universal Speech Synthesis

- 论文编号：646
- 报告人：Yongjoon Lee
- 程序：Monday 28 September 2026 / Text-to-Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/lee26e_interspeech.pdf

## 问题
GAN 声码器架构进步快，但训练目标常不足以学到可泛化表示；提升泛化往往牺牲单步效率（如扩散/大模型）。需在保持 GAN 效率下同时抬升见域保真与未见域泛化。

## 方法
RAF：用 WavLM/HuBERT 等 SSL 嵌入与频域度量定义 real–fake 的 quality gap；判别器用相对论配对（RpGAN 式）估计 discriminator gap，对抗目标使两者对齐，生成器最小化判别器差距。应用于 BigVGAN-base、HiFi-GAN、Vocos 等，对照 LSGAN/SAN/WaveFM 等。

## 实验与结果
多数据集上客观与主观一致提升；摘要称 RAF 训练的 BigVGAN-base 在感知质量上可超过 LSGAN 训练的更大 BigVGAN，且参数仅约 12%。跨源域与未见集泛化增强。

## 结论
作者认为 SSL 辅助的相对论配对对抗反馈是提升通用 GAN 声码器的有效训练框架。

## 点评
改损失不改推理图，部署友好。SSL 选择（WavLM 末卷积层、HuBERT 第 22 层）有感知/音素依据。与 MetricGAN 系需区分：RAF 强调配对相对反馈而非直接回归可微指标。未见域增益取决于 SSL 覆盖面。


# Iterate to Differentiate: Enhancing Discriminability and Reliability in Zero-Shot TTS Evaluation

- 论文编号：2414
- 报告人：Shengfan Shen
- 程序：Monday 28 September 2026 / Text-to-Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/shen26d_interspeech.pdf

## 问题
零样本 TTS 客观指标（WER/SIM/预测 MOS）在 SOTA 区间易饱和、与人类排序相关弱；主观评测贵且难复现。

## 方法
I2D：对每个模型做多轮自条件合成——上一轮输出作下一轮参考，最多 10 轮；强模型退化慢、弱模型快，从而拉开差距。跨轮聚合（均值/加权）客观分。在 LibriTTS、Seed-TTS-Eval、CV3-Eval 上评 11 个 AR/NAR/混合系统，并做人机相关分析。

## 实验与结果
第 1 轮分数高度拥挤、UTMOSv2 等系统级 SRCC 弱（摘要称约 0.118）；迭代聚合后 UTMOSv2 系统级 SRCC 升至约 0.464。第 10 轮 utterance/system 级相关整体增强。可观察内容/说话人/自然度/情感克隆轨迹差异。

## 结论
作者认为迭代自条件退化可放大模型差、提升客观指标可区分性与人机对齐，适合自动化零样本 TTS 评测。

## 点评
评测协议创新：用误差累积当“压力测试”。代价是算力×迭代次数，且强依赖首轮参考质量；可能偏爱“抗自条件”而非单次生成最优的系统。与 VoiceMOS “zoomed-in”问题直接对话。


# Improving Text-to-Audio Instruction Following via Fine-Grained Feedback from Audio-Aware Large Language Models

- 论文编号：1111
- 报告人：Chun-Yi Kuan
- 程序：Monday 28 September 2026 / Text-to-Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kuan26_interspeech.pdf

## 问题
TTA 在 FAD/CLAP 等全局指标上已强，但多事件与时间顺序指令常失败；现有偏好数据多靠 CLAP/启发式/人工，缺可扩展的指令级正确性监督。

## 方法
用 ALLM 作细粒度裁判，判定目标事件是否存在与时间序是否正确；经基准与人工校验后，将满足/不满足样本构造成偏好对做 DPO。提出 S3Bench：叙事多事件指令约 1200 例（2–4 事件，LLM 生成叙述，仅评测不用训练）。

## 实验与结果
ALLM 与人在存在/时序判断上高一致（协议约 89.8%/93.5%）。DPO 后在既有基准与 S3Bench 上事件完整度、时序与联合指令遵循准确率提升，同时保持音频质量竞争力。

## 结论
作者认为 ALLM 细粒度反馈可规模化改进 TTA 指令遵循，并提供叙事评测基准 S3Bench。

## 点评
把理解侧 ALLM 接到生成侧训练信号，打通“能听懂指令→能生成符合指令”。依赖 ALLM 偏置；S3Bench 叙述由 LLM 生成，可能与裁判同族。相对 Baton 人工标注更可扩展，相对 CLAP 更对准事件/时序。


# StyleStream: Real-Time Zero-Shot Voice Style Conversion

- 论文编号：404
- 报告人：Yisi Liu
- 程序：Monday 28 September 2026 / Text-to-Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liu26c_interspeech.pdf

## 问题
零样本语音风格转换需要把源句改成未见目标说话人的音色、口音与情感，同时保留语言内容。现有方法内容–风格解耦不干净：大码本语义 token（如 CosyVoice 2，6561）仍泄漏口音/情感；Vevo 等纯自监督量化又易损伤可懂度。实时语音转换多只做音色，尚无端到端流式的整体风格转换。

## 方法
StyleStream 分 Destylizer 与 Stylizer。Destylizer：冻结 HuBERT-Large（训练流式时解冻并改因果）+ Conformer，FSQ 码本 `[5,3,3]`（45 码）与 ASR 解码器联合做 seq2seq ASR；推理用 FSQ 前的连续表示作内容特征（50 Hz），而非离散码。Stylizer：WavLM-TDNN2 风格编码器 + 16 层 DiT，以频谱 inpainting + OT 路径 conditional flow matching 训练，CFG=2、NFE=16。声码器为因果 Vocos（16 kHz）。流式用 chunked-causal attention，默认 600 ms chunk，端到端延迟约 1 s（`L = t_chunksize + t_proc`）。

## 实验与结果
Destylizer 在约 1300 h LMG（LibriTTS+MSP-Podcast+GLOBE）训练；Stylizer 在 Emilia 英语音约 50k h。评测 StyleStream-Test：300×10=3000 源–目标对。离线 StyleStream：WER 9.2%，S/A/E-SIM 0.852/0.640/0.827，主观 A/E/S-SMOS 最高（约 4.32/4.42/4.36）；流式 WER 15.3%，风格相似度仍领先 Vevo 等。chunk 增大（200→1000 ms）降低 WER、提高相似度与 UTMOS。RTX A6000 上 600 ms chunk 处理约 0.429 s，可流式。全文抽取在 baselines/消融中段截断，后续分析数字不全。

## 结论
作者认为以 ASR 监督 + 紧凑 FSQ + 连续软单元，可更干净地解耦内容与风格，并首次实现约 1 s 延迟的实时零样本风格转换，口音/情感相似度明显优于先前系统。流式相对离线牺牲可懂度。

## 点评
核心抓的是“内容提取瓶颈过宽导致风格泄漏”与“非自回归等长建模便于流式”两点；相对 CosyVoice 2/Vevo，把监督 ASR 与极窄码本压在一起、却用预量化连续特征喂 DiT，是合理折中。PDF 抽取在实验后半截断，消融与延迟表不完整，流式 WER 仍偏高，口音/情感泛化边界需对照完整原文。


# Coco-VC: Degradation-Robust Streaming Voice Conversion System on the Listener Side

- 论文编号：3571
- 报告人：Ryo Kato
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kato26_interspeech.pdf

## 问题
电话场景中说话人难以知晓己方音色/信道/噪声导致听感差；传统 VC 多在说话人侧且假设较干净输入。需要听者侧、流式、对电话降质鲁棒的实时转换。

## 方法
Coco-VC：因果 ConvNeXt 学生内容编码器（零前瞻、20 ms 帧，重叠相加后算法延迟 40 ms）+ 轻量 Vocos 解码器。多教师蒸馏融合 ContentVec（说话人不变韵律）与 Whisper 编码器（语言内容）。非对称训练：教师看干净 16 kHz，学生看经编解码、失真、混响、噪声等管线破坏的 8 kHz，预测干净融合特征。演示在消费级笔记本上运行（如 M2 约 80 ms 端到端），GUI 可开关 VC 与切换目标说话人。

## 实验与结果
与同解码器的 StreamVC 比：FLEURS-8k 上 WER 0.338 vs 0.451（UT-MOS 略低 3.214 vs 3.271）；VCTK 上 UT-MOS 4.041 vs 3.701。私有投诉电话仿真：61840 h 域内数据 vs 960 h 公开数据，WER 0.125 vs 0.363，UT-MOS 3.35 vs 3.08。

## 结论
电话增强 + 多教师蒸馏可得到降质不变表示，使听者侧流式 VC 在标准硬件上可用，并改善严重电话条件下的可懂度。

## 点评
把场景从“说话人美化自己”翻转到“听者侧补救”，工程闭环（延迟、GUI、域内数据）完整。核心是非对称蒸馏当联合增强器；局限是私有数据不可复现，且噪声极端时 MOS 未必优于基线，需在可懂度与自然度间权衡。


# Listening to Motion in Space: Vision-Grounded Event-wise Video-to-Audio Generation and Rendering

- 论文编号：3574
- 报告人：Dayeon Ku
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/park26m_interspeech.pdf

## 问题
常规 V2A 输出单一单声道混音，难做按源编辑与空间控制；端到端双耳系统又依赖大规模视频–双耳配对数据。影视/游戏/AR 需要可分轨、可空间化的工作流。

## 方法
训练免费流水线 VisionSFX：Gemma 4-VL 将场景拆为事件列表（起止时间、听感提示、片段）并给环境提示；每事件用 MMAudio 在约 5 s 裁剪窗内独立生成，边界 raised-cosine 淡入淡出；环境音改用视频无关的 TangoFlux，避免混入事件声。定位：Farnebäck 光流去自运动后取质心，Depth Anything 3 给相对深度，再经 HRTF 渲染；环境声 Hilbert 解相关成立体声。演示约 1 分钟完成 10 s 片段分轨时间线，支持改提示、时间线注入、方位/仰角/深度实时重渲染。

## 实验与结果
本文为演示系统描述，未报告定量客观/主观分数；强调单源重生成不影响其他轨、空间重定位无需再生成音频。

## 结论
组合现成 VLM/V2A/深度与经典光流+HRTF，可不训练、无双耳配对地得到可编辑、深度感知的双耳 V2A 工作流。

## 点评
价值在组合式后期友好管线，而非新生成模型。事件分解质量依赖 VLM，光流质心对遮挡/多目标可能漂移；缺少听感评测，空间真实感与时间对齐精度仍待验证。


# Automatic generation of audio comic from manga images

- 论文编号：3577
- 报告人：Sota Koshino
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/koshino26_interspeech.pdf

## 问题
有声漫画需为角色配适合剧情的表情语音，人工成本高；希望从漫画页图像（半）自动生成对应朗读/演技语音，兼顾制作降本与视障可及。

## 方法
流水线：检测分镜/文字/角色 → OCR → 阅读顺序 → 人脸与预存姓名–人脸库匹配并关联说话人，产出 XML；VLM（GPT-5.2）据文本上下文、脸与分镜图预测八类情绪，组成 “角色名's voice is Emotion with very clear audio” 提示；ParlerTTS 在约 9 小时 MangaVox 日语有声漫画数据上微调后按行合成。检测理解对比 Magiv2+Yomitoku（v1）与 Magiv3+MangaOCR（v2）。

## 实验与结果
约 700 页/8 部 Manga109+MangaVox 测试：v2 在面板/文本/角色检测、身份、说话人关联、TOER、CER 全面优于 v1，故采用 v2。主观：150 人、五分制整体印象；GT 真人约 4.0，v2+TTS 与 manual+TTS 均约 2.5，自动与半自动接近，但仍低于真人。

## 结论
自动检测–理解–提示 TTS 可生成一定质量的有声漫画，瓶颈更在 TTS 表现力而非理解流水线。未来改进提示设计与角色音色合成。

## 点评
把漫画理解与风格化 TTS 串成可演示闭环，客观任务齐全。主观上自动≈人工校正说明前端够用，差距主要在演技合成；情绪仅八类离散标签、依赖角色脸库，跨风格/无脸分镜时可能脆弱。


# Programmable Speech Synthesis without Computers

- 论文编号：3578
- 报告人：Takayuki Arai
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/arai26b_interspeech.pdf

## 问题
机械声道模型（VTM-UT 系列）可用滑块改变构型，但固定凸轮只对应单一短语；不用电脑/执行器时如何“可编程”地合成多短语动态语音。

## 方法
在 VTM-UT30-D6/D9（六块自下插入的构音滑块，D9 含鼻腔支路）上，用线性凸轮与旋转凸轮两种机构抬升滑块。可编程化：底板/基轴插入可互换异形板片（直角三角形/矩形/梯形等，或对应的斜坡/环扇），拼出任意凸轮轮廓；板片可拆装以换短语。目标高度以主声道高度 20 mm 为上限。

## 实验与结果
用两类凸轮合成同一英语短语 “I love you”；给出归一化时间上的六凸轮位移轨迹与频谱图，两侧共振峰轨迹大体相似。

## 结论
无需计算机即可用可编程机械凸轮驱动声道模型合成短语；线性与旋转方案输出相近。若有 Articulatory Phonology 轨迹，可扩展到任意短语；未来需更系统的轨迹设计。

## 点评
演示向工作，强调物理可解释的动态声道控制与“可插拔编程”。科学贡献在机构可复用性，而非语音质量评测；单短语、无听感/可懂度指标，与数字合成路线互补但规模扩展依赖手工轨迹设计。


# VoiceQualityGUI: A Tool for Word-Level Voice Quality Modifications

- 论文编号：3579
- 报告人：Harm Lameris
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lameris26b_interspeech.pdf

## 问题
嗓音质量（吱嘎、气声、鼻化等）对语用功能重要，但研究工具少；既往用 VoiceQualityVC 需手写各时段属性，难快速试探词级局部调制假设。

## 方法
Streamlit GUI：先对原音频做零偏移 VC 作基线，再调全局音高/音高变化以贴合原句，然后按词选择并滑动调节 creakiness、breathiness、nasality。后端为改进的 VoiceQualityVC：在 FreeVC 上为 HNR35、CPPS、H1–H2、H1–A3 各加仿射编码器，45k 迭代微调；用户侧暴露为三种感知组合。训练用 Expressive Speech 英语子集约 17h20m（prosody score≤0.78），帧级声门特征与句级音高 z 标准化。输入需源音频、≥30 s 目标说话人音频与时间对齐转写。保存修改音频与对齐调节记录。

## 实验与结果
本文为工具/演示论文，未报告独立听感或语用实验数字；动机来自先前游戏配音后编辑中手工改参的成功与繁琐。

## 结论
提供首个支持词级嗓音质量对照刺激制作的工具，便于假设形成与筛选，并期望推动更可控、意图驱动的合成。

## 点评
把可控 VC 接到研究友好工作流，切中“局部语用–嗓音质量”实验痛点。鼻化与所选声门特征关联较弱属已知近似；效果依赖对齐转写与目标说话人样本，跨语种/极端音质外推未验证。


# DsNA(Digital sigNature for Audios): A Unique Method to Fingerprint Audio Files Generated by Text to Speech

- 论文编号：3590
- 报告人：Vishal Gourav
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gourav26_interspeech.pdf

## 问题
高质量 TTS 加剧合成语音溯源与滥用风险；传统音频指纹偏内容检索，难把可验证出处嵌进生成语音本身，且不宜改 TTS 内部结构。

## 方法
后处理框架 DsNA：TTS 波形与元数据经哈希/数字签名（启发自 RSA）生成紧凑签名，切成三片；音频切成两等份，与签名分片交错拼成“自带指纹”文件。验证走反向流水线抽取分片校验。不改声学模型或声码器。

## 实验与结果
250 条 TTS 样本：指纹前后 SNR 均为 45.2 dB；MOS 4.51→4.48；CER 1.8%、WER 2.6% 不变。作者称无可观测保真度损失。

## 结论
交错嵌入可使合成语音自含可验证出处且保持质量。仍需检验压缩/噪声/对抗篡改鲁棒性与更强安全保证。

## 点评
思路是容器级交错签名而非感知水印，实现轻、对波形改动理论上可逆抽取。当前评测几乎无失真可能因嵌入对听感影响极小或指标粗；对重编码、剪切、重采样等常见变换是否仍可验证，正文未给出证据，安全声明需谨慎。


# Two Lessons Learned from the SGILE project: Efficient Building and Evaluation of TTS Voices

- 论文编号：3596
- 报告人：Korin Richmond
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pine26_interspeech.pdf

## 问题
绝大多数语言属低资源，难以按高资源范式用海量数据与大模型建 TTS；听者稀缺时传统 MOS 评测代价高。SGILE 项目需同时解决高效建声与高效评测。

## 方法
展示开源 EveryVoice TTS Toolkit：面向有限算力与少量音频（常仅数小时）从零建高质量音色，带向导降低非专家门槛。评测侧推广 Best-Worst Scaling（BWS）等相对选择范式，对比 AB：四刺激选最好/最差可等价约五对成对判断。演示为网页听测：盲评样本后揭示所用音色与数据量，并与其他用户跨语言偏好对照。

## 实验与结果
本文为 Show & Tell，不报告新的定量 TTS 分数；强调演示样本覆盖不同数据量与多语言，并引用项目前期工作称 BWS 更高效稳健。

## 结论
低资源 TTS 可用适度数据与工具链实现；BWS 等范式可在听者稀缺时提高评测信息量。后续 Own Your Voice 项目将把 EveryVoice 部署到强调数据主权的云环境。

## 点评
价值在社区工具与评测方法论的可体验展示，而非新声学模型。强项是把“少数据可建声”与“少听者可评测”绑在同一交互界面；局限是本文本身缺少对照实验数字，说服力依赖现场听感与已发表配套论文。


# Scalable Audio Scene Generation with the Treble SDK

- 论文编号：3609
- 报告人：Georg Götz
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gotz26b_interspeech.pdf

## 问题
真实共享空间录音难控、难扩展；仅有孤立 RIR 不足以支撑增强/分离等需要混音、目标轨、标签与背景噪声的任务。需要把声学仿真资产变成可复现、可规模化的完整场景数据集。

## 方法
Treble SDK Scene Generator：输入 RIR 集合、干净音频与场景/设备规则。场景以轻量 recipe 表示（轨道、源–IR 映射、听者配置、元数据、目标定义），卷积与混音仅按需渲染（lazy）。支持手工搭场景与规则驱动批量随机化（位置、说话人、重叠、电平、朝向、噪声等）。演示用 Jupyter：多说话人对话 + HVAC 噪声、时间线与 3D 房间视图、渲染混音/分轨/转录/JSON 元数据，再批量生成 SceneCollection。

## 实验与结果
演示系统描述，无独立下游 ASR/分离基准数字；强调 recipe 可序列化、共享、过滤与对齐监督信号。

## 结论
把物理接地仿真接到 ML 友好的场景配方与按需渲染，填补 RIR/干净音频与训练脚本之间的工程缺口，便于共享环境语音系统的数据生成与评估。

## 点评
贡献是工作流与数据工程抽象，而非新仿真算法。lazy recipe 对大规模数据集生成实用；可复现性依赖 SDK/仿真引擎与规则设计，本文未给出与真实录音下游性能的直接对比。


# Learnable Classifier-Free Guidance Null Embeddings for Enhanced Controllable Speech Synthesis

- 论文编号：803
- 报告人：Biel Tura-Vecino
- 程序：Tuesday 29 September 2026 / Controllable and Expressive Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/turavecino26_interspeech.pdf

## 问题
TTS 中 CFG 常用固定零向量作无条件表示，难以区分说话人与文本等正交条件，且可能落在训练分布外，导致大引导尺度下不稳定。需要更稳的无条件基线与可解耦的属性引导。

## 方法
模型：Qwen3-0.6B AR 骨干 + 轻量扩散头预测 64 维 VAE 潜变量，Perceiver 编码说话人，BPE 文本。将固定 ∅ 换为可学习 null 嵌入 ¯s、¯t；训练时各条件独立以 0.1 概率替换。推理可写解耦 CFG：分别对说话人/文本无条件隐藏态施加 ws、wt。对比固定零向量与可学习 null，并与 FishSpeech、Qwen3-TTS、VoxCPM、IndexTTS2 等对比；客观指标含 CER、SECS、PRO、PMR、PQ、UTMOS、Pitch std、SRR；主观多模型 CMOS。

## 实验与结果
耦合 CFG：可学习 null 对 w≥1.0 更稳，说话人相似度平台高于固定零向量峰值；w=0.8 时 SECS 0.817 vs 0.755，CER 相近且 Pitch std 更高。解耦 wt=0.4、ws=1.2 进一步抬 SECS/PRO。CMOS：可学习变体自然度/相似度均为正，固定零为负；解耦版相似度偏好更强、自然度略低于耦合版。文本引导上存在稳定性–表现力权衡，说话人引导存在相似度–绝对质量权衡。

## 结论
可学习 null 提供更稳、有意义的无条件基线，提升相似度与表现力并对大 CFG 更鲁棒；独立 null + 解耦权重可在推理时细粒度控属性。

## 点评
改动小但打在 CFG 实现细节上：把“缺条件”学成域内锚点，比硬塞零向量更合理。解耦引导把相似度与可懂度/表现力的折中显式化，利于产品侧调参；局限是评测说话人偏表现力强，听感上“更像参考”未必总被判为更自然。


# Synthesizing the Lombard Effect: Multi-Level Control of Speech Clarity and Vocal Effort in TTS

- 论文编号：1159
- 报告人：Seymanur Akti
- 程序：Tuesday 29 September 2026 / Controllable and Expressive Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/akti26_interspeech.pdf

## 问题
Lombard 效应（更大音量、更高音高、更慢语速、更平谱倾斜、更清晰发音）可提升噪声下可懂度，但现代 TTS 多训在非 Lombard 风格，缺少对发声力度与构音的统一、可解耦控制，尤其超构音建模不足。

## 方法
基于 Matcha-TTS（流匹配 + MAS 时长）与 Vocos 声码器。用 Expresso 的 default/enunciated/fast/projected 风格构造构音 β 与发声力度 α 伪标签（并入 LJ Speech 作中性扩充，约 11h+）。各属性映射到 32 维连续嵌入，与说话人嵌入拼接；双注入：编码器侧控时长/语速，解码器 U-Net 侧控谱–韵律。推理 α、β∈[0,1] 连续插值，并可按词赋不同 β 做局部强调。基线为 RMS 增益 + 线性时拉伸。

## 实验与结果
Harvard Sentences 上，提高 β 显著降 WER、升 MVD，α 主要抬谱倾斜；相对基线更有效。噪声实验（餐馆 babble、叠语、白噪，SNR=10/5/1，RMS 归一）：构音持续降 WER；发声力度在固定 SNR 下对 WER 帮助有限但对 SII 有增益；联合缩放在 SNR=1 时尤其有益。CMOS（10 人）：自然度 1.97±0.32、噪声可懂度 1.13±0.24（相对基线/中性）。另支持词级强调。

## 结论
双轴连续控制可模拟 Lombard 相关清晰度与力度变化，并在噪声听感上带来可懂度增益；词级控制可针对性加强片段。

## 点评
把 Lombard 拆成“构音 vs 力度”并分别打进时长与声学通路，比单一风格标签更贴真实适应机制。伪标签依赖 Expresso 离散风格到连续轴的映射，数据规模与说话人数有限，极端 α 还会偏离 ASR 分布；噪声评测做了 RMS 归一以排除简单响度作弊，设计合理。


# CrossAccent-TTS: Cross-Lingual Accent-Intensity Controllable Text-to-Speech via Disentangled Speaker and Accent Representations

- 论文编号：1744
- 报告人：Nirmesh J. Shah
- 程序：Tuesday 29 September 2026 / Controllable and Expressive Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/annamdevula26_interspeech.pdf

## 问题
跨语 TTS（尤其低资源、音系多样的印度语）中口音与说话人属性纠缠，LLM-codec TTS 虽有跨语能力却难显式控制口音强度；过强口音伤可懂度，需要转换与连续强度调制。

## 方法
Neucodec（50 token/s）离散化；Perceiver Resampler（Ns=32）从参考声学 token 得说话人/风格嵌入；GRL 对抗分类器抑制嵌入中的口音/语言信息；可学习语言嵌入扩展到所有 latent slot 并相加，推理用 λ e_lang1+(1−λ)e_lang2 插值口音强度。Qwen2.5-0.5B AR 预测声学 token。数据：Indic 多语约 986 小时 + L2-ARCTIC 微调。指标：口音相似度/泄漏、UTMOS、SpkSim；20 人 MOS。

## 实验与结果
Indic：Proposed UTMOS 3.181、AccLeak 0.203、AccSim 0.371、SpkSim 0.842，优于 IndicF5、XTTS-v2。L2-ARCTIC：UTMOS 4.001、AccLeak 0.439、AccSim 0.686，口音控制度优于 CVAE/GST。主观口音相似度 MOS 高于基线；强度 0→1.0 时 AccSim 单调上升。

## 结论
对抗解耦 + 加权语言嵌入可在保留说话人的同时做跨语口音转换与连续强度控制，适用于低资源多语设定。

## 点评
核心是把“口音当可加条件、说话人当需洗掉的泄漏”，用 GRL+语言嵌入插值实现强度旋钮，工程清晰。强度分析与泄漏指标对齐目标；脆弱点是口音评测依赖 GenAID/微调口音嵌入的代理质量，且 SpkSim 在 L2 上略低于部分 GST 基线，解耦仍有折中。


# CtrlSpeech: Coarse-to-Fine Control for Expressive Speech Synthesis

- 论文编号：1760
- 报告人：David Harwath
- 程序：Tuesday 29 September 2026 / Controllable and Expressive Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zheng26c_interspeech.pdf

## 问题
零样本 TTS 自然度与音色克隆已强，但词/音素级细粒度表现力控制仍难：说话人、韵律、风格常纠缠，现有控制多在句级提示，无法对齐到局部音高、响度或时长并保持目标音色。

## 方法
CTRLSPEECH 基于 DiTAR：VAE 将 16 kHz 波形压成 40 Hz、64 维连续潜 token；按 patch（4 token）做因果 AR + 局部扩散（flow-matching）生成。粗控制：CampPlus 说话人嵌入与/或 prompt 语音；细控制：音素对齐的量化 pitch（WORLD→Mel→128 bins）、A 加权响度（64 bins）、强制对齐音素时长帧数，叠加到音素嵌入。约 2 万小时英文（Emilia+GigaSpeech）训 0.1B/0.6B；推理 CFG 32 步、scale 1.5。支持先粗生成再迭代改局部控制。

## 实验与结果
零样本：0.6B 在 LibriSpeech-PC WER 2.46%、SIM-o 0.65，Seed-TTS WER 2.58%、SIM-o 0.63，优于复现 DiTAR；SMOS 亦更好。说话人消融：嵌入+prompt 最佳。有控制信号时 LJSpeech 上 pitch RMSE 67.86→38.39 Hz、loudness 6.35→4.56 dB；音素时长 MAE 28.08→11.86。

## 结论
全局音色 + 音素对齐韵律信号可实现粗到细的可编辑表达合成，同时保持有竞争力的零样本质量。局限：主英文；依赖 pitch/对齐质量；纯文本仍难预测精确局部韵律；未显式建模情感等。

## 点评
抓住“可编辑局部韵律”而非再堆提示词，连续潜空间比离散 codec 更利于细微起伏。控制信号显式、可测（RMSE/MAE）是强项；工程上依赖对齐与提取器误差，且 UI 迭代流程对标注成本敏感。


# ProsoCodec: Prosody-Oriented Speech Codec for Voice Conversion

- 论文编号：2146
- 报告人：Jeongsoo Choi
- 程序：Tuesday 29 September 2026 / Controllable and Expressive Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/choi26d_interspeech.pdf

## 问题
神经语音 codec 常把内容、说话人、韵律缠在一起，利于零样本克隆但不利于变声：变声需改音色、严保源内容与韵律。把韵律当独立可交换流往往丢掉说话人相关韵律细节。

## 方法
ProsoCodec：将韵律建模为条件残差——编码器/解码器以 ASR 文本与 SV 说话人嵌入作前缀，BSQ 离散瓶颈迫使 token 编码内容/说话人之外的韵律变化；编码器仅用低频 mel，解码器用全频 prompt。扩散 DiT 解码器 + 条件流匹配；训练交替随机 span mask 与同说话人双话语策略（prompt 与源不同句），减轻 prompt 风格泄漏。推理：源 token + 源文本 + 参考说话人/prompt。LibriTTS 585 h 训练，Vocos 合成。

## 实验与结果
合并 LibriTTS test + VCTK：ProsoCodec WER 4.451、SIMr 0.565、SIMs 0.167、f0 RMSE 0.428、P-MOS 3.852，整体优于 DDDM-VC、UniAudio、HierSpeech++、FACodec、Seed-VC、Vevo。消融：去掉双话语抬 RMSE；去文本条件 WER 暴涨；去说话人条件泄漏加重；全频 mel 略差。瓶颈约 12.5 Hz、4096 码本（150 bps）权衡较好；无 codec token 则退化为跟 prompt 韵律的零样本 TTS。

## 结论
文本/说话人前缀 + 离散瓶颈可学韵律残差，双话语与低频输入抑制风格泄漏，变声在内容、音色、韵律与自然度上更均衡。

## 点评
不走对抗解耦，而用“先验吃掉内容/音色、瓶颈只剩残差”的信息论思路，对变声更贴切。双话语训练直接打 prompt 抄袭；脆弱点是依赖外部 ASR/SV 质量，且码率过低会伤内容、过高又泄漏源音色。


# LibriTTS-VI: A Public Corpus and Novel Methods for Efficient Voice Impression Control

- 论文编号：2231
- 报告人：Junki Ohmura
- 程序：Tuesday 29 September 2026 / Controllable and Expressive Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ohmura26_interspeech.pdf

## 问题
数值化语音印象（VI，如明亮度等 11 维 1–7 分）可控 TTS 缺公开语料；且易出现印象泄漏——合成被参考音频自身 VI 拉偏。单参考同时供说话人与 VI 条件可能造成纠缠。

## 方法
发布 LibriTTS-VI：在 LibriTTS-R 上人工标注 130 句×10 维（+语速由 ASR WPM），训练 VIE 并按音高/能量/WavLM 相似句扩充到全库。骨干 VIC：HuBERT+BiLSTM 参考编码器、Control Module、STL，接 VITS。提出 VIC-dis：同说话人另一句 r′ 作说话人条件、VI 仍来自目标句；VIC-srf：用高斯噪声替换参考分支，纯 VI 控制。对比 VIC-base 与 Qwen3-TTS VoiceDesign（VI→NL 提示，零样本/微调）。

## 实验与结果
客观：VIC-srf 将 RVI-MSE 从 base 的 0.61 降到 0.41，∆V 从 0.22 到 0.05（泄漏近消失）；调制斜率平均 0.199>dis 0.159>base 0.121。QVD 数值控制弱（斜率 0.068），且文本语义与 VI 纠缠。主观多维调制 MSE：srf 0.92 vs base 1.15。质量 MOS 大多保持，部分极端调制略降。

## 结论
公开 VI 语料使可复现；双话语解耦与无参考生成显著减轻印象泄漏并提升数值可控性，优于基于 NL 提示的 LLM-TTS 在精细 VI 上的表现。

## 点评
问题定义清楚：泄漏来自“同一句既当身份又当印象”。解耦与无参考两条路互补；公开语料是社区价值。标注一致性中等、VIE 代理误差会传导到评测；部分维（如 Powerful–Weak）仍难学，极端调制可能伤自然度。


# MeloDISinger: Melody-Aware & Duration-Preserving Singing Voice Editing with Audio Infilling

- 论文编号：3285
- 报告人：Yoonjeong Park
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/park26k_interspeech.pdf

## 问题
文本驱动歌声编辑需改歌词同时严格保持总时长与旋律以对齐伴奏；既有方法或隐式控制无法硬性保时长，或复用原音素时长导致替换不自然，且常整段重生成破坏未编辑区。

## 方法
MeloDISinger：MeloDRP 在固定编辑跨度预算下预测时长比（span 内 softmax 归一），融合音素信息与伪 MIDI（由 F0 导出）经交叉注意，并用音素–音符时间重叠引导注意；FPIP 预测编辑区 F0；flow-matching mel 解码器只在编辑掩码区域做 infilling，未编辑帧原样保留。另用 WhisperX+LLM（含音节容量约束）生成可评估的编辑歌词。

## 实验与结果
GTSinger-En（13 h，三歌手）。相对 EditSinger、Vevo2：各编辑场景（替换/插入/删除/混合）DDUR≈0、DC≈99.93%，WER/CER 与 FPC 多数最优；主观 Lyric/Melody/Naturalness MOS 亦全面领先。消融去掉时长预算条件降幅最大，去旋律条件损害节奏相关编辑。

## 结论
时长比预测 + 旋律感知 + 掩码 infilling，可在保总时长与未编辑区的前提下做旋律一致的歌词编辑，并达 SOTA 主客观表现。

## 点评
把 SVE 的硬约束（跨度预算）直接写进时长建模，比事后裁剪更干净；伪 MIDI 交叉注意缓解“像说话的时长”。评测流水线本身也是贡献，但数据规模偏小、场景由 LLM 生成，真实制作流水线的编辑分布可能更杂。


# SingFox: A Multi-Lingual Singfake Detection Corpus

- 论文编号：2573
- 报告人：Arth J. Shah
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shah26_interspeech.pdf

## 问题
现有 singfake 数据多偏英语、生成范式单一，缺少多语、替代假唱（假人声+真伴奏）与源追踪设定；语音反欺诈模型难迁移到含节奏/旋律的歌声伪造检测。

## 方法
构建 SingFox：20 语种（14 国际+6 印度）、113,802 片段、约 126.32 小时、1150 歌手；六轨 T1–T6 分别覆盖全球语、Indic、乐器类、合集、替代假、源验证。真唱来自开放资源，假唱由 GAN（HiFi-GAN/BigVGAN/UnivNet）、扩散（DiffSinger/DiffRhythm）、VC（RVC/So-VITS-SVC）、TTM（MusicGen）等生成；4 s 切片、峰值+RMS 归一、不做源分离。约 30% 子集用部分生成器训练，其余含未见生成器测试。

## 实验与结果
LFCC+ResNet 等声学特征与 SSL 基线；跨数据集时 FMC 训练在 SingFox T4 上准确率最高达 77.84%，CtrSVDD/WildSVDD 训练迁移较差。T5 替代假上 LFCC+ResNet 准确率可低至 45.13%。源追踪上 LFCC 准确率 89.06%。生成器侧 BigVGAN/RVC 极难检（准确率约 1%），UnivNet 相对易检（71.17%）。人类 MOS：假唱约 3.47，真唱约 4.03。

## 结论
提供多语、多范式、含替代假与源追踪的 singfake 评测资源，暴露现有检测器在跨语/跨生成器与混合真假伴奏上的脆弱性。

## 点评
贡献是基准与威胁面设计，而非新检测器；T5/T6 特别贴近真实攻击（假声真伴、可解释溯源）。正文注明为高度压缩版、细节在 arXiv，部分表与结论表述略乱，使用时需对照完整版协议。


# Singing Voice Conversion via Shared Speaker Space and Min-Pooling Adversarially Enhanced Flow Matching

- 论文编号：2090
- 报告人：Hao Huang
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hu26g_interspeech.pdf

## 问题
SVC 中内容–音色解耦与重建质量常冲突：VQ 等显式解耦易丢细节或漏源音色；KNN 映射到共享歌手空间可去音色，但帧级拼接不连续，且 flow matching 易糊高次谐波。

## 方法
MinFlow-SVC：WavLM 特征经 content encoder，用指定共享歌手特征池做 KNN 对齐训练（Lknn）；对 encoder 输出做 min-pooling 对抗（盯最差连续性格子）平滑不连续。目标 Mel 由 OT-CFM 在内容、目标音色、F0 条件下生成；再以动态谐波掩码（DHM）+ min-pooling 对抗强化谐波区。先训 encoder 再冻住训向量场，HiFi-GAN 声码。

## 实验与结果
M4Singer 训练，OpenSinger 6 人零样本评测。说话人分类：原 WavLM 95%，转共享空间后 98%（表明源音色被抹掉）。MinFlow-SVC-10：NMOS 3.83、SMOS 2.65、F0CORR 0.948、MOSNet 4.26，整体优于 So-Vits-SVC、DiffSVC、NeuCoSVC；消融去 content encoder 损 SMOS，去 Lmin-pooling/Ladv-harm/DHM 均降自然度或 F0 相关。

## 结论
共享空间 KNN 去音色 + 双阶段 min-pooling 对抗（特征连续与谐波感知）可缓解解耦–质量权衡，零样本转换主观/客观更优。

## 点评
用共享说话人空间替代码本，解耦更“硬”；min-pooling 专门打最差局部，贴合歌声瞬态/谐波瑕疵。依赖选定共享歌手与 KNN 匹配质量，共享池覆盖不足时可能引入内容失真。


# YingMusic-Singer: Controllable Singing Voice Synthesis with Flexible Lyric Manipulation and Annotation-free Melody Guidance

- 论文编号：1547
- 报告人：Chunbo Hao
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hao26_interspeech.pdf

## 问题
改歌词保旋律的歌声编辑：上下文掩码法控制弱，商业 SVS 需手标 MIDI/时长；Vevo2 虽免对齐但可懂度与旋律贴合不足，SoulX 仍要字级时间戳。

## 方法
YingMusic-Singer：Stable Audio 式 VAE + MIDI 提取器中间表征作旋律、IPA 句级对齐歌词、DiT-CFM。课程：TTS 预训练 → 歌声 SFT（先无旋律再开旋律+CKA）→ GRPO（多奖励、组内相对优势）。输入为可选音色参考、旋律歌声片段、修改歌词，无需手标对齐。并提出 LyricEditBench（GTSinger 衍生，六类编辑×中英，7200 例）。

## 实验与结果
相对 Vevo2，跨六类任务在 PER、F0-CORR、Vocal Score 上全面更优（尤其翻译/语码混合）；主观 N-MOS/M-MOS 亦更高。消融：SFT Phase2 抬高 F0 但损 PER，GRPO 同时拉回 PER 并再提 F0/VS；去 CKA 略损旋律，去旋律扰动会导致模型“抄”旋律潜变量语义而 intelligibility 崩塌。

## 结论
免标注对齐的扩散课程+GRPO 可同时强化歌词忠实与旋律保持，并给出首个系统评测基准 LyricEditBench。

## 点评
问题设定贴产品（只给旋律片段+新词），CKA 与 GRPO 正面处理歌词–旋律权衡。单阶段 CFM 在 SIM 上不如 Vevo2 多阶段，但作者明确优先可懂度与旋律；大规模内部歌声数据与奖励模型细节对复现仍敏感。


# CTMusic: A Traditional Chinese Instrumental Music Dataset Towards Text-to-Music Generation

- 论文编号：882
- 报告人：Haotian Guo
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26l_interspeech.pdf

## 问题
文本到音乐模型训练数据高度偏西方流行/电子，非西方仅约 5.7% 时长；缺少面向传统中国器乐的文本–音频配对资源，限制风格生成。

## 方法
构建 CTMusic：741 对、约 42.7 小时；独奏 601（12 种乐器）、合奏 140。来源为数字专辑与 Bilibili 等，机筛+人工去短于 20 s/人声/噪声，裁剪≤400 s、44.1 kHz、−14 LUFS。三位民乐专业背景标注者按三段模板写描述，合奏文本经 DeepSeek 释义增强。验证：在 CTMusic 上两阶段（独奏→合奏）LoRA 微调 Stable Audio Open，并提出 SA-TTT（每四块插入门控 TTT 层）。

## 实验与结果
相对预训练 SA，SA-LoRA 在独奏/合奏测试上 FD、KL、CLAP 与主观 OVL/TA 全面提升；SA-TTT 进一步最好（如 stage1 FDopenl3 156.77、CLAP 0.38；stage2 137.49、0.51）。预训练模型对国乐生成能力明显不足，凸显专用数据必要。

## 结论
首个面向文本生成传统中国器乐的配对数据集，并证明 LoRA/TTT 适配可显著改善风格与文本对齐。

## 点评
核心贡献是数据与文化域适配，TTT 是增强而非全新生成范式。规模相对西方大数据仍小，合奏子集尤其有限；标注依赖专家模板，扩展自动标注质量是作者自述的下一步。


# SRF-SVB: Style-Consistent Singing Voice Beautifying via Rectified Flow

- 论文编号：615
- 报告人：Wenhui Li
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26h_interspeech.pdf

## 问题
歌声美化需改正业余音高/节奏并提质，同时保歌词与原唱歌手风格；现有 APC 多只改音高，NSVB 依赖难采集的平行录音，扩散式方法质量–效率难兼顾，过度“专业化”易抹掉个人音色与表达。

## 方法
SRF-SVB：解耦音高（RMVPE）、内容（Conformer PPG）、音色（CAM++）；训练时对 Mel 连续掩码（α=0.5）做 DiT 参数化的 rectified flow 填补，损失只算掩码区。推理：业余段作上下文 Mel，专业音高+DTW 对齐内容作生成条件，音色仍取自业余；Euler 10 步，NSF-HiFiGAN 声码。

## 实验与结果
约 160 h 中英歌声训练；英测 617、中测 874 业余–专业对。RPA：英/中 0.57/0.50（业余 0.40/0.22）；SECS 0.85/0.82，显著高于 NSVB（0.58/0.40）；MOS-Q/S 英 3.91/4.47，中 3.62/4.06，风格相似领先。连续 α=0.5 掩码优于更小比例或随机碎片掩码。英测 CER 略高于仅改音高的 Diff-Pitcher。

## 结论
首个基于 rectified flow 的风格一致 SVB，可高效同时校正音高节奏并保住业余歌手个性；生成重构偶发影响发音清晰度。

## 点评
用上下文 Mel 填补把“风格一致”写成训练–推理同构的 inpainting，比事后音色约束更直接。相对 NSVB 不再强依赖平行训练对是实用优势；CER 代价说明生成式美化仍可能碰歌词保真，实时场景还需压采样步数。


# Towards Unified Song Generation and Singing Voice Conversion with Accompaniment Co-Generation

- 论文编号：481
- 报告人：Ziyu Zhang
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26e_interspeech.pdf

## 问题
歌曲生成与 SVC 长期割裂：前者缺细粒度零样本音色克隆，后者忽视人声–伴奏协同；两者输入模态与优化目标冲突，朴素多任务易梯度对抗。

## 方法
UniSinger：多模态编码器（Qwen2.5 指令、Zipformer 音素、HuBERT+VQ 语义、CAM++ 说话人、自训 VAE 44.1 kHz 潜变量）接入 MM-DiT flow matching。四阶段课程用任务特异模态掩码：纯文本歌曲 → 纯 SVC → 说话人克隆歌曲 → 指令条件下伴奏协同 SVC。跨任务说话人空间先在 SVC 中纯化再迁移到歌曲生成。

## 实验与结果
约 20k+5k 小时内部歌曲。歌曲生成：PER 19.61%、Spk-Sim 68.85%，多项 SongEval 领先 DiffRhythm+/YuE 等。SVC：PER 0.151、Spk-Sim 0.712；带伴奏变体 Harmony MOS 3.891。消融去任务掩码、去 SVC 阶段或去歌曲阶段均显著损伤对应任务。

## 结论
统一框架首次同时支持说话人克隆歌曲生成与伴奏协同 SVC，课程掩码化解冲突并带来任务互惠。

## 点评
核心是用模态掩码课程把异构任务接到同一潜空间，并把 SVC 学到的说话人表征转给歌曲生成。强在伴奏协同与可懂度；主观音质仍受野外数据伪影制约，相对超大规模 YuE 在相似/质量上未必全面领先。


# Towards Chinese Yue Opera Singing Voice Synthesis: A Benchmark with Dataset, Data Augmentation and Baseline Model

- 论文编号：131
- 报告人：Peng Bai
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bai26_interspeech.pdf

## 问题
中国戏曲 SVS 资源稀缺，越剧（吴语）此前无专用数据集与基准；专业演员少、电子谱缺失、自动对齐难、源分离差，导致低资源困境。

## 方法
构建 YOAT：专业小生演员工作室干声约 1.35 h，切分为 565 句（均约 8.61 s），人工音素/时长+Parselmouth 音高对齐。增强：DA1 约 1 h 念白；DA2 字典拼接念白至 8 h；DA3 混入 4.5 h 歌仔戏对齐数据。基线 YueOpera-Singer：Transformer 编码器 + 乐谱时长扩展 + OT-CFM U-Net 解码，HiFi-GAN 声码。

## 实验与结果
543/22 训练测试划分。YueOpera-Singer-10：F0 RMSE 0.2133、MOS-N 3.92，优于 FFT-Singer、DiffSinger、FT-GAN，参数与显存更省。DA3 最有效（F0 RMSE 0.1834、MOS-N 4.01）；DA2 随规模提升发音 MOS；DA1 主要提发音、对 F0 帮助有限。

## 结论
给出越剧 SVS 首个数据集–增强–基线基准，MOS 约 3.92，为吴语戏曲合成提供可复现起点。

## 点评
贡献在文化低资源的数据与标注管线，而非架构创新；CFM 基线质量–效率均衡。单歌手、短时长限制泛化，跨剧种音高迁移（DA3）比同语念白更有效，提示“节奏–音高结构相似”比发音同域更关键。


# Back to Ear: Perceptually Driven High Fidelity Music Reconstruction

- 论文编号：219
- 报告人：Kangdi Wang
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26d_interspeech.pdf

## 问题
开源音频 VAE 常忽视听觉感知，相位与立体声空间重建差，导致瞬态抹糊与声像不准，难作专业级音乐重建前端。

## 方法
ear-VAE：卷积编码器 + 解码端 Transformer（RoPE）瓶颈；MS-STFT 判别器。损失含多尺度对数幅度、特征匹配、LS-GAN、弱 KL；提出相位相关损失（仅 LR）；重建前加 K-weighting；幅度在 MSLR 全通道监督、相位相关仅用 LR。两阶段训练：公开数据预训练 + 约 1 万小时内部高质量音乐继续训练。

## 实验与结果
相对 DAC、EnCodec、AGC、SAO，在 MuChin 与内部验证上 Mel/STFT 距离、ICPC/CCPC、SI-SDR、dbTP 与 MOS（4.70）全面领先。消融：相关损失、去 CQT 判别、K-weighting、Transformer 块均逐步抬升 SI-SDR；仅 M/S 相位监督反而有害。

## 结论
感知加权、相位相关与 MSLR 分流监督使开源音乐重建 VAE 达更优保真，尤其高频谐波与空间特性。

## 点评
把混音工程里的 K 计权与相关表思路写进重建目标，比单纯加大模型更对症。部分优势来自内部后训练数据，与纯开源基线对比需留意；作者也指出细微空间效果仍可能被衰减。


# Low-Resource Speech Synthesis: What Have We Solved, and What Remains?

- 论文编号：
- 报告人：Sakriani Sakti
- 程序：Tuesday 29 September 2026 / Low-Resource Speech Synthesis
- 技术分类键：tts
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
传统语音合成依赖大量转写语音，导致仅少数语言可用。低资源语音合成已大幅降低数据门槛，但仍需厘清哪些问题已解决、哪些对真正低资源/濒危语言仍然困难。

## 方法
报告综述推动进展的关键技术路线：多语言与跨语言迁移、利用未配对数据学习、无监督语音单元发现，以及更近期的基础模型。摘要指出如今可合成成百上千种语言，有时目标语言几乎无需转写语音。随后讨论仍存挑战（尤其对真正低资源语言）：语言多样性、合成质量与可靠评估，并结合原住民与濒危语言技术经验，讨论如何把合成进展与语言社群需求对齐。

## 实验与结果
摘要给出「可合成数百甚至上千种语言」的定性规模描述，但未提供具体系统名、评测集或 MOS/客观指标数值。

## 结论
数据门槛已显著下降，但真正低资源场景下的多样性、质量与评估仍是核心缺口；未来需更好连接技术进展与社群优先事项。

## 点评
框架是「已解决 / 仍困难」二分，适合作为低资源 TTS 的现状图。「数百/上千语言」来自摘要表述，缺少可核验评测细节。


# Lightweight Cross-Lingual Speaker Adaptation for Indic TTS

- 论文编号：2050
- 报告人：Tarun Kumar
- 程序：Tuesday 29 September 2026 / Low-Resource Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kumar26e_interspeech.pdf

## 问题
印度语 TTS/克隆多依赖大模型；IN-F5 等虽相似好，但易丢词、推理慢，难低资源部署，且跨语种需额外录音。

## 方法
三阶段： (1) FastSpeech2+HiFi-GAN 多说话人预训练（约 119 h，印地/马拉地/泰米尔/泰卢固），CLS 统一音素，双位点 ECAPA-TDNN 说话人条件（韵律前 + 声学解码前）与余弦一致性损失；(2) 用 10 s 参考经 IN-F5 合成约 2 h，经音素 CER、音高、时长、log-likelihood 四级过滤得 2088 句；(3) 在过滤合成数据上微调说话人条件层。推理仅用非自回归 FS2。

## 实验与结果
相对 IN-F5：印地 WER 11.8%→9.6%，跨语平均相对降约 21.8%；SECS 0.87–0.88（略低于 IN-F5 的 0.89–0.91）；输出完全确定（\(\sigma_{F0}=\sigma_{syl}=0\)）；单句推理约 53× 更快、参数约 4.7× 更少。主观 MOS 全语种最高（印地 4.14），SMOS 与 IN-F5 接近。过滤以 CER 阶段剔除最多（5.3%）。

## 结论
10 s 参考 + 质量控制合成数据即可得到轻量、确定、跨语（CLS）的说话人适应 TTS，在可懂度与速度上优于克隆基线，相似可竞争。局限：单说话人演示，多说话人验证仍待做。

## 点评
把“慢且不稳的克隆教师”蒸馏成非自回归学生，四级过滤是落地关键。双位点条件与 CLS 支撑跨语一致。当前证据绑定一名印地男声与合成教师质量上限；SECS 受合成语料相似度天花板约束。


# Scalable Neural TTS for Latin-Script Low-Resource Languages of Manipur

- 论文编号：2304
- 报告人：Hoomexsun Pangsatabam
- 程序：Tuesday 29 September 2026 / Low-Resource Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/pangsatabam26_interspeech.pdf

## 问题
曼尼普尔邦多数部落语言使用改编拉丁文正字法，方言与拼写不统一，缺乏可用 TTS 语料；既有 Indic 资源几乎不覆盖 Tangkhul、Maring 等藏缅语。

## 方法
工作室教材/故事/圣经译本文本，单说话人棚录（各一名标准方言女声），经 VAD 切分（2–8 s）、22.05 kHz 重采样与 LUFS 响度归一，得到 Tangkhul 9.58 h、Maring 10.79 h。字符级训练 Tacotron 2 与 FastSpeech 2（ESPnet），声码器用 Griffin–Lim 或 StyleMelGAN。开放预处理管线。

## 实验与结果
StyleMelGAN 相对 Griffin–Lim 显著降 MCD；FastSpeech2+SM 总体更优（如 Tangkhul Blind MOS 3.06、Maring 3.51）。Maring 听感受方言差异影响大；Tangkhul 变音符字符化易致短时不可懂。英语预训练模型因忽略声调等差异无法替代。

## 结论
约 10 h 棚录语料即可为拉丁文低资源声调语言建立可用基线；同脚本不保证跨语迁移。未来拟共享音素空间与实时部署。

## 点评
资源与管线贡献大于模型创新，对“无原生文字”情境务实。方言听感与变音符建模暴露了字符级正字法的脆弱点；单说话人限制表达多样性。


# High-Quality Speech Synthesis for Under-Resourced Ethiopian Languages

- 论文编号：2658
- 报告人：Rahel Mekonen Tamiru
- 程序：Tuesday 29 September 2026 / Low-Resource Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/tamiru26_interspeech.pdf

## 问题
阿姆哈拉语与阿凡奥罗莫语虽使用广泛，但缺少面向 TTS 的棚录语料；早期拼接/HMM 系统数据小、难处理非标准词与阿姆哈拉语叠音/同形异读。

## 方法
构建多说话人棚录语料：两语各约 100 h（各一男一女），阿姆哈拉另加 13 h 针对叠音与同形异读的句子，合计 113 h。文本清洗、数字展开、阿姆哈拉 Ge’ez→拉丁转写；微调 SpeechT5（英 LibriTTS 起点），用 512 维 x-vector 条件化多说话人。

## 实验与结果
数据从 50→100 h 降验证损失；阿姆哈拉加 13 h 后总体 MOS 由 4.12 升至 4.65。阿姆哈拉/奥罗莫总体 MOS 4.65 / 4.43（自然度、可懂度、发音分项见文内表）。推理依赖标准化输入，同形异读自动消歧留待前端。

## 结论
语言知情的大规模棚录数据 + SpeechT5/x-vector 可为低资源埃塞语言带来高自然度 TTS；语料拟在政策允许下公开。

## 点评
把“更多数据”具体化为同形异读/叠音靶向增广，对阿姆哈拉语收益直观。与早期系统对比主要靠 MOS 叙事；缺与 VITS/FastSpeech2 等同语料对照，跨模型结论仍待补。


# IN-F5: Adapting an English TTS Foundation Model for Multilingual and Zero-Resource Indian Speech Synthesis

- 论文编号：3366
- 报告人：Praveen Srinivasa Varadhan
- 程序：Tuesday 29 September 2026 / Low-Resource Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/varadhan26_interspeech.pdf

## 问题
英语大模型 TTS 已近人类水平，印度多语低资源场景难以从零复现；是否可用英语 F5-TTS 作先验，在严格数据预算下获得克隆、多语、语码混合等涌现能力，尚缺受控证据。

## 方法
扩展字符词表至 685 token（11 语原生脚本），比较三种策略：从零训 IN11、直接 EN→IN 微调、EN→EN+IN 混合微调。IN11 约 1417 h（IndicTTS/LIMMITS/Rasa/众包/IndicVoices-R）。再做 1/10/100 h 每语缩放；对无资源 Bhojpuri、Tulu 用相关脚本说话人合成 + 母语核验。

## 实验与结果
直接 EN→IN 总体 MUSHRA 最高（73.4），优于混合与从零（43.2）；见说话人自然度可与真人持平或略高。涌现：零样本克隆、跨语族 polyglot、语码混合与 Rasa 风格表达均较强。10 h/语已接近 100 h 多数能力；零资源 Bhojpuri 可达约 86 MUSHRA。相对既有 Indic TTS，IN-F5 MUSHRA 80.5（表 5 设定）。

## 结论
英语基础 TTS 经直接微调即可成为低资源印度多语先验，并支撑零资源跨语启动；不必持续混入英语数据。

## 点评
受控对比直接挑战“继续混高资源语更好”的直觉，实用性强。合成音有时高于真人，可能部分来自更干净、少瑕疵的生成偏置。语码混合在不自然语对上仍弱；从零失败也强调预训练不可替代。


# Preferences of a Voice-First Nation: Large-Scale Pairwise Evaluation and Preference Analysis for TTS in Indian Languages

- 论文编号：3357
- 报告人：Ashwin Sankar
- 程序：Tuesday 29 September 2026 / Speech Synthesis Evaluation 1
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/anand26b_interspeech.pdf

## 问题
众包成对评测可扩展，但印度多语与语音多维感知方差大；绝对 MOS 难诊断，仅报总体偏好无法解释“为何更好”。

## 方法
构建 5357 句、10 语基准（含规范化/符号/语码混合与 16 域）。1900+ 母语评委、>120K 成对比较，先锁总体偏好再评 6 维（可懂度、表达、音质、活泼、噪声、幻觉）。Bradley–Terry+Elo 排行，bootstrap CI；XGBoost+SHAP 解释轴对偏好的贡献；分析评委数/句数对排名稳定的影响。

## 实验与结果
排行：Gemini 2.5 Pro TTS > ElevenLabs V3 ≈ Sonic3 > … > IndicF5。Gemini 在 9/10 语与多数域领先；表达与可懂度对总体偏好贡献最大（SHAP），噪声/幻觉因多数系统已较强而区分度低。约 100–200 评委、~1000 句可达 ρ≥0.95 的排名一致。轴级判断可跨语预测总体偏好（准确率约 86%）。

## 结论
可控多维成对评测能稳定排出 Indic TTS 榜，并揭示偏好主要由表达与可懂度驱动；公开基准与偏好数据。

## 点评
规模与协议（先总体后分轴）设计扎实，对“可扩展又要可解释”的评测很有参考价值。商用系统主导榜单也暴露开源 Indic 差距；信噪/幻觉轴饱和时解释力下降，需更难的失败样本。


# Application context in speech synthesis evaluation: A problem and a solution

- 论文编号：747
- 报告人：Fritz Seebauer
- 程序：Tuesday 29 September 2026 / Speech Synthesis Evaluation 1
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/seebauer26_interspeech.pdf

## 问题
合成语音评测常在“中性”孤立句上做 MOS，假定质量可模块化、与应用无关；生态效度不足，且跨场景比较可能混淆系统差异。

## 方法
80 名德语母语者，4 任务×4 系统拉丁方：学习对话、寻物导航（WoZ）、自由对话、听短故事；系统为 Tacotron2+WaveNet、VITS、Auralis/XTTS-V2、Orpheus。实体公寓与其 Unreal 数字孪生并行。评总体质量、听努力度、自然度等与短版 UEQ。贝叶斯层级模型检验任务、系统及交互；ROPE 判定实际等价。

## 实验与结果
导航任务在总体质量、听努力度、自然度等上显著更高；任务×系统交互在听努力度、语调、音质、愉悦度等上超出 ±10 ROPE。部分维度（UEQ、外向性等）更接近等价。VR 与实体条件统计可比（RQ3）。

## 结论
应用语境显著且系统依赖地改变合成语音评分；未指定场景的系统对比可能混淆。数字孪生可作为更生态评测的可行路径。

## 点评
交叉设计直接冲击“中性评测可迁移”假设，对工业选型很实用。VR 等价是降低成本的亮点。任务顺序固定、系统含未知商用数据，因果解释需谨慎。


# Is Natural Always Appropriate? Investigating Naturalness and Appropriateness Across Different Domains for TTS Evaluation

- 论文编号：3392
- 报告人：Dominika Woszczyk
- 程序：Tuesday 29 September 2026 / Speech Synthesis Evaluation 1
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/woszczyk26_interspeech.pdf

## 问题
TTS 保真提升后，单一“自然度”难反映是否适合下游用途；合适性如何随域变化、与人类相似度是否一致，缺少系统证据。

## 方法
150 名英语听者，拉丁方评 5 系统（Kokoro、Gemini TTS、Kyutai-TTS、GPT-4o-mini-tts、ElevenLabs）+ 真人，覆盖朗读、演员、动画角色、助手、自发说话者等人格；刺激来自 LibriQuote、MSP-Podcast、MELD、AnimeVox 等。同时报人类相似度与“说服力/合适性”，并分析声学特征与自动指标相关。

## 实验与结果
合适性跨域独立于自然度：Kokoro 适朗读/助手但弱于对话；Kyutai 适自发对话但弱于助手/动画。人类相似度与合适性在 Actor/Spontaneous/Reader 正相关，动画近零、助手负相关（ρ≈−0.44）。动画偏好更高节奏波动，助手偏好更稳、更低 f0 范围。单一自动指标难以普适预测合适性。

## 结论
TTS 未“通吃”：优化一域可伤另一域；自然度会惩罚风格化、奖励自发性，需域感知评测。

## 点评
把自然度与合适性拆开并跨域对照，直接服务产品选型。低评者一致性（α≈0.2）说明合适性主观且期望驱动，榜单需报告域与协议。助手“略机器感更合适”的现象值得后续验证。


# NV-Bench: Benchmark of Nonverbal Vocalization Synthesis for Expressive Text-to-Speech Generation

- 论文编号：2211
- 报告人：Qinke Ni
- 程序：Tuesday 29 September 2026 / Speech Synthesis Evaluation 1
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ni26_interspeech.pdf

## 问题
表达 TTS 越来越多纳入非语言发声（NV），但评测缺标准、缺配对真人参考，常只能粗查“有没有事件”，无法量化与真实录音差距。

## 方法
发布 NV-Bench：1651 条多语（中/英）野外话语、配对 GT，按 Batliner 功能分类覆盖 14 类 NV；平衡单标签与相对平衡多标签子集。训多语 NV-ASR（SenseVoice-Small 微调）作自动评委。双维协议：指令对齐（CER/PCER/OCER）与声学保真（SIM、DNSMOS、FAD/FD、主观）。评 Orpheus、CosyVoice 变体及自训 NV-CV3/NV-FlexiVoice。

## 实验与结果
NV-ASR 在标准 ASR 与 NV 集上可靠（如 SMIIP-NV CER 1.29%）。多数模型 PCER 仍高（控制弱）；NV-CV3、NV-FlexiVoice 在对齐与保真上整体更强。客观指标与人类感知相关，可作标准化框架。

## 结论
NV-Bench 把 NV 当作交际行为评测，分离“控不住”与“听不真”；公开测试集与协议支撑可复现对比。

## 点评
配对 GT + 平衡类别 + PCER 是相对现有“有没有笑声”评测的实质进步。依赖 NV-ASR 作裁判，其标签错误会传导；多标签子集仍受长尾共现约束。


# Phonetically Grounded Vowel Space Metrics for Evaluating Synthetic Speech During TTS Model Training

- 论文编号：1579
- 报告人：Pasindu Udawatta
- 程序：Tuesday 29 September 2026 / Speech Synthesis Evaluation 1
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/udawatta26_interspeech.pdf

## 问题
训练中反复做听感测试不现实，损失曲线又缺语言可解释性；需能在训练过程中跟踪口音/元音系统学习的客观指标。

## 方法
提出 Vowel Space Overlap（合成与真值元音空间多边形交面积）与 Procrustes Normalised Disparity（去位姿/尺度后的形状残差）。在 GAE 预训练 Tacotron 2 上分别微调 NZE 与 GIE，多步提取角元音 F1/F2，算两指标；听者评目标口音相似度并与指标做 Pearson 相关。

## 实验与结果
两口音上，Overlap 最大与 Procrustes 最小的步数与视觉最佳形状对齐（NZE≈3000、GIE≈24000）。指标与感知口音相似度显著相关，可作损失曲线的可解释补充。

## 结论
元音空间几何指标可在训练中提供感知相关、语音学可解释的监控信号，并在多口音上稳健。

## 点评
把“看图收敛”落成可复现度量，对口音适应实验很实用。依赖角元音与强制对齐/共振峰估计，噪声与错误切分会扰动；目前仅 Tacotron 2 与两口音，外推到神经声码器端到端系统仍待证。


# The Binding Effect: Analysis of How Multi-Dimensional Cues Form Gender Bias in Instruction TTS

- 论文编号：66
- 报告人：Kuan-Yu Chen
- 程序：Tuesday 29 September 2026 / Speech Synthesis Evaluation 1
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/chen26b_interspeech.pdf

## 问题
指令式 TTS（ITTS）评测性别偏见多做单属性探测，忽略社会地位、职业刻板与人格描述等线索的组合；现实提示下的 Binding Effect 会改写单维先验，掩盖交叉偏差。

## 方法
将控制空间解耦为 Social Status、Career、Persona（Big Five）三轴；Stage1 测单描述符的女性声学概率 \(P(x)\)（wav2vec2 性别分类器）；Stage2 构造双/三维组合，在 logit 空间量化相对加性基线的交互项 \(I\)。评 VoxInstruct、PromptTTS++、Parler Mini/Large；每描述符 100 条性别中性内容句。并比对文本编码器语义先验与训练数据人口分布。

## 实验与结果
单维上职业/人格常强偏女性；组合后出现显著 Binding Effect 与主导覆盖（如高地位+reckless 可翻转 nurse 的女性先验）。交互模式与预训练文本编码器语义先验强相关，不止训练数据倾斜。通用多样性提示难覆写这些组合偏差；上下文属性插入更可行。

## 结论
ITTS 性别偏差具组合依赖，需成分化诊断；偏见根源更多在文本编码器先验。缓解应面向组合动态而非单维提示。

## 点评
把交叉社会线索写入可控实验，比“测 nurse 是否女声”更贴近部署。依赖声学性别分类器作代理，音色/F0 与社会性别不完全等同；提示模板由 Gemini 生成，也可能引入额外先验。


# Deterministic Prompting for Speaker-Stable Low-Resource Greek TTS

- 论文编号：2481
- 报告人：Alexandros Potamianos
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/syllas26_interspeech.pdf

## 问题

现代希腊语缺高质量单说话人语料，低资源 TTS 易损韵律、可懂度与说话人一致性。众包多说话人数据碎片化，全参微调易学成“平均声”；LLM 生成的风格提示在推理时还会引入说话人漂移。

## 方法

数据策展：WhisperX 对齐 + 置信度/时长/声学过滤，整理 CSS10、过滤后 Common Voice（约 15.5 h）与人工核验有声书（约 3.5 h 男声）。在多语言 Parler-TTS（880M）上先全参微调解码器，再用确定性提示（属性分位数分箱、固定拼接）替代 LLM 风格描述，最后在 3.5 h 单说话人数据上做 LoRA（约 25M/5% 参数）锚定身份。推理用统一 canonical 确定性提示与贪心解码。

## 实验与结果

Det.+LoRA：WER 10.7%（人类 ASR 底 7.8%，差 2.9 pp）、CER 3.7%；MOS-I 4.00（人类 4.36）、MOS-C 4.24（人类 4.30）。无 LoRA 时 LLM 提示 WER 更好，加 LoRA 后确定性提示反超（10.7% vs 21.1%）。LLM+LoRA 的 MOS-C 仅 3.56。希腊 VITS 微调未达正式评测质量。失败模式含重音错位、幻觉音节、标点–韵律不匹配。

## 结论

作者认为多语言先验 + 确定性提示 + 说话人 LoRA 是少数据希腊单说话人 TTS 的可行配方；高质量转录比堆时长更重要。局限为单一男声朗读风格与部分主观差异未达显著。

## 点评

把“提示随机性”和“多说话人平均声”拆开治理：确定性提示降条件方差，LoRA 专锚身份，二者协同才稳。客观 SIM-S 仍一般，主观侧重系统内一致性而非严格仿某参考说话人，评价口径需读清。ASR WER 对形态丰富希腊语可能低估/高估感知错误。


# DiaMoE-TTS: A Unified IPA-Based Dialect TTS Framework with Parameter-Efficient Adaptation and Reward-Driven Optimization

- 论文编号：2447
- 报告人：Ziqi Chen
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/chen26z_interspeech.pdf

## 问题

统一方言 TTS 面临数据稀缺、正字/拼音跨方言读音歧义、多方言联合训练风格平均与相互干扰；新方言仅有数小时数据时难扩展，高质量方言数据直接续训也不一定稳。

## 方法

基于 F5-TTS 的多阶段流水线：统一 IPA 前端；Stage 1–2 在普通话+多方言 IPA 数据上训练，Stage 2 在文本嵌入后加方言感知 residual MoE，并用方言分类辅助损失引导门控；Stage 3 冻结主干，仅训 LoRA 与 Conditioning Adapter，并用音高/时长微扰增广适配新方言。另用 Flow-GRPO，以 ASR WER 为奖励，在高质量川方言语料上优化 DiT 主干。

## 实验与结果

约 0.7k h 普通话 + 0.4k h 方言。消融：去 MoE 或改用 pinyin 均明显变差（pinyin 时 WER&gt;90%）。相对商业系统 WER/MOS 仍有差距（数据规模差数量级）。对成都高质量数据：Flow-GRPO 将 CD WER 从 29.25% 降至 23.93，并改善 XA/ZZ 等相关方言；直接续训改善有限甚至变差。低资源京剧念白与南京话可经 PEFT 扩展。

## 结论

作者认为 IPA + 方言 MoE + PEFT 构成可扩展统一方言 TTS；GRPO 比直接续训更能利用高质量方言数据并产生跨相关方言增益。

## 点评

IPA 统一拼音歧义、MoE 抗风格平均，问题拆分清楚。客观 WER 绑特定 ASR，方言/戏曲语音上可能偏严；与商业系统对比不公平处作者已指出。奖励仅用 WER，韵律与自然度未直接优化，是当前边界。


# SALT: Selective Allophone-Level Tokenization for Korean Text-to-Speech Synthesis

- 论文编号：2055
- 报告人：Kwangsung Kim
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kim26p_interspeech.pdf

## 问题

韩语 Hangul 虽偏表音，但正字法形态音位性强，字素≠实际发音；低资源下模型难靠隐式学习消歧。全量音位变体标注会膨胀词表、破坏 token 分布平衡，损害可学性。

## 方法

提出 Selective Allophone-Level Tokenization（SALT）：在 G2P 后的音素上选择性附加音位变体标签（如词首清化 i、腭化 j、韵尾 c）。用 Gini 与 Rényi 效率（α=2.5）筛选标签组合；优选仅区分鼻韵尾的 SALT-N（词表增幅小、效率高）。在预训练 F5-TTS（英/普）上，对文本嵌入与 ConvNeXt 全参微调，其余用 LoRA；数据为 KSS 12.75 h 与极低资源 1 h 子集。

## 实验与结果

12.75 h：SALT-N CER 3.30%、WER 11.24%，优于字素 4.74%/15.26% 与音素 3.74%/14.06%；NMOS 最高 3.10。全标签 SALT-VCP CER 反升至 6.03%。1 h：仅 SALT-N CER 低于 10%（8.19%），字素/音素/VCP 均≥10.78%。人类听感对发音错误更敏感，故 NMOS 更青睐低 CER 的 SALT-N，即便 UTMOS 略低于 VCP。

## 结论

作者认为不必改架构或堆数据，用选择性音位变体输入作归纳偏置即可提升韩语 TTS；关键是在声学消歧与 token 统计效率间取平衡。局限为单说话人小数据，未来将扩到多说话人与其他规则性强的语言。

## 点评

把“语言学先验要注入多少”量化成分布效率指标，再选最小有效标签集，比盲目全规则 G2P 更工程化。低资源增益最大，符合归纳偏置预期。依赖标准发音规则与 G2P 质量；方言/口语变体更自由时，选择性规则可能需重标定。


# G2PO: A Lightweight Lexicon-enhanced Framework for Open-Vocabulary Mandarin Polyphone Disambiguation

- 论文编号：1064
- 报告人：Feifan Chen
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/chen26i_interspeech.pdf

## 问题

普通话多音字消歧是 TTS 前端关键环节。现有 BERT 类方法参数过大难上端，且闭集分类无法预测训练未见读音；词典增强方案常需存储稠密词向量，占存储。

## 方法

提出 g2pO：用 RoBERTa-tiny（约 3.2M）编码；词典融合模块用 Trie 匹配含目标字的词，对 span 隐状态做 mean+max mix-pooling，动态构造词表示并与拼音嵌入拼接，再经注意力聚合成 lexicon prior 与增强字符状态；辅以 POS 预测；最终用加权 softmax（结合 prior 与合法拼音 mask）输出。词典仅存字–拼音映射（约 100K 词约 3MB），无需预训练词向量。

## 实验与结果

CPP 测试准确率 99.15%（3.99M 参数），优于 g2pW 的 99.08%（约 108M）；RCPP/RCPP(S) 为 99.03%/98.51%。Hard 子集（词典冲突）准确率 93.62%（随机基线 54.26%）。未见读音零样本准确率 70.79%，闭集方法基本为 0。消融显示去 lexicon adapter 掉至 98.55%。

## 结论

作者认为轻量编码器 + 动态词典融合可在极小体积下达到 SOTA，并具备开放词表泛化，适于端侧部署。

## 点评

把“词典知识”从巨大 embedding 表改成隐状态上的 on-the-fly 池化，同时用 prior 打开输出空间，同时解决体积与开放词表。Hard 子集说明模型不是简单查表。未见音依赖词典覆盖与 prior 温度设定；极低频多音字仍可能弱。


# UR-BERT: Scaling Text Encoders for Massively Multilingual TTS Through Universal Romanization and Speech Token Prediction

- 论文编号：909
- 报告人：Sangmin Lee
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/lee26h_interspeech.pdf

## 问题

多语言 TTS 文本编码器常依赖 G2P，可靠工具约仅覆盖百来种语言；纯文本预训练又缺声学线索。需在更大语言覆盖下保持音素保真与文本–语音对齐。

## 方法

提出 UR-BERT：用 Uroman 罗马化统一书写系统；BERT-base 字符级分词；预训练除 MLM 外增加 speech token prediction（STP）：从 omnilingual ASR W2V 中间层提特征，经 MMS-FA CTC 强制对齐到字符，再 k-means（256+静音）离散化为目标。预训练语料约 13K 小时、8M 句、495 语。下游冻结/微调后接 VITS。

## 实验与结果

高资源英/德/普：UR-BERT 的 MOS 分别为 4.35/3.78/3.88，优于 XPhoneBERT 与 m-PLBERT。低资源多语（含 XPhoneBERT 不支持的爪哇语等）MOS 全面最高；未见语巽他语零样本仍优于纯 VITS。消融显示 STP 多数语言提升 MOS。预训练句数仅约 XPhoneBERT 的 2.5%。

## 结论

作者认为罗马化突破 G2P 覆盖瓶颈，STP 补偿罗马化音素粗粒度，可在数据更少时扩展到数百语并保持合成质量。

## 点评

用“共享拉丁书写 + 声学 token 蒸馏”同时扩覆盖与保音素，比堆更大 G2P 更可扩展。罗马化跨语同形异音仍可能混淆，STP 是关键补偿。评测依赖多语 ASR/UTMOS，跨语偏差用相对指标缓解，但仍需留意。


# Listenability of Synthetic Speech: On the Effect of Linguistic Registers in Text-to-Speech Input

- 论文编号：894
- 报告人：Maja Jønck Hjuler
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/hjuler26_interspeech.pdf

## 问题

LLM 文本越来越多直接送入 TTS，但其语域是否适合听读未知。既有评测多关注自然度/可懂度，较少测听者加工与记忆负荷；可读性指标也不等于可听性。

## 方法

被试内设计（N=47）：四类输入经同一 Google TTS（澳式口音）合成——ART 对谈广播转写、Wikipedia Simple English（WSiE）、标准维基（WStE）、GPT-4o-mini 生成。测 AIME、NASA TLX 主观努力与线索回忆；并用可读性指标与 Biber MDA 刻画语域。

## 实验与结果

ART 努力显著最高（AIME 62.9、TLX 46.8），书面与 GPT 显著更低且彼此接近（约 25–29 / 15–18）。回忆上 WStE 最高（94.3%），ART 最低（78.7%）。MDA：ART 偏互动口语，WStE 偏正式信息文，GPT 与 WSiE 居中且接近。可读性上 WSiE 最易读，WStE 最难，GPT 居中。

## 结论

作者认为合成语音中，书面/维基源比广播对谈转写更易听；LLM 文本与维基源可听性相当，支持其作为合成输入。研究属初步，语域与话题样本有限。

## 点评

把焦点从“合成器好不好听”转到“输入语域好不好听”，对 agent/播客管线很有现实意义。对谈转写难听可能来自口语纠缠结构经 TTS 朗读后更吃力，而非“口语更自然”的直觉。样本与音色单一，外推需谨慎；也提示“为说话而写”可能比直接喂聊天转写更重要。


# Uncovering the Impact of G2P Precision on Korean TTS: A Large-Scale Statistical Validation via a Novel Morphological Engine

- 论文编号：887
- 报告人：Heejo You
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/you26_interspeech.pdf

## 问题

韩语 G2P 常用 g2pk 延迟高、词界音变不准，相当于给 TTS 喂标签噪声，拖慢收敛并伤可懂度。需可解释、高速、形态深度整合的规则引擎，并用统计严谨方式验证对下游 TTS 的影响。

## 方法

提出规则 G2P：Kiwi 分析后构建 Sentence→Eojeol→Syllable 层次，音节指针连到语素实现 O(1) 边界判定；规则专用隔离词典；按优先级迭代扫描，命中后重置到 Eojeol 首音节再评估，模拟连锁音变。下游用 96 个 VITS（字素 / g2pk / 所提引擎各 32）训 500k 步，去掉 |z|&gt;1.96 离群后做 ANOVA。

## 实验与结果

G2P：平均 3.14 ms vs g2pk 14.98 ms；句级准确率 85.7% vs 27.2%，CER 0.002 vs 0.021。TTS：Proposed 组 CER 显著优于另两组；g2pk 与字素无显著差异。PESQ/WV-MOS 组间不显著，说明可懂度提升不以牺牲声学自然度为代价。训练曲线显示高质量 G2P 更早收敛。

## 结论

作者认为高精度规则 G2P 同时提升速度、可懂度与训练效率；不准确 G2P 不优于直接用字素。剩余错误多来自同形多义与分析器窗口限制。

## 点评

用大规模重复训练 + ANOVA 把“G2P 准不准有没有用”做成可复现的因果证据，方法学上扎实。规则引擎对连锁音变友好、可调试。同形歧义仍是上界；未覆盖神经 G2P/LLM 前端对比，但作为可引导数据的确定性基线价值高。


# Phonikud: Overcoming Phonetic Underspecification for Hebrew Text-To-Speech

- 论文编号：604
- 报告人：Morris Alper
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kolani26_interspeech.pdf

## 问题

现代希伯来文书写常省略元音与重音等语音细节，即便加 nikud 仍有重音、shva、不规则词等歧义；现有 TTS/评测用无标音 ASR，对元音与重音错误“看不见”。

## 方法

Phonikud：冻结 DictaBERT 标音器，加轻量头预测增强符号（非末音节重音、发声 shva、不规则词标记），再规则转全规格 IPA。训练用 IsraParlTweet 半自动伪标签 + 人工校正高频词。发布约 2 h 双说话人 ILSpeech（音频–文本–专家 IPA）；训 Whisper-small 作 audio-to-IPA 评测 ASR。下游用 Phonikud IPA 微调 Piper/StyleTTS2。

## 实验与结果

G2P（ILSpeech 子集）：WER 17.4%、CER 3.8%，优于实时标音器与多语 G2P，接近 Gemini。TTS：StyleTTS2 WER/CER 35.2%/8.9%，优于开源基线，接近专有系统；CMOS 相对 Robo-Shaul 自然度 +1.3。重音难例：全方法 WER 3.2%、EM 77.0%，显著优于去重音与 Robo-Shaul。消融：去增强标音或元音均伤性能。

## 结论

作者认为补全语音欠规格说明后，小本地模型可接近大专有系统；框架、数据与评测基准开源。局限继承基座标音器错误与书面对白语体差异。

## 点评

同时修“生成前端”和“评测盲区”：没有 audio-to-IPA，希伯来 TTS 改进难以量化。轻量 adaptor 保留原标音能力再补缺口，工程干净。伪标签+人工校正可扩展，但对口语变体与基座错误仍敏感。


# Speech-Worthy Alignment for Japanese SpeechLLMs via Direct Preference Optimization

- 论文编号：976
- 报告人：Mengjie Zhao
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/zhao26d_interspeech.pdf

## 问题

SpeechLLM 常继承书面体输出（markdown、列表、冗长复杂句），日语口语与书面在敬体、句末助词、句法复杂度上差距大，不利于 TTS 与听懂。尚无可靠日语 speech-worthy 评测资源。

## 方法

在 Whisper 编码器 + Sarashina-7B 架构上，预训练对齐模态后，用 DPO+SFT 偏好对齐：偏好口语化、不偏好书面体。偏好数据来自翻译后的 SpeechPref、InstructS2S-200K 滚动采样 + DeepDialogue。构建 SpokenElyza：过滤 ELYZA 中不适口语任务，风格改写并经母语者听测校验。评测用 LLM-as-judge 与词数/依存深度/不可发音字符比例。

## 实验与结果

SpokenElyza：预训练 2.91 → DPO+SFT+口语系统提示 3.44（约 +18%）；Elyza 书面评测从 3.97 微降至 3.78。表面形式：词数约 326→78，NV% 13.46%→3.24%，依存深度降至约 4.97。单独提示可大幅缩短，与偏好训练互补。

## 结论

作者认为偏好对齐可显著提升日语 SpeechLLM 的可听合成友好度，同时大体保留书面指令跟随；SpokenElyza 开源以支持后续研究。

## 点评

把“能听懂的回复”从文本 LLM 对齐迁到 SpeechLLM，并补日语基准，针对语体落差。依赖 LLM 改写与 LLM-as-judge，可能与真实听感不完全一致；书面分略降是风格权衡。偏好数据经翻译，日语特有礼貌策略是否充分覆盖仍待验证。


# Knowing What to Stress: A Discourse-Conditioned Text-to-Speech Benchmark

- 论文编号：2743
- 报告人：Avihu Dekel
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/turetzky26_interspeech.pdf

## 问题

同一句子因语篇语境不同需强调不同词（对比焦点），现代 TTS 虽能显式控重音，但能否仅从语境推断并实现恰当词级重音尚不清楚；缺对比控制基准。

## 方法

提出 CAST：对比语境对——相同目标句 + 两种语境，语义上要求不同重音词。用结构化提示生成并由多模型裁判过滤；113 对（226 项），位置与语用类型均衡。评测系统在无语境 / 拼接语境 / 指令语境 / 显式重音下合成，用 WHISTRESS 检测重音，报告 Hit、Pair-Contrast、Pair-Correct。另释放大约 10k 合成训练资源。

## 实验与结果

各系统 Pair-Correct 接近 0；提供语境（拼接或指令）相对无语境无明显提升。显式重音上界更高（如 CosyVoice3 Pair-Contrast 40.3、Pair-Correct 10.6），但仍不可靠。人类校验：标签多数一致率高；检测器与人一致程度落在听者间一致性范围内。文中亦报告文本 LM 能较好从语境恢复目标重音，而 TTS 难落地到声学。

## 结论

作者认为当前 TTS 普遍不能可靠做语篇条件重音；实现能力（显式）与推理能力（语境）之间存在鸿沟。CAST 与流水线开源以推动语境感知韵律。

## 点评

用“同句异境”设计干净隔离语境效应，Pair-Correct 严格卡死句内偏置。结论对下一代对话 TTS 很刺耳但证据清楚。自动检测器 κ 不高反映突显感知本身主观；基准规模中等，扩展合成语料可支撑训练但评测需防污染。


# ARCHES: An Agent-Based Refinement Cycle for Hierarchical Synthesis of Sound Effects for Variety Shows

- 论文编号：561
- 报告人：Li Liu
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/lei26_interspeech.pdf

## 问题
综艺音效依赖人工剪辑，成本高、难规模化；通用文本/视频到音频模型偏现场自然声（diegetic），难覆盖风格化、喜剧化、稀有签名音效，且时序与情绪控制不足。

## 方法
ARCHES 多智能体迭代：Planning 检测需增强的事件 → Generation 条件合成 → Checker 评估后经 AXIS 路由到时序/情绪等细化智能体。AURA 用 Qwen2-Audio 多模态检索 26k+ 专业音效库作上下文示例；CEB 记录成功交互作模板捷径。生成骨干基于 MultiFoley，高层规划多用 Gemini-2.5 Pro。自建 VSSE-Bench（约 1000 集综艺切分）评测。

## 实验与结果
相对 MMAudio、Kling-Foley、HunyuanVideo-Foley、FoleyCrafter：LSD 0.77、OD 0.048 s、FAD 7.04、A-MOS 2.68 及主观 MOS-S/T/E（4.04/4.54/4.46）均最优。消融：无 AURA 损害多样性/FAD；无 AXIS 时序误差大增；无 CEB 略降。换 MLLM 骨干时 Gemini-2.5 Pro 最好，开源 Qwen3-VL 仍可用。

## 结论
检索增强 + 智能路由细化 + 经验库可使综艺风格音效在保真、同步与情绪匹配上显著优于通用 V2A；未来将降延迟、减对底层模型依赖并扩展跨模态生成。

## 点评
把后期剪辑流程 agent 化，切中综艺非叙境音效痛点；新基准与音效库是实质贡献。系统强依赖闭源/强 MLLM 与外部库质量，消融已显示去掉检索或细化回路即掉点；客观 LSD/FAD 对“喜剧恰当性”覆盖有限，主观三项是更关键证据。


# Scalable Direction-Following TTS via Voice Impression-Guided Pseudo Triplet Construction

- 论文编号：919
- 报告人：Kenichi Fujita
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/fujita26_interspeech.pdf

## 问题
导演式“相对上一遍如何改”的 direction-following TTS 需要 (参考句, 指导语, 修改后句) 三元组，但大规模语料几乎没有这种相对风格配对。作者要可扩展地构造伪三元组并学习说话人保持的相对风格变换。

## 方法
用印象可控零样本 TTS 生成同脚本 pre/post 句对，经说话人一致性与语速过滤后估计 13 维印象向量差 ΔI，由 LLM 生成自然语言指导语，构成伪三元组。在固定骨干 TTS 的语音嵌入空间上训练方向条件风格精炼器（整流流匹配预测加性嵌入偏移）。另采集约 8.9 小时专业配音真实三元组。对比仅伪数据、仅真实、混合及不同说话人规模子集。

## 实验与结果
伪数据约 35 万三元组（127.6 小时）。客观：精炼不损害 UTMOS；伪数据与 Full 比仅真实录制在未见说话人上更稳地保持说话人相似。主观：Recorded AlignMOS 最高但 SMOS 较低；Pseudo-all SMOS 高而对齐略保守；Full 折中。伪数据 F0 变化幅度小于专业录音，解释了更保守的调制。

## 结论
伪三元组 alone 即可稳定做说话人保持的相对修改；与真实数据结合可提升方向对齐同时维持身份稳健。伪数据韵律变化偏小是当前局限。

## 点评
把“相对指导”从绝对风格标签中拆出来，并用印象差驱动 LLM 写导演语，数据管线可扩展。伪数据依赖印象可控 TTS 与同一印象估计器，存在分布收缩风险；客观对齐也用该估计器作代理，需主观 AlignMOS 交叉验证——作者已做，但伪–真韵律差距仍制约表现力上限。


# Poly-InstructTTS: Learning In-the-Wild Expressive Speech Synthesis from Open-Ended Instructions

- 论文编号：930
- 报告人：Junhui Zhang
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26m_interspeech.pdf

## 问题
开放自然语言指令控制细粒度表情仍难，因语料多为中性朗读，且许多零样本系统把参考音频送入 GPT 易与指令风格冲突（style leakage）。

## 方法
从影视媒体构建约 1000 小时指令语料：切分去噪、ASR/说话人分离/副语言标签、字幕对齐，再用多模态 LLM（Gemini）三阶段生成上下文摘要、属性与自然语言指令。模型为 prompt-free GPT（属性型 thinking tokens：性别/强度/风格/口音）+ CosyVoice3 式 FM 仅在声学侧注入音色；另有带 Speaker ID 的指令条件说话人 SFT。扩展 InstructTTSEval 测试集覆盖口音、极端情绪、非主流风格等。

## 实验与结果
相对多开源/闭源基线，RP 等指令指标与 I-MOS 强（基测 I-MOS 3.81 最高）；WER 中等，作者归因于野生声学与标签噪声。去掉 thinking tokens 主观下降；外接指令编码器无增益。SFT 相对基座提高人格一致性 P-MOS，但 I-MOS 略降。

## 结论
野生影视指令数据 + prompt-free GPT/thinking tokens/FM 音色注入可提升开放指令表现力；说话人 SFT 可把控制迁移到指定人设。未来需平衡表达力与稳定，并改进 FM 与参考无关音色。

## 点评
数据管线与“风格走 GPT、音色走 FM”的分工直接针对泄漏问题；扩展评测集有社区价值。原始影视数据因版权未公开，可复现性依赖自建语料；表达力提升伴随 WER 上升也显示指令后训练的稳定性代价。


# Spiking Vocos: An Energy-Efficient Neural Vocoder

- 论文编号：1086
- 报告人：Yukun Chen
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/chen26j_interspeech.pdf

## 问题
频域声码器如 Vocos 算力轻但仍非真正为低功耗优化；直接把 ANN 换成 SNN 常因二值脉冲信息瓶颈与时序建模不足而掉点。

## 方法
Spiking Vocos：在 ConvNeXt 点卷积前插入 PLIF 神经元，并用幅度捷径 |Zin|⊙Zout 保留幅值；自架构蒸馏对齐中间特征与幅相谱（含抗缠绕相位损失）；每块加入 Temporal Shift Module 融合过去/当前/未来通道。在 LibriTTS 训练，对比 ANN Vocos 与不同步数/消融。

## 实验与结果
4 步 + TSM + 蒸馏：UTMOS 3.74（ANN 3.82），PESQ 3.45；主观 MOS 3.69 接近 Vocos 3.80。理论能耗约 ANN 的 14.7%（>6.8× 能效）。单独 TSM 或蒸馏均可显著回升 4 步基线；8 步更接近 ANN 但延迟加倍。

## 结论
幅度捷径、自蒸馏与 TSM 协同可使脉冲频域声码器在感知质量接近 ANN 的同时大幅降能耗。

## 点评
把 SNN 约束对准声码器瓶颈（点卷积算力、幅值丢失、因果时序盲区）很对症。能耗为 45nm 理论估算，真实芯片部署与延迟–质量权衡仍需验证；PESQ 与主观差距也提示脉冲量化对信号级指标更敏感。


# Stabilizing Instruction Supervision for Instruct-TTS via Controllable Diversification and Drift Filtering

- 论文编号：1227
- 报告人：Yizhong Geng
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/geng26b_interspeech.pdf

## 问题
Instruct-TTS 常用 LLM 把结构化标签改写成自然语言指令，但无约束改写超过 40% 存在语义漂移（执行化、角色扮演、改属性），污染监督并削弱泛化；单纯扩多样性与单纯过滤也无法兼顾覆盖与保真。

## 方法
数据中心稳定配方：(1) 音高/语速/音量扰动 + 模板属性提示做属性对齐监督；(2) 约束人设×句法×属性槽位的可控多样化改写；(3) 异族 LLM 验证器打分投票过滤三类漂移。在 CosyVoice 2 上对中文约 90h 语料做 SFT，评 InstructTTSEval（中文）APS/DSD/RP。

## 实验与结果
约束改写使漂移 40.4%→15.4%。完整配方指令跟随平均准确率 56.4%（无 SFT 34.5%，朴素 SFT 51.0%），NR/CMOS 均 4.16。消融：去漂移过滤伤害最大（→48.9%）；去多样化与去属性监督亦降点；属性监督对音高/语速/音量 APS 增益最大。

## 结论
指令监督不稳定主要是数据质量问题；覆盖扩展、漂移过滤与属性对齐三者互补，过滤是最大单项贡献。漂移分类或可推广到其他指令生成任务。

## 点评
把 TTS 标签改写中的失败模式显性分类并量化，比“再换模型”更切中要害。评测依赖 Gemini judge，作者用多模型族缓解自评估偏差；情感维度上朴素 SFT 有时更高，说明过滤也可能去掉部分有用的情绪描述，需权衡保真与覆盖。


# Improving Stable Speech Synthesis Post-Training with ChatScorer and Margin-Based Preference Construction

- 论文编号：1881
- 报告人：Wenhuan Lu
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/niu26c_interspeech.pdf

## 问题
Codec TTS 后训练常把 CER/SIM 等异构指标融成标量奖励，候选分数分不开，偏好监督模糊，且难压制明显“机器感”对话输出。

## 方法
对每条提示采样多候选，用 CER+SIM+ChatScorer 融合排序；ChatScorer 为 WavLM+轻量 Transformer 的高斯打分头，并用 GRL 抗说话人泄漏。仅保留质量间隔足够大的组：正样本需满足 CER/SIM/Chat 阈值，负样本至少两项差，并按 margin 抽中间样本，构造 DPO / Rank3/5DPO 数据。对比 GRPO。对话式长文本提示约 2000 训 / 500 测。

## 实验与结果
Rank3DPO：CER 1.17%、SIM 失败率 0.10、BadRate 2.44%，优于 SFT/DPO/GRPO。Margin 构造优于直接按融合分选；加 ChatScore 对 CER 影响小但大幅降 BadRate 并抬高 MOS。ChatScorer 与人类 A/B 一致性高于 DNSMOS/UTMOSv2。

## 结论
辅助 ChatScorer + margin 偏好构造可把嘈杂多指标信号变成更可学监督，提升生成稳定性并抑制不良对话输出，同时保持可懂度与说话人相似。

## 点评
问题诊断（弱分离→模糊监督）清晰，稳定性指标（组失败率、BadRate）比只看均值 CER 更贴后训练目标。过滤丢弃大量提示（DPO~40%，RankDPO 更高）以换可学性；GRPO 未同用 margin 过滤，对比不完全对等。


# Accent-Emotion Entanglement in LM-Based Text-to-Speech Systems

- 论文编号：2749
- 报告人：Matthew Hayden
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/hayden26_interspeech.pdf

## 问题
零样本 TTS 常靠说话人相似度（SSM）宣称接近真人，但 SSM 可能掩盖口音问题。作者在 CosyVoice2 指令控情时观察到口音被意外改变，称之为 accent–emotion entanglement，需系统刻画并改进评测。

## 方法
以 CosyVoice2（指令“Make this sound x”+情绪参考）与 MaskGCT（仅情绪参考）为案例，在 MEAD 的 happy/angry/neutral 上合成。主观：口音 SMOS（30 名多国英语 L1）。客观：GenAID 口音嵌入 UMAP、到质心余弦距离、口音分布熵。多说话人扩展客观分析。

## 实验与结果
CosyVoice2 口音 SMOS 跨条件约 1.17–4.13、方差大；MaskGCT 多在约 3.4–4.3 且更稳。UMAP 显示 CosyVoice2 扩散到印巴/英爱/东亚非裔等区域，MaskGCT 紧靠北美参考。各说话人–情绪下 CosyVoice2 到质心距离均更大。两系统原报告 SSM 接近，但口音行为迥异。

## 结论
情感条件可诱发口音幻觉，标准 SSM 不足；应常规加入口音主观与针对性客观指标。作者推测根因可能在指令微调数据标注/分布，但因训练数据未公开无法确认。

## 点评
用“SSM 相近却口音分裂”的对照有力说明评测盲区，且点出情感–口音纠缠的刻板印象风险。案例限于两模型与有限说话人/句子；对 CosyVoice2 成因仍是推断。贡献主要在问题定义与评测范式，而非修复方法。


# How Do Instructions Shape Speech? Cross-Attention Attribution for Style-Captioned Text-to-Speech

- 论文编号：2805
- 报告人：Nityanand Mathur
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/mathur26_interspeech.pdf

## 问题
风格字幕 TTS 用自然语言控音色，但单个词如何影响声学仍不清楚，妨碍诊断失败与改进可控性。图像域有 DAAM，语音尚缺等价框架。

## 方法
将 DAAM 适配到 CapSpeech（T5 风格字幕 + 流匹配 DiT）：在 25 层×24 ODE 步钩取交叉注意力，聚合为每 token 时序热图。对 120 风格字幕×30 文本约 3600 组合分析，分 Style/Content/Function 类，度量时序方差、峰均比、熵，以及与 F0/能量相关，并看层–步重要性。

## 实验与结果
风格词时序方差显著低于内容/功能词（p≪0.001，d=−1.16），呈全局调制；风格注意力与 F0/能量相关且语义一致（如 “loud”–能量 r=+0.64）。风格条件在早期 ODE 步与深层更强（早期相对后期约 5.2× 衰减）；注意力熵在第 17 层最低并与风格重要性峰重合。

## 结论
首次显示风格字幕在语音扩散/流匹配中的交叉注意力机制：风格全局、内容更局部，条件作用呈层–步层次。可为诊断与可控编辑提供归因工具。

## 点评
把 DAAM 迁到时序 mel latent，并做大规模 token 统计，解释性强。归因基于注意力作为忠实代理的假设，未做因果干预（如遮挡/改写 token）验证；仅针对 CapSpeech 架构，换其他条件注入方式时模式可能不同。


# Beyond Two-stage Diffusion TTS: Joint Structure and Content Refinement via Jump Diffusion

- 论文编号：2875
- 报告人：Jiabao Ai
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ai26b_interspeech.pdf

## 问题
扩散/流匹配 TTS 中，两阶段固定对齐易塌向平均韵律；单阶段无显式时长又易对齐不稳。需要在同一过程中联合演化离散时序结构与连续频谱内容。

## 方法
跳跃扩散：前向同时删帧（保护各音素首帧）与加噪；反向用 Location Predictor 选插入槽、Content Predictor 填内容，再做标准去噪。提出 Upsample–Diffuse–Downsample（UDD）以复用固定维预训练 U-Net；One-shot 退化为用分类时长替代 Grad-TTS 回归时长预测。冻结 Grad-TTS 编码器与扩散骨干，在 LJSpeech 训练跳跃预测器。

## 实验与结果
One-shot：WER 3.37% vs Grad-TTS 4.38%，UTMOSv2 略升。直接变维 TDD 最差。UDD 在匹配目标时长下 MCD/F0 有竞争力。0.75× 慢速 OOD：Grad-TTS 近似均匀拉伸，UDD 提高静音占比（如 Argmax 静音比 9.63% vs Grad-TTS 6.38%）并略降 WER，呈现自适应停顿。

## 结论
分类时长与跳跃–扩散联合细化可缓解均值韵律，并在非常规总时长下更自然地插入停顿；UDD 使变长结构与固定维网络兼容。

## 点评
把“时长多模态”写成插入槽分类，比 MSE 时长更贴停顿等稀有事件。主表最优往往是 One-shot 而非完整迭代 UDD，说明联合细化收益仍场景依赖；实验限 LJSpeech 与 Grad-TTS 骨干，对更强单阶段流匹配基线的相对优势待证。


# PhonemeCVAE: Contrastive Latent Clustering with Class-Conditioned Priors for Controllable Phoneme Interpolation

- 论文编号：2277
- 报告人：Nina Goes
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/goes26_interspeech.pdf

## 问题
高质量 TTS 内部表征难解释，细粒度音素级编辑（如 /s/–/f/ 插值）常受限于离散音素表示，难以在连续空间平滑变换。需要结构化、可插值的音素潜空间。

## 方法
PhonemeCVAE：β-VAE 为每类音素学习条件高斯先验；编码器用时长感知高斯下采样 + Conformer 得音素 token，解码器上采样 + PostNet；辅以监督对比损失促进类内紧致、类间分离，并含时长预测与对抗/特征匹配损失。推理时在最小对立对的类中心间线性插值替换对应 token，再解码与 HiFi-GAN 声码。

## 实验与结果
在 LJSpeech、LibriSpeech、CMU ARCTIC 等上，先验+对比相对消融显著提升 silhouette 与类间分离（UMAP 更清晰）。听测（N=18）：沿 α 插值可感知音素连续变化；编辑音自然度/质量均值约 3.14/3.22，略低于原音 3.45/3.55。

## 结论
类条件先验与对比正则形成可跨数据集泛化的音素潜拓扑，支持可控插值编辑且大体保持合成质量，有望服务发音清晰与治疗等场景。

## 点评
把音素编辑写成“在先验中心间插值再 patch token”，接口直观。依赖 MFA 对齐与最小对立对听测，对协同发音与跨说话人稳健性仍待更大规模评测；编辑质量略低于原音，说明重建–可编辑性折中仍在。


# TAP-ETS: Time Aligned Phoneme Guiding for EMG-to-Speech Synthesis

- 论文编号：3485
- 报告人：Dongyub Han
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/han26f_interspeech.pdf

## 问题
EMG 到语音（ETS）常把音素分类仅作辅助损失，语言信息未显式条件化生成，外部文本/音素纠错也难回注到帧级声学合成。

## 方法
TAP-ETS：训练时以帧级音素嵌入经交叉注意力注入 mel 解码器（EMG 特征为 Q，音素为 K/V），并保留辅助音素分类。推理时用 TAP 精炼：把合并音素/文本纠错（如 MONA-LISA+GPT）经 Levenshtein 时长重分配与掩码 Transformer 再对齐到 EMG 帧，无需改合成骨干。在 Gaddy silent EMG 基准评测。

## 实验与结果
相对 Gaddy/Scheck，Acc 73.03%、PER 15.59%、CER 11.15%、WER 19.77%（基线 WER 约 25–26%），达文中所称 SOTA。消融：Lev 与掩码精炼互补；帧级音素条件优于文本或合并序列条件。

## 结论
帧对齐音素条件 + 可插拔精炼管线可显著提升静默 EMG 可懂度，并使任意音素/文本纠错模块无缝接入。

## 点评
把“音素从监督变成可控条件”是对 ETS 控制力的关键升级。精炼依赖外部强纠错（识别 WER 12.70%）与 DTW/MFA 对齐质量；测试集仅 98 句静默样本，规模有限。


# Semantic-VAE: Semantic-Alignment Latent Representation for Better Speech Synthesis

- 论文编号：533
- 报告人：Zhikang Niu
- 程序：Wednesday 30 September 2026 / Speech Synthesis: Speech Features, Codec and Representations
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/niu26_interspeech.pdf

## 问题
连续潜在 TTS 中，高维潜在重建与说话人相似度好但可懂度差，低维相反，形成信息瓶颈式权衡。

## 方法
提出 Semantic-VAE：在 VAE 潜在上与 SSL 表征做语义对齐（如余弦相似度约束），使高维空间保留声学细节同时结构化语义。编码器将 16 kHz 下采样至约 40 Hz 潜在。用于下游零样本/潜在扩散等 TTS，对照不同潜在维度配置。

## 实验与结果
Semantic-VAE 特征在 LibriSpeech-PC test-clean 上达约 2.10% WER 与 0.64 说话人相似度，缓解高维可懂度崩塌。相对未对齐高维潜在，可懂度提升同时保持较好重建/相似度。

## 结论
SSL 语义对齐可打破“高维好听但听不清”的困境，为连续潜在 TTS 提供更稳表征。

## 点评
把瓶颈诊断清楚并用对齐直接干预潜在几何，比单纯调维度更 principled。主数字集中在单一测试集；与离散 codec-LM 路线的系统对比深度取决于正文完整表。


# One-Step Token-to-Waveform Generation with MeanFlow in Latent Space

- 论文编号：791
- 报告人：Zheqi Dai
- 程序：Wednesday 30 September 2026 / Speech Synthesis: Speech Features, Codec and Representations
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/dai26c_interspeech.pdf

## 问题
LLM 式 TTS 依赖语义 token 时，Token2Wav 解码器既要恢复韵律/音色，又要满足低延迟。主流 flow-matching 解码器质量高，但推理需多步 ODE 积分，延迟大；直接在波形空间做一步 MeanFlow 又因序列过长而不稳、吃显存。

## 方法
两阶段流水线：先用轻量波形 VAE 把 24 kHz 语音压到与语义 token 对齐的 25 Hz 潜变量 `z`（潜维 `D∈{8,16,24}`），再用条件 1D DiT 在潜空间做 MeanFlow，学区间平均速度场，推理时一次前向从噪声得到 `z_gen`，再由确定性 VAE 解码器还原波形。条件为 CosyVoice2 风格语义 token（25 Hz、单码本）与 CAM++ 说话人嵌入。为缓解生成潜变量与 VAE 训练分布不一致，在不改变推理路径的前提下做两类精炼：冻结生成器只微调解码器，或端到端联合微调（波形域 MR-STFT + 对抗 + feature matching）。

## 实验与结果
在 LibriTTS 训练、LibriSpeech test-clean 评测。最佳配置为 140M DiT、`D=24`、Joint-FT：相对 CosyVoice2 的 10-step Token2Wav（RTF 0.0775），端到端 RTF 降至 0.0046（约 17×）；WER 3.41%、SpkSim 0.932、UTMOS 3.64、MOS 3.85（基线 WER 3.18、MOS 4.05）。消融显示潜维增大改善质量；140M 略优于 600M；No-FT→Decoder-FT→Joint-FT 感知质量逐步提升。

## 结论
潜空间 MeanFlow 可在固定一次生成器+一次 VAE 解码的代价下实现近似多步 Token2Wav 的可懂度与感知质量，并显著降低 RTF；剩余差距主要来自 token→潜变量生成而非波形解码。

## 点评
核心是把一步生成放到短、低维潜序列上，用 MeanFlow 的平均速度回避多步积分，再用 decoder/joint 精炼吃掉分布 mismatch。路线对实时/端侧 Token2Wav 很务实；脆弱点在于一步大跨度对平均速度估计敏感（更大 DiT 未必更好），且条件仍绑定 CosyVoice2 tokenizer 与说话人编码器，跨 token 体系可迁移性未在正文验证。


# CycleCodec: Distillation-Free Factorized Neural Speech Codec via Cycle-Consistent Speaker Swapping

- 论文编号：806
- 报告人：Yang Ai
- 程序：Wednesday 30 September 2026 / Speech Synthesis: Speech Features, Codec and Representations
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/zheng26_interspeech.pdf

## 问题
因子化神经语音编解码常靠 ASR/SSL 蒸馏拆开内容与说话人，低资源或未见语言缺可靠 teacher；无蒸馏的 TiCodec 等又易残留跨流泄漏，可控合成不稳。

## 方法
在 TiCodec 骨干上从零训练：帧级离散时变码 `q`（单码本大小 256，约 0.6 kbps）承载内容/韵律，全局连续嵌入 `g` 承载说话人。架构上缩小码本容量抑制时变流泄漏，并用可学习 query 的 Transformer 聚合器（N=8、L=4）+ 说话人对比损失强化 `g`。核心自监督是 cycle-consistent speaker swapping：批内置换配对，用源 `q`+目标 `g` 合成 swap 语音，再编码约束 `q_swap≈q_src`、`g_swap≈g_tgt`，并用源 `g` 解码回 cycle 语音施加 mel 重建损失。两阶段训练：先 `L_codec+L_spk`，再冻结编码器与量化器，对解码器做 cycle 微调。

## 实验与结果
LibriTTS（24 kHz）训练；重建与零样本 VC 在英语（LibriTTS）、普通话（Seed-TTS-ZH）、越南语（VieNeu-TTS）上评测。重建上 CycleCodec 全面优于 TiCodec，PESQ/STOI/V/UV F1 也优于蒸馏式 LSCodec，但 WER 仍高于 LSCodec。零样本 VC：英语上逊于 LSCodec、优于 TiCodec；跨语言时 CycleCodec 的 WER 低于 LSCodec（如 Seed-tts-zh：13.488 vs 15.426；VieNeu：25.706 vs 31.606），说话人相似度仍具竞争力。消融显示去掉 cycle 对内容保持伤害最大；迭代 VC 中 CycleCodec 的 WER 漂移小于 TiCodec。小规模听感：英/中 VC 自然度 MOS 相对 TiCodec 提升。

## 结论
不依赖预训练 teacher，仅靠编解码内部的 cycle 说话人交换与容量/对比约束，即可在跨语言设定下获得更稳的说话人–内容解耦与可控合成。

## 点评
抓住的是“低资源因子化”里 teacher 不可用时，用 codec 自洽的 swap→再分析→swap-back 代替外部语义监督。相对蒸馏路线，跨语言内容保持更稳；相对纯重建指标，WER 仍偏弱，说明内部约束对细粒度声学细节友好、对 ASR 级内容对齐未必最强。依赖说话人标签做对比损失，且第二阶段冻结分析路径，解耦上限仍受第一阶段表示质量制约。


# Low-Framerate Speech Tokenization via Two-Stage Latent Patch Modeling

- 论文编号：2863
- 报告人：Théodor Lemerle
- 程序：Wednesday 30 September 2026 / Speech Synthesis: Speech Features, Codec and Representations
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/lemerle26_interspeech.pdf

## 问题
低帧率语义语音 tokenizer 对下游 TTS 很重要，但通常要把波形压缩、对抗训练与语义监督绑在一起训，算力贵、难在消费级 GPU 复现；离散大码本/多层量化也易塌缩、下游建模复杂。

## 方法
提出两阶段连续编解码 Z-CODEC。第一阶段 WavVAE：轻度压缩（100 Hz、瓶颈维 24），SNAC 式编码器 + Vocos 风格 ConvNeXt/iSTFT 解码，用对抗目标吸收波形建模难度。第二阶段 PatchAE：把 `z` 按 patch（8 帧）压到 12.5 Hz 的 `˜z`（连续 VAE 或 FSQ，约 1.1 kbps），用潜空间 flow matching 从 `˜z` 重建高帧率 patch；在 velocity head 上对 WavLM-large 第 6 层特征做余弦语义对齐。下游 TTS 为 encoder–decoder Transformer + 轻量 MLP 预测到 PatchVAE 潜空间的速度场。整套可在单卡 RTX 4070/4090 上训练。

## 实验与结果
数据为 HiFiTTS2 + LibriTTS。LibriTTS test-clean 上，WavVAE 重建 PESQ 达 4.14；完整 Z-CODEC（VAE/FSQ）在 12.5 Hz 上与 Mimi、Higgs、XY-Tokenizer 等可比（FSQ：PESQ 2.23、UTMOSv2 3.05、dCER 0.59%）；去掉 WavLM 监督后 dCER 升至 1.49%。MUSHRA 主观质量与 Higgs 同属前列。TTS（0.24B）CER 1.1%，NMOS/SMOS 与更大参数的 F5-TTS、SparkTTS 接近。编解码在 RTX 4090 上约 130× 实时。

## 结论
分阶段把对抗波形建模与低帧率语义压缩解耦，可在消费级硬件上得到高质量低帧率（连续/离散）tokenizer，并支撑可训练的连续潜空间 TTS；当前非因果、仅英语。

## 点评
关键设计是“先把波形难点锁在高帧率 VAE，再在潜空间做 patch 压缩+FM+SSL”，用训练可负担性换端到端一体优化。强在复现门槛与低帧率质量；脆弱点是第二阶段解码依赖多步 ODE、非因果限制流式，且语义对齐质量高度依赖 WavLM 蒸馏。


# Transcript-Free Flow-Matching Text-to-Speech via Speech Feature Conditioning

- 论文编号：3190
- 报告人：SooHwan Eom
- 程序：Wednesday 30 September 2026 / Speech Synthesis: Speech Features, Codec and Representations
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/eom26_interspeech.pdf

## 问题
F5-TTS 等 flow-matching 零样本 TTS 推理需参考音频转写（常靠外部 ASR）；对构音障碍、口音等非典型说话人，ASR 易错，且即便用 oracle 转写，文本条件与参考 mel 中非典型声学也可能冲突，把异常模式灌进合成。

## 方法
提出 RTFree-F5：冻结 WavLM-Large 提取参考语音连续特征，经两层 MLP 投影器映射到 F5-TTS 原文本条件空间，与目标文本经文本编码器得到的特征在时间维拼接，替代原先的参考转写条件；参考 mel 仍作 unmasked 声学上下文。两阶段训练：先只训投影器对齐空间，再联合微调投影器与 DiT 骨干；训练用同说话人跨句对。推理无需参考转写。

## 实验与结果
基于 F5-TTS v1 Base，LibriTTS 训练。典型说话人（LibriSpeech-PC / SeedTTS）：Stage 2 的 WER/MOS 不低于或优于 oracle/ASR 基线（如 LibriSpeech-PC：WER 1.77%、MOS 4.13）。非典型：SAP 构音障碍上 WER 从原始 24.62%、oracle 基线 20.71% 降到 10.39%，MOS 2.16→2.85，但 SIM 0.60→0.50；L2-ARCTIC 上 WER 10.75%→1.44%，优于 oracle 2.00%。仅 Stage 1 在 SAP 上几乎失效（WER 90%）。

## 结论
用 SSL“潜在文本”替换参考转写，可复用预训练 F5-TTS，显著提升非典型说话人可懂度与自然度，并去除参考转写依赖；说话人相似度与可懂度之间存在权衡。

## 点评
问题抓得很准：infilling 里参考文本带来的规范音素期望会与病理/口音声学打架。用与参考声学同分布的 SSL 条件化解冲突，同时保住目标文本控制。脆弱处是 SIM 下降、训练仅在健康 LibriTTS 上做跨句对，以及依赖冻结 WavLM 对非典型语音的表示质量。


# Unified Prosody Restoration Using Diffusion Models for Controllable Text-to-Speech Synthesis

- 论文编号：2942
- 报告人：Yuki Ito
- 程序：Wednesday 30 September 2026 / Speech Synthesis: Speech Features, Codec and Representations
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ito26_interspeech.pdf

## 问题
显式韵律可控 TTS 常要帧级 pitch/VUV/energy，用户难指定又要符合语言（尤其日语音调）的合法结构。已有工作只覆盖局部补全或平滑细化等单一场景，且常预测音素平均韵律、损失帧内细节。

## 方法
把韵律恢复统一为线性逆问题：由退化算子 `H` 从干净韵律得到易指定的退化输入。覆盖五类任务：Inpainting、从平滑/分段平均细化（Ref-S/Ref-A），以及掩码+粗化组合（InpRef-S/InpRef-A）。提出两类扩散韵律恢复器（DPR）：监督版按模拟退化训练并条件于退化 ID；无监督版只在干净韵律上训条件 score，推理用 DDRM（非盲）或 GibbsDDRM（盲平滑核）。恢复结果再送入可条件于 pitch/VUV/energy 的 FS2+flow-matching 声学模型与 HiFi-GAN。

## 实验与结果
日语情感语料 IH（约 31h）与 JVNV。相对 Det/CVAE 基线，Diff-S 与 Diff-U 在多数任务上降低 log F0/energy 误差并改善 PA-ER；主观韵律自然度上 Diff-U-B（InpRef-S）达 4.74、Diff-S 约 4.21–4.22，明显高于基线约 3.4–3.5。JVNV 上趋势一致。盲任务中已知真实退化时 Diff-U-NB 作 oracle 更优。

## 结论
扩散先验可在统一框架下从部分/粗化/二者兼有的输入恢复帧级合法韵律，监督与无监督 DPR 均优于非扩散基线，并更好保持口音相关结构。

## 点评
把多种用户交互统一成线性退化+扩散求解，对可控 TTS 产品流程很实用；无监督路线用逆问题采样扩展未见退化模式。脆弱点在于评价多用 GT duration、日语情感数据规模有限，且盲设定仍假设平滑核参数化，复杂非结构化用户输入未必覆盖。


# Beyond Text-to-Music: Control, Agency, and Evaluation in Generative Audio

- 论文编号：
- 报告人：Lauri Juvela
- 程序：Wednesday 30 September 2026 / Generative Audio and Music
- 技术分类键：singing
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
生成式音频已从语音合成扩展到音乐、歌唱、环境声、乐器合成与音频制作。面向语音社区，需要把音乐/音频生成与 TTS、声转换、增强、分离、韵律、神经声码等熟悉问题连接起来，并抓住可控性与评估不足等核心议题。

## 方法
综述覆盖：基于神经编解码器的音频语言模型、diffusion 与 flow-matching、Transformer 生成器，以及可微 DSP。中心主题是控制：文本提示易用但音乐上歧义大；创作者还需要 MIDI、歌词、分轨（stems）、参考音频片段、合成器旋钮等可解释、可编辑表示。讨论任务包括 text-to-music、歌唱合成、Foley、continuation、inpainting、stem 条件生成、符号建模与生成式增强。

## 实验与结果
摘要未给出具体模型排行或定量分数；评估部分强调感知质量与 Fréchet 距离不足，并提出以条件遵循、音乐连贯性与创造性主体性（creative agency）指引未来交互式音乐工具。

## 结论
生成音频的关键不只是「能生成」，而是可控、可编辑，以及更贴合创作过程的评估。文本条件只是入口，不是全部。

## 点评
把语音社区熟悉的问题映射到音乐/音频生成，降低跨领域阅读成本；评估批评指向明确。无 PDF，无法核对具体系统对比。


# Negation in Audio Generation Models

- 论文编号：1756
- 报告人：Bikash Dutta
- 程序：Wednesday 30 September 2026 / Generative Audio and Music
- 技术分类键：singing
- 全文：https://www.isca-archive.org/interspeech_2026/arora26_interspeech.pdf

## 问题
文本到音频（T2A）模型常忽略否定约束，生成被要求排除的声音；现有基准几乎不测否定理解，训练数据也几乎只描述“在场”事件，形成肯定偏置。

## 方法
构建 Audio Negation Benchmark：由 AudioCaps 派生约 100 万否定提示，覆盖四类否定与三种范围，人工抽检正确率 99.6%。提出音频问答（AQA）等协议探测生成音频中否定事件是否缺失；评测 AudioGen、AudioLDM2、TangoFlux，并辅以再描述验证。

## 实验与结果
所有模型、所有否定类型上，否定音频的 AQA recall 均 <0.05；否定与肯定提示产生近乎相同的声学输出，再描述亦显示系统默认肯定声景。

## 结论
否定处理是当前 T2A 的系统失败模式，需要否定感知训练目标与专用评测。

## 点评
把肯定偏置用大规模对照与 AQA 钉死，对生成音频可信度很关键。局限是基准由字幕改写而来、评价依赖问答模型本身，且未给出有效缓解方法（正文定位为问题界定）。


# DiffRhythm 2: Efficient and High Fidelity Song Generation via Block Flow Matching

- 论文编号：128
- 报告人：Yuepeng Jiang
- 程序：Wednesday 30 September 2026 / Generative Audio and Music
- 技术分类键：singing
- 全文：https://www.isca-archive.org/interspeech_2026/jiang26_interspeech.pdf

## 问题
全长歌曲生成需歌词–歌声对齐与结构连贯。纯 NAR（如 DiffRhythm）对齐难或依赖时间戳/REPA 约束损害乐感；多偏好 RLHF 常分模型再合并导致性能折中。

## 方法
DiffRhythm 2：半自回归块级 flow matching——块内 NAR、块间 AR，无需时长标签即可对齐；5 Hz 音乐 VAE 压缩长序列；随机块 REPA 提升结构/乐感；跨对偏好优化（交叉配对冲突/协同偏好）做多维 DPO，避免合并退化。支持最长约 210 秒可变长（EOP 帧）与块级 KV cache。

## 实验与结果
客观上 DiffRhythm 2 在开源模型中 PER 0.13、Mulan-T 0.40，SongEval 多项领先（如 CO 4.09）；相对 DiffRhythm+/ACE-Step/LeVo 整体更均衡。主观与客观均报告优于开源基线并保持高效（正文强调相对 AR 仍快）。

## 结论
块级半 AR flow matching + 跨对偏好优化可在效率与保真之间取得更好歌曲生成折中。

## 点评
用“块内双向上下文 + 块间因果”同时缓解 NAR 对齐与 AR 慢速，设计动机清楚。细节依赖训练注意力掩码与 EOP 设计；多偏好分组策略对冲突维度的稳健性仍需更多消融支撑。


# Scaling Properties of Continuous Diffusion Spoken Language Models

- 论文编号：2980
- 报告人：Eeshan Gunesh Dhekane
- 程序：Wednesday 30 September 2026 / Generative Audio and Music
- 技术分类键：singing
- 全文：https://www.isca-archive.org/interspeech_2026/ramapuram26_interspeech.pdf

## 问题
纯语音 SLM 多走离散 AR，语言能力远落后文本 LLM，且缩放代价极高；连续扩散是否更可行、其缩放律如何，尚缺系统证据。

## 方法
研究 continuous diffusion SLM：提出音素 Jensen–Shannon 散度（pJSD）度量生成“语言性”；拟合验证损失与 pJSD 的缩放律，并分析最优 token–参数比随算力变化。最终缩放至约 16B 参数、千万小时级对话数据。

## 实验与结果
验证损失遵循缩放律；最优 token–参数比随算力增大而下降；高算力下近最优区对 N/D 配置显著变宽（利于推理前沿）。pJSD 亦随规模可预测改善，类似离散 AR 的语言评测趋势。常规感知指标多不服从缩放律且易饱和；Audiobox Aesthetics 中部分维度可缩放。16B 模型可生成多说话人、多语、富情绪韵律对话，但长程语言连贯仍难。

## 结论
连续扩散 SLM 缩放轨迹与离散 AR 相似，未根本改写算力需求；在当前数据/算力下进一步纯语音缩放可能不切实际，或需新表示/范式或转文本–语音模型。

## 点评
把 pJSD 与“isoFLOP 平坦化”作为可操作发现很有价值。结论偏悲观但证据导向；生成样例与长程失败模式的细粒度诊断仍有限。


# FoleyGenEx: Unified Video-to-Audio Generation with Multi-Modal Control, Temporal Alignment, and Semantic Precision

- 论文编号：112
- 报告人：Shiyao Wang
- 程序：Wednesday 30 September 2026 / Generative Audio and Music
- 技术分类键：singing
- 全文：https://www.isca-archive.org/interspeech_2026/wang26b_interspeech.pdf

## 问题
现有视频到音频方法常在“多模态可控”与“帧级时序对齐”之间权衡：MultiFoley 可控但同步弱，MMAudio 同步强但缺参考音频条件与细粒度副词语义。

## 方法
FoleyGenEx 基于 MMDiT：条件注入参考音频以支持 AC-VTA/Foley 扩展；多模态动态掩码保证训推一致；掩码 MSE 聚焦对齐段；副词增强（速度/距离/音量信号处理 + LLM 重写字幕）强化语义精度。统一支持 TTA、VTA、TC-VTA、AC-VTA、FE 与潜空间局部编辑。

## 实验与结果
AudioCaps：CLAP_T 达 0.364/0.366（+AA），优于 MMAudio 0.348。VGGSound：FD_VGG 0.73–0.74、IS≈18.4–18.5，与 MMAudio 同步接近并在多项上更优。正文报告在 Greatest Hits 等上也具竞争力。

## 结论
在单一框架内同时获得强同步、参考音频可控与更细语义控制，缩小既有方法之间的能力缺口。

## 点评
掩码对齐 + 参考音频注入是对 MMAudio 生态的务实扩展；副词增强针对数据稀缺很对症。代价是系统复杂、依赖 Synchformer/CLIP，且副词控制的主观/定量评测细节正文相对简略。


# Adaptive Oscillatory Inductive Bias for Modeling Sharp Prosodic Dynamics in Diffusion-Based TTS

- 论文编号：1655
- 报告人：Nirmesh J. Shah
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/dhar26_interspeech.pdf

## 问题
扩散 TTS（如 StyleTTS2）音质已较强，但对表情语音中的尖锐韵律转折、快速基频变化仍难稳。解码器里常用 Snake 等固定周期激活来拟合谐波结构，但对突变幅度/频率与清浊边界的适应性不足。

## 方法
在 StyleTTS2 框架上提出 **OscillaTTS**：整体两阶段训练与模块布局不变，核心是把解码器（iSTFT-Net 声码器）中的非线性换成自适应振荡激活
\[
x + \tanh(\alpha\sin^2(x)),
\]
其中 \(\sin^2(x)\) 提供周期归纳偏置，可学习 \(\alpha\) 调节振荡强度，线性旁路保持稳定性。Stage1 用重建损失训练解码器相关组件；Stage2 联合训练（含 style diffusion、SLM 判别器等），推理时从文本侧预测风格嵌入。作者从梯度/Taylor 展开对比 Snake、HOSC，说明 Oscilla 具有输入依赖的门控式振荡响应。

## 实验与结果
数据：LJSpeech（单说话人）与 ESD 英语子集（Happy/Angry/Sad）；80/10/10 划分；24 kHz；stage1 200 epoch、stage2 120 epoch。
- LJSpeech：主观 Speech Quality 86.67（StyleTTS2 81.48）；MCD 6.59、F0-RMSE 0.35；AutoPCP 4.05、WER 1.85（优于 StyleTTS2 的 3.92 / 2.86）。
- ESD：Angry/Happy/Sad 的 ES MOS、MCD 等多项优于 StyleTTS2；AutoPCP/WER 亦改善（如 Angry WER 9.21→4.05）。
- 激活消融：可学习 α 的 Oscilla 在 MCD/F0-RMSE 上优于固定 α、Snake1D、ReLU、tanh 等变体。

## 结论
作者认为在扩散 TTS 解码器中引入自适应振荡归纳偏置，能更好建模快速韵律变化；在 LJSpeech 与 ESD 上主客观均有一致提升。局限/展望：多说话人表情 TTS 与歌声合成。

## 点评
这是一篇「只改激活函数」却对准真实痛点的工作：表情语音的尖锐转折往往卡在解码器局部非线性的表达能力，而不是再加一套韵律预测器。Oscilla 相对 Snake 的可学习幅度 + tanh 阻尼 + 线性旁路，设计动机能从梯度分析直接看出来，消融也支撑了「自适应 α」的必要性。脆弱点在于：改进高度绑定 StyleTTS2/iSTFT-Net 解码路径；主观样本与情绪类别有限；与更大系统级改动相比，增益幅度中等，外推到更复杂多说话人设定仍待验证。


# Word-level Emotional Intensity Control in TTS via Emotion Residual Vectors

- 论文编号：3079
- 报告人：Ji-Hyun Park
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/park26i_interspeech.pdf

## 问题
情感 TTS 多采用句级情绪条件，难以在词级分配韵律突显，易把强度加错词。已有词级强度控制（EmoQ-TTS、HED-TTS、EME-TTS 等）虽可控，却常带来突变基频、不自然时长或过突显目标词，自然度下降。

## 方法
提出 **情绪残差向量（ERV）** 作为无标注的词级控制信号：
1. 在 ESD 平行中性–情绪同文对上，用 MFA 对齐 + WavLM-Base（层 7–12 聚合）得到词级嵌入，定义 \(r_w=u_w^{\mathrm{emo}}-u_w^{\mathrm{neu}}\)。
2. 三阶段训练：先训带说话人/句级情绪的 FastSpeech2；冻结骨干、全局情绪固定为中性，只训残差注入模块（RIM）：瓶颈投影 \(B\in\mathbb{R}^{a\times D}\)（默认 \(a=32\)）再映射到编码器隐空间，加 LayerNorm，按词级权重 \(\alpha\) 注入；再用学到的 \(B\) 生成投影目标，微调 RoBERTa 预测器从文本+情绪提示预测投影 ERV。
3. 推理：预测器输出 \(\hat z_w\)，经冻结 RIM 注入中性条件骨干，用 \(\alpha\) 连续调节词级强度。

## 实验与结果
ESD 英语子集（10 说话人，五情绪；14,900/950/1,550）；抽取约 88,400 词级 ERV。主观 NMOS/EMOS 与客观 UTMOS、Emotion2vec 情绪准确率：Proposed（\(\alpha_w=1\)）与 FS2+emo 接近（NMOS 3.83、Emo.Acc. 0.71），明显优于 HED-TTS。词级 A/B：相对 EME-TTS 赢 55.3%，相对 HED-TTS 赢 87.1%。增大 \(\alpha\) 时平均音高按情绪方向变化。消融：无瓶颈时 Emo.Acc. 偏低；\(a=32\) 附近情绪准确较好；带预测器后 Emo.Acc. 达 0.71。

## 结论
作者认为 ERV + 瓶颈注入可实现词级情绪强度控制并更好保持自然度；瓶颈使高维 S3L 残差变得可预测、可缩放。局限：依赖平行、词对齐的中性–情绪对，扩展到非约束数据仍是开放问题。

## 点评
关键洞察是「控制信号应是中性→情绪的局部残差，而不是另造一套强度标签」。把残差压进低维瓶颈再让 RoBERTa 预测，既稳定了 \(\alpha\) 缩放，又把监督从声学残差转到文本条件——这是相对直接注入高维 ERV 更工程化的一步。相对 HED/EME 类显式强度/分布控制，主观词级自然度优势明显。脆弱点紧扣作者自己指出的平行对齐依赖；且全局情绪固定为中性、情绪主要靠残差表达，对「非平行」或跨语料泛化可能变脆。


# Continuous Time-Varying Emotion Control Zero-Shot Text-To-Speech With Emotion Orthogonal LoRA

- 论文编号：1798
- 报告人：Chenchen Wan
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/wan26b_interspeech.pdf

## 问题
高质量情感 TTS 常依赖大规模语料与粗糙离散标签，难以做细粒度、随时间变化的控制。参考音频提示易把情绪与说话人/内容韵律缠在一起；句内情绪转折容易被平滑或被 prompt 情绪拖偏。

## 方法
在预训练 flow matching TTS（F5-TTS / DiT）上提出两阶段方案：
1. **EO-LoRA**：在选定线性层（默认 attention 的 Value/Output 与 FFN）插入三条分别对应 Valence、Arousal、Dominance 的低秩分支（r=16），每帧用对应 VAD 标量缩放更新；用 Frobenius 余弦正交正则 \(L_{\mathrm{orth}}\) 抑制维度间干扰。支持句级常数或帧级时变 VAD。
2. **Flow-DGPO**：对候选组做偏好对齐，用组内标准化优势把样本分成正/负集，以 flow matching loss 相对冻结参考模型的间隔做偏好目标；奖励综合情绪相似度、说话人相似与 (1−WER)。
Stage1：\(L_{\mathrm{FM}}+\lambda_{\mathrm{orth}}L_{\mathrm{orth}}\)；Stage2：Flow-DGPO。帧级 VAD 由 wav2vec2 预测器（MSP-PODCAST）提取并归一化到 \([-0.5,0.5]\)。

## 实验与结果
训练：EmoVoice-DB（约 40h）+ ESD 英语（约 10h）。评测：EMO-Change（时变转折）、JVNV S2ST（日→英跨语）。相对细调 F5-TTS，EO-LoRA + Flow-DGPO 在 EMO-change 上 SIM-o 0.751、WER 0.2%、AutoPCP 3.60、Emo SIM 0.778、Aro-Val SIM 0.914；主观 SMOS/NMOS/EMOS 亦最高。数据量远小于 EmoCtrl-TTS 的大规模设定，但可控性指标可竞争甚至更优。消融：去掉 \(L_{\mathrm{orth}}\) 或改注入位置（含 Q/K）会削弱可控性；Flow-DGPO 进一步提升可控与可懂度。

## 结论
作者认为 EO-LoRA 与 Flow-DGPO 能在有限情感数据下实现稳健的连续/时变零样本情绪控制，并保持可懂度与说话人相似；计划扩展到其他生成骨干。

## 点评
核心设计是「把 V/A/D 拆成三条正交低秩调制」，比单条 LoRA 或外挂条件流更可解释，也直接服务帧级轨迹控制。Flow-DGPO 用复合奖励把情绪对齐与质量约束绑在一起，缓解了只追情绪相似度时的崩坏风险。脆弱点：VAD 依赖外部预测器质量；跨语设定下骨干未学日语，SIM/WER 仍有差距；EmoCtrl-TTS 结果来自原文报告而非同环境复现，跨论文对比需谨慎解读。


# ETC-TTS: Emotion Trajectory Learning for Controllable Emotional Text-to-Speech

- 论文编号：3088
- 报告人：Gaeun Kim
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kim26u_interspeech.pdf

## 问题
情感强度控制常在推理时对情绪嵌入做缩放/插值，中间强度并未在训练中显式学习，导致强度单调性不稳、自然度下降。作者指出这造成训练–推理不匹配：模型只在离散端点上优化，却指望推理期潜空间操纵给出一致感知强度。

## 方法
**ETC-TTS** 把强度重写为潜在风格空间中的 **中性→目标情绪轨迹**：
1. **RVQ 情绪原型**（L=3）：每级码本大小=情绪类别数，与标签一一对应；k-means 初始化 + 级联 triplet 聚类损失，并周期性复活未使用码字。
2. **原型锚定 flow matching**：源为中性原型加噪、目标为情绪原型；学习条件于音素特征与风格标签的速度场；推理用轨迹参数 \(t\in[0,1]\) 调节强度，无需参考音频。
总损失含 FastSpeech2 重建、RVQ、聚类、flow（\(\lambda_f=30\)）与中性对齐项。三阶段训练：原型初始化 → 冻结 flow 先稳抽取器 → 联合训练。

## 实验与结果
数据：AIHub 韩语情感语音（约 80h，七情绪）与 ESD 英语。骨干统一 FastSpeech2 + HiFi-GAN。相对标签条件、RA、SF：
- ESD：Proposed N-MOS 3.14、E-MOS 3.78、EmoAcc 92.93%；AIHub 上 E-MOS/CER 等亦更优。
- 强度单调性 AB 错误率在多数情绪/强度对上低于 RA/SF；emotion2vec 概率随 \(t\) 更平滑单调。
- 跨强度 UTMOS/CER 更稳定；用 SER 嵌入或高斯先验替代中性锚定会伤 EmoAcc 或自然度。

## 结论
作者认为应在训练中学习中性–情绪轨迹，而非推理期启发式嵌入操纵；在韩/英数据上获得更稳的单调强度控制并保持竞争力音质。

## 点评
问题诊断很准：强度控制的失败往往不是「没标量」，而是「中间态从未被监督」。把 rectified flow 端点钉在 RVQ 原型上，把可控 \(t\) 变成真正学过的路径参数，比 SF/插值更有训练一致性。脆弱点：原型与类别数硬绑定，细粒度/复合情绪表达受限；flow 权重大（\(\lambda_f=30\)）需小心与声学重建权衡；主对比都在同一 FastSpeech2 骨干上，换现代零样本骨干时轨迹模块是否仍成立未验证。


# Beyond One-Size-Fits-All: Personalized and Culturally Adaptive Emotional TTS via Interactive Optimization of Individual Emotion Perception Spaces

- 论文编号：1696
- 报告人：Wangzixi Zhou
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/zhou26e_interspeech.pdf

## 问题
情感 TTS 即使用 arousal–valence（A–V）连续控制，训练标注常来自单一人群平均，默认「声学线索→感知情绪」映射普适。个体与文化差异会导致模型情绪与听者感知错位；RLHF 类对齐又需大量偏好数据并重训模型，不适于快速人均适配。

## 方法
提出轻量 **训练后个性化层**，不改声学骨干：
1. **情感生成器**：Grad-TTS + Emotion Controller（Emotion Feature Predictor + pitch/energy 预测）。A–V 经 Gaussian Fourier 特征映射后由四层 MLP 预测 SER 衍生的高维情绪特征；训练用 L1 对齐预训练 SER 特征，推理只需 A–V。
2. **交互遗传算法（IGA）**：对目标离散情绪，在 A–V 空间生成候选坐标并合成语音，用户选偏好样本；多亲算术交叉 + 衰减突变强度（\(M_1=0.20,\gamma=0.90,M_{\min}=0.05\)）迭代，通常约三轮收敛，得到个人/文化平均 A–V 映射。

## 实验与结果
数据：约 9 小时美式英语女声（EXPRESSO + EmoV-DB + ESD），A–V 由 SER 估计。相对 Grad-TTS+情绪嵌入，Emotion Controller：MOS 3.37→3.75，WER 21%→17%，CCC(A/V) 0.60/0.64→0.84/0.77。
个性化：中/印尼/日各 10 人共 30 人；个人化 A–V 相对美式数据集均值明显偏移。A/B：亲历个性化者偏好个人映射 76%；新文化听者对文化平均映射偏好约 64.8–69.8%；跨文化排序亦偏好本文化映射（约 65–70%）。

## 结论
作者认为应把情绪感知空间个性化/文化适配，而非一刀切平均 A–V；交互优化可在少量反馈下提升感知对齐。未来工作包括更广语言文化与实时个性化。

## 点评
工作抓住的是「控制空间」而非「声学模型」：把适配限制在 2D A–V，用 IGA 做极少交互的人均搜索，比 RLHF 更贴近产品侧快速定制。Emotion Controller 用 SER 特征桥接低维控制与高维声学，使个性化不必重训扩散解码器。脆弱点：骨干与语料偏英语女声，跨文化听评仍用同一声学模型；A–V 监督本身来自 SER 估计，存在标签噪声；偏好实验规模中等，文化结论更偏初步观察。


# Cross-modal Consistency Guidance for Robust Emotion Control in Auto-Regressive TTS Models

- 论文编号：1986
- 报告人：Yizhou Peng
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/peng26g_interspeech.pdf

## 问题
自然语言情绪指令的 AR TTS 在「文本语义情绪」与「要求渲染的语音情绪」冲突时（如用惊讶语气说悲伤内容），表现力、自然度与音质会明显下降。标准 CFG 用无条件 dropout 外推，难以对抗文本语义拉力，且易引入伪影。

## 方法
在 CosyVoice2 上提出 **CCG-CFG** 及其蒸馏：
1. 外部 LLM 抽取 Text-Emo，并判定与 Rendered-Emo 的不一致程度（Identical / Inconsistent / Highly Inconsistent）。
2. **CCG-CFG**：不一致时把 CFG 的无条件支路换成 Text-Emo 条件，放大 Rendered-Emo 与 Text-Emo 的 logit 差；一致时退回标准 CFG。
3. **DS-CCG-CFG**：按不一致档位动态设 guidance scale（网格搜索得 {1.0, 2.5, 3.0}）。
4. **蒸馏**：用硬样本挖掘构造文本–对立情绪对，多尺度/多种子生成候选，按 \(0.5(1-\mathrm{WER})+0.5\cdot\mathrm{EmoConf}\) 排序做 DPO，把引导内化，去掉双通道推理与 CFG 伪影。

## 实验与结果
合并 ESD/MESS/MEAD/TESS/SAVEE/LibriTTS/VCTK 等，七情绪；约 40h 训练。中性参考下相对 CosyVoice2-N（EmoACC 50.63%）：
- DS-CCG-CFG：EmoACC 64.83%，MaJ 58.4（训练免费最佳之一），但 WER 升至 7.86%。
- DS-CCG-CFG-DPO+硬样本：EmoACC 59.55%，WER 3.76%，UTMOS/DNSMOS 保持高；主观 MOS 4.33、EMOS 3.67、NMOS 3.94，优于 CosyVoice2-N/R，并接近 Qwen3-TTS-R。
不一致子集上增益最大；传统高尺度 CFG 则显著伤 WER。

## 结论
作者认为用文本情绪作对比条件、按不一致动态尺度，再蒸馏进模型，可在冲突场景下显著提升情绪表达并保住可懂与自然度。

## 点评
问题设定很现实：NLEC 的失败模式往往不是「不会说情绪」，而是「文本语义把渲染情绪拉回去」。把 unconditional 换成 Text-Emo，等于显式做跨模态对照，比盲目加大 \(w\) 更对症；动态尺度与 DPO 蒸馏则分别处理「何时用力」与「推理成本/伪影」。脆弱点：推理期依赖外部 LLM 判不一致（蒸馏后可摆脱）；EmoACC 依赖 SER，与文本语义冲突时「正确情绪」定义本身主观；硬样本挖掘的对立情绪配对策略会影响泛化边界。


# A Large-Scale Dataset of Listener Impressions of Emotional TTS

- 论文编号：1521
- 报告人：Erica Cooper
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/cooper26_interspeech.pdf

## 问题
情感 TTS 的金标准仍是听测，但成本高、难快速迭代。现有自动质量评估（如 UTMOS）多在中性合成语料上训练，难以泛化到情感合成；情感 TTS 还需评估表达力与目标情绪匹配度，而公开听测结果与含合成样本的标注数据几乎空白。

## 方法
构建大规模听感数据集（非提出新合成模型）：
1. 收集/生成约 18,208 条样本：自然情感语音（主要 ESD）+ 13 类合成系统（Emo-DPO、EmoSpeech、ECSS、GPT-Talker、EmoKnob、Tortoise、MaskGCT、VALL-E X、Vevo、PromptTTS++、ParaSpeechCaps、MiMo-Audio、Gemini API 等），覆盖克隆、文本提示说话人与 API 预设音色。
2. 262 名美式英语母语听者评分：QMOS、EMOS、自由选择感知情绪类别、valence/arousal/dominance（SAM 量表）；多数样本约 7 次评分。
3. 分析评分关系，并用 SSL-MOS、UTMOS、Emotion2Vec、Gemini LLM-as-judge 做零样本预测实验。

## 实验与结果
组内系统排名给出（跨组因内容/说话人不同不可直接比）：如 ESD 自然语音 QMOS/EMOS 3.71/3.90；Gemini API 4.21/3.89；Tortoise QMOS 高但 EMOS 偏低。目标情绪选择比例与 EMOS 相关约 0.92。VAD 分布相对自然语音的 EMD 与 EMOS 呈强负相关（按情绪有所不同）。零样本预测：UTMOS 对 QMOS 系统级 SRCC 总体 0.80；Gemini 对 EMOS 总体 0.84；各情绪差异大（如 Angry 更具挑战）。

## 结论
作者贡献首个面向情感合成语音质量评估的大规模听感数据集，将公开以支持自动评估模型开发；现有预测器有一定相关性但仍有明显提升空间，且表现依赖情绪类别。

## 点评
这是「评测基础设施」论文：价值在于把多系统、多轴标注做成可训练资源，而不是比拼某个 TTS 分数。分析部分有用地提醒：QMOS/EMOS/VAD 可互补，中性 MOS 预测器不能直接当情感评测银弹。脆弱点：系统间条件不完全对齐（作者已强调），零样本预测不等于专用评估模型上限；公开后实际训练效果仍待社区验证。


# DECRA: Dynamic Emotion Control for Real-time Speech Anonymization

- 论文编号：2927
- 报告人：Ghady Nasrallah
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/nasrallah26_interspeech.pdf

## 问题
实时说话人匿名化既要抹去身份，又要控制/中和情感以防副语言泄露。现有流式 VC 多只管身份、无意中保留情绪；情感 VC 则多为离线、句级全局条件，无法因果低延迟地做时变、闭环情感操控；说话人嵌入常与情绪纠缠。

## 方法
**DECRA** 以 TVTSyn 为流式骨干，加入：
1. 对抗学习：把全局说话人嵌入投影到「去情绪」音色子空间（GRL + V/A 回归），情绪信息改由连续 valence–arousal 轨迹回注解码器。
2. 离线 SER 伪标签在大规模自然语音（LibriTTS + Natural Voices）上监督；训练时用时变 V/A 条件（250 ms hop）。
3. 因果 SER 头挂在 VQ 前内容特征上，在线预测帧级 V/A，闭环反馈到情感控制器；波形解码用 Conditional LN Fusion 融合 TVT 与 V/A。端到端可流式，GPU 延迟 <80 ms。

## 实验与结果
情感评测在 ESD。中和/转换相对 SeedVC、Vevo、TVTSyn：DECRA 的 CCC(A) 更高（中和 0.81、转换 0.74），WER/说话人相似可竞争；NISQA 低于离线基线，作者归因于流式约束而非情感模块。主观：怒/喜→中性准确率约 91–92%，悲→中性较弱；中性→情绪方向亦多数优于无控制骨干。动态 arousal 斜坡与预测轨迹相关约 0.78，valence 仅约 0.21。VPC’24：EER 46.64、WER 4.90、UAR 48.70，在匿名与情绪保留间更平衡。流式：76.1 ms 延迟、RTF 0.268。

## 结论
作者给出可同时做身份转换与闭环时变情感控制的因果流式系统；局限是 valence 控制弱于 arousal，未来拟用更丰富 SSL 情绪嵌入并加强与内容/说话人解耦。

## 点评
问题组合很贴隐私场景：匿名化若「保情绪」会泄露，若「抹情绪」又需实时可控。对抗解耦 + 在线因果 SER 闭环是清晰设计。结果也诚实：arousal/prosody 跟得上，valence 难控；音质代价主要来自流式而非控制头。脆弱点：伪标签 SER 误差会传导；与离线高保真情感 VC 比，质量–延迟权衡仍陡。


# Emo-BPO: Emotion Bidirectional Preference Optimization for Diffusion-based Emotional TTS

- 论文编号：1613
- 报告人：Jiacheng Shi
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/shi26d_interspeech.pdf

## 问题
扩散情感 TTS 的偏好对齐（如 Emo-DPO）通常只强化目标情绪条件轨迹，未显式建模与竞争情绪模式的分离；而 CFG 本质依赖条件对比，这种「单向」优化会削弱细粒度可控性。

## 方法
**Emo-BPO** 在 Grad-TTS 扩散解码器上：
1. 用同文不同情绪的平行对构造双向监督：\((c,a_1,a_2)\) 学情感对齐分支 \(\epsilon_{\theta}^{\mathrm{EA}}\)，颠倒顺序学对比分支 \(\epsilon_{\theta}^{\mathrm{EC}}\)（两套参数，非单网络硬兼两职）。
2. 推理对比引导：\(\epsilon^\omega=(1+\omega(t))\epsilon^{\mathrm{EA}}-\omega(t)\epsilon^{\mathrm{EC}}\)，并用晚步日程 \(\omega(t)=1-t/T\)，早期弱引导保结构、后期加强情绪。
无需额外奖励模型或新标注；冻结文本编码器与时长预测器，只微调 score 网络。

## 实验与结果
数据：ESD + EmoVoiceDB。客观：Emo SIM 99.23、Prosody SIM 3.85、UTMOS 4.52、SER 均值准确 0.87，多项优于 EmoSpeech、CosyVoice(2)、EmoSphere++、EmoVoice；可懂度竞争（WER 3.84，CosyVoice2 更低）。主观 MOS/Emo MOS/MOS EC 与人类情绪识别亦领先；AB 偏好优于 EmoSpeech 与 CosyVoice2。消融：去掉对比分支或晚步日程均伤情绪/韵律/WER。

## 结论
作者认为应在 CFG 框架下同时学习情绪吸引与排斥轨迹；双向偏好 + 渐进引导可提升可控性与感知质量并保持可懂度。

## 点评
洞察贴合扩散机制：CFG 已是对数似然比，把「无条件」换成「竞争情绪条件」并把两条 score 分开学，比只做 DPO 推目标更吃透对比结构。晚步日程也符合「先结构后细节」的去噪直觉。脆弱点：依赖平行同文多情绪对；双分支推理成本更高；骨干是 Grad-TTS，相对现代 LLM-TTS 的绝对 WER 仍可能吃亏。


# DeSRPA: Decoupled Speech Role-Playing Agent via Inference-Time Intervention

- 论文编号：1627
- 报告人：Wenqiu Tang
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/tang26b_interspeech.pdf

## 问题
语音角色扮演智能体（SRPA）若端到端微调，依赖角色专用数据、难泛化到未见角色，且音频–文本联合训练带来「模态对齐税」，损伤 LLM 推理与人设一致性；纯级联 LLM→TTS 又易丢情感推理，TTS 只做脱节渲染。

## 方法
**DeSRPA**：推理期干预、不更新参数的解耦框架：
1. **内部认知转向**（冻结 Qwen3-4B）：用 SAE 学稀疏控制向量，在残差流注入人格基向量、情境激活向量（Layer 15）与语言风格向量（Layer 20）；缩放系数结合 PDB 人格指标与人–LLM 协作标注。
2. **外部表达渲染**（冻结 StyleTTS 2）：从 ESD/CREMA-D 过滤高置信情绪样本，用风格减法 \(v_{\mathrm{acoustic}}^{(c)}=\mathbb{E}[S(x^{(c)})]-\mathbb{E}[S(x^{(n)})]\) 得说话人无关情绪方向；按 LLM 情绪标签与强度 \(\tau\) 做双路径融合注入风格空间并经扩散 style predictor 细化。

## 实验与结果
SpeechRole（72 英角色）与 OmniCharacter-10K（原神 10 角色）。多模态裁判均值 0.8379，开源最优、接近 GPT-4o Audio(0.8862)；EEA 0.701、SIM 0.886。消融去掉 LLM/Speech CV 分别伤人格/知识一致性与 EEA（降至 0.549）。OmniCharacter 人类评测：流畅、清晰、情感表达最高；Consistency/Immersion 逊于高度风格化的 OmniCharacter E2E（作者归因动漫夸张韵律 OOD）。

## 结论
作者认为双层推理期控制向量可在不微调下对齐「心智」与「嗓音」，提升人格/情绪一致性并缩小与专有模型自然度差距。

## 点评
路线明确反对「一切端到端」：把角色适配做成两侧冻结骨干上的向量算术，可扩展性好。风格减法解耦说话人与情绪方向，和 LLM 侧 SAE 人格向量形成对称设计。脆弱点：依赖外部过滤质量与裁判 LLM；TTFA 高于纯 E2E；对夸张 OOD 人设，固定 StyleTTS 2 风格空间仍可能不够。


# EmoInstruct-TTS: Dual-Path Instruction-Guided Emotional Speech Synthesis

- 论文编号：1834
- 报告人：Ganjun Liu
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/wu26f_interspeech.pdf

## 问题
自然语言指令可控 TTS 灵活，但常依赖粗糙情绪标签，缺少细粒度类别与强度的显式建模；仅靠语言指令也难稳定捕捉情绪的声学对应。参考音频条件则易受说话人/音色绑定。

## 方法
**EmoInstruct-TTS** 双路径框架：
1. **Emotion2embed**：Sentence-BERT 文本特征与 ECAPA-TDNN 声学特征拼接投影为 896 维；多任务分类 + 序数强度排序损失，覆盖 48 态（27 细粒度类别 + 7 主情绪×3 强度）。
2. **ICE-Flow**：MiniLM 编码指令，流/回归生成声学接地的 Emotion2embed；样本级 L2 + 协方差分布正则；推理可 CFG 调节指令遵从。
3. **合成**：指令进 LLM（Qwen2.5-0.5B+LoRA）做语义规划，Emotion2embed + 说话人嵌入条件 CFM 生成 mel，BigVGAN 声码。

## 实验与结果
ESD + CNCED；弱标注字幕集 + 人工细粒度标注集。相对 CosyVoice2/3：21 强度任务与 27 细粒度任务上 Dual-Path 的 MOS/ESMOS 整体更优；去掉任一路径均下降。48 类客观 ECS 0.870（最高），WER 2.59%（CosyVoice3 更低 1.97%）。ICE-Flow 增加端到端延迟约 <1–2%。分布一致性消融显示 Sample+Dist 最优（IOA 0.91）。

## 结论
作者认为语义指令与结构化情绪嵌入应分工：前者规划语言、后者调制声学；双路径提升细粒度/强度可控与自然度。未来拟支持无预定义类别的开放描述。

## 点评
「双路径」直接回应指令 TTS 的常见失败：文本能描述情绪，却不一定能驱动正确声学。Emotion2embed 用序数几何把强度做成可排序方向，ICE-Flow 再把自由指令接到该空间，工程上完整。脆弱点：48 态标签体系仍是封闭集；部分字幕来自 Gemini 自动生成，噪声可能影响表示；相对 CosyVoice3 在 WER 上仍有差距。


# SAM: A Mamba-2 State-Space Audio-Language Model

- 论文编号：639
- 报告人：Taehan Lee
- 程序：Wednesday 30 September 2026 / Audio Foundation Models and Generation
- 技术分类键：generation
- 全文：https://www.isca-archive.org/interspeech_2026/lee26d_interspeech.pdf

## 问题
Transformer 音频语言模型算力随序列长度二次增长。Mamba 等 SSM 在语言与图像理解中已显示潜力，但在音频–语言模型中如何与音频编码器交互、是否需要端到端微调、以及长未压缩 token 是否真正有利，尚缺系统表征级分析。

## 方法
SAM：EAT-base 音频编码器 → 两层 MLP 连接器 → 预训练 Mamba-2（130M/780M/2.7B）作 LLM。连接器对比 (a) 沿频率维拼接压缩为 64 token；(b)/(c) time-major / frequency-major 保留更长序列并插入 “&&” 分隔符。在 OpenAQA 上按 LTU 四阶段课程 + LoRA（in_proj/out_proj）训练，自回归 caption 交叉熵。另构 OpenReasonAQA（基于 ReasonAQA 的 BQ/MCQ，约 3.8M）强化指令跟随与推理。

## 实验与结果
SAM-2.7B（r=256, concat）AudioSet mAP 21.1、AudioCaps SPICE 17.6，可匹敌或超过更大 7B Transformer ALM 与 ssLALM-2.8B。联合微调音频编码器优于冻结；更小 SSM 对应更低 τ-effective rank、更高 token 相似度，且尺寸匹配的编码器迁移效果最好。未压缩长序列 (b/c) 未稳定超过压缩 (a)，长序列增加状态更新负担。OpenReasonAQA 使 MMAU-Sound 从约 22.8 升至 56.8（SAM+OR-2.7B），超过 Gemma3n-4B 的 sound 设置。

## 结论
Mamba-2 可作为参数更少却有竞争力的 ALM 骨干；实践上应联合微调编码器、优先紧凑信息丰富的音频 token，并用结构化 BQ/MCQ 监督解锁推理。未来拟探索 SSM–Transformer 混合结构。

## 点评
贡献不只是换骨干，而是用有效秩、编码器互换与连接器消融把“SSM 固定维状态瓶颈”说成可检验的设计原则：编码器会按容量压缩表征，盲目拉长序列未必帮 SSM。相对常见冻结编码器或堆长上下文的路线，这组结论更贴 SSM 归纳偏置。局限是主表仍偏描述/分类，强推理依赖额外数据配方；Clotho 等上并非全面 SOTA，混合架构是否补足全局交互仍待验证。


# Samsone: A Family of Open Small Audio Language Models for On-Device Inference

- 论文编号：763
- 报告人：Michal K. Grzeszczyk
- 程序：Wednesday 30 September 2026 / Audio Foundation Models and Generation
- 技术分类键：generation
- 全文：https://www.isca-archive.org/interspeech_2026/masztalski26_interspeech.pdf

## 问题
LALM 规模大、成本高，隐私与低延迟场景需要可端侧运行的 Small Audio Language Models（SALMs，本文定义为 <1B）。现有 Pengi、Mellow 等 SALM 推理能力与真实手机部署、开源可复现实验仍不足。

## 方法
标准 ALM：Whisper-Tiny 编码器 → Mellow 式非线性 projector（两层 Linear+GeLU、残差与 LN）→ SmolLM2（135M/360M）解码。音频帧嵌入时序平均池化为每样本 50 token；可训练 SEP token 分隔多段音频与文本。尺寸优化：(1) 词汇削减（小写 ASCII、过滤稀有 token，去掉约 15042 词，降约 8.7M 参数）；(2) 深度剪枝（99M 版去掉最后 10 层，30→20 块）。变体：Samsone-99M / 134M / 356M。数据：ReasonAQA + AudioSkillsXL；对 ReasonAQA 多选题随机置换选项以纠正答案偏向；单阶段训 100 epoch（每 epoch 20 万样本），除 LM embedding 外全可训；XNNPACK/ExecuTorch 导出端侧权重。

## 实验与结果
MMAU：99M/134M/356M 平均 Test 约 58.13 / 61.33 / 62.00，均超 Mellow（53.34），134M 可与更大 LALM 竞争；MMAU-Pro 相对 Mellow 约 +34%–36%。ClothoAQA 与 entailment（CLE/ACE）上优于或持平 Mellow；AudioCaps SPICE 低于 Mellow（归因训练中 AudioCaps 占比更小），Clotho SPICE 更好。消融：换 AST、GPT-2 或线性 projector 均降 MMAU。Galaxy S25 Ultra：生成约 39–125 tok/s（356M→99M）。局限：重度 AQA 微调损害通用语言能力；以参数量代理效率、未做 GPU/NPU 硬件优化。

## 结论
开源 Samsone 系列在同尺寸 SALM 上刷新 MMAU 等表现，并给出手机实时推理与可扩展尺寸谱。未来可探索量化大模型与硬件加速。

## 点评
主线是“公开数据 + 词汇/深度剪枝 + 端侧导出”，把 SALM 从纸面精度推向可跑的 Android 应用，工程闭环完整。相对只堆更大 LLM 的路线，强调 <1B 与实机 tok/s。脆弱点在于 caption 并非全面领先、通用语言能力被 AQA 微调侵蚀，且效率叙事仍偏参数量而非精度–内存曲线。


# FreeSonic: Training-Free Temporal-Aware Decoupled Attention for Precise Audio Editing

- 论文编号：1121
- 报告人：Yuxuan Jiang
- 程序：Wednesday 30 September 2026 / Audio Foundation Models and Generation
- 技术分类键：generation
- 全文：https://www.isca-archive.org/interspeech_2026/jiang26d_interspeech.pdf

## 问题
文本条件音频编辑需同时满足时间一致性（只改目标段）与背景保持（重叠声源下非编辑区不变）。现有反演/全局条件方法改一处常牵动整段；训练式方法依赖复杂三元组与专用结构，成本高、灵活性差。

## 方法
基于 TangoFlux（Rectified Flow + MM-DiT）的免训练框架 FreeSonic。(1) 优化 RF 反演–重建，为后续编辑提供稳定结构。(2) 反演前 5 步聚合 double blocks 的 text–audio attention，阈值+膨胀平滑得时间掩码 M，定位待编辑段。(3) 在 single blocks 做三阶段 Scheduled Attention Decoupling：早期按 δ（0.85→1.0）混合源/目标 KV，并用 M 在非编辑区强制注入源 KV；中期 δ=1 且保持掩码；后期去掉约束做全局协调。(4) Task-Oriented Noise Injection：仅在 M 内对潜变量加可调度噪声，便于删除与非刚性替换。推理用 RF-Solver、25 步；噪声强度按 Add/Remove/Replace 分别为 0.1/0.4/0.25，截止步 t1=5。

## 实验与结果
基准：AudioCaps / AudioSet Strong 等构建的 Add(1300)、Remove(1300)、Replace(750)。对比 SDEdit、AudioEditor、ZETA、训练式 SAO-Instruct。FreeSonic 多数客观指标领先（如 Add FAD 1.55、Remove FAD 1.95、Replace CLAP 0.424）；主观 Quality/Relevance/Faithfulness 整体强。消融去掉掩码、改全量 KV 替换或去掉噪声注入均变差。固定 NFE=150 时 RTF 约 0.854，优于多数训练无关基线。

## 结论
免训练下用 RF 反演 + 注意力时间定位 + 调度解耦 + 任务噪声，在保背景与局部编辑间取得更好平衡，并在多种编辑任务上达到高保真与较高效率。

## 点评
抓住音频“可加性/重叠”导致全局反演难局部改的本质，把 MM-DiT 的跨模态注意力当作时间定位器，再用掩码约束 KV，比纯改文本条件更可控。相对训练式编辑省数据与微调。风险在于掩码依赖早期注意力质量与阈值、强依赖 TangoFlux 骨干，复杂重叠或弱对齐文本时定位可能漂移。


# Resonate: Reinforcing Text-to-Audio Generation via Online Feedback from Large Audio Language Models

- 论文编号：1823
- 报告人：Xiquan Li
- 程序：Wednesday 30 September 2026 / Audio Foundation Models and Generation
- 技术分类键：generation
- 全文：https://www.isca-archive.org/interspeech_2026/li26ba_interspeech.pdf

## 问题
TTA 上已有 RL 多采用离线 DPO，并以 CLAP 作奖励：偏好数据与策略脱节易分布漂移，CLAP 有 bag-of-words 倾向，奖励偏粗、与人对齐不足。在线 RL 与更细粒度奖励在 TTA 中仍少见。

## 方法
Resonate：MeanAudio 风格 Flux Transformer（16 MMDiT + 36 DiT，470M），FLAN-T5 条件，先在约 3.7M 对/1 万小时语料上 Conditional Flow Matching 预训练。再将去噪建成 MDP，用 Flow-GRPO：对每条 prompt 采 G 条轨迹，组内标准化优势，裁剪策略比 + KL 到参考策略；确定性 ODE 改为等价边缘的 SDE 采样以引入探索。奖励用 LALM（训练期 Qwen2.5-Omni）对 AQA 问题“音频是否包含文本描述事件？”的 Yes/No 归一化概率（AQAScore）；评测用另一模型 Qwen3-Omni-Instruct 降奖励黑客风险。后训练：AudioCaps 训练 prompt，G=24，a=0.7，β=0.04，1000 步。

## 实验与结果
TTA-Bench Accuracy（1500 prompt）：Resonate-GRPO 相对预训练全面提升（AQAScore 0.651→0.737，PQ 5.923→6.064，CLAP 0.476），并在多项上达 SOTA；主观 OVL 3.86、REL 3.83。消融：DPO/SFT 增益有限或降质量；直接 GRPO 优于 SFT+GRPO；AQAScore 奖励总体优于 CLAPScore；噪声 a=0.7、更大 G 更稳。25 NFE 推理。

## 结论
在线 Flow-GRPO + LALM 细粒度奖励可同时提升 TTA 音质与语义对齐；Resonate（470M）在 TTA-Bench 上达到新 SOTA。

## 点评
把“离线偏好 + CLAP”两条瓶颈一起拆：在线组相对优势缓解分布漂移，LALM-AQA 奖励补时间/组合推理。与图像 Flow-GRPO 同构迁移到音频较自然。需警惕奖励模型与评测模型虽不同仍属同类 LALM 家族；SDE 噪声与 G 需调，噪声过大可奖励黑客；SFT 在嘈杂 AudioCaps 上伤音质，说明后训练数据质量仍关键。


# GACA-DiT: Diffusion-based Dance-to-Music Generation with Genre-Adaptive Rhythm and Context-Aware Alignment

- 论文编号：2348
- 报告人：Jinting Wang
- 程序：Wednesday 30 September 2026 / Audio Foundation Models and Generation
- 技术分类键：generation
- 全文：https://www.isca-archive.org/interspeech_2026/wang26da_interspeech.pdf

## 问题
Dance-to-music（D2M）需节奏一致与帧级时间对齐。已有方法常用全局运动特征或二值化关节节奏，丢失细粒度运动、跨舞种鲁棒差；特征下采样还造成舞蹈节奏嵌入与音乐潜变量长度错位，对齐不足。

## 方法
GACA-DiT（约 56M）：(1) Genre-Adaptive Rhythm Extraction（GARE）：由姿态差分得运动幅度，多尺度 Gabor 小波建模时间动态，MLP+softmax 得关节自适应权重，再构多尺度相位直方图刻画空间运动分布，经时间注意力融成节奏嵌入 R。(2) Context-Aware Temporal Alignment（CATA）：将 R 切成 Tm 段，用可学习 context queries 对段内帧做注意力池化，得到与音乐潜变量同长的 ˜R。(3) I3D 视频语义特征 V 与 ˜R、时间步共同条件化 DiT，Conditional Flow Matching 学速度场；DiffRhythm VAE 编解码波形。训练 5 s/44.1 kHz，32 步 Euler，CFG=4。

## 实验与结果
AIST++ / TikTok 上相对 D2M-GAN、CDCD、LORIS、MotionComposer：AIST++ BCS 98.13、BHS 98.72、F1 98.47、FAD 20.14 等多项最优；TikTok BCS 91.55、F1 91.21 等亦领先。消融逐步加入小波、直方图、自适应加权与 CATA 指标递增；GARE 优于 ST-GCN 与 LORIS 式节奏特征。20 人 MOS：节奏一致性与整体质量中位数更高、分布更集中。

## 结论
细粒度、舞种自适应节奏表征 + 查询式跨模态时间对齐，使扩散式 D2M 在客观对齐/美学与主观评价上全面超过先前 SOTA。

## 点评
把“粗节奏”和“长度错位”拆成两个可模块化补丁，GARE 用时–空互补特征、CATA 用可学习查询对齐下采样，问题定位清楚。参数量远小于若干大基线却指标领先，说明条件表征质量比堆模型更关键。潜在脆弱点：依赖姿态检测质量与舞种覆盖；TikTok FAD 未全面领先；短 5 s 片段设定外的长视频对齐未充分验证。


# Rethinking Speech Foundation Model Fine-tuning: Better SFT or Better Match?

- 论文编号：2436
- 报告人：Wangjin Zhou
- 程序：Wednesday 30 September 2026 / Audio Foundation Models and Generation
- 技术分类键：generation
- 全文：https://www.isca-archive.org/interspeech_2026/zhou26i_interspeech.pdf

## 问题
下游分类上常把单一预训练 checkpoint 下的小幅 SFT 增益解读为“方法更好、天花板更高”，却默认 SFT 相对优劣在同类预训练实例间稳定。实际上骨干、预训练数据与配方交互强烈，单 checkpoint 结论可能缺乏外部效度。

## 方法
把 SFT 视为 capacity elicitation：配方差异主要反映对特定 checkpoint 的 elicitation match（激活可靠性），而非普遍抬高上限。在 FEATURE MODE（末层 / 倒数第 4 层 / 层加权和）与 FREEZE MODE（全微调 / 冻 CNN / 冻 CNN+前 N=4 层）上构造 8 种配置，作用于 wav2vec 2.0、HuBERT、WavLM 共 9 个 checkpoint；在 SUPERB 的 IC、ER、SID 上评测。用 McNemar 检验定义相对最优的 top-group；全矩阵默认 seed 1337，并对三个 base 模型额外用 seed 2048/7395。

## 实验与结果
表 2/3 显示 top-group 配方随 checkpoint 变化，同架构同规模但预训练数据不同时排序可翻转；部分“常进 top-group”的配方在个别 checkpoint 上严重 under-activation（异常低分仍完成训练）。多 seed 下同一配置可在 fully activated 与 under-activated 间双向切换。hubert-large 在 ER 上八种配方统计不可分，说明有时配方边际效应很小。约一万 GPU 小时（H20）。

## 结论
统计上“最优/同组最优”的 SFT 配方依赖预训练实例与 seed；表观增益常是激活匹配，而非普适更高天花板。应跨多 checkpoint 与多种子评估。

## 点评
把“方法进步”与“碰巧激活某 checkpoint”拆开，用 top-group 不稳定性与 seed 双向翻转直接打穿单点对比的外部效度，对 SUPERB 式对比实验很有警示意义。局限是配置空间仍沿特征层/冻结轴离散采样，未覆盖学习率等更广超参；结论偏方法论，不给出新 SOTA 配方。


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


# Privacy and quality trade-off in real-time speaker anonymization via editing of age and sex attributes

- 论文编号：2741
- 报告人：Waris Quamer
- 程序：Wednesday 30 September 2026 / Voice Editing
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/quamer26_interspeech.pdf

## 问题
说话人匿名化常把变换当黑盒，不清楚改哪些属性、改多少才能在身份抑制与音质间取平衡。实时流式系统尤其需要可操作的属性级调参指引。

## 方法
流式合成：因果 CNN 内容编码器（HuBERT-Kmeans 单元）+ X-vector/ECAPA 说话人编码器 + AdaIN/FiLM 适配器 + 因果 HiFiGAN。对说话人嵌入做 PCA，按与年龄/女性度（连续 sex）的 Pearson 相关构造复合方向 V_attribute，Z′=Z+Σ λ_attribute V_attribute。年龄/性别标签由 wav2vec2 预测器在 LibriTTS 上生成。用线性回归量化 |λ| 对余弦相似度与 DNS-MOS 的影响，并做 AMT 听感验证。

## 实验与结果
女性度比年龄更能压低余弦相似（β≈−0.459 vs −0.309）；二者对 DNS-MOS 亦均显著负向，女性度更强。隐私（相似）下降斜率陡于质量下降，约 ±0.25 std 附近存在 sweet spot。匿名化不对称：推向分布对侧更有效（如女性降女性度）。听感：中等修改约 83% 判为不同说话人，极端约 94% 但自然度显著下降；中等仅改女性度分化率约 98%，综合建议 λ_fem≈0.25、λ_age≈0 附近。延迟约束约 <350 ms。

## 结论
通过可解释的年龄/性别嵌入编辑，可刻画隐私–质量权衡并标出中等修改的最优匿名区；框架可推广到语速、口音等属性，意在指导调参而非刷新匿名化 SOTA。

## 点评
贡献是属性级计量而非新模型：把“改多少”用回归与听感钉死，对工程调参很实用。PCA 不完美解耦年龄–性别（经音高相关），交互项与不对称性说明方向需按说话人人口统计定制。身份代理是嵌入余弦而非完整攻击者模型，与 VoicePrivacy 式评测仍有距离。


# RIVET: Robust Idempotent Voice Attribute Editing

- 论文编号：395
- 报告人：Dareen Alharthi
- 程序：Wednesday 30 September 2026 / Voice Editing
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/alharthi26_interspeech.pdf

## 问题
属性条件嗓音编辑依赖年龄/性别等标签，大规模数据标注常噪声或不一致，易学到错误条件映射，导致编辑不稳、身份漂移；重复编辑会累积漂移。

## 方法
RIVET：ECAPA-TDNN 说话人编码 + 条件归一化流做属性编辑 + VITS 生成。在潜空间施加幂等约束：z_re=E(D(E(x))) 应接近 z，L_idemp=∥sg(z)−z_re∥²，总损失为 VITS + flow MLE + 年龄/性别分类 + λ_i L_idemp；对说话人与语音编码器均施加。相对 VoiceShop，端到端联合训练。对比同结构无幂等基线。

## 实验与结果
GLOBE（约 535 h、自然噪声标签）上，相对基线：还原编辑后 Titanet 余弦相似更高（年龄 0.66 vs 0.63，性别 0.55 vs 0.54），性别准确 85.9 vs 77.2；UTMOS/WER 相近。EARS OOD：相似与性别编辑更稳。受控标签翻转 10%–60% 时，RIVET 身份相似与属性表现更稳。重复重建 20 轮基线身份快速漂移，RIVET 保持更高相似。AMT 听感多数表决显示编辑成功率提升（尤其性别）。

## 结论
潜空间幂等正则在噪声标签下提升身份保持与编辑成功率，且不改架构；可推广到其他属性与编辑骨干。

## 点评
把“反复编辑应回到流形固定点”变成对噪声监督的隐式正则，比显式估标签置信度更轻。评测用“改再改回”的余弦相似直接对准稳定性。注意 GLOBE 年龄准确提升有限、EARS 上年龄准确略降，幂等不能替代干净监督；开源对可复现有帮助。


# FineCombo-TTS: Collaborative and Precise Controllable Speech Synthesis Using Text Descriptions and Reference Speech

- 论文编号：2280
- 报告人：Zhiyong Wu
- 程序：Wednesday 30 September 2026 / Voice Editing
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/zhou26h_interspeech.pdf

## 问题
可控 TTS 或靠参考语音（灵活差）或靠文本描述（细粒度不足）；近年联合方法仍松耦合——参考只管音色、文本粗改全局风格，跨模态协作弱。绝对属性对也不利于相对参考做增量控制。

## 方法
FineCombo-TTS：Speech Attributes Extractor（FACodec 音色 + Mel-Style 残差风格）得统一属性嵌入 E_a；CFM Speech Variance Predictor（1D UNet）在 T5 描述与源属性条件下学参考→目标变换；TTS 骨干自回归多层声学 token + DAC。两阶段：先训骨干与属性抽取，再训 Variance Predictor。构造 FineEdit 三元组〈源语音, 控制描述, 目标〉，覆盖韵律/情感/音色配对子集。推理支持联合、仅参考或仅描述；多 CFG（文本与描述掩码训练）。

## 实验与结果
相对同数据重训的 VoxInstruct-Joint：韵律控制 MOS-I 更高、Controlled Accuracy（速度/音高）更好、Uncontrolled Variation 更低、SECS 70.20 vs 56.79。情感准确 85% vs 47%；音色控制 MOS-I 3.75，FPC/Emotion-S 更优。消融：加强描述 CFG 提情感准确；残差风格编码器改善零样本 MCD/SECS。

## 结论
统一属性空间 + CFM 方差预测 + FineEdit 相对控制数据，实现参考锚定与文本精控的协同可控合成，优于松耦合联合基线。

## 点评
关键不在硬解耦属性，而在“相对变换”数据与 CFM 条件流；用 Controlled Accuracy / Uncontrolled Variation 把“改对目标、别动其他”测清楚。基线靠改 VoxInstruct 拼接参考，对比公平性尚可。局限是配对数据大量合成/自动标注，真实用户指令分布外推未充分验证。


# Edit Content, Preserve Acoustics: Imperceptible Text-Based Speech Editing via Self-Consistency Rewards

- 论文编号：1186
- 报告人：Yong Ren
- 程序：Wednesday 30 September 2026 / Voice Editing
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ren26e_interspeech.pdf

## 问题
基于文本的语音编辑需改内容却尽量听不出痕迹。直接在声学 token 上编辑内容–风格纠缠，易幻觉与边界伪影；NAR 韵律偏平，AR 稳健性不足。现有语音 RL 奖励多对准 TTS 指标，难保证编辑区与上下文无缝融合。

## 方法
原则 “Edit Content, Preserve Acoustics”：(1) 语义空间编辑：语义 tokenizer 得 token，PSM 格式条件填充中间段，Flow Matching 解码器重建波形（CosyVoice3 组件冻结）。(2) Self-Consistency Rewards GRPO：组采样估优势；冻结预训练 TTS 对编辑 token 的平均 log-prob 作一致性奖励；ASR WER 作可懂度奖励；门控要求 WER 与时长相对误差均 ≤0.2，否则奖励为 0。Libriheavy 监督预训练后再 RL。

## 实验与结果
Ming-Freeform-Audio-Edit（插入/删除/替换）上，语义编辑 + GRPO 相对 FluentSpeech、VoiceCraft、Ming-UniAudio 取得更低 WER、更高 SIM/DNSMOS/MOS；删除任务 GRPO 后 basic WER 降至约 0.47% 量级改进显著。Seed-TTS 子集掩码 0.5–2.5 s：长编辑下 WER/SIM 衰减更缓，GRPO 对长时长自然度增益更明显。

## 结论
语义空间解耦提供声学保持结构基础，TTS 一致性批评 + WER/时长门控的 GRPO 进一步做感知对齐，在多类编辑与长时长上优于主流 AR/NAR 基线。

## 点评
把编辑从声学 token 挪到语义 token，与“结构基础 + 感知对齐”两段叙事一致；用预训练 TTS 似然当隐式批评，比只追说话人相似更贴“听不出拼接”。门控防奖励黑客设计务实。SIM 主要靠冻结解码器，GRPO 对音色增益有限；依赖 CosyVoice3 组件与高质量对齐区间。


# Bagpiper-Edit: Zero-Shot Open-Ended Audio Editing via Rich-Caption

- 论文编号：631
- 报告人：William Chen
- 程序：Wednesday 30 September 2026 / Voice Editing
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/gong26b_interspeech.pdf

## 问题
文本引导音频编辑常依赖配对数据、固定原子操作模板，或拼多专家管线，难统一覆盖语音/音乐/环境声的开放式自然语言指令。直接用 caption–音频基础模型做编辑易忽略原音频，导致风格与身份漂移。

## 方法
Bagpiper-Edit 把编辑改写为 rich-caption 变换：先从原音频抽详细 caption，再由文本 LLM 按用户请求改写 caption，最后以原音频为声学锚生成目标音频。自监督学锚：音频重复（同一 clip 复制）与相邻切段（共享说话人/房间/背景）构造 (a1,a2,c1,c2)；训练 Single-Turn（拼接 caption/音频）与 Multi-Turn（两轮对话，先 a1 再 a2）两种模式。数据约 50 万样本，无配对编辑数据；骨干 Bagpiper-Base（Qwen3-8B + X-Codec）。

## 实验与结果
语音编辑：MT 转写 Acc 79.76%、WER 14.01%、SpkSIM 0.83，优于 Base 的严重身份丢失；情感准确可比专家，风格略弱。事件增删：MT 在一致性与编辑成功间更平衡（增 editCLAP 更高，删 FAD 更低）。开放式 rich-caption：MT CapSIM/LLM 分最高，ST FAD 最低但语义对齐较弱。作者建议默认用 MT。

## 结论
无配对编辑数据即可通过 caption 重写 + 自监督声学锚实现跨域零样本开放编辑；MT 对话模式在多数任务上更稳。

## 点评
把“改什么”完全放到文本空间，避开原子操作与配对数据，统一多域是亮点。自监督相邻段锚很巧。代价是转写全句替换受 LLM 改写误差传播，稳定性不及大量配对训的专家模型；复杂多说话人场景仍受 base 能力限制。


# HybridCodec: Fast Dual-Stream, Semantically Enhanced Neural Audio Codec

- 论文编号：3393
- 报告人：Arjun Gangwar
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/gangwar26_interspeech.pdf

## 问题
语义–声学解耦编解码有两路：蒸馏进 RVQ-1（快但语义弱）与双流+推理时 SSL（语义强但慢）。需要兼得解耦强度与推理速度。

## 方法
HybridCodec：公共因果 CNN 编码器（24 kHz→25 Hz）分语义/声学支路；语义 VQ（16384）经轻量 ConvNeXt 解码蒸馏 w2v-BERT-2.0 第 16 层（训练时冻结，推理去掉 SSL）；声学支路对“公共潜变量−语义解码”做 RVQ。GAN+谱重建+蒸馏训练。对比 DAC、DAC(Distill)、DualCodec。

## 实验与结果
60k 更新 LibriSpeech：HC-SED-AED RVQ-1 WER 15.36% 最优；高码本层重建具竞争力。跨语/零样本（SeedTTS-en、CV-French）语义仍强。相对 DualCodec 约 3× 加速（RTF 约从 0.042 量级降至约 1/3）。消融显示双流+蒸馏组合对 RVQ-1 最关键。

## 结论
双流结构加语义蒸馏可在无推理 SSL 下保持强 RVQ-1 语义与快速推理，适合下游语音 LLM tokenize。

## 点评
把 DualCodec 的解耦与 Mimi 式蒸馏拼成“训练重、推理轻”的折中，工程动机清楚。25 Hz 低帧率有利于长上下文 LM；声学质量与纯 DAC 仍有取舍。


# WavSLM: Single-Stream Speech Language Modeling via WavLM Distillation

- 论文编号：2803
- 报告人：Luca Della Libera
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/libera26_interspeech.pdf

## 问题
多数语音语言模型依赖文本预训练、多码本层级或混合架构，偏离文本式单流自回归范式。能否用单码本同时建模语义与声学？

## 方法
WavSLM：FocalCodec-Stream 将 WavLM-6 特征压成单流离散 token（50 Hz，可流式，块大小 4，理论延迟 80 ms）；解压特征接 WavLM-large 第 7–24 层作因果骨干，next-chunk 预测（C=4）。无文本监督，约在 Libri-Light 60k 小时训练。变体词汇量 2k/4k/65k（约 305–370M 参数）。滑窗注意力支持持续生成。

## 实验与结果
似然评测：WavSLM-4k 声学一致性 Avg 69.5，多项与更大文本预训练模型可比（如 Spk 88.5、Gend 90.5）。生成：WavSLM-2k UTMOS 3.72、Sim 91.8，优于 LLaMA-Mimi 1.3B/8B 的 UTMOS，且 RTF 更高。消融显示窗口与块大小影响一致性–质量权衡。

## 结论
充分表达的单码本表征可使纯语音、单流、可流式 SLM 在更小规模下达到有竞争力的一致性与生成质量。

## 点评
刻意剥离文本与多码本复杂性，把问题还原为“表征是否够好”。结果支持中层 WavLM+单码本路线；与 7B 级文本预训练模型比参数与数据更省，但口语内容任务仍有差距。


# VOSSA: Voiceprint Optimization for Streaming Speech Architectures

- 论文编号：2763
- 报告人：Mu-Ruei Tseng
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/tseng26c_interspeech.pdf

## 问题
流式 VC 常用冻结 ASV 嵌入，其设计刻意压制说话人内音素/韵律变化，与帧级声学生成冲突；另训说话人编码器又增复杂度。

## 方法
VOSSA 以 TVTSyn 为骨干：从冻结内容编码器的 CNN 末层与每隔一层 MHSA 特征拼接，经 ASP+MLP 得全局说话人嵌入，与 VC 目标联合训练，去掉外部说话人编码器。双路径训练：LibriTTS 自重建 + VoxCeleb 非平行转换。六数据集评测，并做 F0、F1 共振峰诊断与听感测试。

## 实验与结果
NISQA-MOS、WER 与 TVTSyn 相当；归一化目标相似度显著更高；HNR 接近 TVTSyn 且优于多数基线。自重建上 F0 MAE/PCC 与元音 F1 的 Wasserstein 距离最优。听感：相对 TVTSyn，说话人相似 46→54、可懂度 44→56、活力 48→52（百分比偏好）。

## 结论
中间层内容表征足以支撑说话人条件，可在保持流式延迟的同时改善音高动态与元音区分线索。

## 点评
把“说话人嵌入从哪来”从 ASV 惯性改到内容编码器中层，对准生成所需的音素条件可变性。声学诊断（F1/F0）比只报 SIM 更能说明表征差异。


# MeanVC 2: Robust Low-Latency Streaming Zero-Shot Voice Conversion

- 论文编号：1961
- 报告人：Guobin Ma
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ma26c_interspeech.pdf

## 问题
MeanVC 的 chunk 自回归去噪训练加倍序列长度、小块质量差，且 MRTE 直接吃参考 Mel，对低质参考敏感；160 ms 块端到端延迟约 211 ms。

## 方法
MeanVC 2：（1）Future-receptive chunking（FRC）按 DiT 层调度 past/future 注意力掩码，去掉 clean-chunk teacher forcing，支持 40 ms 块+有界未来上下文；（2）Universal Timbre Token Encoder（UTTE）由全局说话人嵌入建 UTT key–value，用 BNF 查询经交叉注意力取细粒度音色，降低对参考 Mel 质量依赖。仍用 mean flows 1-NFE。约 18M 参数。

## 实验与结果
Table 1：MeanVC 2 延迟约 109.9 ms，SSIM 0.710、SMOS 3.89、DNSMOS 3.89，全面优于同约 80 ms 输入窗的 MeanVC(80)；相对 MeanVC(160) CER/NMOS 略逊但延迟近半。消融：去掉前向掩码 CER 飙至 20.65%；去掉 UTTE SSIM 降至 0.682。参考鲁棒实验显示 UTTE 优于 MRTE。

## 结论
FRC+UTTE 使流式零样本 VC 在约 110 ms 延迟下显著提升相似与稳健性，优于原 MeanVC。

## 点评
同时打训练友好度、短块上下文与参考质量三个痛点，产品向很强。有界未来上下文是延迟–质量的明确旋钮。


# FlashTTS: Fast Streaming TTS with MTP Acceleration and X-pred Mean Flow Distillation

- 论文编号：1692
- 报告人：Hanke Xie
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/xie26b_interspeech.pdf

## 问题
对话系统要求 TTS 低延迟且支持流式文本输入；单码本 LLM-TTS 常需缓冲整句，自回归慢且多步流匹配抬高首包延迟。

## 方法
FlashTTS（Qwen2.5-0.5B）：滞后多轨堆叠输入（语音/文本/语言并行）支持增量文本；Stage2 加 Multi-Token Prediction 并行预测多 token；声学端用 X-pred mean flow + 块注意力，2-NFE 出 Mel，再 HiFi-GAN。约 30 万小时开源数据训练。与 CosyVoice2（10-NFE）等同规模基线对比。

## 实验与结果
MiniMax 多语子集：MTP-3（2-NFE）FPL 325 ms、TPS 73、RTF 0.632、WER 18.8、SIM 0.695；相对 CosyVoice2 的 FPL 843 ms/RTF 0.913/WER 26.2 明显更快更清晰。Stage1 2-NFE FPL 377 ms。CMOS 与基线接近或略优。

## 结论
原生流式输入轨 + MTP + 2-NFE mean flow 可把首包延迟压到约 325 ms，同时保持零样本克隆与跨语可懂度，适合作对话级联 TTS。

## 点评
同时砍“等整句”与“慢解码”两条延迟路径，工程完整。MTP 抬速时对 SIM/CMOS 有轻微代价，需按场景选 MTP-3/5。


# Prosodic Boundary-Aware Streaming Generation for LLM-Based TTS with Streaming Text Input

- 论文编号：1192
- 报告人：Changsong Liu
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/liu26i_interspeech.pdf

## 问题
流式文本输入的 LLM-TTS 缺前瞻导致韵律差，且交错生成历史无限膨胀引发长文崩溃；强对齐标注成本高。

## 方法
对预训练 CosyVoice2 LLM 做韵律边界感知后训练：用 WhisperX 弱时间对齐，随机插入 boundary marker 并截断对应语音目标，教模型在有限未来文本下提前停。推理时每 k 词一块、lookahead f 词，滑动窗口用上一块文本/语音作 prompt，KV 缓存 O(k+f)。流匹配与声码器冻结。

## 实验与结果
Seed-TTS-Eval：标准句 WER 4.03%、长文 4.77%；交错基线长文 WER 70.97%（摘要写 71.0%→4.8%）。说话人/情感相似长文显著更高（SPK-SIM 0.65 vs 交错 0.56；相对摘要称 +16.1%/+1.5%）。主观长文 MOS 4.13 vs 交错 3.18。TTFA 约 1296 ms，RTF 0.782。

## 结论
仅用弱对齐后训练即可让现有 LLM-TTS 在流式文本输入下稳定长文合成并改善韵律，无需改注意力结构。

## 点评
边界标记 + 有界滑动窗口直接对准“韵律缺前瞻”与“长文崩溃”两大痛点，且不改架构，迁移成本低。长文 WER 断崖式改善是最强证据。


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


# PF-D2M: A Pose-free Diffusion Model for Universal Dance-to-Music Generation

- 论文编号：248
- 报告人：Jaekwon Im
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/im26_interspeech.pdf

## 问题
现有 dance-to-music 多依赖单人人体姿态（SMPL/2D 关键），难覆盖多人舞、非人类角色，且姿态估计抖动；公开数据（如 AIST++）歌曲少、背景简单，易过拟合、难泛化到真实视频。

## 方法
提出 PF-D2M：用 Synchformer 视觉特征代替姿态，条件 DiT（初始化自 Stable Audio Open 的 VAE/DiT）生成音乐 latent；文本用 T5-base 交叉注意力；视觉特征上采样后与 DiT 输入通道拼接，并经 AdaLN 调制；速度预测 + CFG。渐进训练：Stage 0 保留文本–音频生成能力；Stage 1 在 VGGSound 上学视听同步；Stage 2 按 2:4:1 混合 AIST++、FMA/MoisesDB（无演唱过滤后约 191h）、VGGSound 微调，文本侧用空视觉 embedding。推理 DPM-Solver++ 100 步、CFG=5。

## 实验与结果
AIST++（按未见曲目切测试集）客观节奏指标：PF-D2M (S2) BHS 99.8、HSD 1.9、F1 94.3，多数指标 SOTA，BCS 略低于 Text-Inv/LORIS。主观（20 人、四类野外视频：单/多人 × 人/非人）：对齐与音质均明显优于 LORIS、Text-Inv，多人与非人场景差距更大。Stage 2 相对 Stage 1 结构更连贯、更少“现场收录感”。

## 结论
无姿态、用视频视觉特征 + 渐进训练，可在多样舞姿视频上生成对齐且音质更好的音乐；局限是生成时长较短，且缺合适客观评测集。

## 点评
用 Synchformer 视听同步特征绕开姿态管线，再靠 Stable Audio 初始化与多模态混合微调缓解 AIST++ 过拟合，路线清晰。节奏指标相对 GT 对齐，难反映“另有合理节奏”的感知质量，作者也强调主观评测更关键。脆弱处是短片段生成、依赖文本标签质量，以及野外场景仍可能受视觉噪声与剪辑影响。


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


# MOS-Bias: From Hidden Gender Bias to Gender-Aware Speech Quality Assessment

- 论文编号：67
- 报告人：Wenze Ren
- 程序：Wednesday 30 September 2026 / Speech Synthesis Evaluation 2
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ren26_interspeech.pdf

## 问题
MOS 是语音质量金标准，但听者人口学偏差少被系统研究。若男女听者评分标准不同，简单平均会掩盖组间差异，并可能把某种性别的感知标准写进自动 MOS 模型。

## 方法
在 BVCC（含听者/说话人性别元数据）上分析性别差异；基线用 SSL-MOS。提出 gender-aware 架构：共享 SSL 编码器 + Mean Net（总体 MOS）与 Gender Net（条件于抽象二元组嵌入 0/1，不直接喂性别标签），输出 Avg / Male / Female MOS；多任务等权 MSE（L_avg + L_male + L_female）。

## 实验与结果
男性听者评分系统性高于女性（总体 2.988 vs 2.886，Welch t 检验显著）；差距随质量下降而增大（1–2 档差 0.167，4–5 档仅 0.030）。无性别信息的 SSL-MOS 预测更贴近男性 GT（句级 MSE 0.372 vs 女性 0.430）。Gender-MOS 相对 baseline：全听者句级 LCC 0.862 vs 0.853、MSE 0.239 vs 0.290；男性分支 MSE 0.332、女性 0.366，均优于 baseline。

## 结论
MOS 性别偏差是系统性、质量依赖、可学习的；平均标签与其上训练的模型隐含偏男性标准。抽象组嵌入可提升总体与性别特异预测。未来拟做偏差缓解并在更多数据集验证。

## 点评
把听者性别从“标注噪声”升格为可建模结构，并指出简单全局校准不够（差距随质量变），问题抓得准。抽象 0/1 组嵌入既保留基线“性别中立”接口，又逼模型从数据中挖出两组模式，是务实折中。局限是目前仅 BVCC 有完整性别元数据；且“更准预测各组”不等于“更公平的评估标签”，后续仍需明确公平目标（校准、再加权还是报告分组分数）。


# TDScore: Learning Synthetic Speech Quality Predictors from TTS Training Dynamics without Human annotation

- 论文编号：449
- 报告人：Natacha Miniconi
- 程序：Wednesday 30 September 2026 / Speech Synthesis Evaluation 2
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/miniconi26_interspeech.pdf

## 问题
主观听测贵、难扩展；有监督 MOS 预测器仍依赖大量人工标注，且跨语言/合成范式泛化差。需要不依赖听者标注、又能服务 TTS 开发（如 checkpoint 选择）的质量信号。

## 方法
TDScore：从零训练 TTS，定期合成并收集中间 checkpoint 音频，用训练迭代 k 与训练 loss 作伪标签；用外部客观质量曲线截断饱和 checkpoint，并加入自然参考句。基于 SSL-MOS 架构，分别训练预测归一化迭代（Ite）与标准化 loss 的模型，用 pairwise ranking（BCE over score differences）。TTS 骨干：FastSpeech 2、FastPitch、F5-TTS，均在 Blizzard 2023 法语 NEB 约 51h 上训练。

## 实验与结果
域内 BC（法）：TDScore–F5–Ite 系统/句级 SRCC 0.74/0.54，优于 DeepFake proxy（0.60/0.50）等无 MOS 方法，并接近/超过部分有监督结果。域外 BVCC：F5–Ite 0.73/0.66；SOMOS：0.38/0.22。迭代预测在自建测试集上最强（F5–Ite 句级 0.90）；loss 预测更不稳，且整体 Ite 优于 Loss。作者归因于 loss 振荡、迭代更能表征学习状态，且 F5 训练中质量提升更平滑。

## 结论
TTS 训练动态，尤其是迭代索引，可作为无人工标注的合成质量伪监督；跨语言仍有差距但优于若干无 MOS 代理。局限是依赖当前 TTS 训练轨迹形态，统一多架构联合训练是未来方向。

## 点评
用“checkpoint 质量单调改善”作免费标签，直接对准开发期需求，比再造一套 MOS 数据更省。Ite 稳、Loss 弱也符合直觉：loss 样本依赖且震荡。脆弱处在于伪标签质量高度依赖“训练过程是否真有可感知递进”——非 F5 架构相关性明显变差，说明方法对生成范式敏感，扩展到任意未来 TTS 前需要更稳的 checkpoint 筛选与多系统联合训练。


# Exploring Active Sampling Strategies for Pairwise Comparisons in Speech Synthesis Evaluation

- 论文编号：446
- 报告人：Korin Richmond
- 程序：Wednesday 30 September 2026 / Speech Synthesis Evaluation 2
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/valentinibotinhao26_interspeech.pdf

## 问题
偏好类听测（AB、BWS）比 MOS 方差更小、更少量表偏差，但因“必须测全对”的误解采用不足。在听者少、时长紧（如濒危语言 TTS）场景下，需要更高效的系统对采样策略。

## 方法
用 Blizzard 2013 刺激（自然音 + 5 个旧系统 + 4 个神经系统，共 10 系统）先做覆盖尽可能多对/元组的 AB 与 BWS 听测（Prolific，排除后 AB 54 / BWS 57 人）。再从已收集答案库中回放三种采样：随机、merge-rank（MR，含随机/正确初始排序与不同每对最大请求数）、ASAP（信息增益 + batch，每轮 9 对）。BWS 侧对请求对做贪心检索以覆盖 batch。用 TrueSkill 估计分数，报告显著成对差异数与对全量排序的 Kendall 相关。

## 实验与结果
AB 与 BWS 上 ASAP 在显著差分数与排序相关上均最好；MR 因逐对深挖、中间覆盖不全，收敛前显著差更少。按估计听测时长（AB 约 16.9s/题、BWS 约 36.6s/题）对比：同等时长下 BWS 优于 AB，ASAP 再放大差距。实践对照：约 10 人、20 分钟 ASAP-BWS（约 200 听测分钟）约等于 40 人同等时长 AB（约 800 分钟）。

## 结论
ASAP 主动采样能更快揭示系统差异并逼近全量排序；BWS 比 AB 更省时长效率；二者组合适合听者/时长受限的评估设计。

## 点评
用“全覆盖听测作答案银行 + 离线回放采样”干净地比较算法，避开了在线听测噪声。结论对濒危语言等少听者场景很实用。需注意：刺激含明显强弱系统，小间距 SOTA 场景下 ASAP 优势可能更关键（文中亦引用 ASAP 原作者小范围条件结果）；且 BWS 检索不保证请求对一定被 best/worst 命中，信息增益实现依赖工程细节。


# Decoding the Ear (DeEAR): A Framework for Objectifying Expressiveness from Human Preference Through Efficient Alignment

- 论文编号：2408
- 报告人：Zhiyu Lin
- 程序：Wednesday 30 September 2026 / Speech Synthesis Evaluation 2
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lin26l_interspeech.pdf

## 问题
语音到语音（S2S）模型可懂但常缺表现力；主观评分贵，低层声学特征又抓不住感知细微差别。需要把人类对 expressiveness 的偏好对齐成可扩展客观指标，并用于数据筛选与模型改进。

## 方法
DeEAR 四阶段：将表现力拆为 Emotion（wav2vec2 细调 arousal，CNSCED+IEMOCAP）、Prosody（Gemini-2.5-Pro CoT 评分，SRCC=0.73）、Spontaneity（DNSMOS 启发的伪标签 + 对“过干净但朗读感”惩罚，再蒸馏到 wav2vec2）；用约 480 条人工标注、XGBoost 非线性融合三子分；再蒸馏为单一 DeEAR-Base（wav2vec2-xlsr-53 多任务）。应用：按 DeEAR 从开源情感对话语料筛出约 14K 句 ExpressiveSpeech（约 51h），微调 S2S 基座。

## 实验与结果
与专家 MOS：总体 expressiveness PCC/SRCC 0.91/0.85；DNSMOS/UTMOS 反而与表现力负相关。七个 SOTA S2S 基准：DeEAR 与人类排序 SRCC=0.93，Doubao 最高、Qwen2.5-Omni/Gemini 靠后。S2S-FT vs Base：盲听偏好 78.5% vs 10.0%；客观 S_expr 从 2.0 升到 23.4，情绪与自发维度增益最大。

## 结论
少量标注即可得到与人类偏好对齐的多维表现力指标；用其做评估驱动数据策展，能显著提升 S2S 感知表现力。未来拟接入强化学习做端到端优化。

## 点评
把“表现力”拆成可学子任务再非线性融合，比直接回归抽象 MOS 更贴感知瓶颈（一文指出单维短板会卡死总分）。Prosody 依赖 Gemini、Spontaneity 依赖启发式伪标签，可扩展但外部模型与阈值选择会进指标本身；ExpressiveSpeech 顶 15% 阈值经人工审计，说明指标仍需人校准。DNSMOS/UTMOS 与表现力负相关，提醒“干净度指标”不能当表现力代理。


# CodecMOS-Accent: A MOS Benchmark of Resynthesized and TTS Speech from Neural Codecs Across English Accents

- 论文编号：1273
- 报告人：Wen-Chin Huang
- 程序：Wednesday 30 September 2026 / Speech Synthesis Evaluation 2
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/huang26f_interspeech.pdf

## 问题
神经音频编解码（NAC）与基于其的 LLM-TTS 基准多偏重建质量与客观指标，少主观、少口音等非标准语音。口音相似度如何评、客观指标是否管用、听者口音是否引入偏差，尚缺大规模证据。

## 方法
构建 CodecMOS-Accent：从 VCTK 选 32 说话人、10 口音、160 真值句；9 个重合成 NAC（含低码率配置）+ 15 个开源 voice cloning TTS，共 4,000 样本。众包 25 听者、19,600 标注，三维 5 分：自然度 S-NAT、说话人相似 S-SPK-SIM、口音相似 S-ACC-SIM；并算 O-WER、O-SPK-SIM、O-ACC-SIM、O-UTMOS。

## 实验与结果
真值在 S-NAT 仅排第 9，但说话人/口音相似最高；低层 SpeechTokenizer 仍保留可感说话人与口音线索。系统级：S-SPK-SIM 与 S-ACC-SIM 相关 0.97（句级 0.75）；O-UTMOS 与 S-NAT 相关 0.96；O-SPK-SIM 对 S-ACC-SIM（0.90）甚至高于 O-ACC-SIM（0.81）；O-WER 与主观相关弱。同口音听者对 SPK/ACC（及全数据上的 NAT）给分更高（同口音偏差）。

## 结论
该数据集是作者所知对口音上 NAC/TTS 主观评估规模最大的工作之一；揭示说话人–口音强耦合、客观指标预测力，以及听者口音偏差。拟公开数据并用于训练更好 SQA、尤其口音相似度直接人标监督。

## 点评
把 ICL 式 voice cloning 的“说话人/口音克隆”拆成独立主观维，并系统对比重合成 vs TTS，填补了编解码基准缺主观、缺口音的空白。UTMOS 对 2020 年后系统仍高度相关，提醒“新架构≠绝对质量跃迁”。同口音偏差与听者以美式为主的构成，限制了“普遍自然”结论；口音嵌入指标未必优于说话人嵌入，说明口音客观度量仍需人标驱动。


# MMGenre: Benchmarking Singing Voice Synthesis across Multiple Musical Genres

- 论文编号：137
- 报告人：Wenhao Feng
- 程序：Wednesday 30 September 2026 / Speech Synthesis Evaluation 2
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/feng26_interspeech.pdf

## 问题
歌唱合成（SVS）进步快，但公开数据与评测严重偏流行乐，难系统分析跨流派泛化。流派作为整体风格条件在 SVS 中几乎未被当作一等评测维度。

## 方法
提出 MMGenre：用 Suno V4.5 按层级流派提示生成音乐，Mel-RoFormer 分离人声，STARS 标注音素音高时长，经时长/流派一致性（MuQ-MuLan）过滤与少量人工核验，得到 10 大类、26 子类、3,152 段中文分数–音频对（约 4.36h）。评测 RNN、XiaoiceSing、VISinger/2、DiffSinger、StyleSinger、TCSinger、TechSinger 等；核心指标 GCS-5（Gemini 2.5 Pro 五分流派一致性，与人 Spearman ρ=0.85），辅以 SingMOS 等与 CER。

## 实验与结果
各模型流派剖面高度相似，强对齐集中在 Pop 及相关类，非 Pop（Rock/Rap/Classical 等）普遍低分；合成嵌入跨流派重叠（相对真值可分），呈现“流派坍塌”。零样本风格迁移/技巧控制对 Classical/Rock/Rap 仅小幅抬 GCS-5，远低于 GT。用约 2h Rock 继续训练后 GCS-5 从约 1.5 升至 4.9。整体伪 MOS/CER 仍反映合成质量进步。真/合成 Pop 上模型 MOS 排序相关 ρ=0.90，支持基准相对有效性。

## 结论
MMGenre 提供多流派 SVS 诊断框架；当前模型流派意识强依赖训练分布，而非分数条件可轻松迁移。有限流派专用微调远优于零样本控制。

## 点评
用 T2M 扩流派覆盖是务实数据策略；“坍塌 vs 真值可分 + 微调即大幅回升”把问题钉在数据先验而非符号可控性上，对社区很有诊断价值。GCS-5 依赖 Gemini，且微调后略超 GT 可能含“子类夸张”伪影；中文、AI 生成人声为主，外推到真人多语料库需谨慎，但相对排序在 Pop 验证上已站得住。


# Decoding Order Matters in Autoregressive Speech Synthesis

- 论文编号：1339
- 报告人：Minghui Zhao
- 程序：Thursday 1 October 2026 / LLM Based Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhao26e_interspeech.pdf

## 问题
自回归语音合成默认从左到右生成，但声学依赖含全局韵律与前后协同发音；解码顺序是否最优、如何在统一框架比较，尚缺系统研究。

## 方法
用掩码扩散（MDM）训练顺序无关模型，推理可任意置换逐帧解掩。为隔离编码器归纳偏置，对 Mel 做参数无关标量量化（Q=100）并用现成 HiFi-GAN。比较 l2r、r2l、随机、top1 置信自适应、时长引导段内随机，以及 β 控制的随机插值。

## 实验与结果
LJSpeech：r2l 多项客观指标优于 l2r；top1 MOS 3.91（系统输出最高），vocoded 参考 3.99，r2l 3.87，uro 最差 3.50。top1 局部多为右→左连续扩展（ρ_r2l≈0.9）。量化 Mel 仍可被 HiFi-GAN 较好重建。随机性增大时 MCD 降、UTMOS 降，WER 非单调。

## 结论
左到右并非最优；有效顺序常保持局部连续帧簇并偏向局部右到左，以兼顾长程依赖与局部连贯。解码顺序应作为合成质量的关键建模选择。

## 点评
用 MDM + 标量 Mel 把“顺序”从 token 学习中干净拆出，结论有说服力。单说话人朗读语料与帧级更新限制外推；是否迁移到多说话人/神经编解码 token 仍待验证。


# Decoupling Search and Evaluation: Efficient Beam Decoding for Language Model-Based Text-to-Speech Synthesis

- 论文编号：1531
- 报告人：Chenlin Liu
- 程序：Thursday 1 October 2026 / LLM Based Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/liu26l_interspeech.pdf

## 问题
LM-based TTS 多依赖采样解码，存在随机不稳定；beam search 虽是最大化解码，但在语音生成中易出现时间坍塌（长时间静音/噪声循环），且推理延迟过高。作者分析发现 beam search 约 98% 时间花在搜索扩展上，评估只占很小比例。

## 方法
提出 SaVE-Beam：将假设扩展与序列打分解耦。轻量 student（自蒸馏，温度 τ=2，强调高概率 token 排序）做 chunk 级 beam 树构建；原 teacher LM 做精确评估与最终选择。Chunk 长度 L，学生扩展后由教师树解码、top-K 过滤，并用类似 speculative decoding 的接受比 rt 与阈值 α 做确定性验收，按接受长度与教师对数概率选路径。搜索阶段对近期窗口 w 内已出现 token 做硬屏蔽（概率置零再归一化），避免软惩罚在最大化解码下仍坍塌。另用动态剪枝保留 top-N 节点。

## 实验与结果
在 CosyVoice 2 上实现，训练集 LibriTTS 与 WenetSpeech4TTS premium，评测 SeedTTS-Eval。相对 TRAD-BS，LM 解码加速约 3.9×–5.1×；相对采样 baseline，en/zh 的 W/CER 分别可降约 50%/33%，速度接近 baseline（如 SaVE-Beam-2h：en TPS 22.21、WER 1.83；zh TPS 23.92、CER 0.84）。RTF 从 TRAD-BS 的 4.95 降到约 1.18–1.19。消融表明硬重复约束对抑制时间坍塌关键；去掉动态剪枝可在 test-hard 上进一步改善 CER。

## 结论
通过搜索–评估解耦、chunk 扩展与硬重复约束，SaVE-Beam 可在接近采样系统实时性的前提下，使最大化 beam 解码在 LM-TTS 中实用，并显著降低生成错误。

## 点评
核心洞察是把昂贵的 beam 扩展交给小模型，把目标函数仍交给原 LM，并用硬结构约束补救语音 token 低信息密度带来的坍塌。与把解码完全交给蒸馏学生不同，质量门槛仍由 teacher 决定；学生引入的受控随机性在 hard 集上甚至可能帮助逃离局部最优，这是设计上的有趣副效应。脆弱点在于 chunk/窗口/α 等超参与 student 容量：太弱会频繁拒收而抵消加速，软惩罚替代硬约束则会重新坍塌。


# Eliminating Stability Hallucinations in LLM-based TTS models via Attention Guidance

- 论文编号：1345
- 报告人：Shiming Wang
- 程序：Thursday 1 October 2026 / LLM Based Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/wang26x_interspeech.pdf

## 问题
LLM-based TTS 缺少显式 text–speech 对齐，在长文本/难文本上易出现稳定性幻觉（重复、无尽生成、漏读）。早期 cross-attention 单调约束不适配 decoder-only；硬单调注意力又伤自然度；强制对齐标签在大规模数据上难以获得。

## 方法
在 CosyVoice2（Qwen-0.5B，24 层×14 头）上分析自注意力，发现中层存在类似 cross-attention 的“alignment heads”。提出 Optimal Alignment Score（OAS）：对 speech→text 注意力子矩阵用 Viterbi 求最优对齐路径，再取路径概率占比；OAS 与 WER 相关系数约 −0.638。将第 8、9 层半数头指定为对齐头并 mask 到对齐区域，用可微 OAS 正则 LOAS 监督。进一步做 attention-guided CoT 学生训练：用教师最高 OAS 头路径作伪强制对齐；学生预测稀疏重复文本 token（非整段重复）与 progress bar 位置值（L1 + 一阶差分非负约束），且预测文本不回灌输入，减轻伪标签误差累积。

## 实验与结果
WenetSpeech4TTS 从头训 LLM；Seed-TTS-Eval 与 CV3-Eval 上评 hard/common。相对 CV2，CV2 OAS 在 hard 上 WER 分别降约 2.1%/1.6%（Seed hard 13.568%→11.472%；CV3 hard 10.239%→8.657%），SIM/UTMOS 不降。CV2 AG（sparse text + progress bar）进一步到 Seed hard WER 9.984%、CV3 hard 6.660%。稀疏文本监督的 token 准确率明显高于 full text（train 97.10% vs 90.44%）。common 场景 MOS 略升或持平。

## 结论
用 OAS 损失与注意力引导训练，可在难文本上减少 CosyVoice2 的稳定性幻觉，且不明显损害自然度与相似度，且无需真实强制对齐标签。

## 点评
做法抓住的是 decoder-only TTS 里“对齐头可学、可监督”这一结构：先度量再约束，再用伪对齐做 CoT，比硬单调推理更贴合语音连续性。稀疏重复 + progress bar 是对伪标签不准与重复句式的务实修补。潜在脆弱处是对齐头层位与头选择依赖该 backbone 的统计（文中锁定 8–9 层），换模型需重标定；伪对齐质量上限仍受教师稳定性约束。


# MamTra: A Hybrid Mamba-Transformer Backbone for Speech Synthesis

- 论文编号：1031
- 报告人：Tan Dat Nguyen
- 程序：Thursday 1 October 2026 / LLM Based Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/nguyen26c_interspeech.pdf

## 问题
LLM-TTS 依赖自回归 Transformer，长序列下自注意力二次复杂度与 KV cache 膨胀，限制播客/有声书/边缘部署。纯 Mamba 线性高效但全局上下文与表达力不足；已有混合方案多需昂贵从头预训练且细节不公开。

## 方法
提出 MamTra：在预训练 CosyVoice 2 上按多种策略（Interleaved BlockBeg/End、Contiguous Front/Middle/Back/Sandwich、数据驱动 Importance）把部分 Transformer 换成 Mamba，比例 1:1 到 1:11。用注意力线性化与 SSM 的结构对应，把教师 Q/K/V 投影初始化到 Mamba 的 C/B/x。再用多层蒸馏恢复性能：L = LCE + Llogits（skew KL）+ Lemb（token embedding MSE）。训练只用约 0.5k 小时 LibriTTS（约为教师英语数据的 2%）。

## 实验与结果
评测 Seed-TTS-eval test-en 与 LibriTTS test-clean。MamTra 1:1（BlockBeg）相对 CosyVoice 2：VRAM 可降约 34%，每 token FLOPs 在上下文 2048 时最多省约 1.4×10^11；WER 仅绝对升约 0.25%（2.03→2.28），NMOS/UTMOS/SSIM 接近教师。更激进 1:11 时可懂度明显下降。BlockBeg 在低成本扫描中 CE/WER 更稳；高替换比时 WER 重要性选层更有效。消融显示去掉 LCE/Llogits/Lemb 都会抬高 WER；重用预训练权重收敛远快于 Xavier/Kaiming。

## 结论
通过结构化替换、权重迁移与多层蒸馏，MamTra 可在很少数据上恢复教师级质量，并显著降低推理显存与计算，适合内存受限的长上下文 TTS。

## 点评
价值在“转换预训练 Transformer→混合骨干”而非从零训 SSM：把二次注意力瓶颈换成局部线性状态，同时保留少量全局层。BlockBeg + 适度替换比是效率–质量甜点；过度替换（1:11）会跌破可懂度底线。脆弱点包括蒸馏对教师分布的依赖，以及 Importance/WER 选层在新域是否可迁移。


# DLLM-TTS: Block Discrete Diffusion Language Model for Text-to-Speech Synthesis

- 论文编号：788
- 报告人：Wasim Madha
- 程序：Thursday 1 October 2026 / LLM Based Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/madha26_interspeech.pdf

## 问题
自回归 codec LM 音质与可懂度好，但需大规模数据且逐 token 解码延迟高；非自回归流匹配/扩散虽并行，常需显式时长建模或对齐弱，易漏词/重复。块离散扩散（BD3-LM）在文本上有效，尚未用于条件语音 codec 生成。

## 方法
DLLM-TTS 把 TTS 建成对 X-Codec2（单流 FSQ，|V|=6561，50 Hz）token 的条件块离散扩散。序列切成块（默认 B=32，约 0.64 s），块内掩码扩散并行预测，块间顺序生成。用 staircase attention：噪声块内双向、对前序干净块因果、干净块内因果。训练最小化掩码位置交叉熵；用 EOS 处理变长，无需显式时长。0.6B Transformer 自 Qwen2 初始化。推理：参考文本+参考 codec + 全掩码生成段；每块最多 T 步置信度采样（τ=0.6），可提前停止；默认 T=16 时 RTF=0.15。

## 实验与结果
两阶段：Emilia 采样 16K 小时 20 epoch，再 4K 小时高质量合成数据微调，合计约 20K 小时。Seed-TTS-eval（英）：WER 2.25、CER 1.05、SIM 0.750、MOS 4.25，接近或优于若干更大数据/参数系统。消融：T 从 8→32，WER 14.58%→2.25%；T=64 反而变差。B=32 优于 8/16。掩码目标被视为隐式数据增强，解释相对自回归的数据效率（相对 60K–250K 小时约 3–12× 减少）。

## 结论
块离散扩散可在无显式时长标注下兼顾局部声学一致性与跨块文本对齐，以较小数据与 RTF 0.15 实现实用、有竞争力的零样本 TTS。

## 点评
关键是把“块内并行 + 块间因果”对准语音的局部相干与全局对齐需求，staircase mask 替代了时长模型。速度–质量由 B 与 T 直接调节；T 过大变差说明过度去噪并非单调受益。相对纯 NAR，保留了顺序结构；相对纯 AR，换来并行与数据增强。脆弱处包括块边界伪影风险（文中主观 MOS 未明显受损）以及对 codec 单流设定的依赖。


# Bagpiper-TTS: Natural Language Guided Universal Speech Synthesis

- 论文编号：873
- 报告人：Haoran Wang
- 程序：Thursday 1 October 2026 / LLM Based Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/tian26_interspeech.pdf

## 问题
传统 TTS 依赖固定槽位式输入（文本+预定义元数据），与真实用户自然语言请求不匹配；多说话人对话、角色扮演、歌声等任务又难以在单一管线中灵活统一。

## 方法
Bagpiper-TTS 以 Bagpiper-Base（Qwen3-8B-Base + 50 Hz 多流 X-Codec，8 codes/帧，600B token 预训练）为骨干，采用 Planning–Caption–Generation：先文本规划理解意图，再生成长达数百 token 的 rich caption（转写+副语言/声学蓝图），最后据此合成语音。微调数据用六步仿真：音频精选→自动 caption→WER 过滤→LLM 反推用户请求→规划过程仿真→LLM 一致性校验（均分>3.5）。覆盖 classical / multi-talker / intent-to-speech / role-play / SVS / general-purpose，共约 738k 样本。推理对文本与语音用解耦 Top-k，语音侧 CFG λ=3。

## 实验与结果
SFT 2 epoch。Seed-TTS-Eval (En) classical WER 1.7%（Qwen3-TTS 1.5%，CosyVoice 2 2.6%）。四类进阶任务：LLM-as-a-judge 均分约 4.09，人工 MOS 均约 3.69；如 Multi-Talker WER 4.2 / TF 4.23，SVS WER 7.2 / TF 4.60（相对 YuE WER 11.0）。定性显示能处理倒序计数、委婉批评等需推理的请求。系统不接受参考音频，故未测 speaker similarity。

## 结论
以自然语言与 rich caption 为统一接口，单一模型可覆盖多种合成应用，classical TTS 可懂度接近前沿专用系统，进阶任务在裁判与主观评价上整体可用。

## 点评
核心是把“槽位控制”换成“可扩写的文本蓝图”，让预训练 caption↔speech 对齐直接承接任意用户话术。数据仿真与严格校验决定上限；general-purpose 子集试图覆盖未定义场景。脆弱点包括 caption 幻觉需 WER/多模态校验兜底、相对专用模型在部分主观分上仍有差距，以及无参考音色克隆能力。


# PolyBench: Benchmarking LLM-based TTS Systems for Chinese Polyphone Disambiguation

- 论文编号：998
- 报告人：Feifan Chen
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/lu26_interspeech.pdf

## 问题
LLM-TTS 直接吃文本、多音字消歧隐式完成，ASR 的 CER/WER 难抓发音错；既有中文多音字评测集存在标注错误、覆盖不足与领域偏斜。

## 方法
构建 PolyBench：从《现代汉语词典》第 7 版筛出 494 个高频多音字与 88 个多音词，DeepSeek 生成句子并人工校对，得 Main（6016 句，含 Common/Surname/Dialectal/Colloquial/Literary）、DictWords（2137 词）与 ALLinONE（494 句、同句多读）。用 Qwen3-Omni-Instruct 自动标发音（ALLinONE 上标注准确率 93.06%，接近人工）。评测 3 个 G2P 与 17 个 LLM-TTS，指标 CER、Poly-CharAcc、Poly-PyAcc。

## 实验与结果
Main 上 FireRedTTS-2 最佳，Poly-PyAcc 82.02%（Common 86.01%），仍有约 18% 错读；方言/口语类全面偏低。CharAcc 系统间差约 4%，PyAcc 差约 15%，且 PyAcc 常低于 CharAcc 10–20 个百分点。DictWords 上多数更高、系统差距更大；ALLinONE 上最优也仅 202/494 字全对。G2PW 在姓氏/文言类仍有竞争力。

## 结论
PolyBench 暴露当前 LLM-TTS 多音字消歧仍不足，尤其方言与口语；Qwen3-Omni 可作大规模自动标注器。未来拟扩大字表并改进拼音标注。

## 点评
把“能认出字 ≠ 读对音”拆成 CharAcc/PyAcc，击中 LLM-TTS 评测盲区。自动标注误差会扰动绝对值，但大差距排名仍可用；口语类与词典标音本就不一致时，低分可能混入标注定义问题。


# Towards a Phonology-Informed Evaluation of Multilingual TTS

- 论文编号：3311
- 报告人：Neeraj Kumar Sharma
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/raybarman26_interspeech.pdf

## 问题
MOS 等自然度指标不检验语言特有音系对立；阿萨姆语 ATR 元音和谐由语法决定共现，TTS 可能“好听”却中和或错放和谐条件对比。

## 方法
用 14 名母语者录音（8125 元音 token）建人类基准，提取 Lobanov 归一化 F1–F3、B1、时长及高度/前后特征；Meta MMS TTS（mms-tts-asm）合成同载体句（281 token）。Task 1：LR/RF 做跨域 ATR 分类（H→H、H→TTS 等）。Faithfulness audit：比金标 ATR 与分类器预测，区分 overgeneration（−→+）与 underproduction（+→−）。Task 2：词级三分类和谐类型，用声学聚合与金标/预测 ATR 序列特征。

## 实验与结果
LR 的 H→H 与 H→TTS 准确率均约 82%，宏 F1 0.81；RF 域内更高但迁移落差大。TTS 错配率 0.16，但 underproduction:overgeneration≈7:1（人类近对称）；[+ATR] 中元音 /e/、/o/ 约 1/3 token 被判为 [−ATR]。词级上 H→TTS 时 A+B_pred（宏 F1 0.62）优于 A+B_gold（0.49），说明声学 ATR 轮廓与意图音系不一致。

## 结论
MMS 对中元音 [+ATR] 声学线索系统性 underproduce；框架可推广到其他有可测声学线索的音系对立，但本文仅单系统、单现象、TTS 样本小且类别不平衡。

## 点评
把“听感尚可”与“音系忠实”拆开，用人类训练分类器当声学探针，比 MOS 更对准语法条件对立。结论强度受 TTS token 少（尤其 AgrNoMixYes）与类不平衡约束；方向性偏置比总错配率更有诊断价值。


# An Evaluation Framework for Text-to-Speech Voice Reconstruction

- 论文编号：2600
- 报告人：Ariadna Sanchez
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/sanchez26_interspeech.pdf

## 问题
语音重建需在提升可懂度的同时保留说话人身份，却无“病前真值”；常用 MOS 自然度/相似度敏感度与可靠性不足，客观指标与听感是否对齐也未充分验证。

## 方法
主观：情境化 Best Worst Scaling，分 INTELLIGIBILITY（只评可懂度）与 RECONSTRUCTION（同时考虑可懂度与想象中的病前身份）。客观：WER/PER、WeSpeaker 余弦相似度、UTMOS，以及双参考 TTSDS2——对高可懂 LibriTTS 子集与 SAP 乱序参考分别打分，再取 TTSDSMean 刻画折中。用 17 个零样本克隆 TTS，在 SAP 193 名英语母语障碍说话人（帕金森等，高/低可懂按 WER 30% 划分）上各生成 1 句。

## 实验与结果
全体说话人：INTELLIGIBILITY 上多数 TTS 高于原录音（StyleTTS2 等领先）；RECONSTRUCTION 上多数低于录音，IndexTTS2、Qwen3-TTS、E2-TTS 领先。低可懂子集上几乎所有系统可懂度更好，但 RECONSTRUCTION 仅 IndexTTS2、Qwen3-TTS 高于录音。客观上 WER/PER/UTMOS/TTSDS|LibriTTS 与 INTELLIGIBILITY 强相关；RECONSTRUCTION 上 Spk.Sim. ρ≈0.75，TTSDSMean 更高（全体 0.81，低可懂 0.73）。

## 结论
情境化 BWS 与双参考分布度量比通用 MOS/单指标更能对齐语音重建任务；零样本系统在严重障碍上仍难同时保身份与提可懂度。

## 点评
把“听得清”和“还是本人”拆成两套听测与一套均值分布分数，直接打中重建折中。数据偏帕金森与高可懂；客观相关是系统级排序相关，不等于样本级诊断。听者想象“病前声音”本身主观，框架对更重障碍会更吃力。


# Evaluating Automatic Laughter Phone Annotation for Socially-Situated Laughter Synthesis

- 论文编号：2141
- 报告人：Hiroki Mori
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/mori26_interspeech.pdf

## 问题
情境化笑声合成依赖笑声 phone 标注，人工成本高；既有自动识别数据少、未见说话人弱，且识别误差对合成质量的影响未系统验证；音频 LLM 路线是否还需要 phone 标注也不清楚。

## 方法
在 AGSC/OGVC 上新建 11 说话人笑声集，用改进的 XLSR-53 framewise+d 识别器（含时长后处理）。合成对比：SPSS（BiLSTM 参数语音合成，显式用 phone）与 Fish-Speech（音频 LLM，prompt）。条件含 ManualLabel、AutoLabel、AutoLabel+（SPSS 增广）、NoLabel。听测评自然度 MOS 与“笑法/个体性” SMOS。

## 实验与结果
未见说话人：PBE 23.0 ms，替换/删除/插入约 30%/14%/7%，辅特征错 15%，优于先前未见结果。自然度：Fish（约 3.5–3.6）高于 SPSS（Manual 2.71，Auto 2.51，NoLabel 1.62）。笑法相似度：SPSS Manual 3.94 ≫ Auto 3.46 ≫ Fish（约 2.5）；个体性 SPSS Manual 也更高。Fish 上有无 phone 差异不显著；SPSS 上自动标注明显弱于人工。

## 结论
自动标注对未见说话人已可用但仍不足以匹配人工；Fish 自然度好但笑法可控性弱，SPSS 相反——尚无同时兼得的单系统。

## 点评
把“识别准不准”落到合成听感三条轴上，比只报 PBE 更贴应用。自动–人工标注风格不一致可能放大 AutoLabel 劣势；Fish 的 LoL prompt 实验说明 token 模型对笑声结构仍缺显式控制杆。


# Benchmarking Large Language Models for Grapheme-to-Phoneme Conversion: A Japanese Case Study

- 论文编号：1800
- 报告人：Tomoki Koriyama
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/koriyama26_interspeech.pdf

## 问题
日语 G2P 需分词、多音汉字与数词–量词不规则读法；端到端 TTS 隐含学读音但可控性与稳健性不足。LLM 是否能替代传统形态分析器，以及何种调用方式更稳，尚缺大规模基准。

## 方法
两种模式：parse——LLM 做形态分析并输出各词假名，再规则后处理助词读法与长音规范化；direct——LLM 一步输出整句假名。在 JVS nonpara30 的 3000 句人工假名标注上算 kana CER；评测 30+ 专有/开源 LLM 与 OpenJTalk、MeCab 等传统工具。另将 LLM 假名喂入 LoRA 微调的假名输入 CosyVoice 2，与 E2E TTS 比发音 CER 与 UTMOS。

## 实验与结果
Claude Opus 4.6 parse CER 0.52%、Gemini 3.1 Pro direct 0.53%，优于最佳传统工具 OpenJTalk 1.03%。多数模型 parse 优于 direct；规模与日语持续预训练（Swallow）显著降错。假名 TTS：Gemini 3.1 Pro 假名 CER 2.38%（oracle 2.10%），低于 Gemini 2.5 Flash TTS 等 E2E（3.96%+），UTMOS 相当。

## 结论
强 LLM + 规则后处理可超传统日语 G2P；显式 G2P 再假名合成在发音准确上优于直接文本 E2E，且不明显损自然度。

## 点评
把“难规则”留给确定性后处理、把分词与读音估计留给 LLM，是务实的工程拆分。小模型 direct 极易崩；parse 在数词–量词切碎时也会引入错误，说明级联并非万能。基准句子来自 JVS，对更野文本泛化仍待验。


# The False Resonance: A Critical Examination of Emotion Embedding Similarity for Speech Generation Evaluation

- 论文编号：39
- 报告人：Yun-Shao Tsai
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/tsai26_interspeech.pdf

## 问题
表达性合成与情感 VC 广泛用 emotion2vec 等嵌入的余弦相似度作 EMO-SIM；分类准并不等于零样本相似度可靠，说话人/语言学干扰可能主导距离，从而奖励声学模仿而非情感迁移。

## 方法
对嵌入做均值中心化以缓解各向异性。三类检验：(1) 分类情感三元组（无约束、同说话人同文本、说话人干扰、语言学干扰）；(2) 效价/唤醒的趋势单调性（Spearman ρ）与位移可辨性；(3) 人工偏好对齐（多模型合成候选，Fleiss κ=0.7349，保留 400 个强共识三元组）。另做 emotion2vec 各 Transformer 层探测。对照 emotion2vec/+ 与 HuBERT、Wav2vec 2.0、TERA。

## 实验与结果
同说话人同文本时准确率多仅约 60–70%；语言学干扰下 emotion2vec 在 CREMA-D 可跌至 3.38%，说话人/语言学干扰下常低于随机。位移可辨性近 50%，ρ 近 0。人工对齐约 52–65%，不足以为可靠代理。深层对人类对齐从 L0 约 58% 降到 L7 亚随机约 45%。

## 结论
当前情感嵌入空间不适合零样本 EMO-SIM；高 SER 准确率不能推出可用的情感相似度度量。建议用对比学习等校准抑制非情感声学因素。

## 点评
把“评测指标”本身当成被测对象，用对抗式采样暴露 false resonance，对滥用不加批判的 EMO-SIM 很有杀伤力。均值中心化已尽量抬分辨率，失败更像表征结构问题；尚未给出可替代的成熟指标，实践上仍需谨慎搭配听测。


# LLM-Based Multi-Reference Evaluation for Efficient and Robust Assessment of Phrase Break Annotations

- 论文编号：2225
- 报告人：Hoyeon Lee
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/park26f_interspeech.pdf

## 问题
短语停顿标注存在一对多合法切分；单参考评测会拒掉与金标不同但仍合理的标注，人工评测又难扩展；直接用 LLM 当裁判捕捉细微韵律差异也有限。

## 方法
提出 LMRE：用 LLM 从少量 few-shot 演示池（与评测参考 disjoint）多次采样生成多参考查找表，保留出现次数超过 Niter/10 的标注；假设标注与任一参考相似度（EM 或 F1）超阈值即接受。韩语测试床含 1356 条标注、五种策略（AP-Only、Comma-IP、音频驱动、文本驱动、合成）与十一配置。

## 实验与结果
可接受组（人工分 4–5）上，单参考相对人工欠接受约 13–27%，LMRE Combined 将差距压到约 7%（分 5 组仅 1.75%）。与人工分相关：Combined† 多参考 F1 达 r=0.621、ρ=0.626，高于单参考（约 0.50）。F1 普遍优于 EM；长句上 EM 增益更明显。小演示池（|PFS|=128）即可泛化到未见句。

## 结论
LMRE 在可扩展自动评测与多参考容忍之间取得折中，比单参考更贴近人工接受行为。

## 点评
把“一对多韵律”落到可复用查找表而非黑盒裁判，确定性与可复现性更好。参考质量仍依赖演示池与 LLM 生成分布；目前验证集中在韩语，跨语迁移需另证。


# Investigating the Relationship between Objective AI-driven Metrics and Subjective MOS for In-the-Wild Speech

- 论文编号：2203
- 报告人：Shekhar Nayak
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/sanjotra26_interspeech.pdf

## 问题
UTMOSv2、DNSMOS 等 O-MOS 多在干净/去噪连续语音上训练；对 in-the-wild 离散 token TTS 的生成伪影（幻觉、韵律倒置）可能“听不清但谱面光滑”，客观分与人工自然度可能脱节。

## 方法
四系统对照（文本与说话人固定）：SYS-A StyleTTS 2（连续干净）、SYS-B MQTTS+语义编码器（原始 ITW）、SYS-C 在 A 上加 MUSAN 泡泡噪声且与 B 的 NISQA 对齐、SYS-D 真录音。耳机筛选听测共 768 条自然度评分；评 UTMOSv2、DNSMOS P.835/Pro、PLC-MOS。

## 实验与结果
人工：D>A>B≈C（B/C ΔMOS=0.10，p=0.14）。文件级相关：A 上 UTMOSv2 r=0.51（p<0.01），B 上跌至 −0.01（n.s.）；Steiger 检验确认崩溃显著。DNSMOS 等对加性噪声惩罚更重（OVRL B 3.06 vs C 2.64），与人工等价相悖。B 中 7/32 文件人工 MOS<2.5 但 UTMOSv2>3.8（acoustic camouflage）。

## 结论
在 MQTTS 类 ITW 离散合成上，现行神经 MOS 不宜单独作自然度代理；建议与 ASR WER 等语义指标组合，并建设针对 ITW 生成伪影的指标。

## 点评
用加性–生成配对把“罚错类失真”钉死，比单纯报 OOD 相关下降更有说服力。结论强度受单架构（MQTTS）限制；camouflage 样本说明表面质量指标会主动误导系统排序。


# SongBench: A Fine-Grained Multi-Aspect Benchmark for Song Quality Assessment

- 论文编号：1985
- 报告人：Dapeng Wu
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/wu26h_interspeech.pdf

## 问题
Text-to-Song 评测缺专业粒度；SongEval 等维度语义重叠且分数挤在高分区间，难区分日益接近的顶尖模型。

## 方法
按作曲要素定义七维：Vocal、Instrument、Melody、Structure、Arrangement、Mixing、Musicality（1–10）。用 Hunyuan 生成歌词/提示，收集 Suno 多版本、LeVo、SongBloom、ACE-Step 与真人版权曲等约 2 万样本，经专家校准与过滤得 11717 条标注（约 683.5 小时，中英约半）。以 MuQ 为骨干训自动预测器，并建 352 条外部模型 OOD 集。

## 实验与结果
OOD 上 utterance 级各维 LCC/SRCC 多超 0.78；system 级 LCC>0.95。Musicality 相关显著高于 SongEval。模型对比能拉开 Suno v4.5→v5、MiniMax 等迭代增益，而 SongEval 近乎平台。AB 测试：同模型内判别准确率（LeVo 64%、Suno 62%）明显高于 SongEval（约 43–55%）。

## 结论
SongBench 提供更解耦、更高分辨率的歌曲质量基准与自动评估工具，有助于诊断生成短板。

## 点评
把“好听”拆成可操作的制作维度，直接针对评分压缩与维度纠缠。自动器强依赖专家标签分布；Musicality 仍偏整体审美，与其余六维的独立性需持续监控。


# GRATS : A Natural Multi-Speed Mandarin Dataset for Speech Time-Scale Modification Benchmarking

- 论文编号：1842
- 报告人：Yu Tsao
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/aghniya26_interspeech.pdf

## 问题
STSM 评测多依赖英语语料或人工变速参考；普通话是声调语言，音高–时长协调敏感，人工缩放无法代表自然语速下的韵律与发音变化。

## 方法
发布 GRATS：25 名说话人、60 句、五档自然录制语速（0.5×/0.75×/1.0×/1.25×/1.5×），共 7500 条平行句、8.1 小时、44.1 kHz；卡拉 OK 式视觉提示控速，无后处理变速。协议：以自然 1.0× 为输入，系统输出与同说话人同句自然目标语速对比。指标含 Whisper CER、PESQ、STOI、DNSMOS、音节时长 MAE、WORLD F0 相关（MFA 对齐）。

## 实验与结果
Phase Vocoder 各档 CER 最低；CLPCNet 等神经法 DNSMOS/STOI 更好，说明可懂度与听感可脱钩。时长 MAE 在 0.5×/1.5× 呈 U 形升高，F0 相关随极端语速下降。实现语速 α 与标称因子总体对齐但仍有自然偏差。

## 结论
自然多语速平行数据使评测对准“是否接近真实目标语速实现”，而非复现确定性缩放；普通话 STSM 需多指标联合解读。

## 点评
把参考从“缩放后的同一条”换成“同文本再录的目标语速”，对声调语言特别关键。局限是朗读、台湾华语；客观指标不能替代音调忠实度听测。


# On the Effect of Segmentation Width and Cluster Size on Speech Resynthesis and Continuation in Generative Spoken Language Models

- 论文编号：999
- 报告人：Shunsuke Kando
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kando26_interspeech.pdf

## 问题
GSLM 的离散单元序列远长于文本，训练成本高；常规 N=20 ms 设定对语音生成是否冗余、降低码率会否伤重合成与续写，尚缺系统扫描。

## 方法
HuBERT-base 第 9 层特征按 N∈{20…280} ms 分段均值池化，再 K∈{128…16384} 做 K-means（64 种码率）。uLM 为 OPT，训于 LibriSpeech 960 h；u2s 分别为 Tacotron2+PWG 与 VITS（LJSpeech）。评重合成（WER、UTMOS、MCD、LogF0 RMSE）与续写（PPL/VERT、GPT-4.1-mini 成对裁判、MMOS、AB）。

## 实验与结果
重合成：中等 N（40/80）在更低码率下接近 N=20；Tacotron2 更可懂，VITS 声学更好。续写：在 WER<5 且 UTMOS>4 的设定中，N=80–120 大 K 的 LLM 裁判常优于基线；人工 AB 显示 (20,256) 与 (80,4096) 等可竞争。LLM 裁判与 MMOS 的 SRCC 仅 0.323，高于 PPL/VERT 但仍偏低。

## 结论
更低码率仍可支撑可懂重合成与高质量续写，常规高码率对生成任务可能冗余；续写自动指标与人工对齐仍弱。

## 点评
把“理解向”的 N/K 扫描延伸到生成任务，并点出任务最优码率不同（音素保真 vs 语义建模）。评价瓶颈在续写指标——LLM-as-judge 相关性仍低，结论对温度选择与归一化方式敏感。


# ConformalMOS: Uncertainty-Aware MOS Prediction with Conformal Intervals and Ordinal Modeling

- 论文编号：572
- 报告人：Tashfain Ahmed
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/elelu26_interspeech.pdf

## 问题
多数 MOS 预测器只给点估计、无可靠不确定性；人类评分主观且有噪声，部署时难以判断低置信或分布偏移样本。

## 方法
ConformalMOS：冻结上游（M2D2 或 wav2vec）均值池化嵌入 → 两层 MLP 序数头；将 MOS 划为等宽 bin，用高斯平滑软标签训 KL+辅助 L1；再在 10% 校准集上做 split conformal，取残差 (1−α) 分位数为半宽，输出截断到 [1,5] 的区间。

## 实验与结果
BVCC（VoiceMOS 划分）：M2D2 α=0.05 系统级 MSE 0.080、LCC 0.953、SRCC 0.943，优于 FUSE-MOS（MSE 0.086）；句级略弱于 UTMOS。经验覆盖贴近名义水平，校准误差低、区间相对窄；wav2vec 骨干覆盖不足、区间更宽。α 增大则区间变窄、覆盖下降。

## 结论
在交换性假设下可为 MOS 提供有限样本覆盖保证的区间，且不牺牲（甚至提升）系统级点估计；强骨干对校准质量关键。未测跨域，听者分歧建模留作未来工作。

## 点评
把 conformal 接到序数 MOS 头上，比启发式置信更可解释。系统级亮眼、句级仍落后顶尖点估计器；交换性在新 TTS 系统上是否成立是实际部署的硬约束。


# Hierarchical Conditional Continuous Normalizing Flows for Creaky Voice Editing under Speaker Identity Preservation

- 论文编号：1341
- 报告人：Petra Wagner
- 程序：Thursday 1 October 2026 / Flow Matching for Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rautenberg26_interspeech.pdf

## 问题
嗓音编辑希望改 creak 等副语言品质而不动说话人身份；群体数据上 creak 与平均基频、性别强相关，单阶段条件流易学到跨说话人相关，改 creak 时连带改 pitch/身份。数据增强去相关仅针对特定属性，缺乏通用结构解耦。

## 方法
提出分层条件连续归一化流：a1=平均 f0+性别，a2=breathiness+roughness+creak。两段 ODE：先用 f1 条件 a1，再用 f2 条件 a2；中间潜变量 z(tm) 上对 f0/性别做 Domain Adversarial Training（GRL），促其中间表征对高层属性不变。编辑时前向到基分布再按目标条件反传。后端 YourTTS；在 LibriTTS-R 上训练，对比 base-flow、加条件与对抗的单阶段 base-extd.、以及 pitch 数据改造的 data-mod.-flow。

## 实验与结果
客观：跨 β∈[-1.25,1.25] 的 creak 操纵，hierarch 的 |Δf0|、性别准确率与说话人验证 EER 最稳，明显好于 base。主观（11 名嗓音质量专家）：两模型都能放大感知 creak；hierarch 的 SMOS 下降显著小于 base（尤其放大条件），MOS 无显著变差。

## 结论
作者认为分层注入条件并对抗剥离高层属性，可在无任务专用数据改造下更好保留说话人身份地编辑 creak；是否泛化到其他纠缠属性仍待验证。

## 点评
用“阶段分隔 + 中间对抗”硬切断低层编辑回流到高层身份，比单靠数据去相关更可迁移。主观上身份仍会有一定损失；creak 抑制因基线感知 creak 较低而不够显著，效果边界需更多标注与场景检验。


# TC-DBI: A Plug-and-Play Trajectory Confidence-Guided Dynamic Block Inference Strategy for Speech Synthesis with Continuous Block Flow Matching

- 论文编号：1242
- 报告人：Ren Wang
- 程序：Thursday 1 October 2026 / Flow Matching for Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26v_interspeech.pdf

## 问题
连续 Block Flow Matching TTS 训练/推理常用固定块长，但语音信息密度不均：难区需要更强上下文，易区可大步并行；固定块在效率与质量间难兼顾，且连续 ODE 采样缺少离散模型那样的 token 置信度信号。

## 方法
定义 Trajectory Confidence（TC）：ODE 轨迹起终点位移范数 / 路径总长，越接近 1 越“直”、越可信。TC-DBI：先以 Lmax 并行生成候选块，按阈值 τ 找最长可靠前缀，截断低置信后缀并用更新后的上下文重生；每步至少保留 1 帧以防死循环。即插即用，无需改结构或重训。复现 BFM（DiT + 冻结 VoxCPM VAE，Emilia 中英约 100k 小时），推理 32 步 ODE，默认 τ=0.75。

## 实验与结果
Seed-eval：BFM+TC-DBI 相对无 DBI 降低 WER（zh 1.628→1.568%，en 1.921→1.798%），N-MOS 升至 3.809/3.973，SIM 基本持平。低 TC 句子错误率显著富集（阈值 0.65 时错误率约 35% vs 全局 21.4%）。τ=0.75 时相对 RTF 约 1.08× 且 WER 最优；过高 τ 使 RTF 升至 1.63× 收益递减。重生后 >90% 原低置信帧升到阈值以上。

## 结论
作者认为轨迹直线度可作为免训练可靠性指标，TC-DBI 能自适应块粒度，在相近效率下提升稳健性与感知质量。

## 点评
把 OT 直线流的几何性质变成可操作的动态解码信号，对连续块模型很贴切。阈值需折中；TC 是局部速度一致性代理，不等价于语义正确性，极端韵律/难文本是否总能被截断–重生修好仍依赖基座 BFM 能力。


# Bridging the Gap: A Hierarchical Framework for Cross-Modal Style Modeling in Expressive TTS

- 论文编号：1513
- 报告人：Jiale Chen
- 程序：Thursday 1 October 2026 / Flow Matching for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/chen26p_interspeech.pdf

## 问题
自然语言风格 prompt 控制表达式 TTS 时，文本与语音之间存在跨模态表征鸿沟，且同一 prompt 对应多种合理声学实现（one-to-many），点对点对齐不稳定。参考音频常不可得，粗粒度风格标签又缺乏描述细度；已有因子化/对比学习方法多依赖专用编码器或点式目标，难以显式处理分布级模态失配。

## 方法
提出 **OTAFlow** 三阶段层次框架：
1. **统一风格空间**：冻结 CLAP 文本/音频编码器，用对称轻量 adapter 映射到共享空间；用熵正则最优传输（Sinkhorn）做分布级对齐（余弦代价），再加对称 InfoNCE 保留实例级对应，并用 emotion/pitch/energy 多任务分类头增强表达因子可分性。
2. **Prompt-to-style 采样**：在统一空间上用条件流匹配（轻量残差 MLP）学习 \(p(z_s|z_t)\)，配合 classifier-free guidance，从噪声 ODE 采样多样音频风格嵌入，缓解残差模态间隙与一对多问题。
3. **下游 TTS**：将采样风格嵌入接到基于 Matcha-TTS、DiT 估计器与 AdaLN 条件的流匹配声学模型，再经声码器波形重建。

## 实验与结果
数据：Textrolspeech（约 330 小时，多说话人自然语言风格 prompt）；平衡测试集每情感随机 50 句（八类情感）。检索：联合 InfoNCE+OT 在 Text→Audio / Audio→Text 上 R@1 达 0.135 / 0.142，MedR=4，明显优于冻结 CLAP、仅 InfoNCE 或仅 OT。合成（Track-1 纯文本）：sMOS 3.88、ESIM 69.19 高于 EmoVoice、IndexTTS2、CosyVoice2；nMOS/UTMOS 有差距，作者归因于轻量 backbone 与训练规模。Track-2 音色参考下仍保持较高风格控制。消融：CFM 相对确定性回归头提升 sMOS/ESIM，同 prompt 多样本 Style Dist.=0.1279。

## 结论
OT+对比+多任务监督可构建兼顾对齐与因子可分的统一风格空间；条件流匹配能对同一 prompt 采样多样声学风格嵌入，并提升下游表达一致性。框架可即插即用到标准 TTS backbone。

## 点评
核心抓的是「prompt 风格控制」里分布失配与一对多采样两件事：先用 OT 稳住跨模态几何，再用嵌入空间 CFM 把剩余间隙做成可采样条件分布，而不是端到端硬吞变异。强在控制可解释、风格与音色解耦（Track-2 防参考音频风格泄漏）的设计动机清晰；脆弱点在下游声学模型仍偏轻量，自然度指标落后，且风格空间高度依赖 Textrolspeech 标签与冻结 CLAP 的表征上限。


# RobustSpeechFlow: Learning Robust Text-to-Speech Trajectories via Augmentation-based Contrastive Flow Matching

- 论文编号：3086
- 报告人：Jinhyeok Yang
- 程序：Thursday 1 October 2026 / Flow Matching for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/yang26p_interspeech.pdf

## 问题
流匹配 TTS 在零样本相似度与自然度上已较强，但对齐仍易出现 skip/repeat，尤其在小模型或低 NFE 时更严重。已有偏好数据/DPO、ASR/CTC 辅助监督、架构加强等方法有效，但常需额外数据策展或外部模型，不利于轻量部署。

## 方法
**RobustSpeechFlow** 是面向 TTS 的对比流匹配训练策略，无需外部对齐器或偏好集：
- 正样本：标准条件流匹配，在 Supertonic 自编码器潜空间上回归速度场。
- 负样本：批内随机负样本 + **长度保持的失败模式增强**——以 0.5 概率做 repeat（覆盖另一段）或 skip（前移后续帧并用静音潜表示填尾），在潜空间制造声学上相近但局部文本–语音对应被破坏的 hard negatives。
- 总损失：\(L = L_{\mathrm{pos}} - \lambda_{\mathrm{rand}} L_{\mathrm{rand}} - \lambda_{\mathrm{aug}} L_{\mathrm{aug}}\)，推理流程不变。

## 实验与结果
训练：英/韩各约 10k 小时内部数据，固定 SupertonicTTS（0.06B）架构与预训练 text-to-latent，比较 Baseline / ContrastiveFM / RobustSpeechFlow。Seed-TTS-eval：WER 1.44→1.38（相对 Baseline 降约 4.2%），SIM 保持 0.60，为表中最低 WER。自建 ZERO500（每语 50 音色×10 文本）：NFE=24 时英 CER 0.48%→0.35%、韩 CER 0.81%→0.57%；低 NFE 下韩语收益更明显。训练曲线显示后期对齐更稳。

## 结论
用长度保持的 skip/repeat 潜空间增强作对比负样本，可在不改推理、不引入外部模型的前提下提升内容保真；在紧凑模型与低 NFE 上更稳。局限：公开基准上说话人相似度仍落后大模型，作者归因于紧凑架构与编解码器而非目标本身；客观 ASR 指标也受识别误差与文本规范化影响。

## 点评
把对比流匹配的负样本从「随机错条件」换成「同句对齐失败的硬负样本」，直接对准生产里最痛的 skip/repeat，是很务实的训练侧改动。强在零额外推理成本与易集成；脆弱处在增强覆盖率/span 启发式是否覆盖真实失败分布，以及 SIM 瓶颈是否真能靠放大模型消解——若负样本过强也可能压制合理韵律变异。


# Improving Flow Matching based Text-to-Speech with Dual-Model Preference Optimization and Classifier-Free Guidance

- 论文编号：2412
- 报告人：Minchuan Chen
- 程序：Thursday 1 October 2026 / Flow Matching for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/chen26y_interspeech.pdf

## 问题
流匹配零样本 TTS 常用 CFG，但常规训练/推理难以有效融入人类反馈，训练目标与评测指标（可懂度、说话人相似、自然度）存在错配；同输入不同采样质量波动大。单模型同时编码偏好/非偏好易产生参数冲突，CFG 也未利用偏好信号。

## 方法
基于 F5-TTS Small，提出 **PA-Dual** 统一框架：
1. **双模型偏好优化**：从同一参考模型初始化 preferred / dispreferred 两个模型；用统一 DPO 式目标分别拟合 win/lose 分布，避免单模型权衡。偏好对用 WER、SSIM 等代理指标构造（GT vs 生成、模型多样本 Pareto 排序；含常规与舌尖/重复等困难文本）。
2. **采样引导**：将两模型速度场与代理 prompt \(\hat{c}=-\alpha c+(1+\alpha)\phi\) 结合，用三项目标推向偏好、排斥非偏好，并减少前向次数。
3. **改进 CFG**：引入优化尺度因子 \(s\)（条件速度在无条件方向上的投影）与 early-step zero-init，稳定早期 ODE 步。

## 实验与结果
预训练：WenetSpeech4TTS Premium（945h 普通话）+ LibriTTS（约 585h）。偏好集 DT1/DT2/DT3 各 2000 对。Seed-TTS test-zh/en：PA-Dual(w/ DT3) 中文 WER 2.87、SSIM 0.634、UTMOS 2.728；英文 WER 2.38、SSIM 0.625，全面优于 Baseline 与单模型 PA-Base。数据效率：约 250 对即可让 WER 趋稳，SSIM 约 500 对趋稳。CFG \(\omega=2.5\) 较优；消融显示 zero-init 对 TTS 增益更明显。主观 CMOS/SMOS 与客观趋势一致。

## 结论
双模型分别建模偏好与非偏好，并与改进 CFG 协同，可用少量偏好数据提升流匹配零样本 TTS 的可懂度、说话人相似与自然度。后续拟用蒸馏/LoRA 降低双模型开销。

## 点评
把图像领域里「正/负偏好分模」迁到语音，并用 WER/SSIM 作可扩展代理，抓住了 FM-TTS 训练目标与听感指标错配。强在数据效率与困难文本对构造；脆弱点是推理需维护两套权重、代理指标可能与真实听感不完全一致，以及偏好对质量高度依赖排序策略。


# Enhancing Flow Matching with A Unified Guidance Framework for Efficient and Robust Speech Synthesis

- 论文编号：1015
- 报告人：Zuda Yu
- 程序：Thursday 1 October 2026 / Flow Matching for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/yu26b_interspeech.pdf

## 问题
流匹配语音生成面临两大瓶颈：语义 token 残留声学线索导致**音色泄漏**；ODE 路径弯曲与 CFG 双前向带来**推理延迟**。VQ 等瓶颈易伤可懂度；仅拉直轨迹或仅内化 CFG 往往顾此失彼。

## 方法
统一引导框架，两支柱：
1. **Data-guidance (DG)**：双阶段异构扰动——先用预训练 VC/TTS 对源语义 token 做跨说话人合成，再对中间波形做随机 pitch/energy 变形，得到声学不可靠但语言内容不变的条件 \(\tilde{c}\)，迫使模型从 token 取内容、从目标声学 prompt 取音色。
2. **Enhanced Model-guidance (MG)**：同一 batch 内先做内禀引导蒸馏，把 CFG 感知速度场写入网络（单前向即可对齐条件）；再用更新后的模型在线 ODE 仿真并做轨迹拉直，消除 CFG 开销并减少 NFE。

骨干：约 330M 纯 DiT（20 层，AdaLN 注入说话人），启发自 CosyVoice2；先在 Emilia 50k 小时匹配条件预训练，再在 60k 小时混合语料（含 30k 小时扰动对）上做统一优化。

## 实验与结果
VC（LibriTTS/Seed-TTS）：Unified（3 NFE）RTF 0.024，相对 10-step Base（RTF 0.078）约 **3.25×** 加速；Non-Parallel LibriTTS SIM 0.850，优于 Base 0.793，且超过 GT Parallel SIM 0.799。仅 DG 的 SIM 最高但无加速；仅 Enhanced MG 加速但 SIM 有损。TTS：同 CosyVoice2 LLM 后端下，Unified SIM（LibriTTS 0.888 / Seed-TTS 0.806）高于 Base，WER 略升但仍可比。

## 结论
数据侧异构扰动切断声学捷径，模型侧蒸馏+在线拉直去掉 CFG 并缩短轨迹，可在 VC/TTS 上同时提升零样本说话人相似与推理效率，并可作为现有 TTS 的高效声学 detokenizer。

## 点评
把「防泄漏」和「加速」放进同一训练环，比单独做 rectify 或单独做 CFG 蒸馏更完整。强在 3-step 无 CFG 仍保住甚至抬高零样本 SIM；脆弱点在依赖外部生成系统做交叉合成、在线 ODE 训练成本高（文中约 90h），以及强拉直可能轻微伤 WER。


# SSL-GMMVC: Interpretable Voice Conversion via Locally Linear GMM Transforms in Self-Supervised Representation Space

- 论文编号：1688
- 报告人：Tomoya Tanabu
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/tanabu26_interspeech.pdf

## 问题
LinearVC 等在 SSL 空间做全局线性映射简单有效，但无法适配不同音素簇的局部结构；深度 VC 又难解释。需要在可分析前提下提升表达力。

## 方法
SSL-GMMVC：WavLM-Large 第 6 层特征经双向最近邻对齐成源–目标对，对联合向量拟合 \(K\) 分量 GMM；转换时用源侧后验加权各分量仿射映射 \(\hat y=\sum_k p(k|x)\{\mu_k^y+\Sigma_k^{yx}(\Sigma_k^{xx})^{-1}(x-\mu_k^x)\}\)。\(K=1\) 退化为 LinearVC。协方差分 Full 与 Cross-Diag；HiFi-GAN 合成。

## 实验与结果
CMU ARCTIC 六说话人。数据充足时 Full+\(K>1\) 说话人 EER/主观相似度可超过 LinearVC NC，并常优于 FreeVC；可懂度与 UTMOS 总体可比。Cross-Diag 随 \(K\) 增大也可超过 FreeVC 相似度（参数更省）。分量选择与响音/阻音纯度相关；单分量变换矩阵呈收缩旋转，跨性别角度更大。

## 结论
SSL 空间局部线性 GMM 变换在保持可解释性下提升说话人相似度，并揭示分量与语音学结构、变换几何的联系。

## 点评
“简单可分析 VC”路线上把全局线性换成混合局部仿射，分析扎实。高维 SSL 下 \(K\) 难做大、跨分量旋转平面难对齐，扩展性仍受估计稳定性限制。


# From A to B to A: Palindromic Zero-Shot Voice Conversion with Non-Parallel Data

- 论文编号：1663
- 报告人：Moshe Mandel
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/mandel26_interspeech.pdf

## 问题
非平行 any-to-any 零样本 VC 常靠内容–说话人解耦，易泄漏身份或丢内容；纯 KNN-VC 在短参考下邻居稀疏、质量崩。需要能从非平行数据构造可监督训练信号的方案。

## 方法
回文（palindromic）训练：用 WavLM 特征上的 KNN-VC 把真实目标片段 \(a_1\) 映射成合成源 \(\hat B_1\)，再训 Transformer 把 \(\hat B_1\)（加目标参考 \(A_2\)）还原到目标，波形级用预训练说话人验证损失强化身份。三阶段：先 WavLM→波形 vocoder，再训转换器，再对转换特征重训 vocoder。推理时输入真实源、短目标参考。

## 实验与结果
仅英文 LibriSpeech 训练。英语上各 prompt 时长 Spk Sim/EER 优于 Seed-VC、KNN-VC、Vevo、OOVC，WER/CER/MOS 可比；3 s 参考仍稳健（相对 KNN-VC 优势最大）。多语 LibriSpeech 无微调下 WER 常最佳，相似度与 DNS-MOS 可比。vocoder 后训练抬高 DNS-MOS、抑制伪影。

## 结论
合成→真实回文监督 + 波形说话人损失，可在非平行数据上做强零样本 VC，并跨语泛化。

## 点评
把 KNN-VC 从“推理算法”变成“造平行对的数据工厂”，短参考场景收益最大。依赖离线 KNN 质量与额外 SV 模型；超大规模/高表现力数据与流式仍待扩展。


# MeanVoiceFlow2: Joint Optimization of Mean Flow and Content Encoder for Fast One-Step Zero-Shot Voice Conversion

- 论文编号：1596
- 报告人：Takuhiro Kaneko
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/kaneko26_interspeech.pdf

## 问题
MeanVoiceFlow 等一步流匹配 VC 推理快，但固定重型内容编码器（如 Conformer 瓶颈特征）耗时约为一流步的 10 倍，成为瓶颈；需在无额外预训练声码器条件下联合压缩内容编码与转换模块。

## 方法
MeanVoiceFlow2：用轻量可训内容编码器 \(c_\phi\) 替换教师固定内容编码器，并联合训学生平均速度网 \(u_\phi\)。训练含：(1) 相对教师 MeanVoiceFlow 的转换蒸馏 + 真实数据重建；(2) diffusion-GAN + 样本混合的对抗，提升真实感且不依赖外部声码器判别器；(3) 教师引导条件增强（用教师在打乱说话人条件下生成样本喂内容编码器）促内容–说话人解耦。推理仅用 \(c_\phi\) 与 \(u_\phi\)。

## 实验与结果
VCTK 零样本：相对教师 MVF，nMOS 3.93 vs 3.76，UT/DNSP 更好，CER/SECS 相近，RTF 约降 9×（0.00084 vs 0.0072）。对比 FasterVoiceGrad 主观/客观更优或持平且训练无需预训练声码器。消融显示转换+重建、扩散+混合、CondAug 均有贡献。LibriTTS 上同样约 9× 加速且质量提升。

## 结论
联合蒸馏轻量内容编码器与 Mean Flow，可在保持说话人相似度下明显提速并改善感知质量。

## 点评
抓住“一步流已快、编码仍慢”的真实瓶颈，蒸馏设计完整。仍依赖同数据训好的教师；波形合成用 HiFi-GAN，端到端一步波形未完全打通。


# Zero-VC: Zero-Lookahead Streaming Voice Conversion via Speaker Anonymization

- 论文编号：1340
- 报告人：Yudong Li
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/li26w_interspeech.pdf

## 问题
流式零样本 VC 中，信息瓶颈去音色常丢掉韵律，被迫注入 \(f_0\) 等并缓存未来帧（如 StreamVC 约 60 ms 算法前瞻）；既有说话人扰动又难在“音色泄漏 vs 效用保留”间取得优平衡。

## 方法
Zero-VC：训练时用现成 Speaker Anonymization（SA）扰动源语音以压泄漏、保语言/韵律，再经严格因果流式编码器（20 ms 帧移、零前瞻）提内容；WavLM-large 第 7 层 + 可学习注意力池化提参考音色；因果卷积 HiFi-GAN 式解码器注入全局音色。对抗训练后推理丢弃 SA 与判别器，chunk-by-chunk 缓存因果状态。

## 实验与结果
相对 LSCodec/Seed-VC 扰动，SA 中间音频 SS-S 最低（0.119）且 FPC 较好；训成 VC 后更近“低泄漏高目标相似度”理想区。零前瞻系统相对非流式开源模型：SS-S 0.171、SS-R 0.521、SMOS 最高，WER 3.96%、FPC 0.688，CPU RTF 0.063；算法延迟 20 ms，低于 DualVC3/StreamVC/RT-VC 报告值。无 SA 时对 40–60 ms 前瞻依赖更强。

## 结论
SA 作扰动可同时改善泄漏–效用权衡，并支撑真正零前瞻流式架构，把算法延迟压到单帧下限。

## 点评
把匿名化目标显式对接流式 VC 的核心权衡，延迟叙事有力。训练仍依赖外部 SA 预处理；端到端并入 SA、跨语与总系统延迟仍是后续点。


# Improving Model Expressivity and Speaker Matching in Low-Latency Voice Conversion

- 论文编号：796
- 报告人：Anders R. Bargum
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/bargum26_interspeech.pdf

## 问题
实时零样本 VC 在轻量因果约束下说话人相似度偏低：内容离散单元/发音合成丢失韵律，全局说话人嵌入容量不足，难以表达时变音色。

## 方法
并行编解码器：内容编码器蒸馏 HuBERT 软单元；韵律编码器估计 F0、周期性、V/UV、响度并合成 sinusoid-plus-noise 激励，在解码器各残差块注入；全局说话人编码器（VoxCeleb 预训练）+ 互补说话人编码器，用因果 MHA 将说话人 token 与内容/韵律查询融合为 S_Emb。训练时对内容输入做音高移位、加噪、参数均衡，对说话人编码器做单元级时间掩码以促解耦。推理时将源 F0 按目标均值比缩放。

## 实验与结果
LibriTTS 全 train（555 h / 2311 说话人）训练；零样本：LibriTTS test-clean 377 句 × VCTK 6 未见说话人。相对 RT-VC / StreamVC：SECS 80.83%（+4.18 / +3.02 pp），F0 PCC 0.885；WER/CER 与基线接近。主观 S-MOS 最高（3.25），Q-MOS 略低于 StreamVC；CPU 延迟 64.9 ms。消融显示扰动与互补编码器均提升 SECS。

## 结论
在保持可懂度与低延迟的前提下，激励注入 + 互补说话人融合 + 编码器特定扰动可提升零样本说话人匹配与音高一致性；作者将增益归因于表达能力增强，而非严格证明“动态音色”提取。

## 点评
针对实时瓶颈的设计很务实：用轻量旁路补回离散内容丢掉的韵律，并用因果注意力扩充说话人表征，而不是堆非因果 SSL。互补嵌入的可解释性仍弱（L2 与 F0/响度无清晰对应），扰动会略损可懂度，主观相似度优势也未达统计显著。


# Universal Speech Content Factorization

- 论文编号：198
- 报告人：Matthew Wiesner
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/xinyuan26_interspeech.pdf

## 问题
Speech Content Factorization（SCF）在 WavLM 特征空间用低秩线性分解做免训练 VC，但是闭集：未见说话人需重算分解，难用于开放集 VC 与众包 TTS。

## 方法
USCF：先在若干说话人上做内容对齐 WavLM 矩阵的截断 SVD（默认 r=75），再学通用 speech-to-content 映射 W（三种最小二乘：W1 以 Σ^{-1}U 为目标、W2 近似反转说话人矩阵、W3 取某说话人 S 的伪逆）。对未见说话人，用约 500 帧（约 10 s）目标 WavLM 估计 S_m≈(X'W)^†X'。VC 时 X'_s W S_t 重建目标侧 WavLM 再合成。特征也可用作 TTS 声学目标。

## 实验与结果
LibriSpeech 四组各 20 说话人评测。客观：W1 WER 2.70%、UTMOS 2.805、Spk Sim 0.524，可懂度接近/优于 kNN-VC、LinearVC，相似度弱于闭集 SCF/kNN-VC；主观 MOS/SMOS 与多数基线无显著差异。TIMIT 同音素内：说话人 EER 36.40%（去说话人信息强于 WavLM/ContentVec），音素 EER 11.43%。目标帧数低于 500 时相似度骤降；用 USCF 特征训 flow-matching TTS 较 mel 目标 WER 更低、训练更省（11.44% / 25 epochs）。

## 结论
将 SCF 推广为开放集线性内容因子，可用少量目标语音做零样本 VC，并作为去音色声学特征服务 TTS；未来拟用轻量神经网络稳定 W 与少样本 S_m。

## 点评
抓住 WavLM 几何结构做闭式线性解，数据与训练成本极低。瓶颈在 content-to-speaker 一侧：开放集相似度系统性落后闭集方法；对目标时长与秩敏感，且依赖 kNN 对齐与 WavLM 空间假设，跨域鲁棒性未充分验证。


# CFLOW-VC: An unsupervised cycle training strategy based on normalizing flows for Voice Conversion

- 论文编号：48
- 报告人：FeiBao Song
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/song26_interspeech.pdf

## 问题
非平行 VC 存在训测失配：训练时常从同说话人取样内容与音色，推理却需任意组合；FreeVC 等未充分覆盖内容–音色交叉，泛化不足。

## 方法
CFLOW-VC 基于 FreeVC/VITS：WavLM 先验 + 说话人编码器后验 + Mel-Style 风格编码器；用 flow 可逆性做 cycle training（CTS）：源先验经逆 flow 注入目标音色再循环回源，配合 StarGAN 式对抗、双向 KL、循环 KL 与 HiFiGAN 重建损失；先验侧加 GRL 说话人分类促解耦。WavAugment 加噪声/混响增强。两阶段：backbone 预训练 500k → 冻结后验与解码器后 CTS 200k。

## 实验与结果
VCTK 训练（109 说话人，16 kHz）。Clean/Noise/Accent 三测集相对 DiffVC、Diff-HierVC、StarGANv2-VC、FreeVC：Clean 上 SIM 73.5%、UTMOS 3.948；Noise 上 WER 12.09%、SIM 73.89%、UTMOS 3.911，显著优于基线；Accent 亦最优。主观 MOS 在三集均为最高（Clean 4.39）。消融：去 CTS 大幅变差；去风格编码器伤 SIM/UTMOS；去增强伤噪声鲁棒性。

## 结论
将归一化流与 StarGAN 式循环一致性结合，可在非平行设定下缓解训测失配，提升音色相似度、表现力与噪声/口音鲁棒性。

## 点评
核心是把 CTS 做在高斯先验/后验上而非 mel，降低对抗训练难度，思路清晰。仍依赖预训练说话人编码器与 VCTK 规模；去 CTS 单独加风格编码器反而劣于 FreeVC，说明循环损失才是解耦关键，组件耦合较强。


# WhispEar: A Bidirectional Framework for Scaling Whispered Speech Conversion via Pseudo-Parallel Whisper Generation

- 论文编号：1827
- 报告人：Yingda Shen
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/fang26b_interspeech.pdf

## 问题
耳语缺基频与周期激励，W2N 困难；平行耳语数据稀缺，DSP 伪耳语分布偏差大，现有方法音色/韵律保留差。

## 方法
WhispEar 三阶段：(1) 从 SenseVoice-Large 蒸馏轻量语义 tokenizer（Transformer+FSMN+FSQ），用耳语与正常语音促说话方式不变；(2) 共享 Flow-Matching Transformer（自 CosyVoice2）按方向指示 d∈{w2n,n2w} 从语义 token 生成 mel；(3) 先用真实平行数据训较易的 N2W 统一 tokenizer，再对大量正常语音零样本生成伪平行耳语，最后用真实+伪数据训更难的 W2N。发布双语语料 wEar（真实约 18 h / 146 说话人 + 伪约 3026 h）。

## 实验与结果
wTIMIT（英）与 wEar（中）测试：WhispEar-Scaled（约 3000 h 伪数据）英 SIM 0.577、WER 22.44%、UTMOS 3.75、F0 CoRR 0.513；中 SIM 0.750、CER 14.93%，全面优于 WESPER、DistillW2N、MaskCycleGAN、CosyVoice2。消融：对齐真实对 + 模型伪对（A+P）优于 RAW/DSP；伪数据预训练规模增大后再用真实对齐 SFT，各项持续提升。

## 结论
双向统一语义表征 + 可扩展伪平行耳语生成可缓解数据瓶颈，并带来一致的 W2N 增益；wEar 为后续研究提供双语基准。

## 点评
“先易后难”（N2W→扩数据→W2N）与数据中心 scaling 路线很契合耳语稀缺场景。性能仍强依赖伪数据质量与少量真实对齐微调；噪声鲁棒与多语扩展被作者列为后续工作，部署效率也未充分讨论。


# Imitation Learning for Elder-Facing Speech Synthesis

- 论文编号：2107
- 报告人：Dongrui Han
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/han26d_interspeech.pdf

## 问题
通用 TTS 未照顾老年听感；直接收老人偏好成本高、易疲劳。用专家示范做 RL 微调时，固定奖励易 reward hacking（过度放慢、插停顿）。

## 方法
模仿学习框架：医护人员录制面向老人的粤语示范（及中性对照）；专家奖励头接冻结 StyleTTS 2 韵律编码器，Bradley–Terry 成对训练；发音奖励用 SenseVoice 转写的 Jyutping 音节错误率（SER）；二者调和平均为复合奖励。以 CosyVoice2-Yue 经 SFT 为策略，用带 PPO clip 的 GRPO 优化。OPRL 两阶段：Stage1 把中等奖励、低 SER 的 rollout 并入奖励集并重训；Stage2 在外部文本上按 SER 分箱与分位数赋奖励，再 GRPO。

## 实验与结果
专家数据 125 对 / 1.5 h（train 89）。客观：GRPO w/o OPRL 静音时长 11.51 s、总时长 27.62 s（GT 约 5.43 / 19.27），SER/MOS 差，显 hacking。OPRL Stage2：SER 7.54%、CER 3.86%、MOS 3.78（8 名 66–83 岁听者），优于 base / SFT / 无 OPRL；多项韵律与可懂度指标最佳或次佳，MOS 显著高于 base 与无 OPRL。

## 结论
用专家示范 + 两阶段 OPRL 的 GRPO 可在低资源偏好对齐下缓解 reward hacking，生成更受老年人偏好、可懂度更好的粤语合成语音。

## 点评
把“奖励也 on-policy 更新”对准 hacking 很有针对性，复合奖励抑制牺牲可懂度换慢速。示范仅 1.5 h、听者 8 人，风格是否覆盖真实老人偏好仍受限；发音奖励依赖 ASR/粤拼质量，跨语种移植需重设计。

