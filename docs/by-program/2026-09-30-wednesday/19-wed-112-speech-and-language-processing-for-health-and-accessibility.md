# Speech and Language Processing for Health and Accessibility

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Show And Tell（Show and Tell 3）
- Area：—
- 论文数：8
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。技术表述仅依据各条目摘要，不补写摘要未给出的数字或方法细节。

## 技术趋势

本场以健康与无障碍场景下的可演示系统为主，突出“把评估、采集与处理搬到临床或自然场景”的工程落地。听力学方向出现两条互补路径：一是用游戏化、浏览器端或 VR 沉浸式体验，让听者直观感受噪声中聆听与掩蔽差异；二是面向单侧聋（SSD）等特殊需求定制侧向波束形成硬件，弥补传统助听器前向指向性不足。

儿童语言与发展研究侧则强调开放工具链：从儿童中心音频的标准化、说话人分离与发声指标提取，到头戴相机的可穿戴采集与本地 AI 标注，目标是降低对高级编程与人工标注的依赖，支撑大规模、可复现的自然场景研究。

临床语音分析方面，嵌入式床旁平台试图把采集、分析与报告收拢到同一设备，以服务精神疾病等场景的即时决策；同时出现对“增强后再做临床生物标志物分析”的警惕——可懂度提升并不自动等价于标志物保真，临床感知成为语音增强设计的约束。

构音障碍 ASR 则采用两阶段 Conformer 个性化适配，在数据稀缺与说话人高变异条件下，把通用病理性词汇适应与快速个性化串联到移动端平台，体现无障碍通信从模型到产品的闭环。

## 技术内容

### 听力学评估与沉浸式聆听体验

**Sound Reactor Mission: Gamified Misophonia Assessment to Bridge the Gap in Audiology and Hearing Care**（论文 3573；presenter：Jorge Mejia）  
摘要指出恐声症（misophonia）缺乏标准化、可扩展的评估路径。SRM 为仅需耳机的浏览器端游戏化噪声中言语评估：约六分钟的太空任务中完成自适应言语接受阈估计、选择个人厌烦掩蔽声、在三种掩蔽条件下比较可懂度，并完成可接受噪声级测量。试点数据（N=14；100% 完成；平均 6.5 分钟）显示，所选厌烦声下可懂度（59.2%）低于合成掩蔽（71.7%）与标准掩蔽噪声（86.3%）。现场演示供参会者完成任务并与他人结果对照。

**An Immersive VR System for Experiencing Spatial Speech-in-Noise Challenges in Clinical Audiology**（论文 3582；presenter：Nicky Chong-White）  
针对临床听力结果难与真实聆听困难对应的问题，系统在 Apple Vision Pro 上提供沉浸式聆听演示：咖啡馆、火车站、客厅三类三维场景，含目标说话人、竞争说话人与空间渲染环境噪声；用户听短对话并回答理解题，临床人员可通过预设调节信噪比、声源数量与空间分离。定位为便携临床演示工具，非诊断评估。

**Head-Worn Dipole Microphone Array-based Speech Enhancement System for Single-Sided Deafness**（论文 3601；presenter：Ken Takaki）  
SSD 用户更需侧向言语可懂度，而传统助听器多为前向指向。工作构建侧向波束的 MEMS 偶极麦克风阵列，在假头上测传递函数并仿真噪声场景；两偶极加一全向的波束形成相对同位置三通道全向阵列，侧向言语 SDR 提升 0.78 dB、ESTOI 提升 0.04。演示含音频样例与实时波束形成。

### 儿童语言数据与可穿戴生态

**ELSI: An Interface for Standardizing Child-Centered Datasets, Applying Machine Learning Models, and Extracting Metrics**（论文 3583；presenter：Kaveri K. Sheth）  
开源 ExELang Legacy Support Interface 面向全球多样社区语言习得研究：标准化儿童中心数据集，运行在儿童中心音频上训练的模型（如说话人分离、音素计数），并提取儿童/成人发声数与会话轮次等指标。演示覆盖标准化、模型执行与指标抽取，降低对高级编程技能的要求。

**The TinyExplorer Ecosystem: Open tools for studying infants’ auditory and visual experiences**（论文 3597；presenter：Cátia M Oliveira）  
针对自然场景下婴儿多模态体验难捕捉、头戴相机受限于安全轻量硬件与人工标注成本，开源 TinyExplorer 组合可穿戴自我中心采集硬件（Gear）与本地运行 AI 标注（Detection App）。当前集成自动人脸检测，并扩展手部检测、手—物体交互标注与音频处理，以支持可扩展、可复现的真实学习环境研究。

### 临床语音分析、无障碍 ASR 与增强的临床意识

**Demonstration of Embedded Systems for Clinical Speech Analysis**（论文 3592；presenter：Jeremiah B Joyce）  
许多计算语音分析依赖非常规临床硬件，使采集、分析与报告在时空上分离。演示将传感器、GPU 与显示集成到床旁嵌入式平台，在床边端到端运行当前用于精神疾病患者评估的语音分析流水线核心组件，以便结果及时进入紧急临床决策。

**BetterSpeak: An Atypical Speech to Typical Speech Platform for Dysarthric Speakers**（论文 3605；presenter：Seyed Reza Shahamiri）  
构音障碍说话人变异大、数据稀缺使传统 ASR 失效。BetterSpeak 为移动端平台，采用两阶段个性化 Conformer 适配：先将稳健 Conformer 适应一般构音障碍词汇，再用有限公开构音障碍样本快速个性化声学编码器，强调数据高效个性化对儿童可及、高准确通信的意义。

**ClinAware: Speech Enhancement Needs Clinical Awareness**（论文 3611；presenter：Pramod H. Kachare）  
远程与居家评估常把语音增强作预处理，但其对神经相关语音生物标志物的影响了解不足。交互演示在噪声输入下比较多种增强方法，通过语谱图、定量标志物变化与轻量可解释风险分数展示：可懂度改善未必保留标志物，需以临床意识指导未来增强设计。

## 本场要点

- 听力学评估向可扩展、游戏化与沉浸式体验延伸，强调与真实噪声中聆听体验对齐，而非仅报告传统测听数字。
- SSD 侧向波束与临床演示 VR 分别从硬件指向性与空间场景理解切入无障碍聆听。
- 儿童语言研究工具链（ELSI、TinyExplorer）同时解决数据标准化/指标抽取与可穿戴采集+本地 AI 标注瓶颈。
- 床旁嵌入式系统把精神疾病相关语音分析接到点照护决策时间尺度。
- 构音障碍 ASR 以两阶段 Conformer 个性化应对数据稀缺与高变异。
- ClinAware 明确区分“听得更清楚”与“临床标志物仍可信”，把增强纳入临床约束。

## 覆盖核对

| 论文 id | 标题 |
| --- | --- |
| 3573 | Sound Reactor Mission: Gamified Misophonia Assessment to Bridge the Gap in Audiology and Hearing Care |
| 3582 | An Immersive VR System for Experiencing Spatial Speech-in-Noise Challenges in Clinical Audiology |
| 3583 | ELSI: An Interface for Standardizing Child-Centered Datasets, Applying Machine Learning Models, and Extracting Metrics |
| 3592 | Demonstration of Embedded Systems for Clinical Speech Analysis |
| 3597 | The TinyExplorer Ecosystem: Open tools for studying infants’ auditory and visual experiences |
| 3601 | Head-Worn Dipole Microphone Array-based Speech Enhancement System for Single-Sided Deafness |
| 3605 | BetterSpeak: An Atypical Speech to Typical Speech Platform for Dysarthric Speakers |
| 3611 | ClinAware: Speech Enhancement Needs Clinical Awareness |
