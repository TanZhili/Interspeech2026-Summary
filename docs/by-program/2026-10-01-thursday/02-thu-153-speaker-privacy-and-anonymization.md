# Speaker Privacy and Anonymization

- 日期：Thursday 1 October 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：4
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕说话人隐私与匿名化：轻量时域修改对通信效用的影响、扩散模型推理时韵律可控、可证明差分隐私机制、属性视角威胁评估、声学 token 同时抹除说话人与内容标识，以及全双工对话模型隐状态泄漏与流式匿名。共同议题是在保护身份（及内容）的同时保留可懂度、韵律与下游评估可用性。

方法从启发式替换说话人嵌入，走向可连续权衡的 CFG 扩散（DiffAnon）与形式化 speaker DP（DP-VOXLET）。评测也从信号对信号扩展到属性集合唯一性与单话语攻击。监管域场景要求同时切断生物识别与语言可识别内容，并尽量保留域内声学特性；端到端全双工模型则暴露 LLM 骨干隐状态的说话人泄漏，需要波形/特征域流式匿名前端。

## 论文技术总结

# Privacy vs. Performance: Assessing Communication Utility of Anonymized Voice Features

- 论文编号：751
- 报告人：Shogo Okada
- 程序：Thursday 1 October 2026 / Speaker Privacy and Anonymization
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chan26_interspeech.pdf

## 问题
语音匿名保护身份，但可能扭曲评估沟通质量所需的声学/韵律特征；既往多看 WER/EER，较少直接量化特征保真及其对沟通构念评分的影响。

## 方法
在端到端评估管线最前端用轻量 PV-TSM 匿名（约 0.4 s/2 分钟），原始音频丢弃。比较内部 Kaldi ASR、Azure 发音评估基线，以及在 AMI（36 小时匿名 + 含 uh/um 的原始）上微调的 Azure 定制模型。评估 WER，并对语速、停顿、犹豫、填充比等低层特征与 confidence/persuasion/formality/proficiency 等高层构念做原音 vs 匿名的 Pearson r 与 MAE。

## 实验与结果
AMI 1.5 小时 hold-out：内部 45.13%→58.88%；Azure 基线 12.66%→15.01%；微调后 7.72%→7.89%。面试语料 1000 条上，微调模型原–匿相关普遍最高（如 repetitions r=0.97、hesitation r=0.99、speaking rate r=0.99）；高层中 confidence/proficiency 相关显著提升，persuasion 相关固定约 0.23 但 MAE 低且配对 t 检验不显著。

## 结论
PV-TSM 可大体保留沟通评估所需信息；对匿名数据微调 ASR 可将 WER 差距压到近乎持平，并改善低层/高层特征一致性。

## 点评
把评估从 WER/EER 推进到沟通构念特征保真，贴合就业评估落地约束。隐私数字主要引用先前 EER，本文重心在效用；persuasion 相关偏低提示部分声学构念对相位声码器变换更敏感。


# DiffAnon: Diffusion-based Prosody Control for Voice Anonymization

- 论文编号：1331
- 报告人：Ismail Rasim Ulgen
- 程序：Thursday 1 October 2026 / Speaker Privacy and Anonymization
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ulgen26b_interspeech.pdf

## 问题
韵律兼具表达效用与说话人身份线索；现有匿名方法多固定抑制/保留/扰动韵律，缺少单模型内连续、推理时可调的效用–隐私折中机制。

## 方法
DiffAnon 在 SpeechTokenizer RVQ 空间做条件扩散：以 Q1 为语义条件、MPM 帧级潜变量为韵律、FreeVC 说话人嵌入为说话人条件，x-prediction 重建全层 Q1:8。训练随机丢弃条件；推理用伪说话人替换身份，经 classifier-free guidance 调节 \(w_{pro}\) 控制源韵律保留强度，并可选用伪说话人 CFG。DDIM 100 步；训练于 LibriTTS。

## 实验与结果
VoicePrivacy 2024：\(w_{pro}\) 从 1→0 时 F0 相关与 UAR 单调下降、EER 上升（如 libri-test lazy EER 33.09→42.43），WER 约 4.62→5.61。\(w_{pro}=1\) 时 F0-corr 达 75.58（test），UAR 约 50.80；伪说话人 CFG（\(w_{spk}=3\)）lazy EER 可达 48.16，接近强基线。单模型覆盖多工作点。

## 结论
扩散 + CFG 首次在语音匿名中提供可插值的推理时韵律控制，实证韵律是效用–隐私折中的主轴之一。

## 点评
把折中从“换系统”变成“调权重”，对部署选点很实用。内容靠 Q1 锚定较稳，但强匿名仍损情绪 UAR；semi-informed 下 EER 明显低于 lazy，说明攻击者适应仍挑战形式化“可控”叙事。


# DP-VOXLET: Provable Speaker Anonymization for Disentangled Speech Representations

- 论文编号：2910
- 报告人：Christopher Liberatore
- 程序：Thursday 1 October 2026 / Speaker Privacy and Anonymization
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ngong26_interspeech.pdf

## 问题
基于解耦表征的说话人匿名经验效果好，但缺可证明隐私；对说话人嵌入做朴素随机扰动又常落出解码器有效区域，导致音质崩溃。先前对整句特征加噪的 DP 方案效用差。

## 方法
定义 speaker differential privacy（基于 Gaussian DP / 权衡函数）：对同内容、不同说话人的解耦嵌入，机制输出经解码后应满足 \(G_\mu\) 下界。Gaussian speaker mechanism 对 L2-clip 后的说话人嵌入加噪。DP-VOXLET：在 VC 编码器说话人嵌入上训练 VAE，于低维潜空间加噪再解码回有效说话人嵌入，并做 L∞ clamp；可包装 OpenVoice、NaturalSpeech3、vec2wav2.0、ControlVC 等。

## 实验与结果
VoicePrivacy 2024、OpenVoice、librispeech-test、semi-informed。随噪声 σ 增大 EER 升、WER 略升但仍 <4%（如 σ=10 时 EER 41.2%、WER 3.4%；σ=0 时 EER 4.6%、WER 3.0%）。36 个挑战提交中仅 6 个 EER>40%；相对 Shamsabadi 等整特征扰动方案 EER/效用更优。理论：μ→0 时 EER 下界趋近 50%。

## 结论
在解耦语音表征上给出可组合的形式化说话人匿名与对抗下界，并用 VAE 保持高效用。保障依赖内容通道无说话人泄漏的假设。

## 点评
把 DP 落到说话人嵌入而非整句，是相对先前形式化工作的关键效用改进。Assumption 1（完美解耦）不可证，泄漏时保证减弱；实证与理论 EER 下界的对照仍值得读者单独审视。


# Voice Privacy from an Attribute-based Perspective

- 论文编号：2061
- 报告人：Mehtab Ur Rahman
- 程序：Thursday 1 October 2026 / Speaker Privacy and Anonymization
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rahman26b_interspeech.pdf

## 问题
现有语音隐私基准（如 VPC）主要做信号级说话人匹配；忽略由分类器从语音推断的类别属性档案（性别、年龄、口音、职业等）仍可能单点识别个体，即使匿名后亦然。

## 方法
在属性视角下用 k-匿名式 uniqueness（k=1、k<5 等）评估说话人档案；在单 utterance 目标上做重识别攻击：用 ECAPA-TDNN 嵌入 + MLP 推断属性，与多句参考档案精确匹配（多匹配则随机选）。数据基于 VoxCeleb2 的 72 名四属性齐全说话人；匿名用 VPC 2024 基线 McAdams/STTTS/NAC/ASRBN。发布属性标注扩展。

## 实验与结果
说话人级：真值唯一率 38.9%，推断 31.9%，但 k<5 比例反而上升（65.3%→68.1%），推断噪声未必提升隐私。单句与匿名后亦无一致隐私增益。攻击：原音错误率约 0.67–0.72；部分匿名系统（如 ASRBN、STTTS 对真值参考）错误率可低至约 0.58–0.62，相关推断误差甚至降低隐私。

## 结论
属性档案在推断误差存在时仍构成隐私风险；未来语音隐私需同时考虑属性威胁与防护，而非仅信号级 EER。

## 点评
把 SDC/k-匿名思路引入语音隐私，补上 VPC 信号视角盲区。攻击假设无匿名系统访问且精确匹配偏严；部分匹配与半知情攻击者会更强，是后续防御设计要面对的。


# Acoustic token admixture for joint speaker and content anonymization

- 论文编号：1949
- 报告人：Ali Golmakani
- 程序：Thursday 1 October 2026 / Speaker Privacy and Anonymization
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/golmakani26_interspeech.pdf

## 问题
受监管场景需同时压制生物特征身份与文本风格/命名实体等语言再识别通道；既有方法常分治两通道且全句重合成，毁掉可作域内训练数据的原声学特质。

## 方法
统一声学 token 空间：Stream A 为 Whisper 编码 + 8 级 RVQ；Stream B 为转写→IPA/发音特征→T5 自回归预测同空间 token。按 β 逐帧随机混入两流；余弦相似度门控（τ=0.6）拒收对齐失败的音素 token。NER 敏感跨度强制用 Stream B 并局部编辑替换。BigVGAN 条件于融合 token、变换 F0（α=0.75+噪声）与 ECAPA 伪说话人嵌入。

## 实验与结果
VPC 2024：β=0.7 时 EER 42.54%、WER 3.73%、UAR 40.11%，EER 距榜首 T12-5（43.23%）约 1 点。β 升则 EER 升、WER 缓增。编辑子集：仅混入 Anon.Sim 0.123；全系统 Edit Sim 0.959、MOS 3.84、WER 11.9%。

## 结论
帧级 token 混入 + NER 跨度替换可在不改全句重合成的前提下联合匿名说话人与内容，隐私接近挑战顶尖且可懂性尚可；UAR 与情绪韵律保留仍是主要短板。

## 点评
把内容隐私嵌进同一合成栈，并保留周围帧，贴合“可复用域内录音”需求。情绪效用偏低、依赖 Whisper/NER 召回；门控与 β 的部署调参决定隐私–可懂折中。


# Privacy-Preserving End-to-End Full-Duplex Speech Dialogue Models

- 论文编号：3181
- 报告人：Nikita Kuzmin
- 程序：Thursday 1 October 2026 / Speaker Privacy and Anonymization
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kuzmin26b_interspeech.pdf

## 问题
端到端全双工对话模型（SALM-Duplex、Moshi）持续把用户语音送入 LLM，隐藏状态是否泄漏说话人身份尚未被系统审计；亦缺适配流式对话的匿名方案。

## 方法
按 VPC 2024 lazy-informed 协议，用 ECAPA-TDNN 探针各层/均值池化隐藏状态，报告 EER 与 Linkability。提出两路 Stream-Voice-Anon：Anon-W2W 在波形前端匿名再送原编码器；Anon-W2F 用可匿名离散编码器替换连续前端并微调 LLM（SALM-Duplex 上演示）。分析层深与对话轮次对泄漏的影响。

## 实验与结果
无匿名：Moshi 离散 EER 6.4%、SALM 离散 11.2%、连续 28.5%。W2W：Moshi 36.9%、SALM 连续 34.6%；W2F：41.0%（相对离散基线 11.2% 超 3.5×）。Linkability 在前几轮急升；匿名后 10 轮仍相对可控。质量：sBERT 保留约 78–93%（文中相对降幅约 7–22%）；FRL <0.8 s，但 RTFx 由数十–数百倍降至约 1.6–2.5。

## 结论
全双工 LLM 隐藏状态普遍编码说话人身份；波形与特征域流式匿名可显著抬升 EER，W2F 最接近机会水平。需在质量与延迟上继续优化。

## 点评
把隐私探针从静态 SSL 推进到 always-on 对话骨干，问题设定有时效性。评估仍用朗读 VPC 数据而非自然对话；探针为下界，更强攻击者可能进一步压低 EER。

