# Acoustic Event Detection 3

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：5
- 论文数：9
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program ；https://www.isca-archive.org/interspeech_2026/index.html）。不补写摘要未给出的数字与细节。

## 技术趋势

本场覆盖声音事件检测与相关声学感知：少样本 SED、临床心音重建、类别可变增量音频分类、呼吸音质量自适应角裕度、认知障碍公平检测、细粒度 VAD、野生黄獴叫声、持续广义类别发现，以及 AudioLLM 的主动音频协助。主题从经典 SED 扩展到医疗声学、公平性、边缘低延迟与可穿戴主动监听。

少样本与增量学习强调在重叠背景与类别增减下无需或少微调即可适应；临床与公平性工作融合 Whisper 嵌入、图注意力与去学习人口统计捷径。边缘部署推动 4 ms 分辨率紧凑 VAD 与主动打断/静默建模。生物声学与持续发现则把语音/视觉方法迁移到动物叫声与流式未标注新类，同时指出音频域的谱时结构使直接迁移易退化。

## 技术内容

### 少样本 SED、增量分类与呼吸音

**POP-SED: Prototype Orthogonal Projection for Robust Few-shot Sound Event Detection**（论文 153；Takehiko Kagoshima）  
免微调方法：将目标事件原型投影到与背景向量正交的子空间；背景向量由 vMF 混合拟合并经稳健性感知支持集准则筛选。DCASE2024 Task 5 验证集 F-score 62.35%，接近需域级与支持集微调的顶尖系统。

**Few-shot Class-variable Incremental Audio Classification via Prototype Adaptation and Pseudo Class-variable Training**（论文 1024；Guoqing Chen）  
研究类别可增可减的 FCIAC：编码器+分类器，分类器由结构随类别变化的原型适应网络初始化，并设计伪类别可变训练增强适应性。三公开数据集上平均准确率超过既往方法。

**Quality Adaptive Angular Margin Learning for Respiratory Sound Classification**（论文 1213；June-Woo Kim）  
QLung 由谱熵与 RMS 能量导出无参考音频质量裕度，自适应缩放角裕度；对数尺度角裕度稳定严重类别不平衡训练，角分类器在单位超球面上施加裕度。ICBHI 相对交叉熵提升 2.46%，SPRSound 域外相对先前 SOTA 最强。

### 临床声学、公平 MCI 与细粒度 VAD

**CLEAR: Clinical LLM Embedding and Attention-based Reconstruction**（论文 883；Eashita Wazed）  
Whisper 编码器提取语义嵌入，GAT 预测潜掩码隔离心音，潜空间 GAN 细化。10 dB SNR 环境噪声下摘要称峰值 PESQ 4.64、SI-SDR 64.35 dB（自严重退化 PESQ 1.03、SI-SDR −29.37 dB）。

**Fair Cognitive Impairment Detection Through Unlearning**（论文 1353；William Nguyen）  
跨模态融合（语音、文本、图像）+ 梯度反转去学习，抑制共享嵌入编码与任务无关的人口统计属性。在 TAUKADIAL 与 PREPARE 上摘要称优于多语多模态 SOTA，并显著缩小性别与语言子群性能差距。

**QuadVAD: Fine-Grained Speech Detection with a Compact Architecture**（论文 2009；Nivedita Chennupati）  
4 ms 分辨率神经 VAD，约 25 KB，卷积+LSTM；用 MFA 与 TIMIT 微调保证边界精度。摘要称起始检测改善，13 代 Intel Core i7 笔记本上 RTF 0.0014，适合始终在线与对话系统。

### 生物声学、持续发现与主动 AudioLLM

**Exploratory analysis of yellow mongoose vocalization: detection from in-the-wild recordings and call classification**（论文 2168；Sevada Hovsepyan）  
对专家标注幼崽叫声与定向麦野外噪声录音，用手工艺语音音节特征与机器学习做检测/分类。摘要称手工艺特征对动物叫声分类有效；野外检测仍难，目标是辅助标注者标记候选片段。

**Continual Generalized Category Discovery for Acoustic Signals via Instance-Adaptive Regularization and Dynamic Teacher Guidance**（论文 2614；Qisheng Xu）  
面向音频的 C-GCD：实例自适应正则、GMM 自适应阈值与 EMA 动态教师。LibriSpeech 与 ShipsEar 上持续提升新类发现与旧类保持；ShipsEar 累积平均准确率 74.14%，超 Happy 4.84 个百分点。

**I'll Keep an Ear Out: Teaching AudioLLMs Proactive Audio Assistance**（论文 2807；Ritvik Shrivastava）  
提出主动音频协助：AudioLLM 监控流并据自然语言意图自主决定是否提醒用户。ISM 将主动决策嵌入解码的打断/静默特殊令牌。Qwen2-Audio-7B 上 ESC-50 打断 F1 99.6% 与完美去重召回；嘈杂 Epic-Sounds 厨声音频上打断 F1 最高且不过度触发/抑制，流式平均延迟约 3.5 秒。

## 本场要点

- 正交原型投影使少样本 SED 接近需微调的顶尖系统。
- FCIAC 显式处理类别增减的增量音频分类。
- 质量自适应角裕度提升呼吸音分类的域外泛化。
- CLEAR 与公平去学习分别服务心音重建与 MCI 子群公平。
- QuadVAD 以 4 ms/25 KB 服务边缘细粒度 VAD。
- 主动 AudioLLM（ISM）与音频 C-GCD 扩展始终在线与持续发现场景。

## 覆盖核对

| id | title |
|---|---|
| 153 | POP-SED: Prototype Orthogonal Projection for Robust Few-shot Sound Event Detection |
| 883 | CLEAR: Clinical LLM Embedding and Attention-based Reconstruction |
| 1024 | Few-shot Class-variable Incremental Audio Classification via Prototype Adaptation and Pseudo Class-variable Training |
| 1213 | Quality Adaptive Angular Margin Learning for Respiratory Sound Classification |
| 1353 | Fair Cognitive Impairment Detection Through Unlearning |
| 2009 | QuadVAD: Fine-Grained Speech Detection with a Compact Architecture |
| 2168 | Exploratory analysis of yellow mongoose vocalization: detection from in-the-wild recordings and call classification |
| 2614 | Continual Generalized Category Discovery for Acoustic Signals via Instance-Adaptive Regularization and Dynamic Teacher Guidance |
| 2807 | I'll Keep an Ear Out: Teaching AudioLLMs Proactive Audio Assistance |
