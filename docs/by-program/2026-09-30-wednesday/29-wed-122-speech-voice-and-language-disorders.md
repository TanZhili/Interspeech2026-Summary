# Speech, Voice and Language Disorders

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Oral（Area 13 - Oral 2）
- Area：13
- 论文数：6
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。临床数字仅取自摘要。

## 技术趋势

本场连接口吃感知、不流畅 ASR、嗓音障碍的日常监测，以及构音障碍识别与韵律异常检测。感知实验显示普通话口吃者在 VOT 范畴边界形成与通达上呈非典型，而非范畴感知本身受损；ASR 侧则用持续学习与显式不流畅标记缓解“模型学会省略不流畅”的信息损失。

嗓音临床走向生态化：无线加速度计+麦克风估计日常发声效率（EVE），以及环境噪声与嗓音声学同步建模 Lombard 效应，区分创伤性/非创伤性发声过度亚型。构音障碍方面，PPG 音素编辑增强病理性误读模式；基于转写锚定与 LLM 的流水线自动检测不当停顿并给出时间对齐与理由。

## 技术内容

### 口吃感知与不流畅感知型 ASR

**Voice Onset Time Categorical Perception in Mandarin-Speaking People Who Stutter: A Zoom-In Nonword Study**（论文 2907；presenter：Yusuke Kiyama）  
用非词连续体并在范畴边界附近“放大”刺激，分析普通话口吃者（PWS）的 VOT 范畴感知。识别任务中 PWS 呈趋势性边界右移，需更长 VOT 才感知送气；边界附近反应时不对称减弱，提示音位范畴通达低效。辨别任务组间准确率与反应时无显著差异，但更严重者对范畴内刺激反应更快，摘要解释为可能右半球代偿。结论：非范畴感知受损，而是范畴映射形成与通达非典型。

**Learning to Hear Hesitation: Continual Learning for Disfluency-Aware ASR**（论文 2080；presenter：Henri-Leon Kordt）  
SOTA ASR 常被优化为省略不流畅，造成信息损失与幻觉。引入显式不流畅标记并持续学习：先在预训练 ASR 中建立稳定标记机制，再在不流畅分布各异的数据上继续训练，以减轻灾难性遗忘。训练动态分析揭示标记学习与 ASR 性能权衡，以及跨 CL 方法共享的交叉注意力头机制。

### 日常嗓音监测与 Lombard 效应

**Measuring Vocal Efficiency in Daily Life in Patients with Voice Disorders Using Wireless Accelerometer and Microphone Sensors**（论文 3457；presenter：Ahmed Yousef）  
用颈表加速度计预测声门下压、麦克风测 SPL，估计日常发声效率 EVE=SPL/Ps。14 名女性（7 声带小结患者、7 匹配对照）实验室 /p/-元音序列测 VE，并做 3 天×12 h 走动监测。患者日常 EVE 更低、变异更小（4.1 vs 4.7，r=0.67；SD 0.4 vs 1.0，r=0.91）；变异指标在场外比实验室更易分群；患者在 EVE 规范范围外时间显著更多（92% vs 36%）。

**Modeling Lombard Effects in Voice Disorders Using Daily-Life Monitoring of Ambient Noise and Voice Acoustics**（论文 2777；presenter：Ahmed M. Yousef）  
24 名 PVH/NPVH 患者与 18 名健康对照（2–4 天，≥10 h/日）同步 Leq 与 SPL、F0、CPP、H1H2。Leq 升高时 SPL、F0、CPP 升、H1H2 降；CPP 相关最强（r=0.36–0.53），非线性模型拟合最佳（CPP 最大测试 r²=0.32）。PVH 的 SPL 与 CPP 斜率陡于 NPVH，显示亚型特异真实世界 Lombard 效应。

### 构音障碍增强与不当停顿检测

**Mispronunciation Modeling via PPG-Based Phone Editing: A Data Augmentation Framework for Dysarthric Speech Recognition**（论文 891；presenter：Tsai-Hsiu Ko）  
量化个体发音变异，选择性编辑典型言语的 PPG 以模拟目标构音障碍说话人的误读，并与说话风格转换、音素级变速结合。UASpeech 上微调 HuBERT ASR，总体 WER 达 19.53%。

**A Transcript-anchored Pipeline With Large Language Models For Detecting Inappropriate Pauses In Dysarthric Speech**（论文 534；presenter：Insung Lee）  
整合逐字 ASR、经细化边界的 Montreal Forced Aligner、LLM 引导词法适配，以及带理由生成的 LLM 分类，以检测构音障碍言语中的不当停顿并精确时间对齐。相对专家评估表现强，强调可扩展与可解释的临床/研究评估。

## 本场要点

- 口吃相关非典型主要在 VOT 范畴映射通达，而非简单的范畴感知缺失。
- 不流畅感知 ASR 需持续学习显式标记，并权衡标记学习与通用识别。
- 日常 EVE 与环境噪声耦合嗓音指标把嗓音评估推出实验室。
- PVH/NPVH 的 Lombard 斜率不同，CPP 捕捉超出响度/音高的音质变化。
- PPG 编辑增强缓解构音障碍数据稀缺。
- 转写锚定+LLM 使不当停顿检测可解释、可对齐。

## 覆盖核对

| 论文 id | 标题 |
| --- | --- |
| 2907 | Voice Onset Time Categorical Perception in Mandarin-Speaking People Who Stutter: A Zoom-In Nonword Study |
| 2080 | Learning to Hear Hesitation: Continual Learning for Disfluency-Aware ASR |
| 3457 | Measuring Vocal Efficiency in Daily Life in Patients with Voice Disorders Using Wireless Accelerometer and Microphone Sensors |
| 891 | Mispronunciation Modeling via PPG-Based Phone Editing: A Data Augmentation Framework for Dysarthric Speech Recognition |
| 2777 | Modeling Lombard Effects in Voice Disorders Using Daily-Life Monitoring of Ambient Noise and Voice Acoustics |
| 534 | A Transcript-anchored Pipeline With Large Language Models For Detecting Inappropriate Pauses In Dysarthric Speech |
