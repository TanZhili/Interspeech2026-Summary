# Flow Matching for Speech Synthesis

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
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

本场以 Flow Matching（流匹配）为主干，覆盖零样本 TTS、表达风格控制、块级并行推理与说话人身份保持等环节。共同取向是：在保持生成质量的同时，用更可控的条件注入、更可靠的轨迹估计，以及与偏好/对比目标对齐的训练，缓解对齐错误、音色泄漏与跨模态风格鸿沟。

推理侧出现“固定块大小不够用”的共识：连续块流匹配虽能兼顾自回归与块内并行，但语音难度非均匀，需用轨迹几何置信度动态截断并重生成不可靠区间。与此并行，统一引导框架试图把数据侧异构增强与模型侧轨迹拉直结合起来，削弱对 Classifier-Free Guidance（CFG）开销的依赖。

风格与副语言控制更强调层次化与解耦：高层说话人属性与低层音质（如 creak）分阶段注入；自然语言提示到声学风格则用最优传输对齐、对比学习与条件流匹配处理一对多映射。鲁棒性与偏好优化则直接针对跳过/重复、文本到参考音频的贴合度，把失败模式或偏好/非偏好信息写进训练目标。

总体看，流匹配已从“能否合成”转向“如何在身份、风格、内容保真与效率之间做可插拔、可诊断的强化”，且多数工作强调与现有流水线兼容而非推倒重来。

## 论文技术总结

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

