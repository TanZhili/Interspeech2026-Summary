# New Architecture and Analyses for ASR and Speech LMs

- 日期：2026年9月30日（星期三）
- 时间：16:30-18:30
- 形式：Poster
- Area：9
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场在 ASR 与语音/文本语言模型交叉处并行推进两类工作：一类改架构或解码范式（动态旋转位置编码、扩散语言模型重打分与联合解码）；另一类做表征与感知分析（词是否独立于音素被编码、可读性是否预测 WER、嵌入中的语言学信息可及性），并延伸到 ASR 转写文本的风格匿名化隐私。

架构侧，CD-RoPE 让旋转时间索引随局部声学上下文连续弯曲，直指离散均匀时间索引与连续语音语义的错位；扩散 LM（MDLM/USDM）进入假设重打分，并与 CTC 帧级分布联合生成候选，体现双向注意力与并行文本生成对识别准确率的增益。

分析侧，通过残差化剔除音素信息后仍可测到后期层的词表征，说明“能分词”不等于“只编码词形”；可读性与 WER 近乎解耦，挑战把文本复杂度当作机器可懂度代理的历史假设；探测显示嵌入对声学—语音学属性线性可及，对形态/句法结构则弱。隐私侧则把 stylometric 指纹风险从书面文本延伸到会议/客服 ASR 转写。

## 技术内容

### 位置编码与扩散语言模型

**Convolutional Dynamic Rotary Positional Encoding**（论文 1312；Euijin Hong）  
RoPE 的离散均匀时间索引与连续语音特征错位。CD-RoPE 用轻量深度可分卷积按局部声学上下文扭曲旋转时间索引，加性调制保留谐波结构。在 Branchformer 上相对 RelPos 于全部 LibriSpeech 测试集一致降 WER，且参数少约 2.2M；SRB 上时域扰动优势最大，验证时间弯曲机制。

**Diffusion Language Models for Speech Recognition**（论文 2070；Davyd Naveriani）  
系统介绍将 MDLM 与 USDM 用于 ASR 假设重打分；并设计 CTC 与 USDM 联合解码：每步融合 CTC 帧级分布与 USDM 标签级分布以生成兼具语言与声学信息的新候选。摘要称 USDM 与 MDLM 均可显著提升识别文本准确率，代码与配方公开。

### 表征分析与人机感知对比

**Do speech foundation models really learn words?**（论文 2676；Robin Huo）  
指出词判别力可能仅来自音素形式编码。用残差化偏出音素信息后，HuBERT 与 wav2vec 2.0 后期层仍以合理保真度编码独立于局部语音内容的词；该简单解耦可增强词发现任务中的高阶语言信息。

**Readability Does Not Predict Speech Recognition Errors: Contrasting Human and Machine Perception.**（论文 2439；Baptiste Ramonda）  
用 CLEAR 语料、合成语音与 babble/混响等声学降质，检验可读性（Global Readability Index）与 WER。结果显示二者近乎完全解耦，在不同声学降质与自然语音上均成立；模型转写无“认知负荷”，已独立于文本复杂度。

**Probing Linguistic Information in Speech Embeddings: A Diagnostic Analysis across Acoustic and Structural Domains**（论文 905；Simon Gonzalez）  
诊断预训练声学嵌入与声学、语音学及语言结构特征的线性关联。嵌入编码声学/语音学属性（时域动态、谱结构、嗓音质量相关）较强，高层语言结构较弱；词汇复杂度可测，形态/句法复杂度线性可及性有限。信息呈分布式、梯度式，对信号实现相关属性最敏感。

### 文本风格隐私

**I Am No One: Style-Aware Paraphrasing for Text Anonymization**（论文 3175；Ahmed Sohair Khan）  
作者归属模型可凭风格指纹再识别“已去标识”文本，风险延伸至会议/客服 ASR 转写。提出风格感知、提示驱动的 LLM 匿名化：用极少样本建紧凑风格画像并改写以压制可识别风格标记、保留语义。博客与评论数据上归属 F1 降 60–70%，内容质量与可读性保持，显著优于 DP 与非 DP 基线。

## 本场要点

- 动态声学条件化的 RoPE 时间索引可改进 Branchformer ASR，尤其抗时域扰动。
- 扩散 LM 适合假设重打分，并可与 CTC 联合解码。
- 基础模型后期层存在相对独立于音素的词编码；可用残差化增强。
- 文本可读性不能预测现代端到端 ASR 的 WER。
- 语音嵌入对声学—语音学线性可读，对句法形态弱。
- ASR 转写仍有 stylometric 泄露；风格感知改写可降归属攻击成功率。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 905 | Probing Linguistic Information in Speech Embeddings: A Diagnostic Analysis across Acoustic and Structural Domains |
| 1312 | Convolutional Dynamic Rotary Positional Encoding |
| 2070 | Diffusion Language Models for Speech Recognition |
| 2439 | Readability Does Not Predict Speech Recognition Errors: Contrasting Human and Machine Perception. |
| 2676 | Do speech foundation models really learn words? |
| 3175 | I Am No One: Style-Aware Paraphrasing for Text Anonymization |
