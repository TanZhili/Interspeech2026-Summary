# Child Speech and Health

- 日期：2026年9月30日（周三）
- 时间：16:30-18:30
- 形式：Oral
- Area：13
- 论文数：6
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。仅依据摘要表述，不补写未给出的实验细节。

## 技术趋势

本场连接儿童语言样本分析、儿童发音障碍检测、自发语音呼吸健康评估、自闭症儿童手势—焦点韵律、儿童口吃自动检测，以及音频语言模型在口吃儿童混合说话人场景下的语义推理。

方法上，临床指标自动化从端到端 LLM 提示转向可分解零样本流水线；病理声学用自编码器嵌入或异构图融合多尺度结构；健康评估尝试从日常自发语音提取呼吸生物标志。发展障碍相关工作同时覆盖多模态手势效应与保留临床上不流畅信息的指令引导 ALM。

## 技术内容

### 语言样本指标与儿童发音障碍

**Correct Then Detect: Zero-Shot FVMC Annotation for Child Language Sample Analysis**（论文 2593；Wei Bo）  
将 FVMC 标注分解为语法纠错与强制时态语境检测，再对齐标记正确/错误/省略。摘要称在 ENNI 上三类 F1 分别为 97.05%、60.15%、70.23%，相对截至 2026 年 2 月最强 LLM 提升 1.99/4.72/6.21 点。

**Detection of Incorrect Place of Articulation in Polish Sibilants Using Convolutional Autoencoders**（论文 2624；Wojciech Pieniążek）  
用卷积自编码器（经典/稀疏/多任务）提取特征并以 SVM 检测波兰语儿童清卷舌擦音/塞擦音错误调音部位。摘要称最佳多任务模型灵敏度最高约 84.32%，证明自编码器嵌入适用于儿科困难数据。

### 呼吸健康、手势—焦点与口吃分析

**SpiroPhonia: Non-Invasive Respiratory Health Assessment from Spontaneous Speech**（论文 2571；Roksana Khanom）  
在 201 名说话人（102 COPD / 99 对照）新数据上，结合统计与递归特征选择识别紧凑语音标记。摘要称最佳模型准确率 78%、F1 80%、AUC 87%，与受控实验室录音方法具竞争力。

**Effects of Co-speech Gesture on the Acoustic Realization of Focus in Cantonese-speaking Children With and Without Autism Spectrum Disorder**（论文 1008；Zhuoran Li）  
比较 22 名自闭症与 25 名典型发展粤语儿童。摘要称图像手势延长两组目标音节；典型儿童缩短焦点后音节强化焦点突显，而 ASD 组在指示手势下对目标与后目标音节均出现缩短，符合弱中央统合与增强知觉功能模型。

**Paediatric-HGNN: A Hybrid Heterogeneous Graph Neural Network for Detecting Disfluency in Children’s Speech via Multiscale Acoustic Fusion**（论文 1131；Rashini Liyanarachchi）  
用 CaPIN 构建词节点与帧节点异构图，捕捉儿童发展性“搜索”行为。摘要称在 UCLASS 与 FluencyBank 上加权准确率 82.4%，典型不流畅 F1=0.386。

**Reasoning Beyond Transcription: Audio Language Models on Child Stuttering Speech**（论文 2909；Chibuzor Okocha）  
在无显式说话人分离的口吃儿童混合说话人访谈上，评测儿童聚焦语义摘要与语音蕴含。摘要称 ALM 可抽取高层意义，但随不流畅增加与说话人干扰，推理显著退化；评估用 LLM 裁判与参考指标，并以转写神谕基线隔离错误来源。

## 本场要点

- 临床 FVMC 可用“先纠错再检测”零样本分解，优于端到端 LLM。
- 自编码器嵌入有助于儿童咝音错误调音部位检测。
- 自发语音可编码有竞争力的 COPD 相关呼吸生物标志。
- 手势对焦点韵律的影响在 ASD 与典型发展儿童间模式不同。
- 儿童口吃检测与 ALM 推理均需显式处理发展变异、不流畅保留与说话人干扰。

## 覆盖核对

- 2593 | Correct Then Detect: Zero-Shot FVMC Annotation for Child Language Sample Analysis
- 2624 | Detection of Incorrect Place of Articulation in Polish Sibilants Using Convolutional Autoencoders
- 2571 | SpiroPhonia: Non-Invasive Respiratory Health Assessment from Spontaneous Speech
- 1008 | Effects of Co-speech Gesture on the Acoustic Realization of Focus in Cantonese-speaking Children With and Without Autism Spectrum Disorder
- 1131 | Paediatric-HGNN: A Hybrid Heterogeneous Graph Neural Network for Detecting Disfluency in Children’s Speech via Multiscale Acoustic Fusion
- 2909 | Reasoning Beyond Transcription: Audio Language Models on Child Stuttering Speech
