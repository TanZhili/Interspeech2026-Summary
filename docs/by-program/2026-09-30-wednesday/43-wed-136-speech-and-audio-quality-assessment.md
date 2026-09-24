# Speech and Audio Quality Assessment

- 日期：Wednesday 30 September 2026
- 时间：16:30-18:30
- 形式：Oral
- Area：5
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场覆盖端到端 MOS 预测增强、流式/多分辨率增量质量估计、FAD 编码器任务偏置分析、音高重音专用评测、多指标与偏好联合学习，以及对大音频语言模型幻觉可靠性的攻击评测。

趋势一是让质量表征在潜空间中按感知质量更好组织（对比学习），并支持前缀音频上的增量预测。趋势二是承认“评测器本身携带任务诱导偏置”，没有单一编码器可做万能 FAD。趋势三是把局部音高重音错误、异构绝对指标与成对偏好纳入统一建模，同时开始用对抗式音频幻觉探测 LALM 是否真正 grounding 到音频。

## 论文技术总结

# DNSMOS-C: Improving End-to-end Speech Quality Models via Contrastive Learning

- 论文编号：342
- 报告人：Xinyu Liang
- 程序：Wednesday 30 September 2026 / Speech and Audio Quality Assessment
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liang26_interspeech.pdf

## 问题
紧凑端到端 MOS 模型（如 DNSMOS Pro）适合实时，但对未见失真/条件泛化不足；SCOREQ 类对比损失有效但依赖重 SSL，难部署。

## 方法
DNSMOS-C：在 DNSMOS Pro 架构上，对中间嵌入施加 MOS 引导的 triplet 对比回归损失（SCOREQ 风格），与 MOS 回归联合单阶段训练；推理与 Pro 相同、无额外开销。在 BVCC、NISQA、Tencent 等上训练，测域内与未见 NISQA 子集；PCA/聚类分析潜空间。

## 实验与结果
10 次运行平均：域内 LCC/SRCC 一致高于 DNSMOS Pro，MSE 相近；未见域相关也更高或持平，标准差更小（更稳）。潜空间两主成分与 MOS 的多重相关升高，呈现质量流形式排序。

## 结论
MOS 引导对比监督可在不增加推理成本的情况下，提升紧凑 SQA 的相关、泛化与训练稳定性。

## 点评
把 SCOREQ 思想压进小 CNN 端到端模型，填补“重模型泛化 vs 轻模型部署”缝隙。增益主要在相关而非 MSE，适合排序/监控场景；与大 SSL SQA 的绝对差距文中未全面对标。


# ANCHOR: Autoregressive Non-intrusive Chunk-Ordered Refinement for Joint Multi-Resolution Speech Quality Modeling

- 论文编号：927
- 报告人：Zhuoyan Tao
- 程序：Wednesday 30 September 2026 / Speech and Audio Quality Assessment
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/tao26_interspeech.pdf

## 问题
流式/生成系统需要从部分音频增量估计质量，但多数非侵入式预测器假定完整话语，前缀输入上退化。

## 方法
扩展 ARECHO，提出 ANCHOR：在统一自回归解码器中联合预测 chunk 级与 utterance 级伪 MOS（UTMOS、PLCMOS、NISQA 等），用分辨率感知层次先出 chunk token 再出全句 token（粗到细）。前缀长度 {2,4,6,8}s 监督；含局部失真压力测试。

## 实验与结果
相对 ARECHO，2s 前缀上 PLCMOS 误差降约 48%，4/6s 亦有增益。前缀→全句收敛分析显示有效感知语境约 4–6s。压力测试表明对局部腐败外推更稳，而非仅拟合截断边界。

## 结论
多分辨率自回归细化可改善增量质量估计，并揭示感知质量随时间累积的大致视界。

## 点评
贡献在于推理体制（增量伪 MOS），而非新主观真值。对 Teams/DNS 类生产指标很实用；依赖教师伪标签，教师偏差会遗传。


# An Empirical Analysis of Task-Induced Encoder Bias in Fréchet Audio Distance

- 论文编号：1549
- 报告人：Wonwoo Jeong
- 程序：Wednesday 30 September 2026 / Speech and Audio Quality Assessment
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jeong26_interspeech.pdf

## 问题
FAD 是文生音频默认指标，但分数依赖编码器嵌入空间；训练任务决定保留/丢弃哪些声学特征，使 FAD 带系统性任务偏置。

## 方法
把评价拆成 Recall、Precision、Alignment（语义/结构），用对数自参照归一化跨编码器比较。在六种编码器（AudioMAE、EnCodec、Wav2Vec2、VGGish、CLAP、Whisper）与两数据集上，对加噪、混响、音高/包络变换、时间反转/块打乱等受控扰动测敏感度。

## 实验与结果
四轴权衡：AudioMAE 精度敏感最高；Whisper 结构检测强但对信号劣化近乎盲；VGGish 语义对齐强但惩罚合理类内变化（Recall 低）。CLAP 较均衡但无峰值。音高轨迹还有方向不对称（如 VGGish 对下移更钝）。

## 结论
没有单一编码器可当通用评价器；未来需面向人类感知的 evaluation-native 编码器，而非复用任意任务嵌入。

## 点评
把“FAD 看编码器”做成可操作的四轴诊断，对 TTA 评测选型很有用。归一化是分析工具而非新感知真值；结论呼吁原生评测编码器，但本文未提出替代模型。


# PASQA: Pitch-Accent-Focused Speech Quality Assessment Model Trained on Synthetic Speech with Accent Errors

- 论文编号：1662
- 报告人：Masaya Kawamura
- 程序：Wednesday 30 September 2026 / Speech and Audio Quality Assessment
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kawamura26_interspeech.pdf

## 问题
常规 utterance 级自然度 MOS 预测对日语等语言的局部音高重音错误不敏感，而许多 TTS 又不暴露内部重音标签，难以专评重音正确性。

## 方法
用可控制重音的 TTS 生成受控日语重音错误语料，由错误率得到伪重音质量分。PASQA 基于 SSL，加入 mora 条件融合、排序损失、重音错误定位辅助任务与说话人不变训练。在见/未见说话人与人工主观评测上验证。

## 实验与结果
常规 MOS 模型排序准确率近随机、相关常近零或负；PASQA 在主观评测达 Order Acc 0.850、SRCC 0.828、KTAU 0.614。客观集上见/未见说话人均保持高排序准确；对 OOD TTS 输出亦有较好两两判别。

## 结论
显式建模重音错误可显著提升日语音高重音质量评估，并优于仅预测整体自然度的模型。

## 点评
把“听得懂重音”做成可训练目标，对日语 TTS 评测很切题。合成伪标签与真人口感可能仍有隙，但主观相关已明显拉开；思路可迁移到其他声调/重音语言。


# URGENT-MOS: Unified Multi-Metric and Preference Learning for Robust Speech Quality Assessment

- 论文编号：1671
- 报告人：Wei Wang
- 程序：Wednesday 30 September 2026 / Speech and Audio Quality Assessment
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26aa_interspeech.pdf

## 问题
URGENT 等协议同时要绝对多指标与成对偏好，但现有 SQA 多只做其一；异构标注与跨域鲁棒性不足。

## 方法
URGENT-MOS：多分支特征提取 + Absolute Metric Prediction Module（分范畴多指标头）与 Naturalness-Conditioned Preference Module（交叉注意力偏好）。联合训练人类 MOS、客观指标与由 MOS 构造的偏好对（任意/语料内/同参考匹配，δ=0.5）。释放偏好标注数据；覆盖 TTS/VC/SE/VoIP 等。

## 实验与结果
偏好准确率跨 SOMOS、TMHINT-QI、UR25、CHiME-7、LIVETALK 等整体强于 DNSMOS/UTMOS 等，且比 SpeechEval/SpeechJudge 更跨域稳健。绝对相关（LCC/SRCC）在多数据集上常居前列或次优（如 F4C1M5Dref）。全指标监督未必优于自然度子集。

## 结论
在共享架构中联合多指标绝对预测与偏好学习，可更好对齐现代评测协议并提升跨域稳健性。

## 点评
直接回应 URGENT 协议缺口，工程完整（代码+偏好数据）。偏好对由 MOS 派生，与真人口头偏好仍有差距；特征分支数与监督范围有可调权衡。


# Audio Hallucination Attacks: Probing the Reliability of Large Audio Language Models

- 论文编号：2448
- 报告人：Ashish Seth
- 程序：Wednesday 30 September 2026 / Speech and Audio Quality Assessment
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/seth26_interspeech.pdf

## 问题
LALM 在标准基准表现强，但可能跳过“声音是否真的存在”的 grounding，在隐式提问或注入虚假语音描述时产生幻觉。

## 方法
提出 AHA：AHA-Eval（约 6.5K QA）含查询侧（显式 vs 预设声音存在的隐式问）与音频侧（TTS 注入描述不存在事件的合成语音）攻击；事件含相关/对抗/随机。用攻击成功率（ASR）评 Audio Flamingo 3、Gemini 3 Pro、Qwen2.5-Omni 等。另释 AHA-Guard（120K）做后对齐缓解。

## 实验与结果
Audio Flamingo 3 / Gemini 3 Pro 等 ASR 分别高达约 95.35% / 79.65%；隐式与音频注入攻击远强于显式问。AHA-Guard 对齐可将部分模型 ASR 降低至约一半（文称最高约 49%）。

## 结论
标准基准掩盖 grounding 可靠性缺口；需专门幻觉攻击评测，后对齐可显著缓解但未根除。

## 点评
用“假定存在”的隐式问揭示模型先验压过听觉证据，问题设定尖锐。AHA 属安全评测而非质量 MOS；缓解依赖额外对齐数据，部署前应视任务再验。

