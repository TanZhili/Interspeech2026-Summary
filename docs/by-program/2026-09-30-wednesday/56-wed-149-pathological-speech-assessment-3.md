# Pathological Speech Assessment 3

- 日期：Wednesday 30 September 2026
- 时间：16:30-18:30
- 形式：Poster
- Area：13
- 论文数：8

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场延续病理语音评估：神经退行与运动障碍（ALS、亨廷顿）、抑郁跨库检测、构音障碍严重度，以及上气道疾病相关鼻化。贯穿问题是临床标注稀缺、异质性强与跨语料/跨人群迁移难。

数据增广与参数高效适配成为主路径：流匹配大规模合成病理/健康元音，并考察合成规模定律；MOS 合成评测语料迁移到构音障碍可懂度/自然度；WavLM 上层次 LoRA-MoE 用临床监督路由做严重度专用专家。图学习则把多发音片段 SSL 嵌入聚成被试级图，服务 ALS 严重度与进展预测。

抑郁检测强调稀疏诊断线索：跨模态自适应门控按帧重加权；层间多因素自适应解缠抑制说话人/语料干扰在层级中的累积。亨廷顿篇章朗读用多语种复合时间语音指数对齐 UHDRS；上气道手术前后则用 A1-P0/A1-P1 系统分析元音鼻化。整体上，临床可用性依赖“可迁移表征 + 可解释声学指标 + 可扩展合成监督”。

## 论文技术总结

# Multi-Phonation Graph Learning with Self-Supervised Speech Embeddings for ALS Detection and Progression Prediction

- 论文编号：844
- 报告人：Behrad TaghiBeyglou
- 程序：Wednesday 30 September 2026 / Pathological Speech Assessment 3
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/taghibeyglou26_interspeech.pdf

## 问题
ALS 相关构音障碍线索分散在多类发声任务与时段；标签少、说话人变异大，单录音/手工特征或端到端深度模型难稳健做严重度与进展预测。

## 方法
SAND：339 人（205 ALS / 134 对照），每人最多 5 元音 + 3 DDK。重采样 16 kHz、铺成 20 s、切成 10×2 s；冻结 SSL（wav2vec 2.0 / HuBERT / data2vec / UniSpeech-SAT）均值池化得 768 维节点；按 cosine 建受试者级 kNN 图，用 GCN / ResGCN / GAT / GraphSAGE / GIN 图分类（均值池化 + MLP）。Task1：5 类构音严重度；Task2：由早期录音预测末次 ALSFRS-R（4 类）。

## 实验与结果
官方验证集最佳 HuBERT+GIN：Task1 mF1 0.73（BACC 0.72），Task2 mF1 0.69；同验证基线约 0.61 / 0.58。10-fold CV 上同配置约 0.67±0.05 / 0.67±0.10。作者提醒与挑战测试榜（服务器）不可直接比。

## 结论
多录音片段在 SSL 嵌入空间用图消息传递可提升受试者级 ALS 评估；HuBERT+GIN 双任务最稳。局限：SSL 多为英语预训练而数据为意大利语等。

## 点评
把“一人多任务多片段”显式建成图，比独立录音更合理。GIN 的 sum 聚合适合稀疏关键线索；跨语 SSL 与验证/测试划分差异使绝对数字需谨慎解读。


# Synthetic Pathological Speech at Scale: A Flow Matching Approach for Clinical Data Augmentation

- 论文编号：2313
- 报告人：Alkis Koudounas
- 程序：Wednesday 30 September 2026 / Pathological Speech Assessment 3
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/koudounas26_interspeech.pdf

## 问题
病理嗓音数据稀缺且不平衡；噪声/变调等线性增强几乎无助，因其抓不住声门非线性不稳。需可控生成健康/病理持续元音并验证合成规模对下游检测的缩放律。

## 方法
在 F5-TTS（Conditional Flow Matching + DiT）上以 “⟨healthy|pathological⟩ + 元音音素” 文本条件微调；参考音频引导说话人/韵律，ODE 生成 mel。训练语料：SVD / AVFAD / VOICED / PVQD 共 7,211 条（四语）。下游用 HuBERT-AS + MLP 做健康/病理二分类；合成规模 \(N\in\{10^2,10^3,10^4,10^5\}\)。

## 实验与结果
仅合成 100k 训、真实 held-out 测：Acc 0.836 vs 真实基线 0.804（+3.9%），Sensitivity +13.3%。Real+Synth 随规模单调升，传统 Real++ 几乎无效。OOD：FEMH/IPV 多类 F1 约 +10.0%/+7.4%；PC-GITA 零样本帕金森 Acc 在 10k 达 0.647（+6.8%），100k 回落。Praat 显示合成病理 jitter/shimmer/HNR 接近真实。

## 结论
流匹配合成可按规模缓解临床数据短缺并提升跨域稳健性；过大合成对远 OOD 任务可能过拟合一般病理模式。

## 点评
缩放律实验设计清楚，且用声学特征与 t-SNE 核对合成是否保留病理线索。二值流形对细粒度病种与 PD 特异特征覆盖有限，作者对 100k 零样本回落的解释合理。


# Learning to Attend to Depression-Related Patterns: An Adaptive Cross-Modal Gating Network for Depression Detection

- 论文编号：1075
- 报告人：Hangbin Yu
- 程序：Wednesday 30 September 2026 / Pathological Speech Assessment 3
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yu26c_interspeech.pdf

## 问题
抑郁相关声学/文本线索稀疏、局部出现；多数方法对整段均匀池化，假设各帧同等重要，易淹没诊断性片段。

## 方法
双分支：冻结 HuBERT（第 12 层）取声学帧特征；WeNet ASR 转写后用指令感知 Qwen-Embedding-0.6B 取文本 token。ACMG 用掩码均值池化得全局上下文，跨模态（或单模态）拼接后经 sigmoid 产生帧/token 门控权重，逐元素重加权；再经各模态 Transformer，拼接送 MLP 预测严重度。

## 实验与结果
PDCD2025（三分类 Healthy/Mild/Moderate，5-fold）：最优 Cross-modal ACMG + Qwen 平均 Acc 81.25%（相对无 ACMG 的 Transformer(Qwen) +1.47；相对 RoBERTa 基线更高）。DAIC-WOZ 开发集 F1 69.39（相对无门控 64.38）。声学门控与能量负相关（整体 −0.329）；文本门控抬高负向情感等词。

## 结论
自适应跨模态门控能突出低能量停顿等与负向文本线索，提升抑郁检测；未来可探索其他门控权重计算方式。

## 点评
直接针对“稀疏诊断线索”设计门控，可视化与能量相关分析增强可解释性。转写质量与指令嵌入选择影响上限；DAIC 仅报开发集，跨语/场景泛化仍待看。


# Layer-wise Multi-factor Adaptive Disentanglement for Cross-corpus Speech Depression Detection

- 论文编号：465
- 报告人：Minggang Wang
- 程序：Wednesday 30 September 2026 / Pathological Speech Assessment 3
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26j_interspeech.pdf

## 问题
说话人解耦有助语料内抑郁检测，但跨语料时说话人/语料等多源偏移在编码器各层累积；仅输出层或仅说话人约束不够，均匀解耦强度又易过/欠解耦。

## 方法
LMAD（无监督域适应）：在多个关键层用 HSIC/CKA 估计表示对说话人 \(u\)、语料 \(c\)、抑郁 \(y\) 的依赖；层间/层内依赖比例与主损失梯度方向一致性共同得到自适应权重 \(w^*_{l,v}\)。目标：源域 BCE + 加权抑制 \(u,c\) 依赖 − 加权保留 \(y\) 依赖。骨干 DepAudioNet 与 ECAPA-TDNN；输入 3.84 s 段的 40 维 Fbank。

## 实验与结果
双向 DAIC-WoZ↔Androids。带自适应的 LMADw_Eb：DAIC→Androids macro-F1 0.62（基线 Eb 0.39；MDFA 0.42），Androids→DAIC 0.56（基线 0.44）；语料内仍具竞争力（如 DAIC 0.70）。层间抑郁依赖比例与 UMAP 显示自适应版更把最终嵌入推向抑郁相关、减弱语料/说话人簇。

## 结论
多层多因子自适应解耦可稳定提升跨语料迁移并保持语料内表现；关键层需先验选定是局限，未来希望训练中自适应选层。

## 点评
把域偏移当作层级累积问题，并用梯度一致性调节解耦强度，比单点对齐更细。HSIC 线性核与 batch 估计对小 batch/类别不均敏感；Androids 仅用自发语音以贴近 DAIC，迁移结论受此协议约束。


# Augmenting Dysarthric Speech Severity Assessment with MOS Supervision

- 论文编号：1300
- 报告人：Zengrui Jin
- 程序：Wednesday 30 September 2026 / Pathological Speech Assessment 3
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jia26_interspeech.pdf

## 问题
构音障碍严重度评估依赖临床标注，数据稀缺；生成式增强缺乏感知级重标注，难直接服务严重度回归。合成语音伪影与构音障碍在可懂度/自然度上有感知共性，能否用 TTS MOS 语料作增强。

## 方法
SSL（wav2vec 2.0 / HuBERT）均值池化 + 两层回归头，端到端微调。目标：SAP 开放域构音障碍语料的 Intelligibility / Naturalness（1–7）。辅助：QualiSpeech 的 Overall / Naturalness MOS（1–5），线性映射到 SAP 尺度。两种范式：JT（1:1 混合联合回归）；FT（先 QualiSpeech 再 SAP）。

## 实验与结果
开发集作测试（说话人未见）。FT 在两维上稳定优于仅域内训练；JT 对自然度有效，对可懂度常负迁移。维度匹配增强（QualiSpeech Naturalness→SAP Naturalness）MSE 相对降幅最大（如 wav2vec Base 约 36.4%）。小编码器在仅域内时更稳，大模型更吃增强。

## 结论
TTS 评估语料可作标签高效增强；可懂度更适合顺序微调而非联合优化。合成失败与构音障碍共享感知/声学共性。

## 点评
把“感知 MOS”直接接到临床严重度，绕过无标注合成。可懂度与 Overall/Naturalness 语义错位解释了 JT 失败，论证清楚；SAP 可懂度标签严重偏斜（多为 1）仍限制上限。


# Clinically-Supervised Hierarchical LoRA-MoE: A Parameter-Efficient Framework for Severity-Aware Dysarthric Speech Assessment

- 论文编号：3043
- 报告人：Jiaqi Wang
- 程序：Wednesday 30 September 2026 / Pathological Speech Assessment 3
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26ga_interspeech.pdf

## 问题
构音障碍数据少、严重度声学异质大；全量微调 SSL 易过拟合，标准 LoRA 对所有输入共享低秩适配，难刻画不同严重度模式。

## 方法
冻结 WavLM-Large Transformer，仅训 CNN 前端与 LoRA。下层 N 层共享 LoRA；上层用多专家 LoRA，由临床严重度监督的 utterance 级 router（时序注意力池化）选专家。损失：加权 CE + \(\lambda_1\mathcal{L}_{router}+\lambda_2\mathcal{L}_{bal}\)。默认 N=9，r=16，5 专家。训练用噪声/变速/音高扰动与随机时段静音掩码。

## 实验与结果
UA-Speech，OSPS 说话人独立五折；2 类（健康/障碍）与 5 类（健康+四档可懂度）。WavLM LoRA-MoE：5 类 Acc 64.32%、macro-F1 61.55%；2 类 F1 94.54%、AUC 96.59%，优于全量微调与标准 LoRA。N 消融呈倒 U，N=9/12 最优。

## 结论
分层共享 + 严重度条件专家路由以极少可训参数超越全量微调；未来拟做连续严重度与多模态。

## 点评
把临床严重度先验写进 router，比均匀 LoRA 更贴异质性。训练时 router 用真标签、推理不用，需依赖表示是否学到可分线索；UA-Speech 说话人少、低/中档仅各 3 人，方差仍大。


# A multilingual composite speech index to assess passage reading in Huntington’s disease

- 论文编号：2654
- 报告人：Valentina G. Constantin
- 程序：Wednesday 30 September 2026 / Pathological Speech Assessment 3
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/constantin26_interspeech.pdf

## 问题
亨廷顿病（HD）罕发病，临床试验需跨语合并数据；段落朗读兼具运动与认知负荷，但语言差异曾使朗读特征被排除在跨语分析外。

## 方法
89 HD + 82 对照，英/波/西三语朗读。TKEO 包络 + 窗内 Otsu 自适应阈值检测有声能量 burst；提 10 个时序特征。线性混合模型（语言、性别固定效应，受试者随机截距）筛出三语均显著的 6 个特征（TST、NST、TPT、MBD、NBR、nP）；按同语对照标准化后平均得 CTSI，与 cUHDRS、SDMT、SWRT、TMS 做相关。

## 实验与结果
六特征三语均显著区分 HD/对照。CTSI 与 cUHDRS r=−0.74、SDMT −0.77、SWRT −0.70、TMS 0.64（均 p<0.001），与加工速度/注意（SDMT）最高。

## 结论
全自动、跨语可用的复合时序语音指数可反映 HD 运动与认知改变，或有助于早期监测。

## 点评
用对照标准化避开语言混杂，比硬训跨语 ML 更适合小样本罕见病。仅能量/时序特征，未用谱或 ASR；段落与设备因站点而异，长期进展敏感性仍待纵向验证。


# Vowel Nasalization in Upper Airway Diseases: An Analysis Using the CUCO Database

- 论文编号：46
- 报告人：Qi Wang
- 程序：Wednesday 30 September 2026 / Pathological Speech Assessment 3
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wei26_interspeech.pdf

## 问题
上气道疾病改变鼻气流与鼻–口共鸣耦合，但既往多用 F0/jitter 等，对鼻功能不敏感。需在统一框架下比较病理类型、术前后与元音依赖的鼻化。

## 方法
CUCO（卡斯蒂利亚西班牙语）：对照 26、鼻中隔矫正 29、FESS 27、扁桃体切除 25；TDU 朗读，术前/术后 2 周/3 月。目标 VN/CVN 鼻协同元音 /e/、/u/、/o/。MFA 对齐 + Styler Praat 脚本提 A1–P0、A1–P1（值越低鼻化越强）。截面 ANOVA+Tukey；纵向配对 t + Holm–Bonferroni。

## 实验与结果
术前：仅 /u/ 的 A1–P0 组间显著（F=4.287, p=0.007）；鼻中隔组比 FESS/扁桃体组更低（更鼻化），与对照无显著差异。A1–P1 各元音均无组间差。纵向：仅扁桃体组术后早期（约 2 周）鼻化指标短暂变化后回落；其余组与对照无长期改变。

## 结论
A1–P0 对病理区分更敏感，鼻化呈元音依赖（/u/ 最敏）；扁桃体术后可有短暂效应。支持鼻化指标用于上气道相关语音分析。

## 点评
把语音学鼻化度量系统接到临床手术队列，补传统声学敏感性不足。对照与手术组截面差异有限，临床筛查价值需谨慎；语料与鼻语境较窄，跨语推广待证。

