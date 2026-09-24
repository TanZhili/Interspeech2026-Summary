# Generative Audio and Music

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Long Oral
- Area：
- 论文数：5

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场为跨领域长文 oral，主题是生成音频与音乐：从控制、主体性与评测的综述，到否定理解失败、整曲生成、连续扩散口语语言模型扩展律，以及视频到音频的统一 Foley 框架。主线是超越纯文本提示，追求可解释、可编辑的条件与语义忠实性。

综述强调文本提示易用但音乐上含糊，创作者需要 MIDI、歌词、分轨、参考音频与合成器旋钮等控制；评测也不能只靠感知质量与 Fréchet 距离。实证工作则暴露 T2A 模型对否定提示几乎无效（否定与肯定输出近乎声学相同），整曲生成用半自回归块流匹配与跨对偏好优化改善歌词–人声对齐与多偏好训练，连续扩散 SLM 在大规模数据下可产生富情感多说话人多语语音但长程连贯仍难，视频到音频则整合多模态控制、帧级时序对齐与细粒度语义。

## 论文技术总结

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

