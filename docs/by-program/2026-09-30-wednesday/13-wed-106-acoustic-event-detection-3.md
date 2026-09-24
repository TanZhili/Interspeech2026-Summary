# Acoustic Event Detection 3

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：5
- 论文数：9

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场覆盖声音事件检测与相关声学感知：少样本 SED、临床心音重建、类别可变增量音频分类、呼吸音质量自适应角裕度、认知障碍公平检测、细粒度 VAD、野生黄獴叫声、持续广义类别发现，以及 AudioLLM 的主动音频协助。主题从经典 SED 扩展到医疗声学、公平性、边缘低延迟与可穿戴主动监听。

少样本与增量学习强调在重叠背景与类别增减下无需或少微调即可适应；临床与公平性工作融合 Whisper 嵌入、图注意力与去学习人口统计捷径。边缘部署推动 4 ms 分辨率紧凑 VAD 与主动打断/静默建模。生物声学与持续发现则把语音/视觉方法迁移到动物叫声与流式未标注新类，同时指出音频域的谱时结构使直接迁移易退化。

## 论文技术总结

# POP-SED: Prototype Orthogonal Projection for Robust Few-shot Sound Event Detection

- 论文编号：153
- 报告人：Takehiko Kagoshima
- 程序：Wednesday 30 September 2026 / Acoustic Event Detection 3
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kagoshima26_interspeech.pdf

## 问题
少样本声音事件检测中，支持集与查询中的目标事件常与背景重叠；现有做法多靠域级/支持集微调适应背景，计算重、灵活性差。

## 方法
POP-SED（无需微调）：用基础音频编码器提帧特征；对支持正例算目标原型；对背景与查询特征拟合 vMF 混合，再按稳健性支持集准则选背景均值向量；将目标原型正交投影到背景子空间的正交补，再与查询做相似度阈值检测。编码器可用 BEATs / CLAP，均不微调。

## 实验与结果
DCASE2024 Task 5 验证集：POP-SED + BEATs 平均 F-score 62.35%，相对 Full Background Model 基线 40.20% 大幅提升；接近需域级与支持集微调的顶尖系统。消融表明向量选择与 PDF 背景建模均有贡献。

## 结论
正交投影可在不微调编码器的前提下抑制背景，使通用基础模型达到接近微调系统的少样本 SED 表现，便于现场定制。

## 点评
把“背景适应”做成几何投影而非梯度更新，适合部署约束紧的场景。依赖背景向量估计质量与 vMF 假设；极端非平稳背景或目标与背景高度共线时投影可能过杀目标能量。


# CLEAR: Clinical LLM Embedding and Attention-based Reconstruction

- 论文编号：883
- 报告人：Eashita Wazed
- 程序：Wednesday 30 September 2026 / Acoustic Event Detection 3
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wazed26_interspeech.pdf

## 问题
临床心音受医院噪声、摩擦、呼吸等非平稳干扰，传统滤波与局部 CNN 难抓住心动周期长程结构，掩码分离又易产生波形断裂。

## 方法
CLEAR 三阶段：(1) 预训练 Whisper 编长序列生物声学嵌入；(2) Masked GAT 将嵌入建图并预测潜在掩码，抑制噪声；(3) Latent GAN 在嵌入空间修复生理结构并重建波形。相对直接回归干净嵌入，掩码路径约束更紧。

## 实验与结果
10 dB SNR 环境噪声下：输入 PESQ 1.03、SI-SDR −29.37 dB；增强后峰值 PESQ 4.64、SI-SDR 64.35 dB。作者报告自然、无明显伪影的听诊友好输出。

## 结论
LLM 嵌入 + 图注意力掩码 + 潜空间 GAN 可从严重降质输入恢复高保真心音，有助临床听诊与早期筛查。

## 点评
把语音大模型编码器挪到心音，强调长程周期，问题动机清楚。报告的 SI-SDR/PESQ 峰值极高，需注意是否含特定样本峰值、评价是否宽带模式等协议细节；临床诊断效用仍需下游疾病识别实验支撑（正文以增强指标为主）。


# Few-shot Class-variable Incremental Audio Classification via Prototype Adaptation and Pseudo Class-variable Training

- 论文编号：1024
- 报告人：Guoqing Chen
- 程序：Wednesday 30 September 2026 / Acoustic Event Detection 3
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26q_interspeech.pdf

## 问题
既有少样本类增量音频分类默认类别只增不减；现实中类数可增可减。需定义并求解 Few-shot Class-variable Incremental Audio Classification（FCIAC）。

## 方法
编码器 + 分类器：基座会话训编码器后冻结；分类器由 Class-variable Prototype Adaptation Network（CPAN：APGM/SAMP/PAMP/融合）随类增删动态生成与更新原型。基座阶段用 Pseudo Class-variable Training（PCTS）混伪类做加减类演练。增量时用旧类重构嵌入更新原型。代码公开。

## 实验与结果
LS-100 / NSynth-100 / FSC-89。LS-100 上全类平均准确率 AA 92.62%，优于 CEC、PAN、AMFO 等；增量类 AA 可达 97.91%（配合 PCTS）。消融：CPAN 与 PCTS 均提升，二者齐用最优。会话序列含 +5/−2 交替增减。

## 结论
原型自适应网络加伪类可变训练使模型同时应对类增加与删除，平均准确率超过先前少样本增量方法。

## 点评
把“类可变”写进问题定义是必要扩展；CPAN 模块分工清楚。评估仍是受控会话协议，真实开放世界中的类删除触发与旧类样本可得性更苛刻。编码器冻结限制对新声学域的适应。


# Quality Adaptive Angular Margin Learning for Respiratory Sound Classification

- 论文编号：1213
- 报告人：June-Woo Kim
- 程序：Wednesday 30 September 2026 / Acoustic Event Detection 3
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kim26k_interspeech.pdf

## 问题
呼吸音分类面临录音质量参差、类别严重失衡，以及 crackle/wheeze/both 细粒度重叠；固定角间隔学习未按样本质量调节，低质样本可能破坏决策边界。

## 方法
QLung：用谱熵与 RMS 构造无参考音频质量分数，自适应缩放角间隔；对数尺度角间隔稳定失衡训练；角分类器对特征与类权重单位化，在超球上施间隔。可挂在 AST、Audio-CLAP 等骨干。

## 实验与结果
ICBHI 官方 60–40：AST 上 CE 59.55% → QLung 62.01%（+2.46 Score）；Audio-CLAP 上 62.56% → 63.39%。SPRSound OOD：QLung+Audio-CLAP Score 59.80%，优于 BTS 等。消融显示固定间隔、质量间隔、失衡校正、角分类器逐步叠加有效。

## 结论
质量自适应角间隔可提升呼吸音判别与跨数据集泛化，无需依赖额外增强或元数据引导策略即可具竞争力。

## 点评
把“录音质量”直接写入间隔强度，比一律 ArcFace 更贴临床数据异质。OOD 优势是亮点。crackle 准确率有所下降、换来漏报减少，需结合临床代价权衡；质量分数启发式是否跨设备稳定仍待验证。


# Fair Cognitive Impairment Detection Through Unlearning

- 论文编号：1353
- 报告人：William Nguyen
- 程序：Wednesday 30 September 2026 / Acoustic Event Detection 3
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/nguyen26e_interspeech.pdf

## 问题
轻度认知障碍（MCI）筛查模型常编码性别、语言等人口属性，导致子群表现不公；多模态融合不足时鲁棒性也差。

## 方法
FMD：跨模态融合（语音/文本/图像）+ 前馈网络；辅助人口分类器识别伪相关人口特征，用梯度反转对其 unlearn。分别可对性别或语言属性做遗忘。在 TAUKADIAL、PREPARE 等多语基准评估，主指标 F1 与 worst-group F1。

## 实验与结果
TAUKADIAL：FMD_Lang 总体 F1 92.6 vs 最佳基线 CogniVoice 84.1；worst-group 90.9 vs 81.3。PREPARE：FMD_Sex 总体 F1 60.1 最高；FMD_Lang worst-group 57.4 优于 Whisper 等。探针显示遗忘后人口属性可预测性下降（更接近随机）。消融去掉跨模态或 unlearn 均伤表现或公平。

## 结论
人口属性遗忘与更强跨模态融合可同时提升 MCI 检测平均性能与最差子群表现，朝更公平筛查迈进。

## 点评
把公平做成可训练目标而非事后重加权，探针验证有说服力。需选择遗忘哪类属性；过度遗忘可能丢弃与病理相关的合法相关。PREPARE 绝对 F1 仍偏低，说明数据难度与方法上限并存。


# QuadVAD: Fine-Grained Speech Detection with a Compact Architecture

- 论文编号：2009
- 报告人：Nivedita Chennupati
- 程序：Wednesday 30 September 2026 / Acoustic Event Detection 3
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rachumallu26_interspeech.pdf

## 问题
常开设备与对话 AI 需要低延迟、精确边界的 VAD；现有神经 VAD 多为 16–40 ms 帧，边界偏移大，难以服务唤醒词等精细场景。

## 方法
QuadVAD：约 6k 参数，对每 4 ms 非重叠帧拼接前 3 ms 上下文（7 ms@16 kHz）做轻量卷积分类。多阶段训练：先用 MFA 对齐监督，再在 TIMIT 上精调时间精度；噪声/增益增强。目标 4 ms 分辨率。

## 实验与结果
相对 Silero/TenVAD 等，开源集 AUC 更高。电平 [−40,−15] dBFS：QuadVAD F1 0.95，与 Silero 相当并优于 TenVAD；更低电平 [−60,−40]：F1 0.96、AUC 0.99 最优。模型约 25 kB、25 MFLOPs，i7 上 RTF 0.0014。结论称跨语趋势稳健，适合唤醒词集成。

## 结论
超轻量 4 ms VAD 在精度与算力间取得平衡，可部署于资源受限常开设备。

## 点评
把帧率推到 4 ms 并配套对齐训练，切中唤醒/端点场景。与商用/开源基线比边界质量比单纯帧分类更有意义。极端噪声与远场会议是否仍稳，正文侧重增强 TIMIT 类设置。


# Exploratory analysis of yellow mongoose vocalization: detection from in-the-wild recordings and call classification

- 论文编号：2168
- 报告人：Sevada Hovsepyan
- 程序：Wednesday 30 September 2026 / Acoustic Event Detection 3
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hovsepyan26_interspeech.pdf

## 问题
黄獴（YM）行为生态依赖叫声类型解析，但野外录音噪声大、部分叫声标签模糊（含 undefined），需同时做野外检测与幼崽叫声分类探索。

## 方法
分类：手工谱时特征 + 随机森林，对比小型 CNN；9 类幼崽叫声（8 已知 + undefined）。检测：在含幼崽/成体/他种与噪声的野外录音上比较 rVAD 与 wSeg；对短时误检做时间合并后处理。置换检验分析特征重要性。

## 实验与结果
5 折：RF 均准 0.684±0.016，CNN 0.61±0.029。测试准确约 0.67；部分类型（如 begging call）F1 较高，undefined 与已知类有混淆，子群或暗示未描述新类型。rVAD 重叠/灵敏度优于 wSeg；未合并时 precision 低（约 0.19），合并邻近预测可提升 precision 且保持灵敏度。

## 结论
手工特征 RF 对 YM 幼崽叫分类有效；通用 VAD 类工具经简单时序平滑可辅助野外录音筛查，但假阳性仍需人工复核。探索性分析指向可能的新叫型。

## 点评
生物声学里“先分清叫型、再从噪声中捞出来”的双问题设定务实。undefined 类既是噪声也是发现源。检测 precision 低说明更适合作为候选段生成器而非全自动标注；样本量不均限制细类结论强度。


# Continual Generalized Category Discovery for Acoustic Signals via Instance-Adaptive Regularization and Dynamic Teacher Guidance

- 论文编号：2614
- 报告人：Qisheng Xu
- 程序：Wednesday 30 September 2026 / Acoustic Event Detection 3
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xu26q_interspeech.pdf

## 问题
声学系统需在无标注流中持续发现新类并保住旧类（C-GCD）；直接搬视觉 C-GCD 会因谱时结构复杂、类重叠与基类偏置而大幅掉点。

## 方法
面向音频的 C-GCD：实例自适应正则平衡巩固与探索；GMM 自适应阈值；EMA 动态教师稳定伪标签。无回放设置下增量发现新类。

## 实验与结果
LibriSpeech 与 ShipsEar：相对视觉向强基线 Happy 等，旧类保持与总体累计准确率提升。ShipsEar 累计平均准确率 74.14%（+4.84）；CAA-Old 66.27%→75.00%，CAA-New 相对 Happy 仍略低（63.92 vs 71.56）。LibriSpeech 上 CAA-All 76.94%（+8.34），主要靠旧类保持。

## 结论
实例自适应正则与动态教师使音频 C-GCD 在新类发现与旧类保持上更稳，尤其提升累计准确与旧类保留。

## 点评
明确指出声学相对视觉的失败模式并改正则/伪标策略，问题对准。ShipsEar 新类准确仍落后 Happy，说明巩固–探索权衡未完全解决；无回放设定贴近部署但更难。


# I'll Keep an Ear Out: Teaching AudioLLMs Proactive Audio Assistance

- 论文编号：2807
- 报告人：Ritvik Shrivastava
- 程序：Wednesday 30 September 2026 / Acoustic Event Detection 3
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yadav26b_interspeech.pdf

## 问题
现有 AudioLLM 只在被查询时响应；面向听障辅助等可穿戴场景，需要根据单一自然语言意图持续监听并自主决定何时打断用户。

## 方法
Interrupt and Silent Modeling（ISM）：在 LLM 解码中引入 `<interrupt>` / `<silent>` 特殊词元，覆盖四态——起振检测、持续相关触发、无关抑制、去重。模型无关，应用于 Qwen2-Audio-7B。定义主动辅助评测指标与流式协议。

## 实验与结果
ESC-50：interrupt F1 99.6%，去重 recall 完美。噪声厨房 Epic-Sounds：无域特训仍获最高 interrupt F1，且不过度触发/抑制。流式评估平均延迟约 3.5 秒，显示实时可行性。

## 结论
用两个特殊词元即可把主动监听嵌进标准 AudioLLM 解码，近完美完成环境声主动辅助原型任务。

## 点评
任务形式化清楚，评测覆盖起振与去重，比单纯分类更贴辅助场景。延迟 3.5 s 对紧急告警可能偏慢；开放环境误报代价与意图表述鲁棒性仍待现场验证。

