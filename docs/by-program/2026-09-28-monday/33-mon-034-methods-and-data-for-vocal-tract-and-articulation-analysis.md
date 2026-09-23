# Methods and data for vocal tract and articulation analysis
- 日期：Monday 28 September 2026 / 时间：14:30-16:30 / 形式：Special Session（Area 14）/ 论文数：9
- 材料：官方程序论文摘要。未出现的数字与细节不写。

## 技术趋势

本特邀场聚焦声道与构音的方法与数据：如何跨说话人规范化 EMA、如何量化性别相关声道形态差异、如何从语音反演构音/声源参数并跨语言泛化，以及如何用 FEM、MRI 约束形变、多模态同步采集与超声聚类刻画动态三维声道与音段对比。

规范化与说话人差异是第一瓶颈。腭长缩放加咽部测声锚定的可审计归一化能降低舌轨迹说话人间离散，但未必改善说话人无关的构音–声学映射；形态计量则提示男性声道形态差异更大，或可解释识别准确率的性别偏向。二者共同说明：几何可比性提高，不等于声学预测或识别公平自动改善。

物理与成像建模侧，弯曲声道 FEM、MRI+LDDMM 动态三维声道，以及 rtMRI+EEG+sEMG 同步采集，分别回答曲率对共振/高阶模态的影响、持续姿态与实时协同发音如何衔接、神经–肌肉–构音链条如何同窗观测。伪影抑制与超发音条件下的共振峰偏高，是摘要明确提到的实践约束。

数据与音系对比方面，ArtComp 用自然手段扰动颌位并记录 EMA/EGG/视频；普通话齿龈–卷舌对比用 rtMRI 网格跟踪；卷舌咝音则用超声与无监督聚类揭示多种舌形策略与说话人偏好。方法学上，场内既有“锚点归一化/反演泛化”，也有“多策略构音实现”的描写转向。

## 技术内容

### 跨说话人规范化、形态差异与语音反演

**Acoustic Pharyngometry as an Auditable Anchor for Cross-Speaker EMA Normalization**（论文 1883；presenter：Valeriia Vyshnevetska）
跨说话人 EMA 受声道形态混淆。方法结合腭长缩放与咽部测声导出的口腔地标，做低参数前后向扭曲。德语 DDK 上舌轨迹离散下降，但 leave-one-speaker-out 岭回归未改善由 EMA 预测 F1/F2；去除静态偏移后说话人识别下降。摘要结论：几何可比性提高，说话人无关构音–声学映射未改善。

**Vocal Tract Disparity and Potential Implications for Speaker Recognition**（论文 2627；presenter：Valeriia Vyshnevetska）
感知与自动识别常对女性说话人准确率更低。作者用几何形态计量量化静息与构音构型下的性别相关声道形态差异，发现男性在两类构型上差异更大。摘要提出这可能产生更可分的声学签名，为识别偏向提供生物学解释线索。

**Towards Language-Agnostic Speech Inversion**（论文 1633；presenter：Saba Tabatabaee）
在美式英语共录语音与构音运动学上训练同时估计口腔 tract variables 与三类声源参数的 SI 系统，并在未见语言上评估。摘要报告法语、俄语上 oral tract variables 与声源信息的 Pearson 相关，讨论跨语言可泛化性。

### 三维声道物理/成像建模与多模态数据采集

**Influence of Vocal Tract Curvature on Speech Acoustics: A Three-Dimensional FEM Analysis**（论文 2325；presenter：Debasish Ray Mohapatra）
许多物理声学模型把声道近似为直管。三维 FE 波求解器系统改变曲率，均匀截面时曲率对频响影响可忽略；非均匀截面时高频率激发高阶横向模态，并在 10 kHz 以上产生明显共振峰偏移。

**Morphoacoustic Modeling of a Dynamic 3D Vocal Tract Using MRI-Constrained Deformations and FEM Acoustics**（论文 1890；presenter：Tharinda Piyadasa）
用约束 LDDMM 结合持续姿态容积 MRI 与短协同发音中矢状 rtMRI，构建时变三维声道并做有限元共振峰估计，示例为澳大利亚英语 [5ô5]。模拟共振峰系统性偏高但跟踪参考轨迹，摘要将其与噪声条件下持续语音的超发音相一致。

**An Approach to Simultaneous Acquisition of Real-Time MRI Video, EEG, and Surface EMG for Articulatory, Brain, and Muscle Activity During Speech Production**（论文 140；presenter：Kevin Huang）
首次同时采集动态 MRI、EEG 与表面 EMG，覆盖脑信号、肌肉激活与构音运动。针对 MRI 电磁干扰与肌电伪影提出三模态伪影抑制管线；源码与数据可用。摘要定位为言语神经科学与 BCI 的窗口性框架。

### 扰动构音数据与普通话卷舌对比

**The ArtComp dataset: Articulatory and Acoustic Measurements of Swedish in Speech with Naturally Manipulated Jaw Position**（论文 2647；presenter：Elísabet Eir Cortes）
七名中部标准瑞典语说话人的时间对齐构音（EMA、EGG、视频）与声学数据；颌位经自然手段扰动，诱发由软到喊叫的不同用力。摘要详述采集与后处理，并给出传感器轨迹预览，服务于其他构音器自适应行为研究。

**Articulatory Analysis of the Mandarin Alveolar–Retroflex Contrast Using Real-Time MRI**（论文 1593；presenter：Qi Wu）
rtMRI 网格跟踪提取归一化收紧位置、收紧长度、前后腔等测量。结果称卷舌对收紧位置与前腔效应稳健，收紧长度不一致、后腔区分弱；帧上常见舌尖向下。摘要建议收紧位置与前腔扩张可作为稳定构音目标。

**Tongue-Shape Strategies for Standard Mandarin Retroflex Sibilants: A Preliminary Ultrasound and Unsupervised Clustering Study**（论文 1495；presenter：Zixi Jing）
五名女性母语者超声舌轮廓经对齐与无监督聚类，得到六簇并合并为 domed / humped / concave 三类超策略。成分聚类显示说话人间系统差异与稳定偏好，支持普通话卷舌咝音允许多种舌形策略。

## 本场要点
- EMA 跨说话人归一化可降几何离散，但不自动改善构音–声学映射或消除残余说话人结构。
- 声道形态差异被讨论为说话人识别性别偏向的潜在生物学因素。
- Speech inversion 开始报告跨未见语言的相关表现，指向语言无关反演目标。
- FEM 与 MRI 约束形变把“曲率/动态三维几何–声学”关系量化到高频率与时变轨迹。
- rtMRI+EEG+sEMG 同步采集强调伪影抑制是多模态言语产生研究的关键工程。
- 普通话卷舌相关工作从单一目标描写转向多测量相关与多舌形策略聚类。

## 覆盖核对
`1883 | Acoustic Pharyngometry as an Auditable Anchor for Cross-Speaker EMA Normalization`
`2627 | Vocal Tract Disparity and Potential Implications for Speaker Recognition`
`1633 | Towards Language-Agnostic Speech Inversion`
`2325 | Influence of Vocal Tract Curvature on Speech Acoustics: A Three-Dimensional FEM Analysis`
`1890 | Morphoacoustic Modeling of a Dynamic 3D Vocal Tract Using MRI-Constrained Deformations and FEM Acoustics`
`140 | An Approach to Simultaneous Acquisition of Real-Time MRI Video, EEG, and Surface EMG for Articulatory, Brain, and Muscle Activity During Speech Production`
`2647 | The ArtComp dataset: Articulatory and Acoustic Measurements of Swedish in Speech with Naturally Manipulated Jaw Position`
`1593 | Articulatory Analysis of the Mandarin Alveolar–Retroflex Contrast Using Real-Time MRI`
`1495 | Tongue-Shape Strategies for Standard Mandarin Retroflex Sibilants: A Preliminary Ultrasound and Unsupervised Clustering Study`
