# Multimodal and Non-Speech Healthcare Applications
- 日期：Tuesday 29 September 2026 / 时间：09:00-11:00 / 形式：Oral（Area 13）/ 论文数：6
- 材料：官方程序论文摘要。未出现的数字与细节不写。

## 技术趋势

本场连接呼吸音、构音运动学、帕金森病数字生物标志物、生物声学健康编解码评测，以及视听抑郁检测。非言语/多模态健康信号的共同瓶颈包括：临床语义接地不足、实验室设备难规模化、声学指标纠缠呼吸–喉–构音贡献、试验中安慰剂/霍桑效应，以及压缩传输是否保留诊断信息。

方法上，零样本呼吸音分类用医学 LLM 合成报告做对比对齐；MediaPipe Face Mesh 单摄像头 3D 跟踪对标光学动作捕捉；从 EMA/声学导出构音无力指数以解耦构音成分；临床试验数据检验视听与轻拍数字标志物的被试内稳定性；BACH 系统评测编解码在重建保真与下游任务间的错位；抑郁检测则用优势加权排序损失在潜空间重建潜在序数结构。

## 技术内容

### 呼吸音语义对齐与构音运动学

**Zero-Shot Respiratory Sound Classification through LLM-Augmented Audio-Text Alignment**（论文 2235；presenter：Mustafa Talha İlerisoy）
自监督呼吸编码器缺临床语义接地，难零样本。用医学 LLM 由元数据合成结构化报告作对比学习锚点，结合 sigmoid 对比损失、原生 SSL 目标与相似度感知负采样。摘要报告跨多任务/数据集的零样本与线性探测 AUC，并称以更少数据优于通用大模型。

**From Lab to Laptop: Validating 3D Speech Kinematics with MediaPipe Face Mesh**（论文 3022；presenter：Victoria Sanchez）
无标记管线由单路 RGB 摄像头经 MediaPipe Face Mesh 捕获 3D 构音轨迹，经每人标定到毫米并对标光学动作捕捉。摘要报告毫米级跟踪精度、低归一化位移误差，以及 15 fps 下效用不减，论证可扩展临床转化。

**Toward an Articulatory Weakness Index for Speech Kinematics in Parkinson’s Disease**（论文 159；presenter：Shrishail Baligar）
许多声学度量混合呼吸、喉与构音贡献。由健康 EMA 学习构音状态坐标并导出 AWI；帕金森队列中 AWI 升高并与运动严重度相关，在健康对照与嗓音过度功能说话人中保持稳定。摘要称可从声学得到可解释的解耦构音无力指数。

### 试验生物标志物、编解码基准与抑郁检测

**Speech and Video Biomarkers Exhibit Reduced Within-Subject Variability in Early Parkinson’s Disease and Resistance to Placebo and Hawthorne Effects**（论文 2850；presenter：Vikram Ramanarayanan）
在 II 期临床试验数据上评估言语、面部与手指轻拍数字生物标志物。相对 MDS-UPDRS，这些客观度量基线相关但变异更低、对安慰剂/观察效应更不敏感。摘要强调其作为更稳试验终点的潜力。

**BACH: Benchmarking Audio Codecs for Bio-Acoustic Health**（论文 1588；presenter：Zixing Zhang）
首个系统评测音频编解码在生物声学健康任务上的基准，覆盖多种编解码与任务，统一比较原始、压缩表征与重建音频。核心发现：重建保真高者未必保留任务相关语义线索，医学应用编解码需同时优化感知质量与诊断信息。

**Uncovering Latent Depression Severity for Binary Depression Detection via Advantage-weighting Ranking**（论文 535；presenter：Manning Gao）
视听抑郁检测面临特征分布重叠与边界脆弱。框架含时间编码器与 mutual transformer；Binary Advantage-weighting Ranking Loss 通过难例加权分离与类内紧致，在潜空间重建潜在序数结构。摘要称在 D-vlog 与 LMVD 达先进。

## 本场要点
- 临床零样本依赖医学文本/报告锚点，而非仅扩大通用音频模型。
- 单摄像头 3D 构音跟踪经分析验证后具备规模化潜力。
- AWI 试图从声学中解耦构音无力，补充呼吸/喉指标。
- 数字生物标志物在 PD 试验中显示更低变异与更强抗情境效应。
- 健康场景编解码不能只优化重建 SNR/听感。
- 抑郁二分类可通过排序损失利用潜在严重度结构。

## 覆盖核对
`2235 | Zero-Shot Respiratory Sound Classification through LLM-Augmented Audio-Text Alignment`
`3022 | From Lab to Laptop: Validating 3D Speech Kinematics with MediaPipe Face Mesh`
`159 | Toward an Articulatory Weakness Index for Speech Kinematics in Parkinson’s Disease`
`2850 | Speech and Video Biomarkers Exhibit Reduced Within-Subject Variability in Early Parkinson’s Disease and Resistance to Placebo and Hawthorne Effects`
`1588 | BACH: Benchmarking Audio Codecs for Bio-Acoustic Health`
`535 | Uncovering Latent Depression Severity for Binary Depression Detection via Advantage-weighting Ranking`
