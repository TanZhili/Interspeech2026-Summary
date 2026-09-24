# Spoken Language Understanding

- 日期：Wednesday 30 September 2026
- 时间：16:30-18:30
- 形式：Poster
- Area：11
- 论文数：12

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场覆盖口语理解（SLU）从数据与基准、SpeechLLM/LALM 适配，到对话状态跟踪、多意图与多说话人场景，以及能力遗忘与长时音频时间锚定。主线是：把语音侧线索与大模型推理能力接到意图/槽位/对话状态上，同时用新基准暴露单说话人、单意图设定下的盲区。

数据与评测上，DEBATE 用语音消歧文本歧义；MAC-SLU、MSU-Bench 分别加压汽车座舱多意图与会话多说话人；若干工作显示 ICL 远弱于 SFT，端到端 LALM 可接近管线并避免 ASR 级联错误。方法上，RG-FT 蒸馏结构化拒斥推理以拉开相邻意图边界；SPARE 用语义摘要寄存器缓解长 CoT 偏离音频；增量符号编辑 + GRPO、跨域语音—文本联合训练推动口语 DST。

鲁棒与治理方面，原型感知对比与粗到细注意力强化多模态意图；覆盖引导 RL 约束检索代理查询分解；语义帧级多任务自洽聚合多意图输出；Binding Subspace 在表示层削弱意图—槽位条件映射以实现选择性能力遗忘；GigaChat Audio 用周期时间标记支撑长达 120 分钟的时间锚定问答。

## 论文技术总结

# DEBATE: A Dataset for Disentangling Textual Ambiguity in Mandarin Through Speech

- 论文编号：3146
- 报告人：Haotian Guo
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：https://www.isca-archive.org/interspeech_2026/guo26e_interspeech.pdf

## 问题
中文书面语因多音字、无显式词界与重音缺失易产生歧义，文本消歧研究较多，但“通过语音消歧”（DTS）缺乏成对的歧义文本与含发音/停顿/重音线索的口语数据。

## 方法
构建公开中文语音–文本数据集 DEBATE：从开源歧义语料、社交媒体与公考言语理解题收集句子，人工筛入三类任务——多音字（TPronu）、韵律停顿切分（TPause）、重音焦点（TStress）；标注发音、“/”停顿与“<>”重音，并由 LLM+人工审校生成语义解释。10 名母语者（年龄/性别均衡）用自备设备录音；双人协作纠错；SenseVoice-small CER 作质量对照。零样本评测 Qwen2-Audio、Qwen2.5-Omni、Gemini 2.0 Flash：听音频后在二选一释义中作答；并与三人人工听辨对比。

## 实验与结果
共 1001 条歧义文本、10010 条音频、约 9.66 小时（三类约 2000/4010/4000 条）。ASR CER：TPronu 4.75%、TPause 2.82%、TStress 1.94%。
模型最优约：TPronu Acc 65.65%（Qwen2.5-Omni）、TPause ~68%、TStress 最佳 58.83%（Gemini）；重音任务接近随机。小规模人工集上人类显著高于模型且更稳定。

## 结论
DEBATE 首次面向普通话语音消歧；现有大语音语言模型对停顿/多音字有一定能力，但对细粒度重音远弱于人。数据亦可服务 TTS 同形异音与重音渲染研究。

## 点评
把三类“文本看不见、语音看得见”的歧义拆成可评任务，填补了 DTS 数据空白。当前基准是封闭二选一零样本，开放生成与交互消歧会更难；录音设备与自备麦增强生态效度，也可能引入通道噪声，解释模型失败时需一并考虑。


# Distilling Structured Reasoning into SpeechLLMs for Spoken Language Understanding

- 论文编号：1540
- 报告人：Toshihiro Tsukagoshi
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：https://www.isca-archive.org/interspeech_2026/tsukagoshi26_interspeech.pdf

## 问题
SpeechLLM 微调做意图分类/槽填充时，语义相近意图仍易混淆；纯标签监督难拉开边界，收集近边界样本成本高。文本侧推理蒸馏有效，但能否迁移到语音输入的 SLU 尚不清楚。

## 方法
提出 **RG-FT**：用 DeepSeek-R1 在转写、金标与意图/槽定义上生成结构化轨迹 \(T=(C,R,L)\)——候选枚举、对错误候选的拒斥理由、最终标签；94% 样本格式合格。训练对比 Direct-FT（只预测 L）、Reasoning-FT（只学完整轨迹，推理时也生成 C/R）、RG-FT（多任务 \(\alpha L_{\mathrm{reasoning}}+(1-\alpha)L_{\mathrm{label}}\)，推理仅直接出标签）。在六个 SpeechLLM 上全参微调，语音+金标转写联合训练，\(\alpha=0.5\)。

## 实验与结果
SLURP 与 Speech-MASSIVE-FR：RG-FT 全面优于 Direct-FT；意图准确率最高约 +2.4%，SLU-F1 最高约 +2.8（如 Music-Flamingo）。Reasoning-FT 普遍差于 Direct-FT。潜空间：Silhouette、Fisher ratio、centroid margin 均上升。消融显示 C→R→L 逐步增益；\(\alpha\) 呈钟形，0.5 附近稳健。

## 结论
把拒斥式结构化推理作辅助正则，可 sharpen 意图边界且推理零额外开销。纯推理监督不稳定；开放问题包括轨迹质量、教师选择、噪声条件下声学如何进入推理。

## 点评
关键设计是“对比拒斥”而非只肯定正确标签，直接针对近义意图混淆。多任务把推理压成训练期表征塑造、推理期仍直出标签，工程上务实。教师依赖文本转写与金标，对纯语音噪声/ASR 错误的鲁棒性正文未充分验证。


# Enhancing Audio Reasoning via Semantic Summary Prediction

- 论文编号：1504
- 报告人：Francesco Bonzi
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：https://www.isca-archive.org/interspeech_2026/bonzi26_interspeech.pdf

## 问题
大音频语言模型（LALM）显式 Chain-of-Thought 常比直接作答更差：长推理易把注意力从音频拽向已生成文本，造成“reasoning gap”。现有缓解多依赖海量监督或昂贵 RL，缺少轻量训练期正则。

## 方法
提出 **SPARE**：在 SALMONN 13B 上，于音频/问题之后、CoT 之前插入 register 令牌 [REG]；用因果掩码使后续 token 看不到 [REG]，推理时丢弃该令牌与对齐头。训练时对 [REG] 末层隐状态与 Conclusion 的 Sentence-BERT 嵌入做余弦对齐损失，总损失 \(L_{\mathrm{CE}}+\lambda L_{\mathrm{align}}\)（\(\lambda=2\)）。数据为 YouTube8M 子集上 AF-Think 结构（summary/caption/reasoning/conclusion），约 16 万训 /4 万验。对比零样本、CoT、SFT、Audio MuToR。

## 实验与结果
MMAU / MMAR 零样本：SPARE 58.03% / 40.32%，高于 SFT（54.65 / 38.15）与 Audio MuToR（53.02 / 38.40）；零样本 CoT 则崩至 18.03 / 12.32。\(\lambda=1/2/3\) 均优于非 SPARE；多章节多 register 变差且不稳。注意力分析：首层 [REG] 对音频关注显著增强，答案 token 相对 SFT 也更听音频。

## 结论
用终局语义目标“播种”早期潜状态，可在不改推理流程、无额外开销下改善音频 grounding 与 CoT 推理。相对工业级大模型仍有绝对精度差距，但方法定位为可控设定下的正则策略。

## 点评
把 MuToR 式 register 从局部多 token 预测改成全局结论对齐，针对音频漂移问题更直接。因果掩码保证零推理成本是亮点。效果依赖 Conclusion 文本质量与 Sentence-BERT 空间；若结论本身短/歧义，对齐目标可能噪声较大。


# Incremental End-to-End Spoken Dialogue State Tracking with a Multimodal LLM and Reinforcement Learning

- 论文编号：592
- 报告人：Tomoya Higuchi
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：https://www.isca-archive.org/interspeech_2026/higuchi26_interspeech.pdf

## 问题
口语 DST 的 ASR→文本 DST 级联易传播错误；端到端多模态 LLM 可直接从音频推断状态，但现有口语 DST 仍常每轮重生完整信念状态，输出冗长且易污染未变槽。增量更新在文本 DST 已复兴，却尚未系统用于端到端口语 DST。

## 方法
基于 Qwen2.5-Omni-7B + QLoRA：输入对话历史、上一信念状态与当前音频，输出转写与符号编辑（set/update/delete），确定性应用到 \(B_{t-1}\)。两阶段训练：SFT 学格式与对齐；再 GRPO，组内相对优化奖励 \(r=\alpha r_{\mathrm{WER}}+\beta r_{\mathrm{diff\text{-}F1}}+\gamma r_{\mathrm{exact}}+\delta r_{\mathrm{format}}\)（权重 0.3/0.5/0.1/0.1）。对比级联 SPACE+WavLM、Gemma-2-9B 全状态、同骨干全状态 SFT。

## 实验与结果
SpokenWOZ predicted mode：增量 SFT JGA 48.52（全状态同骨干 45.36，+3.16）；+GRPO 达 49.20，SER 18.03；WER 21.61（全状态 23.01）。Oracle 下增量 JGA 约 88–90，predicted 掉约 40 点，显示误差传播是主瓶颈。去掉 WER 奖励后 JGA 与 WER 双降。中后期轮次增量仍优于全状态。

## 结论
增量编辑 + GRPO 在 SpokenWOZ 达到正文报告的最佳结果；训练用金标上一状态，部署时自预测状态易级联出错。局限：单模型单数据集、GRPO 采样成本高。

## 点评
把文本 DST 的差分更新搬到语音端到端，并用 GRPO 同时拉转写与编辑质量，针对增量路径的“错一次、错全程”很对症。Oracle/predicted 鸿沟说明下一步应做带噪声历史的训练或恢复机制，否则增益难完全落到真实对话。


# Joint Speech And Text Training For LLM-based End-To-End Spoken Dialogue State Tracking

- 论文编号：2769
- 报告人：Katia Vendrame
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：https://www.isca-archive.org/interspeech_2026/vendrame26_interspeech.pdf

## 问题
端到口口语 DST 依赖稀缺的带标注口语数据，跨域（尤其是地名/店名等槽值）泛化差。为每个目标域再采口语数据成本高，而文本 DST 数据更易获得。

## 方法
在 speech-encoder + connector + LLM（LoRA）E2E DST 上增加仅训练期使用的 text encoder：语音与文本经各自编码器后共用 connector/LoRA，联合训练。损失含：口语 DST、未配对文本 DST、以及口语批次转写上的文本 DST。先冻 LLM 做 ASR 预训练（Fisher/LS/CV/VoxPopuli），再微调 connector、text encoder 与 LoRA。推理丢弃 text encoder。对比无文本基线、无 text encoder 只训 LoRA、以及 Qwen3-TTS 合成语音。

## 实验与结果
SpokenWOZ ↔ Speech-aware MultiWOZ 交叉：源域语音 + 目标域文本可明显收窄与目标语音训练的差距（如 MW 验证上 SW 语音+MW 文本 15.1→19.0；SW 上 MW 语音+SW 文本 20.5→30.6）。混入 DialogStudio 仍有效；仅 DS 时主要帮含 MW 的场景。无 text encoder 有部分收益，完整流水线更好；调大文本损失权重可逼近 TTS 合成效果。更大 LLM（Gemma-3-12B）上联合文本甚至可使跨域 JGA 接近源域语音训练。分析显示跨域收益常来自槽键/实体错误率，而非一律降低 WER。

## 结论
用未配对文本做联合训练可实现“部分域有语音、其余域只有文本”的多域口语 DST，且无需 TTS。方法随 LLM 规模更稳，为文本侧槽增强等策略迁移到口语系统打开空间。

## 点评
共享 connector/LoRA 让文本监督回流到语音通路，比只给 LLM 看目标域 JSON 更实质性。MW 训练/测试城市不一致时值难直接迁移，正文也如实反映；实际部署仍需关心目标域槽值覆盖，而非仅槽键。


# MAC-SLU: Multi-Intent Automotive Cabin Spoken Language Understanding Benchmark

- 论文编号：1055
- 报告人：Yuezhang Peng
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：https://www.isca-archive.org/interspeech_2026/peng26d_interspeech.pdf

## 问题
现有 SLU 数据意图/槽类别少、多为单意图，模型已接近饱和；且对最新 LLM/LALM 缺少统一格式与评测协议，难公平比较 ICL、SFT、流水线与端到端。

## 方法
构建中文车舱多意图数据集 MAC-SLU：真实车载指令文本脱敏后，用 CosyVoice-2 + AIShell-1 说话人模板 TTS；8 域、81 意图、192 槽，含 0–5 意图与拒识。统一评测零样本/少样本 ICL、LoRA SFT，以及 ASR+NLU 流水线与 E2E LALM。指标：IC Acc、SF F1、Overall Acc（IC+SF 同时正确）。

## 实验与结果
约 20539 条（train/dev/test 17997/1391/1151）；多意图约 15.46%，拒识 28%。
- ICL：Overall Acc 普遍 <15%；Qwen3-32B 10-shot SF F1 55.09%，OA 14.42%；Qwen2.5-Omni-7B 可略超同规模 Whisper+Qwen3-8B 流水线。
- SFT：Qwen3-8B 文本 OA 60.73%；流水线因 ASR 误差降至 47.18%（Paraformer CER 3.64%）或 35.45%（Whisper CER 10.40%）；Qwen2.5-Omni-7B OA 55.60%，接近或优于流水线。
- 案例分析：不少错误是语义对但用词与标签不完全一致，严格字符串匹配可能低估能力。

## 结论
MAC-SLU 提高任务难度；ICL 有潜力但远逊域内 SFT；E2E LALM 可规避 ASR 传播并接近流水线。未来需语义对齐评测、更复杂声学与口音。

## 点评
把“车舱多意图 + 统一 LLM/LALM 基准”做实，填补了中文复杂 SLU 评测空白。TTS 语音保护隐私但弱化真实舱内噪声/口音；标签措辞敏感也提示标准 SLU 指标与下游可执行性之间仍有缝隙。


# MSU-Bench: Towards Understanding the Conversational Multi-Speaker Scenarios

- 论文编号：3344
- 报告人：Zhaokai Sun
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：https://www.isca-archive.org/interspeech_2026/sun26j_interspeech.pdf

## 问题
LALM 把 SLU 推向端到端生成，但现有语音基准多为单说话人或孤立子任务，缺少对真实多说话人对话中“说话人中心理解”（身份绑定、关系、动机、交互）的诊断式评测。

## 方法
提出 MSU-Bench：两层 16 任务、2300 道四选一 QA。Tier1 说话人 grounding（识别/属性等），Tier2 多说话人推理（场景、结构、上下文）。数据来自电话、会议、播客、电影中英素材；Gemini 辅助质检与标注，火山 API 做 diarization/转写，人工复核。五种说话人指称：无索引（目标音频片段）、时间、转写、出场顺序、复合线索。干扰项标注错误类型（错说话人/幻觉/未知等）。零样本评测 6 个开源 + 3 个 Gemini 闭源模型。

## 实验与结果
总体准确率约 0.19（Qwen2.5-Omni）–0.77（Gemini-3-Flash）；开源最强 MiMoAudio 0.56。闭源全面领先。Time Index 普遍最难；Complex Index 常因多线索而更好。强模型错误以 wrong-speaker 为主（Gemini-3-Flash Tier2 约 0.67），弱模型更多选 unknown。人工验证：初始 QA 有效性 Tier1/2 为 95%/86%，人类与终标一致 98%/96%。

## 结论
MSU-Bench 暴露出时间定位与正确说话人归因是主要瓶颈；更强模型从“不会答”转向“答错人”。基准标注与脚本已公开。

## 点评
诊断式干扰项与指称方案让“差在哪”可读，而不只给总分。Gemini 参与造题又参与评测有偏好风险，作者用人审缓解，但仍需独立复现。选择题便于打分，开放生成场景下的说话人理解难度可能更高。


# MVCL-DAF++: Enhancing Multimodal Intent Recognition via Prototype-Aware Contrastive Alignment and Coarse-to-Fine Dynamic Attention Fusion

- 论文编号：267
- 报告人：Haofeng Huang
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：https://www.isca-archive.org/interspeech_2026/huang26_interspeech.pdf

## 问题
多模态意图识别（文本+视觉+声学）在噪声与长尾/稀有类下语义锚定弱；MVCL-DAF 等对比对齐停在实例级，融合把模态当扁平 token，忽视层次结构与冗余。

## 方法
提出 **MVCL-DAF++**：保留原 CTC 对齐、BiPeephole LSTM 音频与 BERT 池化解码器，新增 (1) **原型感知对比**：批内按类均值得原型 \(r_c\)，做实例–原型 InfoNCE；(2) **粗到细 DAF**：模态感知 Transformer 以文本为 Q、视觉为 K、声学为 V 得粗粒度 \(M_c\)，再与 token 级特征经两路 DAF 得 \(M_f\)/\(M_{cf}\)。总损失 \(L_{\mathrm{cls}}+L_{\mathrm{proto}}+L_{\mathrm{contrastive}}\)。

## 实验与结果
MIntRec / MIntRec2.0（10 种子平均）：
- Acc 76.18% / 60.40%，WF1 75.66% / 59.23%，相对 MVCL-DAF 分别 +1.46/+2.60 Acc、+1.05/+4.18 WF1；摘要称稀有类 WF1 提升同量级。
- 消融：去掉原型或粗到细融合均下降；三损失齐用最佳。
- 注意分析：更噪的 MIntRec2.0 更依赖粗特征；t-SNE 显示类簇围绕原型更紧。

## 结论
原型锚定与粗–细融合提升跨模态一致性与长尾鲁棒性，在两基准刷新 SOTA。未来拟与 LLM 架构结合。

## 点评
相对纯实例对比，类原型提供更稳的语义锚，适合不平衡意图；粗特征在噪声集上权重升高也符合直觉。增益在 MIntRec2.0 更明显，说明方法主要吃“难分布”红利；与 LLM 时代端到端 LALM 路线相比，仍是经典编码器–融合分类框架。


# PROGRESS: Coverage-guided RL to Train Search-augmented LLM Agent

- 论文编号：2760
- 报告人：Aounon Kumar
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/paul26_interspeech.pdf

## 问题
搜索增强 LLM agent 常用 outcome 级奖励（如 exact match）做 RL，对中间搜索查询质量监督不足，易产生粗粒度复合查询、检索低效，尤其在小模型上。

## 方法
PROGRESS 在 Search-R1 / PPO 框架上加入轨迹级 coverage reward。冻结教师（Qwen2.5-72B-Instruct）离线生成 essential search queries；策略 rollout 提取搜索查询后，由 LLM judge 按语义与粒度匹配，算 precision/recall 的 F1 作为 \(r_{cov}\)。总奖励为 \(r_{ans}+r_{format}+\lambda_{cov}r_{cov}\)（\(\lambda_{cov}=0.2\)）。检索用 2018 Wikipedia + E5，每查询 top-3。

## 实验与结果
策略为 Qwen2.5-3B Base，主训 NQ+HotpotQA。多跳平均 EM：PROGRESS 30.19，优于 Search-R1 (EM,FR) 28.64 与 Zero-search 27.13；仅 HotpotQA 训练时多跳平均 31.28。检索准确率平均 44.96 vs Search-R1 38.66。查询质量（Completeness/Granularity）在 2wiki、MuSiQue 上均提升。1.5B 上亦有小幅增益。

## 结论
教师引导的 coverage 监督可在不需逐步标注的情况下改善查询分解与检索，带来约 2–5% 绝对 EM 提升；作者强调中间搜索行为塑形对 agentic LLM 很重要。

## 点评
把“查什么”从 outcome RL 中拆出，用 F1 式覆盖奖励做轻量过程偏置，方向清楚。依赖强教师与 LLM judge，匹配误差与 \(\lambda\) 设定会传导到策略；文中也承认仍有直接用复杂查询搜索的失败例。


# SFL-MTSC: Leveraging Semantic Frame-Level Multi-Task Self-Consistency for Robust Multi-Intent Spoken Language Understanding

- 论文编号：3369
- 报告人：Po-Yen Chen
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26ea_interspeech.pdf

## 问题
Prompt-based 多意图 SLU 因解码随机性，多路径预测的 intent–slot 语义帧常冲突；输出级多数投票难以细粒度剔除虚假意图与噪声槽位。

## 方法
SFL-MTSC：对同一 utterance 采样 K 条路径，聚合成帧池 \(F=(d,i,s)\)。先按 (domain,intent) 分桶，桶内用 Hybrid Jaccard（key-value 与 value Jaccard 插值，\(\alpha=0.3\)）建阈值图做槽聚类；以跨路径 support 过滤（\(\mathrm{supp}\ge\lceil K/2\rceil\)），再 Value-First 重积成最终多意图预测。零样本后处理，无需微调。

## 实验与结果
MAC-SLU（中文车载多意图）。配置：Qwen3-4B 文本、Whisper+Qwen3 管线、Qwen2.5-Omni-7B。K=5，温度 {0,0.3,0.5,0.7,1.0}。Vanilla Prompting 上 Overall Acc. 分别 +1.23/+0.4/+1.45，Slot F1 最大 +28.86；Intent Acc. 常略降。消融显示槽级 support 过滤是主增益源；\(\alpha\) 在 [0,0.7] 对 Overall Acc. 较稳。

## 结论
帧级自洽聚合可稳定提升 Overall Acc. 与 Slot F1；局限包括 Intent Acc. 偶降、LALM 高方差时增益有限、仅单数据集评估。

## 点评
把 self-consistency 做到语义帧与槽簇，比整句投票更贴合多意图结构。Hybrid Jaccard 针对槽键命名漂移合理；Overall Acc. 绝对值仍很低，说明零样本多意图本身很难，该方法更像稳健后处理而非端到端突破。


# Selective Capability Unlearning in End-to-End Spoken Language Understanding

- 论文编号：3349
- 报告人：Akanksha Singh
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/singh26d_interspeech.pdf

## 问题
端到端自回归 SLU 中，功能是“意图 + 条件槽生成”。只压低目标意图边缘概率时，强制意图前缀仍可恢复槽结构，即 capability persistence；需选择性擦除条件映射并保留其余意图。

## 方法
Binding Subspace Unlearning (BSU) 两阶段：(1) 在槽位上 teacher-force 抽 decoder 隐状态，用 forget vs retain 协方差差 \(M^{(\ell)}=\mathrm{Cov}_{D_F}-\mathrm{Cov}_{D_R}\)，取正特征方向得绑定子空间 \(U^{(\ell)}\)；(2) 对条件 log-likelihood 相对隐状态的梯度投影到该子空间并惩罚 \(\mathcal{L}_{bind}\)。总目标：\(-\mathcal{L}_F+\lambda_{ret}\mathcal{L}_R+\lambda_{kl}\mathcal{L}_{kl}+\lambda_{bind}\mathcal{L}_{bind}\)。无推理开销。

## 实验与结果
SLURP 与 SpeechMASSIVE（法语子集）；Conformer 编码器 + Transformer 解码器，ASR 初始化与 SSL 初始化两套。相对 GA/NPO/RL 等，BSU 大幅降低 forget 集 BRR@10 与语义相似度（如 SLURP NeMo：BRR@10 92.64→22.10，Sim 90.14→24.80），retain 性能大体保持。Random Space 消融与 \(\lambda_{bind}\) 扫描支持子空间对齐的必要性。

## 结论
需在表示空间削弱意图–槽绑定，而非仅抑制意图分类；BSU 显著降低 forced-prefix 可恢复性并保留其余能力。未来拟扩展到更广生成任务。

## 点评
把 unlearning 问题从“别说出意图”改成“别还能按该意图填槽”，评估协议（BRR@10）直接对准失败模式。协方差对比假设 forget/retain 方差差能定位绑定方向，对纠缠强或小样本意图可能脆弱；表格数字密集，但主结论与图示一致。


# GigaChat Audio: Time-aware Large Audio Language Model

- 论文编号：2343
- 报告人：Aleksandr Kutsakov
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kutsakov26_interspeech.pdf

## 问题
长录音上的 audio LLM 时间定位不可靠：时间戳不可解析、过粗或无依据；标准音频 token 流不显式承载时间，短训难外推到长音频。

## 方法
在 10B-A1.8B MoE 文本底座上接 encoder→subsampler→projector（160 ms 帧），在连续音频 token 间周期性插入 inter-timing（默认每 60 s，hh:mm:ss 或专用 timing token）。任务含 temporal grounding、按区间片段描述、带时间戳摘要。合成数据：YODAS2 英语音频经 WhisperX 对齐，切片 ~10 min 用 GPT-OSS-120B 生成并用全局 verifier 校验，按录音级划分 train/eval。

## 实验与结果
去 inter-timing 后长音频 TGr mIoU 53.8→14.2；每 7 s 锚点可到 65.2。时长混合训练对 0–120 min 外推优于单时长。专用 timing token 需更高 TG 数据占比才逼近明文时间戳。AMI 上 MAE 3.50 s（vs Qwen3-Omni 290.5）。发布权重与 10k+ 小时时序数据集。

## 结论
周期性时间锚点与多时长混合对长录音时间感知至关重要；稀疏到每分钟仍可插值到秒级中位误差。开源模型与数据以推动后续工作。

## 点评
把“何时发生”做成可验证的 interval 指标，并用级联合成缓解长音频标注成本。锚点频率与 token 开销的权衡清楚；摘要/描述依赖 LLM judge，且合成管线质量决定上限。会话主题为 SLU，但工作实质是长音频时序 QA。

