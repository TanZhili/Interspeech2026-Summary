# Code-Switching ASR

- 日期：Thursday 1 October 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：9
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场专攻语码转换（CS）ASR：LLM 引导热词偏置、合成语音的语码混合保真、数据高效 RL 适配 Audio LLM、DPO 纠正转录失败模式、贝叶斯因子化适配保护单语能力，以及低资源黏着语流式 CS。核心矛盾是语言边界快速切换、真实 CS 数据稀缺，以及适配常损害强多语基线。

合成与偏好学习成为主路径：用 Code Mixing Index 偏好优化 TTS、用可验证奖励 RL（错误率 + 文字系统保真）与 DPO 偏好对纠正省略/翻译/幻觉。部署侧强调把切换知识高效注入预训练模型（MoE 适配器、贝叶斯因子化），并在黏着语场景用动态块在线与形态感知指标处理后缀跨边界问题。

## 论文技术总结

# LLM-HB: Language-Aware LLM-Guided Hotword Biasing for Code-Switching ASR

- 论文编号：1113
- 报告人：Yuxuan He
- 程序：Thursday 1 October 2026 / Code-Switching ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/he26c_interspeech.pdf

## 问题
码切换 ASR 易受跨语混淆；热词偏置多服务单语系统，CS 场景下较少与 LLM 自适应偏置结合。

## 方法
LLM-HB：Whisper-medium 编码器 + MoE adaptor（默认 2 experts、top-2）得到语言特化语音嵌入；Qwen3-4B 经 LoRA，输入拼接语音、热词与（训练时）转写嵌入，并用辅助语言头对 LLM 隐状态做 Mandarin/English/other 监督。训练目标 L = L_ASR + λ1 L_Bias + λ2 L_Lan（λ1=0.6，λ2=0.3）。热词经冻结 LLM tokenizer/文本编码器注入提示。

## 实验与结果
评测 ASRU2019-CS，每句 15 个干扰热词。全量约 2200h（ASRU+LibriSpeech+AISHELL-2）上，完整模型 MER 5.85（基线 7.34，相对降 20.30%），B-MER 8.99（基线 22.11）；CER/WER 4.94/13.21。仅 200h CS 数据时完整模型 MER 7.36（基线 9.59），热词提示单项收益最大。消融：2 choose 2 优于更多专家；λ1 增大使 CER/WER 更平衡，主实验取 0.6。

## 结论
语言特化 MoE、语言监督与 LLM 热词提示互补，可在码切换 ASR 上显著改善总体与热词相关错误率；作者称首次将 LLM 引导偏置引入 CS-ASR，并释放热词列表。

## 点评
把“分语表示”和“上下文热词”绑在同一 LLM 条件接口上，适合双语切换。热词损失权重调节英/中错误平衡；专家数不必多，双语场景两专家即可。小数据时单独加 MoE 可能略伤性能，需与语言/偏置信号联合才稳。


# Improving Code-Switching ASR with Code-Mixing Guided Synthetic Speech

- 论文编号：642
- 报告人：Yue Heng Yeo
- 程序：Thursday 1 October 2026 / Code-Switching ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/heng26_interspeech.pdf

## 问题
码切换 ASR 缺高质量 CS 语料；用 TTS 增广时多优化重建保真度，未显式约束语言边界一致性，合成数据对下游未必有用。

## 方法
提出声学级 CMI_speech：用带 Language Alignment Loss 的 Whisper 解码器交叉注意力得到帧级伪语言标签，再按非主导语言帧占比定义混合度；与真值语音的 |ΔCMI| 衡量结构保真。对 CosyVoice2 先做 SEAME CS 微调，再以 DPO 对齐：同文本随机采样多样本，用归一化 UTMOS、MER、ΔCMI 打分构造偏好对（最优 vs 最差，并过滤 MER>20%、UTMOS<2.5、ΔCMI>20%）。合成语音与真实数据按等时长混合微调下游 ASR。

## 实验与结果
SEAME 约 192h。TTS 上加 ΔCMI 使 ΔCMI 28.1→16.1、MER 16.2→10.3，UTMOS 维持约 3.8。Whisper-large v3：Real 100h MER 12.1/17.8；+CosyVoice 10.1/16.0；+DPO(UTMOS,MER) 9.6/15.1；+ΔCMI 8.9/14.2（DevMAN/DevSGE）。CTC Conformer 同步改善至 15.4/21.9。定性显示 ΔCMI 更能稳住跨语边界与英文段发音。

## 结论
用声学码混指标引导 DPO，可让合成 CS 语音更贴近真实混合结构，从而更有效地提升下游码切换 ASR。

## 点评
关键是把“文本 CMI”落到帧级声学，直接进偏好学习，补上仅 MER/MOS 管不了的边界问题。依赖伪标签 LID 质量与过滤阈值；合成与真实等时长设定保证公平，但未展开更大规模合成比。


# Reinforcement Learning for Data-Efficient Code-Switched ASR

- 论文编号：2667
- 报告人：Ziwei Ye
- 程序：Thursday 1 October 2026 / Code-Switching ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ye26c_interspeech.pdf

## 问题
语音 LLM 可提示做码切换，但自回归交叉熵未直接优化序列级错误，切换边界易出现翻译整段、脚本污染等失败；标注 CS 数据稀缺。

## 方法
以 Qwen2-Audio 为可控试验台，用 GRPO 做 RLVR：组内采样 G=8 候选，用可验证奖励做相对优势。奖励 = −CER + β_sf·Script（β_sf=0.05），Script 要求字符落在语言对允许 Unicode 脚本并集。训练期两遍 draft-and-refine：第一遍 GRPO，再以最高奖励草稿条件第二遍；测试仍单遍。仅更新解码器，音频编码器冻结。

## 实验与结果
在 CS-FLEURS XTTS-TRAIN（TTS 合成）上训，评 READ-TEST 与零样本 SwitchLingua。10% 数据的 RLVR（CER+SHR+refine）可匹配全量 LoRA SFT；20% 时微均 CER 0.147 优于全量 LoRA 0.159。SHR 奖励显著降脚本幻觉且不伤 CER；CER 奖励几乎消除翻译错误。收益在类型学上更远的语对（如 ara/jpn/rus）最大。训练全用 TTS，零样本转移到真人录音。

## 结论
序列级可验证奖励 + 脚本保真与两遍自修正，能以远少于 SFT 的数据把语音 LLM 对齐到码切换转写行为，并跨声学域迁移。

## 点评
把 CS 失败拆成“翻译”与“错脚本”两条奖励通路，分析清楚；两遍 refine 对部分语对有益但阿拉伯语可能过修正，需 SHR 约束。定位是数据效率与奖励设计研究，非追 SOTA。


# Direct Preference Optimization for English-Mandarin Code-Switching Speech Recognition in Audio LLMs

- 论文编号：110
- 报告人：Minh Duc Pham
- 程序：Thursday 1 October 2026 / Code-Switching ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/nguyen26_interspeech.pdf

## 问题
多语 Audio LLM 在英–汉码切换转写上仍系统失败：漏掉一种语言、整段翻译、幻觉重复；即使含 CS 监督数据的模型也可能如此。

## 方法
用 DPO 对齐：chosen 为真值混合转写，rejected 由 Qwen3-32B 对真值做全局翻译（80%）或部分片段翻译（20%）以模仿失败模式。约 100K 对 / ~570h，来自 CS-Dialogue（自然对话）与 EMILIA（英汉拼接）。训练 MERaLiON-2-3B、Phi-4-MM（全参）与 Qwen2-Audio-7B（LoRA，全参易幻觉）；训练时从 20 英 + 20 中提示池随机采样，评测固定英文转写提示。

## 实验与结果
相对基线 MER：Phi-4 在 EMILIA 70.98→7.38（相对 −89.6%）；Qwen2-Audio SEAME dev man 72.89→58.30（−20.0%）；MERaLiON 因已有 CS SFT，SEAME 增益较小（0.7–2.0%），CS-Dialogue −11.1%。定性显示翻译、幻觉、漏语等三种失败模式均被纠正。SEAME 为分布外。

## 结论
偏好对可把已具备多语能力的 Audio LLM 引出正确的“原样混合转写”行为，分布内与分布外均有一致改善。

## 点评
核心是行为对齐而非重训声学：用可控合成 rejected 放大“翻译≠转写”信号。未显式构造幻觉/漏语 rejected，但三类错误仍下降。局限：仅英汉、rejected 非模型自身采样、未测对其它音频能力的副作用。


# Adding Robust Code-Switching Capabilities to High Performance Multilingual ASR

- 论文编号：1099
- 报告人：Enes Yavuz Ugan
- 程序：Thursday 1 October 2026 / Code-Switching ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ugan26_interspeech.pdf

## 问题
在已很强的多语 ASR（如 Whisper）上加码切换能力时，标准合成数据微调常严重破坏单语表现；文献多评弱基线或域内设定，强模型保真场景研究不足。

## 方法
场景定位为“强模型保真”。用 GPT-4o 按等价约束与德英形态整合规则生成 CS 文本（§§…§§ 标出切换点），xTTS-v2 按段分语合成再拼接。适配采用 BLoRA（贝叶斯低秩，μ/σ 先验推向稀疏 ΔW，λ_KL=0.5）而非标准 LoRA。评 CSFleurs 的 WER 与切换词 PIER，并用 CommonVoice 做单语回退测试。

## 实验与结果
基线 Whisper：DE/EN/CSFleurs WER 8.53/13.56/11.49，PIER 26.59。标准 LoRA 在任意数据量上单语与 CS 均大幅恶化；复杂 MT+对齐拼接同类。BLoRA + 全量合成：CSFleurs WER 10.88（相对改善约 5.31%），PIER 20.84（相对约 −21.6%），单语接近基线。严过滤 CER≤5% 时，仅 1k 样本即可将 PIER 降约 32.87%（文中最佳约 17.85）。文本多样性比说话人多样性对 PIER 略更有利。定性：基线把 matter 误成 meta，BLoRA 可保留英文插入。

## 结论
对强多语模型，瓶颈在知识整合而非合成数据复杂度；稀疏不确定性感知的 BLoRA 可用少量合成数据提升 CS 且保住单语能力。

## 点评
刻意选 Whisper 已很强的德英，否定“更好合成必更好”的假设。BLoRA 稀疏更新是关键机制；过滤在小数据时极重要。依赖手工 PIER 标注与特定语言对规则，向更远语对迁移仍需验证。


# Dynamic Block-Online Streaming ASR for Low-Resource Agglutinative Code-Switching Speech with Morphology-Aware Evaluation

- 论文编号：3334
- 报告人：Nabeel Mohammed
- 程序：Thursday 1 October 2026 / Code-Switching ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/rafat26_interspeech.pdf

## 问题
低资源黏着语（Bangla–English）句内码切换 ASR 中，固定前瞻的因果流式注意力无法回头修正词根–后缀与脚本重排依赖，易在切换点截断形态；码切换数据稀缺，标准 WER 也难以区分切换、词根与后缀错误。

## 方法
以非自回归 Paraformer（SAN-M + CIF）为骨干：离线用全局双向注意力训练；推理改为 Dynamic Block-Online——VAD 在自然停顿（>200ms）切语义宏块（上限约 3s），块内恢复全局注意力以事后绑定词根与后缀。数据侧用 Script-Anchored Loanword Injection：用约 750 个英–孟语义对，将孟加拉词根替换为英语词根并保留孟加拉后缀，诱导句内 CS。提出 CS-WER，分解为 Eswitch / Eroot / Emorph。

## 实验与结果
训练约 750h Bangla（Common Voice、OpenSLR 53、IndicVoices、KathBath 等）+ 250h Gigaspeech 子集；注入后约 20% 句含 CS。Common Voice 上：因果流式即便扩到 3s（WER 37.20%）形态仍平台（Eroot≈0.35、Emorph≈0.42）；Dynamic Block（3s）WER 38.73%，但 CS-WER 达 .53/.29/.35，接近离线 topline。月经/更年期医疗 TTS 适应后，Block-Online 在噪声留出集上 WER 27%、Eroot 22。

## 结论
对黏着语 CS，灵活延迟预算上的双向块注意力比单纯拉长因果窗口更能保住形态与切换语义；脚本锚定注入与 CS-WER 分别解决数据与诊断。局限：依赖可靠 VAD，词表仅覆盖常见借词。

## 点评
核心洞见是“因果不可逆提交”与黏着 CS 的长距依赖不匹配，用 VAD 宏块换回全局注意力，比硬堆 lookahead 更对症。CS-WER 把切换/词根/后缀拆开，解释了为何 Global WER 接近时语义仍差。医疗域“无损迁移”叙事有吸引力，但合成 TTS 适应与真实临床声学差距仍需谨慎解读。

