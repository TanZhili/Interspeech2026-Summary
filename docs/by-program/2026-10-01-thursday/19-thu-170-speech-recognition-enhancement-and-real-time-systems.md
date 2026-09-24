# Speech Recognition, Enhancement and Real-Time Systems

- 日期：Thursday 1 October 2026
- 时间：09:00-11:00
- 形式：Show And Tell
- Area：
- 论文数：4

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场 Show and Tell 面向可落地的实时通信与联络中心：连续说话人验证防冒用、边缘时域神经 AGC、手机端十亿级模型编排的实时转写+日志+自定义词表，以及人在回路多代理实体抽取把坐席修正回流 ASR。共性是低 RTF/低算力、跨设备与无需声学重训的反馈闭环。

安全与前端侧强调通话全程比对声纹并告警，以及内容感知增益映射替代规则 AGC。识别侧则把前沿精度搬到移动端，并与上下文偏置、流式日志研究结合。联络中心用 UI 确认实体驱动上下文偏置条目或后 ASR 替换规则，缩小与“提前给出实体表”的 oracle 差距。

## 论文技术总结

# A light weight Continuous Speaker Verification System for Real time Monitoring

- 论文编号：3584
- 报告人：Harish Rajamani
- 程序：Thursday 1 October 2026 / Speech Recognition, Enhancement and Real-Time Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/keetha26b_interspeech.pdf

## 问题
电话客服、银行与医保等场景需要在通话全程持续核验客户身份，防止交接、冒充或盗用设备后泄露敏感信息。传统系统多为通话开头一次性认证，无法实时监测说话人变化；同时需满足低延迟、抗噪声混响与跨语言/语码转换的稳健性。

## 方法
演示级连续说话人验证（CSV）系统：客户侧按用户名取注册声纹或短段现场注册，开头验证失败三次则回退密码；通过后转座席，座席界面持续显示验证状态。流式处理用 1 s 窗、0.5 s 跳，经 VAD、嵌入提取与对注册声纹的余弦相似度打分，约每 500 ms 更新决策；不匹配持续约 3 s 则告警并可终止通话。模型为两阶段：Stage 1 用 ReDimNet-B1 在 log-mel 上做多语说话人分类（margin loss，含噪声/混响/变速增强）；Stage 2 冻结骨干，用轻量卷积投影网络与含同语/跨语对的 triplet 采样，得到更可分、语言不变的 256 维嵌入。

## 实验与结果
在 TidyVoice（约 457 小时多语）上训练增强（SNR 5–20 dB，RT60 0.2–0.8 s，速度 0.9/1.1）。系统在 Intel Core i7-8650U 上处理 1 s 音频约 50 ms，RTF=0.05；总约 2.5M 参数、318 M MAC/s（骨干 2.2M / 290 M MAC/s，投影约 256K / 27.36 M MAC/s）。在 TidyVoice 评估/开发集上 EER=2.08%。

## 结论
作者认为该两阶段轻量模型可学习稳健、语言不变的说话人表征，在实时 RTF 与低算力下完成连续验证与座席告警，适用于电话类安全场景并可扩展到其他应用。

## 点评
工作偏系统演示：把 CSV 接到座席告警闭环，并用两阶段（分类预训练 + 跨语 triplet 投影）压低算力。指标与效率数字清楚，但正文对公开基准对比、误报/漏报业务代价及更复杂噪声信道的系统评测着墨有限，EER 主要来自自有 TidyVoice，跨域泛化仍需外部验证。


# WaveNorm: A Low-Complexity Time-Domain Neural Adaptive Gain Control for Real-Time Speech Applications

- 论文编号：3588
- 报告人：Harish Rajamani
- 程序：Thursday 1 October 2026 / Speech Recognition, Enhancement and Real-Time Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ijjada26b_interspeech.pdf

## 问题
真实语音电平因距离、房间与设备大幅波动，损害 ASR、会议与助听；传统 AGC（如 WebRTC）靠包络与固定 attack/release，难区分语音/噪声，易延迟、削波或放大背景噪声；频域学习方法又增加延迟，不利于边缘实时。

## 方法
WaveNorm AGC 全时域、因果：20 ms 帧、10 ms 移。编码器为堆叠因果 Conv1D（核 3，dilation 2/4/8）+ grouped convolution + BN/PReLU，建模多尺度幅度与包络；瓶颈为 hidden 32 的 GRU 与 32 维全连接，保证增益平滑；解码器用转置 Conv1D 镜像上采样，端到端映射波形，隐式完成归一化与降噪，不显式输出增益系数。感受野约 27 样本（~0.56 ms）。损失为 0.5 MSE + 0.5 多分辨率谱损失（STFT 128–2048）；Adam 1e-3，200 epoch。

## 实验与结果
内部 48 kHz 语料 + DNS3：RMS −10 至 −70 dB，噪声 SNR −5 至 +20 dB。独立 AGC：在 VoiceBank+DEMAND 衰减与 TIMIT 放大设定下，相对 WebRTC、Carnival 更电平不变、增益更平滑，约 6 dB 降噪，Active Speech Level 近 −26 dBov，响度 −26 至 −28 LUFS，符合 ITU-T P.56/P.79。作前端时，在 DeepFilterNet2、DTLN、GTCRN 上最高约 +0.35 NISQA。模型 49 M MACs、55 KB 内存。

## 结论
WaveNorm 以极低时延与很小算存实现宽动态（至 −70 dB）稳定响度归一化，并在噪声下约 6 dB 降噪，避免传统 AGC 的削波与噪声放大，适合会议与边缘实时语音。

## 点评
把 AGC 做成时域端到端“内容感知电平映射”，用 GRU 约束增益平滑，是对规则包络跟踪的直接替代，而非再堆一套频域增强。数字披露偏概括（对比多为定性+少量 NISQA），对极端非平稳噪声与说话人切换时的 pumping 风险仍需更多公开对比表支撑；优势主要在边缘算力与标准响度合规。


# Argmax Pro: Frontier-level Real-time Speech-to-text with Speakers and Custom Vocabulary on Mobile Devices

- 论文编号：3602
- 报告人：Atila Orhon
- 程序：Thursday 1 October 2026 / Speech Recognition, Enhancement and Real-Time Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/angus26_interspeech.pdf

## 问题
云端 ASR 在延迟可靠性、可用性、按分钟计费与隐私上受限，而首代端侧实时系统常缺说话人分离、自定义词表等能力，或在实时模式下牺牲精度，难以成为云端的对等替代。

## 方法
Argmax Pro 在 iOS/Android 上编排三个十亿级 Transformer：Parakeet v2 做语音转写，采用可自纠错的流式推理（interim/final 词），使预录与实时输入精度对齐；Canary v2 CTC 配合 CTC-WS 做上下文偏置/自定义词表，可扩至约 3000 词且不拖累端侧延迟；Streaming Sortformer v2 经 FastMSS 合成数据微调，增强对真实声学、音量与背景噪声的稳健流式说话人分离。推理分别落在 Apple Neural Engine、高通/联发科 NPU 与 Google Tensor TPU，以控制续航、发热与与其他 App 的资源争用。

## 实验与结果
正文以系统描述为主，定量结果多指向相关工作：关键词（尤其人名/公司/产品）精度在 Contextual Earnings-22 等分析中达 frontier 水平；自定义词表规模相对多数云平台（常 <500）扩展到 3000。本文未给出完整独立 WER/DER 表格。

## 结论
作者认为该统一实时系统可在广泛移动设备上提供带说话人与自定义词表的近云端级端侧 STT，作为 feature-rich 云端方案的对等替代。

## 点评
这是工程集成型演示：把流式纠错 ASR、大词表偏置与稳健流式 diarization 绑到 NPU 上，解决“端侧功能不全或实时掉精度”的产品缺口。方法细节依赖引用论文，本文本身缺少自包含的对照实验数字，评估边界需结合配套基准工作理解。


# A Human-in-the-Loop Multi-Agent Companion for Real-Time Entity Extraction and SLU-Driven ASR Error Correction

- 论文编号：3610
- 报告人：Shiva Shankar Arumugam
- 程序：Thursday 1 October 2026 / Speech Recognition, Enhancement and Real-Time Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/arumugam26_interspeech.pdf

## 问题
联络中心通话密集包含客户名、账号、SKU、药名等命名实体，流式 ASR 易错，错误会传到 agent companion 界面，造成 CRM 错录与返工。人工在 UI 上的实体纠正本是高质量监督，却很少回灌到 ASR/抽取栈；且通常不能预先备好完整实体表，也不宜做声学重训。

## 方法
演示 MACE（Multi-Agent Companion Environment）闭环：ASR（带偏置列表 B）→ 词替规则 R → 抽取子代理 → companion UI 建议；reflection 子代理在音频路径外消费 UI 纠正 Δ，将误识/漏抽实体写入 B，对跨对话复发（阈值 τ）的误识模式生成替换规则 R。按对话批更新，B/R 存 KV、按 agent 作用域隔离；不改声学模型。实验用 ContextASR-Bench 英对话子集、Whisper-large-v3，确定性代理抽取器 + oracle 编辑器模拟人在环，K=100 批、τ=2，|B|≤500、|R|≤200。

## 实验与结果
相对无偏置基线，MACE Adaptive 将 NE-WER 从 0.178 降至 0.147（约 −17.1%），EditRate 从 0.304 降至 0.247（约 −18.6%），分别闭合至 oracle 偏置差距的 23.6% / 22.0%；32 批配对 bootstrap 的 95% CI 与基线不重叠。|B| 约在第 3 批饱和至 500，|R| 约第 28 批饱和至 200。

## 结论
作者认为把 companion UI 纠正闭环回写成偏置与替换规则，可在无先验实体表、无声学重训下持续降低实体错误与人工编辑率，并向 oracle 偏置靠拢。

## 点评
抓的是“人在环纠正→上下文偏置/后处理规则”的运营反馈回路，多智能体分工让更新离线于实时转写路径，工程上很贴联络中心。评测用 oracle 编辑与代理抽取，真实 LLM 抽取与真人编辑噪声下的增益可能打折；B/R 容量封顶后增益饱和，跨租户/跨域迁移也依赖作用域隔离设计。

