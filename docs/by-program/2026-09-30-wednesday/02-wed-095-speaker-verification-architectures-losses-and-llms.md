# Speaker Verification: Architectures, Losses, and LLMs

- 日期：Wednesday 30 September 2026
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

本场覆盖说话人确认的架构缩放、离散音频 token、开集噪声标签学习、噪声稳健混合一致性，以及音频/语音感知大模型适配。架构侧 ReDimNet2 在一维通路做时间池化以更激进扩展通道而不成比例增加算力。离散编解码 token 虽隐式保留说话人线索，但需跨特征知识蒸馏才能接近 Fbank 教师。

标签噪声方面用时序集成阈值与邻域感知标签混合缓解开集噪声校正偏差。噪声稳健则用混合物一致性自监督对齐增强信号与输入，避免增强前端把非判别因素也“还原干净”。LLM 线把 SV 重述为音频问答：零样本能力有限，监督微调与难负对采样可改进；亦可注入冻结说话人嵌入并用 LoRA 赋予自然语言接口下的 ASV 能力。

## 论文技术总结

# ReDimNet2: Scaling Speaker Verification via Time-Pooled Dimension Reshaping

- 论文编号：1447
- 报告人：Ivan Yakovlev
- 程序：Wednesday 30 September 2026 / Speaker Verification: Architectures, Losses, and LLMs
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yakovlev26_interspeech.pdf

## 问题
ReDimNet 全程保持时间分辨率，1D 通路算力随 C×T 增长，限制通道加宽；如何在维度重塑框架内引入时间池化以改善精度–算力帕累托前沿。

## 方法
在 2D 块对时间轴做步长卷积池化（减 T 不加倍 C，软放松 C·F·T 守恒）；1D 块在更短序列上运行；阶段加权聚合前最近邻上采样回输入 T，保留残差连通。定义 B0–B6（1.1M–12.3M 参、0.33–13 GMACs）。VoxCeleb2 两阶段训练（SF2-C，LM 微调 6 s），余弦打分无 AS-Norm。

## 实验与结果
几乎每个匹配算力点 ReDimNet2 优于 ReDimNet。B6：Vox1-O 0.29% EER、Vox1-H 0.99%，12.3M/13 GMACs，相对原 B6 约 −28% EER、−36% GMACs。B3 起超过 ResNet293；B6 优于 WavLM 并接近 W2V-BERT 2.0 而参数小约 48×。SITW/VOiCES/Vox1-B 域外平均 1.84 vs 原 1.87。大模型（B4–B6）种子方差更大。

## 结论
时间池化与维度重塑兼容，是扩展说话人嵌入网络的简单有效策略；代码与权重已开源。

## 点评
用整条 B0–B6 匹配算力对照做“消融”，证据比单点刷榜扎实。大模型训练不稳提示还需正则；与更大外部数据训练的 SOTA 对比时需注意数据量差异。


# Text-Independent Speaker Verification Using Discrete Audio Tokens

- 论文编号：1135
- 报告人：Zheng Liang
- 程序：Wednesday 30 September 2026 / Speaker Verification: Architectures, Losses, and LLMs
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liang26c_interspeech.pdf

## 问题
神经音频编解码（NAC）离散 token 在生成任务成功，但直接做 ASV 明显弱于 Fbank；究竟是说话人信息被压缩丢掉，还是常规 CE 训练挖不出 token 中的说话人线索。

## 方法
诊断：同 ECAPA-TDNN 上对比原 Fbank、解码重构波形再提 Fbank、EnCodec token（各码本嵌入求和）。提出 CFKD：Fbank 教师与 token 学生共享骨干，用余弦嵌入对齐损失 L_KD 与分类损失加权（λ）；学生用 24 kHz EnCodec 全 32 层 RVQ。评 ECAPA-TDNN1024 与 ResNet34；另在 VoxCeleb2 上扫码率，并做特征维乱序探针。

## 实验与结果
诊断（Vox1）：原 Fbank EER 2.21 → 重构 2.57 → token 3.38，说明信息大体保留但难用。CFKD（λ=40）：ECAPA token 3.38→2.25（相对约 −35%），接近教师；ResNet 7.55→4.03。错误交集显示师生有互补“盲区”。乱序后 ECAPA 对 Fbank/token 均稳，ResNet 在 Fbank 崩溃、在 token 上基线已差且乱序几乎不变，表明 token 维缺乏谱邻接、1D 更合适。Vox2 上 24 kbps EER 1.05，相对 Codec-ASV 报告的 2.08 约 −49.5%。

## 结论
瓶颈在可及性而非信息丢失；CFKD 能逼近 Fbank 教师，且 1D 骨干更适配离散表示。

## 点评
诊断三元组把“编解码伤说话人”与“训练范式挖不出”拆开，结论对 codec-LM 生态很有用。最优 λ=40 远高于同质蒸馏惯例，跨特征蒸馏强度需小心调；教师质量上限仍约束学生。


# Temporal Ensembling Threshold and Neighbor-Aware Label Mixup for Speaker Verification with Open-Set Noisy Labels

- 论文编号：11
- 报告人：Liang He
- 程序：Wednesday 30 September 2026 / Speaker Verification: Architectures, Losses, and LLMs
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/fang26_interspeech.pdf

## 问题
大规模说话人数据噪声标签难免；开集噪声（真说话人不在标签集）经硬标签纠正仍错，软标签又学不稳，现有选样/纠正方法对此不足。

## 方法
提出 TET-LM：每轮用嵌入–原型余弦相似度拟合双成分 GMM 得阈值，EMA 集成得 ¯τ 划分 clean/noisy；mean-teacher 对 noisy 取 top-K 邻类（高置信则 K=1），归一化权重做邻域标签 mixup 损失。三阶段：全量 warmup → 仅 clean → clean + mixup。ECAPA-TDNN1024 + AM-Softmax；在 VoxCeleb1/2 注入 10–50% 同性别对称/非对称噪声。

## 实验与结果
消融表明去掉 TET 或 LM 均变差，高噪声下 LM 更关键；K=10、μ=0.4 最优。相对 Standard，平均 EER/minDCF 约降 54%/42%（最佳基线 ES-GMM 约 52%/40%）。Vox1 Sym-50%：Standard EER 13.71 → TET-LM 4.04；Vox2 各评测列表上多数噪声设置亦最优或近最优，干净数据表现稳定。

## 结论
时间集成阈值稳选样，邻域 mixup 更适配开集纠正；多阶段训练提升不同噪声场景鲁棒性。

## 点评
把开集噪声显式当成“邻域混合”而非硬翻标签，比只丢弃 noisy 更贴真实爬取数据。噪声为同性别人工翻转的受控设置；真实网页噪声分布与跨数据集迁移仍待验证。


# Mixture Consistency Learning for Robust Speaker Verification in Noisy Environments

- 论文编号：364
- 报告人：Seung-bin Kim
- 程序：Wednesday 30 September 2026 / Speaker Verification: Architectures, Losses, and LLMs
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kim26c_interspeech.pdf

## 问题
噪声鲁棒 SV 常加 SE 前端，但用“干净”参考做重建会连带恢复通道等非判别因素，反而伤说话人区分。

## 方法
提出 MCL-SV：双解码 SE（说话人路径 + 背景路径），用 mixture consistency 约束两路输出之和重建原始混合输入（自监督、无干净参考）；SV 目标仅耦合说话人路径。后端对接说话人网络（文中与 ReDimNet-B2 等对比），在 VoxCeleb + MUSAN 等噪声条件评测。

## 实验与结果
Vox1 训练时平均 EER 3.03%，低 SNR（如 0 dB）更稳。Vox2 上平均 EER 1.19%，相对复现 ReDimNet-B2 与带 SE 基线分别约改善 16.2%/12.5%，干净条件亦优于基线约 14.4%。消融显示含 MC、弱化目标 SE/NE 的配置优于纯目标重建。

## 结论
相对强制贴合“干净”参考，用输入自一致性分离说话人与干扰更利于噪声鲁棒 SV。

## 点评
把 MixIT/一致性思路接到 SV，直接挑战“SE 一定要有干净标签”的默认设定。干净高 SNR 上未必全面领先；优势集中在严苛噪声，部署需按场景权衡。


# Adapting Audio Large Language Models for Speaker Verification

- 论文编号：1117
- 报告人：Shuai Wang
- 程序：Wednesday 30 September 2026 / Speaker Verification: Architectures, Losses, and LLMs
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ren26c_interspeech.pdf

## 问题
Audio LLM（ALLM）泛化强，零样本能否做说话人确认，以及轻量微调能否缩小与专用 SV 模型差距，尚缺系统评估。

## 方法
将 SV 重写为音频问答；先零样本测公开基准，再在 VoxCeleb2、CN-Celeb、3D-Speaker 等约 900 万对上 LoRA（r=16，约 18M 可训参）微调，用规则硬负样本采样。分数取 “One” token 概率。并扩展为文本相关 SV：同时核验说话人与文本内容。

## 实验与结果
Kimi-Audio 零样本 EER 多在 30–50%；微调后性别/语言条件降至 4.87%/2.93%，仍整体落后 ResNet34/ECAPA/CAM+，但短时长等难条件更具竞争力；硬采样优于随机。多骨干微调均提升 SV。文本相关 LibriSpeech：微调后综合准确率 98.87%，接近 Whisper+ECAPA（98.83%）。

## 结论
适当适配后 ALLM 可作为统一 SV 框架并保留通用音频理解；零样本不足，与专用模型仍有差距。

## 点评
把 ALLM 当问答式验证器并系统扫声学条件，清楚标出“语义强、身份弱”。统一文本相关任务有吸引力；算力与仍存的 EER 差距限制替代专用骨干的短期可行性。


# Speaker Verification with Speech-Aware LLMs: Evaluation and Augmentation

- 论文编号：2670
- 报告人：Yuzhe Wang
- 程序：Wednesday 30 September 2026 / Speaker Verification: Architectures, Losses, and LLMs
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/thebaud26_interspeech.pdf

## 问题
现成 speech-aware LLM 是否编码可用于 ASV 的说话人身份；若不足，能否用轻量增强补上而不牺牲自然语言接口。

## 方法
提出模型无关评测：API 模型用提示置信分，开源模型用 Yes/No token 似然比。在 VoxCeleb1 测多种现成 LLM。进而将冻结 ECAPA-TDNN 嵌入经投影注入 TinyLLaMA 1.1B / Ministral 3.3B，配合 LoRA，使模型在自然语言格式下做验证。

## 实验与结果
现成模型 ASV 弱（EER 常 >20%），但性别等粗属性准确率可达约 92–98%，说明抓的是粗粒度副语言而非细粒度身份。注入 ECAPA + LoRA 后接近专用 ECAPA 余弦基线；仅训连接器、冻结 LLM 时 Vox1-O 升至 5.48% EER，表明需适配骨干以解读说话人表示。

## 结论
隐式预训练不足以支撑可靠 ASV；显式注入强说话人嵌入 + 参数高效适配是可行路径，但训练与推理成本远高于专用系统。

## 点评
与“纯提示做 SV”路线形成对照：评测协议清晰，增强方案务实。API 置信分粗糙、解析失败率高限制公平对比；成本问题仍是落地主障碍。

