# Speaker Recognition and Verification

- 日期：Thursday 1 October 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：4
- 论文数：12

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场海报覆盖说话人表示学习骨干、模型压缩、联邦学习、半监督/自监督伪标签、短时验证、低资源语料构建，以及取证场景下的词 n-gram 与编解码失配分析。主线是在保持或逼近全监督性能的同时，降低部署成本、数据共享风险与标注需求，并正视短时、噪声、话题与编解码带来的不稳定性。

表示与压缩方面，流形约束超连接扩展残差信息流；持续 2D 谱—时 Transformer 避免过早坍缩谱时格；剪枝—量化复合误差用渐进蒸馏缓解。联邦学习用双分类头或 Fisher 关键关键关键维对齐缓解异构与冗余知识。伪标签从瞬时置信度扩展到历史稳定性（HistoMatch）与预训练层聚类一致性 + DINO 式自蒸馏。

应用与取证侧，短时验证构建 VoxPhrase 并混合文本相关/无关注册做神经重打分；VieSpeaker 用不依赖人脸的元数据—LLM 推理建越南语大规模集；取证则警示话题词偏置与编解码—时长—说话人依赖的个体差异，系统级良好指标不保证人人可用。

## 论文技术总结

# Beyond Residual Connections: Manifold-Constrained Hyper-Connections for Robust Speaker Representation Learning

- 论文编号：634
- 报告人：Zhe LI
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jin26_interspeech.pdf

## 问题
说话人嵌入骨干（ResNet、ECAPA-TDNN、Res2Net 等）依赖恒等残差，通道间无显式混合，易冗余；无约束 Hyper-Connections 用可学习混合矩阵虽增带宽，却破坏恒等映射，深度下信号易爆炸/消失。

## 方法
引入 Manifold-Constrained Hyper-Connections（mHC）：将隐状态分成 N 条并行流，经 H_pre 聚合进变换块 F，再 H_post 拆回；流间用 W∈R^{N×N} 混合，并以 Sinkhorn-Knopp（约 k=3）投影到双随机流形（行列和为 1）以守恒能量。相对原 mHC 的输入依赖动态映射，改用静态可学习 W，参数开销从 O(n C n²) 降到 O(n²)，作为残差捷径的即插替换。

## 实验与结果
VoxCeleb2-dev 训练，评 Vox-O/E/H 与 VoxSRC21-val；80-dim Fbank，AAM-Softmax，3D-Speaker。四骨干参数量不变时 EER 一致下降，例如 mHC-ECAPA-L 在 O/E/H 为 0.77%/0.94%/1.88%（基线 0.87%/1.12%/2.12%）；VoxSRC21-val 上 ResNet-34 从 3.83%→3.35%。消融：N=4 最优；ECAPA-L 上 HC 0.84% vs mHC 0.77%（Vox-O）；GFLOPs 几乎不变。

## 结论
作者认为 mHC 能在可忽略参数/算力开销下稳定提升多种说话人骨干；双随机约束对相对无约束 HC 至关重要。

## 点评
把“捷径上的跨通道混合”做成带流形约束的通用模块，对已有残差骨干迁移成本低。N 较小时更好，暗示带宽与收敛稳定性需折中；主要证据在 VoxCeleb 系协议，跨域噪声/远场未单独展开。


# Mitigating Pruning-Quantization Compound Errors for Ultra-Lightweight ResNet34-Based Speaker Recognition

- 论文编号：587
- 报告人：城轩 龙
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
DNN 显著推进了说话人识别，但 ResNet34 一类骨干仍有计算与内存开销，难以部署到资源受限设备。剪枝与量化可压缩模型，但二者叠加会产生复合误差，需要专门缓解。

## 方法
提出统一压缩框架，结合通道剪枝与低比特量化。剪枝侧提出 ResRep-MB：带多分支 compactor 的策略，用于更准确的通道重要性评估，以实现近无损结构压缩。为缓解剪枝与 INT4 量化的复合误差，提出 Progressive Pruning-Quantization Distillation（PPQD），采用双教师机制。

## 实验与结果
在 VoxCeleb1 与 CN-Celeb1 上，压缩后的 ResNet34 达到 19.2× 压缩比，相对 EER 仅下降 6.8%，并保持跨语言稳健性（摘要表述）。

## 结论
通道剪枝与 INT4 量化可在统一框架下大幅压缩 ResNet34 说话人识别模型；PPQD 用于抑制二者复合误差，使高压缩比下性能损失相对可控。

## 点评
贡献点集中在「剪枝+量化复合误差」而非单一压缩手段；摘要给出了压缩比与相对 EER 变化，但仍缺完整设置与对比表，需谨慎解读。


# Continuous 2D Spectral—Temporal Transformer for Speaker Verification

- 论文编号：963
- 报告人：Seongwook Ham
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ham26_interspeech.pdf

## 问题
ReDimNet 等混合架构在全局依赖建模前常把频谱维并入通道，破坏显式时–频网格；全局建模应在坍缩后还是直接在 2D 谱–时网格上进行，尚不明确。

## 方法
提出 C2D-ST：骨干全程保持 X∈R^{B×C×F×T}；五阶段共 16 层 Transformer，每阶段先 Neighborhood Attention 做局部谱–时建模，再 Axial Attention 沿时间与频率轴做全局依赖；阶段输出加权聚合后才 1D 投影，末段 8 层时序注意力 + ASP 出嵌入。RoPE 用于轴向/全局注意力；Neighborhood Attention 含 RPB 与 value-side RPE。

## 实验与结果
VoxCeleb2-dev 训练、VoxCeleb1-O/E/H 评测；80-dim log Mel，SphereFace2，ESPnet-SPK。6.9M 参数下：无 LMFT/QMF 平均 EER 0.627；+LMFT 0.517；+LMFT+QMF 达 0.507/0.051（minDCF），优于 ReDimNet-B6（15.0M，0.633/0.059）与 ECAPA2（27.1M，0.617/0.062）。消融：去轴向→NA 平均 EER 升至 0.693；仅时间轴向 0.533；轴向改为坍缩后 1D Transformer 升至 0.557 且参数多 2.8M。

## 结论
作者认为全程保持谱–时网格并直接在网格上做全局建模，能以更少参数达到有竞争力的验证性能；局部用注意力、末段可用卷积等设计选择亦有消融支持。

## 点评
用结构回答“何时坍缩频谱维”，相对盲目加深更干净。强项在参数效率与对照消融；与更大模型的对比依赖引用结果与 AS-Norm/QMF 设定一致性，跨语料泛化未展开。


# A Federated Learning-Based Speaker Recognition Method with Dual Classification Heads

- 论文编号：25
- 报告人：Liang He
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/meng26_interspeech.pdf

## 问题
机构级联邦说话人识别中，各客户端说话人集合互斥、分布异构；仅靠本地分类头训练时，模型只能经聚合间接获得全局知识，跨客户端信息融合不足。

## 方法
提出 FedDCH：本地同时维护局部分类头（C_k 类）与全局分类头（全体 C 类），联合损失 α L_global+(1−α)L_local 指导 ECAPA-TDNN 嵌入提取器；本地更新后按 speaker ID 将局部类向量写入全局头对应位（β 混合），上传提取器与全局头。服务器对提取器用数据量加权 FedAvg；对全局头按 speaker-ID 加权矩阵（含优势因子 μ）聚合后再下发。

## 实验与结果
VoxCeleb2 按说话人均分为 4 客户端：相对本地训练平均 EER 改善约 46.5%，相对 FedAvg 约 7.6%；Vox-O 上 FedDCH 各客户端 EER 约 2.31–2.54（FedAvg 约 2.52–2.73）。VoxCeleb 与 CN-Celeb 四客户端联合：相对本地约 68.8%、相对 FedAvg 约 5.4%。消融显示双头联合优于仅本地或仅全局头；全局损失用 CE / AM / AAM 均较稳。

## 结论
作者认为在更贴近“组织为客户端、说话人互斥”的设定下，双分类头能更直接注入全局分布知识并缓解异构；加权聚合进一步保留充分训练过的说话人判别信息。

## 点评
把“全局类空间”显式请进本地训练，比只在聚合后对齐更直观。全局头维度随总说话人数增长，通信与内存成本正文未细算；Vox-H 上并非所有客户端都最优，难例仍有优化空间。


# Learning Global Key Knowledge for Federated Speaker Recognition via Fisher Information

- 论文编号：196
- 报告人：Liang He
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/meng26b_interspeech.pdf

## 问题
联邦说话人识别中客户端数据异构，全局模型聚合后仍残留冗余/偏置信息；本地若整嵌入对齐全局，易学到有害漂移，陷入局部最优。

## 方法
本地训练时用冻结的全局提取器与本地提取器分别得到 e_G、e_K；经临时分类器对 e_G 算对角近似 Fisher 信息，按尺度 s 取前 t=s·D 个高重要性维索引 I；在 I 上切片并归一化得 v_G、v_K，以 1−cos(v_K,v_G) 为 l_FI，与 AM-Softmax 分类损失相加。服务器仍按数据量加权聚合提取器。

## 实验与结果
ECAPA-TDNN（1024 通道）、D=512、s=0.2、E=5、R=20。VoxCeleb1→Vox-O：Ours 各客户端 EER 约 4.15–4.47，优于 FedAvg（约 4.90–5.42）与 FedFSS 等。VoxCeleb2→Vox-O/E/H 均为最优（如 Vox-O 约 1.91–2.18）。VoxCeleb1+CN-Celeb1：Vox-O 3.01、CN-Celeb.Eval 12.58（CN 略逊于 FedFSS 的 12.35，但不额外传额外信息）。消融：无 FIM 随机选维或无维选择均变差；s 在一定范围较稳。

## 结论
作者认为用 Fisher 筛出对任务判别关键的嵌入维，再约束本地向这些维对齐，可在保护隐私的同时减轻异构带来的冗余知识，提升联邦说话人识别。

## 点评
“对齐但只对齐关键维”比整向量蒸馏更贴异构场景。Fisher 经临时头与 CE 估计，重要性定义依赖该代理任务；跨语料上相对 FedFSS 互有胜负，说明维筛选并非处处碾压。


# HistoMatch: Unified Transient-Steady Assessment for Noise-Robust Semi-Supervised Speaker Verification

- 论文编号：244
- 报告人：Shenghan Gao
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gao26b_interspeech.pdf

## 问题
半监督说话人验证的伪标签筛选多依赖瞬时置信度阈值，但随机切段与噪声增强易导致预测漂移，伪标签利用率低；*Match 范式在 SV 上增益有限。

## 方法
提出 HistoMatch：在 FixMatch 风格流程上用 AAM 替代 CE。Dual-state History-based Stability Evaluator（DHSE）联合瞬态过滤（弱增强上 max(p)≥T）与稳态过滤（近 K 个 epoch 历史预测直方图最大同类计数 S≥阈值，用于召回置信度不够但历史稳定的样本）；阈值由 EMA 自适应更新。有标与筛后无标样本均用 AAM 损失。

## 实验与结果
VoxCeleb2 训练，每说话人 4/10/20 条为有标；ECAPA-L。20 条/人时 O/E/H EER 达 0.91%/1.13%/2.13%，接近全监督（0.87%/1.12%/2.12%），并优于 FixMatch/FlexMatch/SpeakerMatch 等。ECAPA-S、10 条/人消融：仅瞬态 1.87%、仅稳态 1.22%、双态 1.08%。

## 结论
作者认为瞬态–稳态双阈值可回收因切段/噪声导致置信度失败的优质伪标签，半监督性能逼近全监督并达所报告设定下的 SOTA。

## 点评
把“历史一致性”升为与置信度并列的稳态指标，切中 SV 强增强带来的标签抖动。有标预算固定、骨干统一，对比干净；对历史队列长度 K 与早期噪声累积的敏感性正文着墨较少。


# Self-supervised Speaker Verification with High-Confidence Pseudo-Label Selection and DINO-Style Self-Distillation Based on Pre-trained Models

- 论文编号：1965
- 报告人：Yishuang Li
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26ca_interspeech.pdf

## 问题
无标说话人验证依赖聚类伪标签，噪声标签会拖垮判别；预训练模型（PTM）分层表征如何筛出可靠监督、同时不浪费低置信样本，仍是开放问题。

## 方法
HCPLS：在验证集上按层 EER 选 top-K 说话人判别层，各层独立聚类后经共现矩阵与 Hungarian 对齐，仅跨层一致样本进高置信集 H，其余为无标集 L。学生为 WavLM 前若干层加权和 + ECAPA-TDNN；H 上用 Label Noise Correction 伪监督，L 上 EMA 教师提供置信门控 KD，并加双视图嵌入一致性。迭代中再聚类、离线块级校正与重训。

## 实验与结果
VoxCeleb2-dev 无标训练，评 Vox1-O。K=3 时 H 的 NMI/F1 达 0.9522/0.7571。Iteration-1：HCPLS+蒸馏 EER 2.10%（相对仅 H1 基线 2.64% 降约 20.5%）。4 轮迭代后 EER 1.09%，优于 PTM-LC 的 1.25%（相对降约 12.8%），且迭代轮数少于 IPL。

## 结论
作者认为多层聚类一致性可抬高伪标签纯度，低置信样本宜作无标蒸馏而非硬标签；二者联合可得有竞争力的自监督 SV。

## 点评
“高置信硬监督 + 低置信软蒸馏”分工清晰。层选择依赖验证 trial 上的 EER（虽不更新模型），严格无标场景下该先验需注意；主结果集中在 Vox1-O。


# Stabilizing Short Duration Speaker Verification through Neural Re-scoring with Hybrid Enrollment

- 论文编号：228
- 报告人：Zhiqi Ai
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ai26_interspeech.pdf

## 问题
自定义唤醒词后的短时说话人验证（常 <3 s）嵌入不稳、对噪声与音素敏感；纯 TD 注册内容一致但时长短，纯 TI 信息更丰但与短语测试内容失配。

## 方法
构建 VoxPhrase（ASR+强制对齐从 VoxCeleb 切 0.8–3 s 短语，硬负例挖掘评测）。冻结 ECAPA/CAM++/ERes2Net-L，提取帧级与句级嵌入；混合 TI+TD 注册，计算句级余弦 S_ti、S_td，并用双向并行 cross-attention 做 TD 注册–查询帧级匹配，MLP 融合得最终分数，BCE 训练轻量 verifier。

## 实验与结果
Eval-1 上 TI（3/10 s）普遍优于短 TD；加 verifier 与混合注册再降 EER（如 CAM++ TD Avg 9.15→8.31，10 s TI+verifier 至约 5.35）。TI 时长从 1 s 增至 10 s EER 持续下降，混合神经重打分在 10 s 达约 1.6%（Eval-1 random）。Deepmine OOD（Eval-3/4）上混合亦最优（如 ERes2Net-L 4.88/2.38）。

## 结论
作者认为实用注册时长（≥3 s）下 TI 稳定性常优于短 TD，而混合注册 + 帧级神经重打分可互补二者，尤其在难例与分布外短语上更稳。

## 点评
把 UDKWS 场景的短时验证从“固定短语微调”拉到可自定义短语语料与混合注册，工程贴合度高。短语切分依赖 ASR/对齐质量；冻结骨干使收益主要来自后端重打分，而非端到端短时表征学习。


# VieSpeaker: A Large-Scale Vietnamese Speaker Recognition Dataset Beyond Visual Dependency

- 论文编号：3449
- 报告人：Viet Hoang Pham
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pham26_interspeech.pdf

## 问题
越南语说话人语料规模与声学多样性不足；VoxCeleb 式管线依赖人脸，排除无画面录音且标注成本高，VoxVietnam 等仍受视觉约束。

## 方法
提出不依赖人脸的构建管线：YouTube 多域采集 → Pyannote 说话人日志 → gemini-2.5-pro 据元数据与转写证据映射身份（不确定则 Unknown）→ 名称归一化与 ECAPA 嵌入聚类合并 → IQR 清洗与时长过滤。产出 VieSpeaker：4,715 说话人、365,874 句、约 902 小时；划分 VieSpeaker-T/E/H。

## 实验与结果
WeSpeaker ECAPA-TDNN。从零训练 VieSpeaker-T 在 VoxVietnam 上最强；作预训练再微调 Vietnam-Celeb-T，E/H EER 5.45%/6.74%，优于 VoxCeleb2 预训练（5.79%/6.91%）。本基准上从零训达 2.40%/13.45%，VoxCeleb2→VieSpeaker-T 微调最佳 1.81%/9.83%。

## 结论
作者认为元数据+LLM 推理可规模化越南语说话人标注，VieSpeaker 显著扩大说话人与时长，并提升鲁棒性与跨集泛化；数据在 Hugging Face 开放。

## 点评
绕开视觉模态对播客/电台类数据尤为关键。身份质量依赖 LLM 证据约束与人工抽检；相对 VoxCeleb2 仍偏小，Hard 协议上跨会话难度仍高。


# Confusion-Transport Pruning: Optimal-Transport Redundancy and CKA Geometry Distillation for Hard-Set Robust Speaker Verification

- 论文编号：2193
- 报告人：
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
官方程序未提供摘要。仅能从标题与会场信息判断主题方向：「Confusion-Transport Pruning: Optimal-Transport Redundancy and CKA Geometry Distillation for Hard-Set Robust Speaker Verification」，安排在「Thursday 1 October 2026 / Speaker Recognition and Verification」。

## 方法
官方程序无摘要，无法概括具体方法、模型结构或训练流程；此处不作推断。

## 实验与结果
官方程序无摘要，未给出数据集、对比设置或定量结果。

## 结论
官方程序无摘要，无法归纳作者结论与适用边界。

## 点评
该条目目前只有标题与程序位置可参考，后续若有讲义、幻灯片或正式论文，再据此补充问题设定、方法细节与可核验结果。


# Function words: a topic independent approach to word n-gram selection for forensic speaker comparison

- 论文编号：3166
- 报告人：Michael Carne
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/carne26_interspeech.pdf

## 问题
基于词 n-gram 的似然比法医说话人比对常用“最高频 k 项”隐式选特征，可能混入话题相关内容词，从而高估证据强度。

## 方法
对 AusEng 500+ 中 104 名澳大利亚男性各两段电话闲聊前两分钟净语音做逐字转写。特征级两层 multinomial–Dirichlet LR；基线用全词表频次选 k；提出先固定 156 个功能词显式特征集，再比较频次、MI、ANOVA F-ratio、χ²、方差阈值五种筛选。5 折划分测试/参考/校准，以 C_llr 等评估。

## 实验与结果
基线 k=450 时 C_llr=0.60，但约 35%（157/450）为话题内容词。全功能词控制 C_llr=0.83；ANOVA F-ratio 选 k=50 最佳，C_llr=0.78（C_min=0.66），维度大幅下降。Tippett 显示 DS 强证据比例与幅度有所提升。

## 结论
作者建议用显式功能词集规避话题偏置；虽弱于含内容词的基线，但对话题失配更稳健，且 F-ratio 可进一步改善。未来需检验说话风格失配与社会语言学混杂因素。

## 点评
把“话题泄漏”写成可核验的比例与词例，对法医证据解读很有价值。性能换稳健性的取舍明确；语料为同任务闲聊，风格失配场景尚未实证。


# Codec-induced Mismatch, Speech Duration, and Speaker-dependent Effect in a DNN-based Forensic Speaker Recognition System

- 论文编号：1004
- 报告人：Guangmou Deng
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/deng26b_interspeech.pdf

## 问题
法医自动说话人识别中，质疑语音常经有损编解码且时长有限，与高质量已知样本失配；系统级指标可能掩盖个体说话人表现差异。

## 方法
102 名年轻香港粤语男性跨会话 HQ 录音；仅对质疑侧施加 G.711 A-law、AMR-NB 12.2/6.7 kb/s、Opus（16 kHz, 128 kb/s）。前端 ResNet34-MHA（VoxCeleb1+2 训）提 512 维嵌入，后端 LDA-PLDA + 双高斯化校准出 LR。质疑时长 5–90 s（5 s 步进）；报告系统 C_llr 与按说话人 C_spk_llr。

## 实验与结果
系统级：AMR-NB 6.7 kb/s 劣化最大，Opus≈HQ；C_llr 随时长下降，约 30 s 后平台。个体级：短时长与低码率下部分说话人 C_spk_llr>1 或波动大；90 s 时跨条件均值与标准差正相关（R²=0.43），表现差者对编解码更敏感。

## 结论
作者认为系统级“尚可”不保证每个说话人都可靠；编解码失配与时长效应存在显著说话人依赖，个体级验证对法医解读必要。

## 点评
把 FASR 评测从平均 C_llr 推进到个体轨迹与敏感性回归，切中个案证据解释。语料为实验室 HQ→仿真编解码，真实多级级联信道仍待扩展；C_spk_llr 样本少、方差大，正文亦强调看系统模式而非单人诊断。

