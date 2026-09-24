# Methods and data for vocal tract and articulation analysis

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Special Session
- Area：14
- 论文数：9

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本特邀场聚焦声道与构音的方法与数据：如何跨说话人规范化 EMA、如何量化性别相关声道形态差异、如何从语音反演构音/声源参数并跨语言泛化，以及如何用 FEM、MRI 约束形变、多模态同步采集与超声聚类刻画动态三维声道与音段对比。

规范化与说话人差异是第一瓶颈。腭长缩放加咽部测声锚定的可审计归一化能降低舌轨迹说话人间离散，但未必改善说话人无关的构音–声学映射；形态计量则提示男性声道形态差异更大，或可解释识别准确率的性别偏向。二者共同说明：几何可比性提高，不等于声学预测或识别公平自动改善。

物理与成像建模侧，弯曲声道 FEM、MRI+LDDMM 动态三维声道，以及 rtMRI+EEG+sEMG 同步采集，分别回答曲率对共振/高阶模态的影响、持续姿态与实时协同发音如何衔接、神经–肌肉–构音链条如何同窗观测。伪影抑制与超发音条件下的共振峰偏高，是摘要明确提到的实践约束。

数据与音系对比方面，ArtComp 用自然手段扰动颌位并记录 EMA/EGG/视频；普通话齿龈–卷舌对比用 rtMRI 网格跟踪；卷舌咝音则用超声与无监督聚类揭示多种舌形策略与说话人偏好。方法学上，场内既有“锚点归一化/反演泛化”，也有“多策略构音实现”的描写转向。

## 论文技术总结

# Acoustic Pharyngometry as an Auditable Anchor for Cross-Speaker EMA Normalization

- 论文编号：1883
- 报告人：Valeriia Vyshnevetska
- 程序：Monday 28 September 2026 / Methods and data for vocal tract and articulation analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/friedrichs26_interspeech.pdf

## 问题
跨说话人 EMA 比较受声道形态混淆；全局相似变换可解释但弱，灵活非刚体配准又难审计。需要低负担、可检查的解剖锚。

## 方法
在腭参照坐标系下：用腭包络长做均匀缩放；从声学咽测量面积函数提取口腔扩张峰相对 OPJ 的比例 \(u_{peak}\)，锚定分段单调前后（A–P）翘曲。德语 14 人（有 EMA+咽测量）DDK 与持续元音：评说话人间轨迹离散度、LOSO 岭回归 F1/F2 预测、说话人识别。

## 实验与结果
多传感器舌轨迹离散度从 31.28 mm → 26.36 mm（仅缩放）→ 26.13 mm（缩放+翘曲，总降约 16.5%，主来自缩放）。LOSO 对 F1/F2（Hz/Bark/VTLN）预测未改善。绝对位置说话人识别高；去静态偏移后下降，说明仍有残余说话人结构。

## 结论
腭长缩放+咽测量锚定翘曲可提升几何可比性与可审计性，但不自动改善说话人无关的发音–声学映射。

## 点评
强调“改什么、能查什么”的规范化设计，对实验语音学很务实。结果显示几何对齐≠声学映射统一，提醒技术应用勿过度解读归一化收益。


# Vocal Tract Disparity and Potential Implications for Speaker Recognition

- 论文编号：2627
- 报告人：Valeriia Vyshnevetska
- 程序：Monday 28 September 2026 / Methods and data for vocal tract and articulation analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/danner26_interspeech.pdf

## 问题
人与机器对女性说话人识别常更差，即便训练数据性别平衡；原因不明。本文检验男性声道形态/发音形态差异（disparity）是否更大，从而可能产生更可分的声学签名。

## 方法
USC MRI 库：73 人静息态静态 MRI；子集 32 人 rtMRI 元音 /i,e,a,o,u/。几何形态计量（GPA+PCA），形态 disparity=组内 Procrustes 方差（控制质心大小等），置换检验性别差；按 landmark 可视化差异来源。

## 实验与结果
男性喉位更低、声道更长、质心大小约大 8.4%。合并发音数据上男性形状变异显著更大（\(p=0.006\)）；静息与单元音上趋势常同向但多不显著。男性在后元音等处发音幅度更大。差异热点多在舌根/咽等区域。

## 结论
男性更高形态/发音 disparity 可能贡献于识别优势；先天声道变异或可部分解释语音技术中的性别偏置。

## 点评
把“识别偏置”接到可量化的解剖变异，假说清晰。注意：未直接测声学/ASR 准确率与 disparity 的相关，仍是间接证据；样本与文化因素未控。


# Towards Language-Agnostic Speech Inversion

- 论文编号：1633
- 报告人：Saba Tabatabaee
- 程序：Monday 28 September 2026 / Methods and data for vocal tract and articulation analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/tabatabaee26_interspeech.pdf

## 问题
言语反演（SI）多在英语 EMA/XRMB 上训练；声道声学跨语言共享，但跨语恢复 oral TV、腭咽 TV 与声源参数的能力验证不足。

## 方法
WavLM-Large 特征 → 多任务 SI：六种 oral TV（LA/LP/TBCL/TBCD/TTCL/TTCD）+ Per/Aper/F0，可选 VP（对标 nasalance）。英语 XRMB + 自建 YU（英/法/俄共录 EMA、nasalance、音频）训练；在未见法语、俄语上评 Pearson 相关。

## 实验与结果
跨 oral TV 与声源参数，法语 PPMC 约 0.83、俄语约 0.74。VP/nasalance：英语 0.92、法语 0.89、俄语 0.82。定性轨迹显示 TBCD/TTCD/LA 在未见语言上仍跟踪 ground-truth；可反映预期性鼻化等跨语言差异。

## 结论
仅英训 SI 可较好泛化到法/俄的 oral、VP 与声源参数，支持更接近语言无关的发音反演。

## 点评
补上跨语 SI 实证缺口，尤其含 VP。样本上法语/俄语说话人很少，俄语 VP 仅 1 人，泛化结论需更大样本复核。


# Influence of Vocal Tract Curvature on Speech Acoustics: A Three-Dimensional FEM Analysis

- 论文编号：2325
- 报告人：Debasish Ray Mohapatra
- 程序：Monday 28 September 2026 / Methods and data for vocal tract and articulation analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/mohapatra26_interspeech.pdf

## 问题
许多物理声学模型把声道当直管；真实弯曲对共振的独立贡献难以从不规则截面、旁腔等中分离。

## 方法
3D FEM 波求解器，中心线长固定 17 cm，系统改变弯曲角（60°/90°/120°）与曲率强度；对比均匀截面 vs Story [A] 非均匀面积函数。分析至 14 kHz 的传递函数与声场。

## 实验与结果
均匀截面：弯曲对频率响应几乎无影响，与直管一致。非均匀截面：低于约 8 kHz 与直管接近；更高频出现曲率相关反共振/横向高阶模，位置随弯曲角变化；约 10 kHz 以上可见可辨共振偏移。压力场在非均匀弯管中显示横向模式结构。

## 结论
曲率 alone 在均匀管中可忽略；与截面非均匀耦合时主要在高频激发横向模并移动共振。直管理想化在低频尚可，宽带/高精度合成需考虑弯曲。

## 点评
受控几何消融把“弯不弯”从复杂解剖中拆出，结论对 articulatory 合成建模有直接指导。局限：简化圆柱段拼接、单一 [A] 面积函数、未含唇辐射与旁腔完整解剖。


# Morphoacoustic Modeling of a Dynamic 3D Vocal Tract Using MRI-Constrained Deformations and FEM Acoustics

- 论文编号：1890
- 报告人：Tharinda Piyadasa
- 程序：Monday 28 September 2026 / Methods and data for vocal tract and articulation analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/piyadasa26_interspeech.pdf

## 问题
高分辨率体 MRI 给出持续发音的 3D 声道，rtMRI 给出连续言语的中矢面动态，二者如何结合成声学上合理的动态 3D 模型仍开放；1D 管模型难刻画卷舌等复杂过渡。

## 方法
澳大利亚英语女说话人：持续 [ɜ:]/[ɻ:] 体 MRI + [ɜɻɜ] 的 rtMRI。用 rtMRI 中矢轮廓约束的 LDDMM 在两端点网格间生成时变 3D 网格；在五声学/发音地标处采样网格，COMSOL FEM（Helmholtz、刚性壁、球外域 PML）估 F1–F3，与机外录音对比（每共振峰常数偏置对齐仅用于可视化）。

## 实验与结果
端点持续音 FEM 与直立录音在 F2/F3 较接近，F1 约高 110 Hz。动态轨迹上模拟共振峰系统偏高，但随地标跟踪参考轨迹，符合噪声环境下持续发音超调/过度清晰化的解释。地标 ±1 帧扰动不改定性结论。

## 结论
MRI 约束形变 + FEM 可连接动态 3D 几何与共振峰轨迹；绝对频率仍受姿态与边界假设影响，轨迹形状更可信。

## 点评
把几何 morphing 与声学仿真接到同一 VCV 卷舌例上，验证中间形是否“像样”。单说话人、五地标、机内外不对齐是边界；对卷舌 F3 对几何敏感的问题很有针对性。


# An Approach to Simultaneous Acquisition of Real-Time MRI Video, EEG, and Surface EMG for Articulatory, Brain, and Muscle Activity During Speech Production

- 论文编号：140
- 报告人：Kevin Huang
- 程序：Monday 28 September 2026 / Methods and data for vocal tract and articulation analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/lee26b_interspeech.pdf

## 问题
言语产生跨神经计划、肌电与发音运动；既往多模态最多两两组合，缺少 rtMRI+EEG+表面 EMG 同步，且 MRI 梯度、心电与肌电伪迹严重。

## 方法
0.55T 上螺旋 bSSFP rtMRI（约 99 fps）+ 光学麦克风；BrainVision MR 兼容系统采 EEG/EMG/ECG/EOG（5 kHz，光纤同步 MRI 时钟）。面肌三通道 EMG。多阶段去噪：平均模板减梯度伪迹 → BCG/脉冲伪迹 → ICA（含 EMG/EOG 参考）去肌电与眼电。先导：1 名英语男说话人，发声/无声/想象，机内与机外对照。

## 实验与结果
初步结果显示伪迹明显衰减，可同时观察声道运动、面肌与脑电。论文定位为可行性与管线展示，强调对言语神经科学与静默/想象言语 BCI 的潜在价值；代码与数据公开。

## 结论
三模态同步采集在技术上可行；专用伪迹抑制是关键。完整科学分析待管线成熟后展开。

## 点评
贡献主要在采集与去噪工程，填补“脑–肌–声道”同窗空白。单人先导、电极数有限，定量神经科学结论尚早，但对后续开源实验平台意义大。


# The ArtComp dataset: Articulatory and Acoustic Measurements of Swedish in Speech with Naturally Manipulated Jaw Position

- 论文编号：2647
- 报告人：Elísabet Eir Cortes
- 程序：Monday 28 September 2026 / Methods and data for vocal tract and articulation analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/cortes26_interspeech.pdf

## 问题
既有瑞典语 EMA 数据少，且下颌扰动多用咬块等人工方式；需要更自然、覆盖软到喊叫的下颌开度变化，以研究其他发音器官的补偿。

## 方法
发布 **ArtComp**：7 名中央标准瑞典语者，18 元音于 `i"bVb` 框架，用自研 DOVA（衰减麦克风输出 + VU 视觉反馈）诱发多级嗓音力度，自然改变下颌开度。采集 EMA（6 传感器）、EGG、双视角视频与高质量音频。详述采集与后处理；约 3000 token，已分析约 1100。

## 实验与结果
本文以数据集与方法学为主，展示传感器轨迹时变与 2D 追踪预览。相对 Lombard 噪声诱发，DOVA 在下颌响应与相对强度范围上更大或至少相当。

## 结论
提供可研究补偿发音的瑞典语多模态资源；“自然咬块”式下颌扰动适合语音学与临床/技术应用。

## 点评
数据集论文价值在可控自然扰动与完整方法文档。说话人少、分析仍部分完成；与咬块范式的直接对比需后续研究展开。


# Articulatory Analysis of the Mandarin Alveolar–Retroflex Contrast Using Real-Time MRI

- 论文编号：1593
- 报告人：Qi Wu
- 程序：Monday 28 September 2026 / Methods and data for vocal tract and articulation analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/wu26d_interspeech.pdf

## 问题
普通话“卷舌”常被描述为舌尖上卷，但仪器证据多显示非上卷、舌体成束等；需量化齿龈–卷舌对立的稳定发音相关，服务二语教学。

## 方法
4 名北方普通话者，rtMRI 中矢面产 8 辅音 ×12 元音环境（Tone 4）。网格法提取气–组织边界，度量：归一化收紧位置、收紧长度、前腔/后腔伪面积。线性混合效应模型（辅音类、对、交互；元音与声道长协变量）。

## 实验与结果
卷舌相对齿龈：收紧位置显著后移（\(F(1,361)=1073.93,p<0.001\)）、前腔显著扩大（\(F=1433.47,p<0.001\)）；收紧长度效应较弱且对相关；后腔区分力弱。帧图常见舌尖向下姿态而非传统上卷。

## 结论
收紧位置与前腔扩张是对立的稳健发音相关，可作为发音教学的目标，而非强调舌尖上卷。

## 点评
用 rtMRI 把“卷舌神话”落到可统计的腔体几何上，教学含义清晰。样本仅 4 人、仰卧扫描、稳态帧手工选取，推广到连续语流需谨慎。


# Tongue-Shape Strategies for Standard Mandarin Retroflex Sibilants: A Preliminary Ultrasound and Unsupervised Clustering Study

- 论文编号：1495
- 报告人：Zixi Jing
- 程序：Monday 28 September 2026 / Methods and data for vocal tract and articulation analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/jing26b_interspeech.pdf

## 问题
标准普通话卷舌咝音常被视作非典型卷舌，实现多样；既有超声研究多集中少数方言背景，跨地域说话人的舌形策略分布不清。

## 方法
5 名不同地域背景女说话人，超声舌成像产韵母匹配的齿龈–卷舌最小对。目标帧舌轮廓 42 点、质心对齐；无监督聚类得 6 簇，归并为 **domed / humped / concave** 三种超策略；再做说话人层面的组成聚类。

## 实验与结果
存在多种舌形策略，说话人偏好强烈且可稳定分群（蒙特卡洛 \(\chi^2\) 支持说话人间分布差异）。与先前框架不完全相同：观察到拱顶（domed）等构型。部分说话人偏 humped，部分偏 domed。

## 结论
标准普通话卷舌咝音允许多种舌形策略，且呈现说话人特异、可聚类的偏好结构。

## 点评
用聚类把定性“多样”变成可重复的策略类型学，适合作为更大样本研究的试点。5 人、仅女性、10 fps 超声限制时间分辨率；与声学对立清晰度的关系未深入。

