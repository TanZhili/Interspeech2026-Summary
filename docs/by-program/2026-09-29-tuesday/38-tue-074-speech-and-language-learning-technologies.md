# Speech and Language Learning Technologies

- 日期：Tuesday 29 September 2026
- 时间：14:00-16:00
- 形式：Show And Tell
- Area：
- 论文数：9

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本 Show & Tell 场展示面向二语/手语/临床与编程教育的可运行系统。多套工具围绕音高可视化与实时反馈（Amadea、CARFAC/SAI pitchogram），把声调/音高重音学习从抽象规则转为可对齐轮廓比较。

另一类系统整合听说训练作者环境、流利度自适应对话、角色化日语口语练习，以及儿童言语治疗游戏化与音素/音系属性分析。手语应用 lisero 与印地语等母语语音编程助手 CodeVaani，把“学习技术”扩展出口语中心之外。

共同趋势是：即时反馈、自适应难度与教师/治疗师可配置流水线；演示强调端到端工作流而非单一模型分数。

## 论文技术总结

# Amadea: An AI Companion for Pitch-Aware Spoken Language Practice

- 论文编号：3570
- 报告人：Mrigendra Agrawal
- 程序：Tuesday 29 September 2026 / Speech and Language Learning Technologies
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/agrawal26_interspeech.pdf

## 问题
日语音高重音、普通话声调等对音高敏感语言，现有 CAPT 多固定 prompt 与机械重复，难在自由对话中给韵律反馈。

## 方法
Amadea：课堂模式预写短语 + 对话模式与 AI 同伴闲聊。Whisper 转写推断意图 → gpt-4o-mini-tts 生成母语式参考 → pYIN 提 F0 → 强度轮廓 DTW 对齐 → z 归一化后以 100/(1+d) 得 pitch-pattern score，并可视化分歧。反馈按整句而非单 mora。

## 实验与结果
系统演示文，尚无与专家评分相关或纵向学习增益的定量结果；作者列局限为 ASR 错、F0 噪声、对齐失败及单一参考轨迹。

## 结论
把韵律反馈嵌进结构化与开放对话，使学习者可对自选短语练习音高。

## 点评
设计抓点准（自由对话也能出参考），工程闭环清晰；当前缺外部效度验证，参考单一也可能误罚可接受变体。


# Real-Time CARFAC/SAI-derived Pitchogram for Seeing and Correcting Pronunciation in Mandarin Chinese Tones

- 论文编号：3575
- 报告人：Yuka Maruyama
- 程序：Tuesday 29 September 2026 / Speech and Language Learning Technologies
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/maruyama26_interspeech.pdf

## 问题
普通话四声学习中，传统频谱图时间细结构变化快，初学者难实时解读；需更稳定的音高可视化 CAPT。

## 方法
用 Google CARFAC/SAI 生成 pitchogram。感知原型：听参考+看图选调；产出原型：双屏实时自语音图 vs Google TTS 参考图对照。16 kHz、约 28 ms 帧；默认 22 个 HSK1–2 词，可手动扩词表。Windows 命令行、单键切换，无需校准。

## 实验与结果
演示系统，无正式用户学习效果统计；作者主张 pitchogram 有助直观感知与纠正四声。

## 结论
CARFAC/SAI pitchogram 可作为声调 CAPT 的可行可视化组件；未来可自动扩词表与加文本反馈，并扩展到其他声调语言。

## 点评
替代 mel 谱做实时对照，思路直观、门槛低；尚缺对照实验证明优于频谱图，词汇规模也偏小。


# AURORA: A Web-based Authoring System for Bridging Aural-Oral Language Training and Communicative Practice

- 论文编号：3581
- 报告人：Nobuaki Minematsu
- 程序：Tuesday 29 September 2026 / Speech and Language Learning Technologies
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/minematsu26_interspeech.pdf

## 问题
教师难自建 CALL；EMI 过渡需要可组合的听–说–交际训练与自动反馈。

## 方法
AURORA 网页创作系统：听辨侧影子跟读/延迟复述等，用 DTW 算 listening disfluency（LD）并相对全班均值可视化；口语侧重叠跟读，展示时长、音节凸显、音高与 ASR 词级分（对照全班均值区分机器/发音错误）；交际侧用 ChatGPT 语音模式做猜词、故事回忆、测谎、话题讨论、TED 访谈等任务，事后按 ASR 转写评估并给易混音素对。支持声转换生成百余声学变体。用其部署 STEAC 两个月课程（约每日 30 分钟）。

## 实验与结果
2025 年暑/春共 832 人注册；暑期前后测 LD、PD 显著下降，开放问卷总体正面（摘要链接）。2026 年 2 月办教师教程工作坊。

## 结论
教师可授权式搭建听口语料与交际任务，并把客观 LD/PD 与 GPT 评估接到同一平台，支撑 EMI 过渡训练。

## 点评
工程与教学双视角的创作器，场景完整。强在可视化反馈与规模部署；弱在论文定量细节偏少、交际评估依赖 ASR 转写质量。


# VoxKit: Desktop Phone Alignment and Goodness of Pronunciation Analysis

- 论文编号：3591
- 报告人：Nina R Benway
- 程序：Tuesday 29 September 2026 / Speech and Language Learning Technologies
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/benway26_interspeech.pdf

## 问题
临床语音研究需强制对齐后再做发音优良度（GOP），但桌面端缺少一体化流水线，命令行门槛阻碍采用。

## 方法
VoxKit（Python/PyQt6 可执行包）：注册说话人目录语料（.lab/.TextGrid），可选训/适配对齐器——Montreal Forced Aligner 或 Wav2TextGrid（wav2vec2）；生成、查看、比较对齐（重叠率、替换模式）；再以 LibriSpeech 预训练 wav2vec2 在 42 音素上算帧级后验，对数后验作 Acoustic Goodness，导出帧级与聚合 CSV。模块可扩展（stacker/engine/analyzer）。

## 实验与结果
软件演示/系统描述，无新算法榜单；面向儿童与临床群体下游分析。

## 结论
提供从原始音频到对齐再到 GOP 的桌面一体化工具，降低临床研究者门槛。

## 点评
缺口真实、工程抽象清楚；评分骨干来自成人 LibriSpeech，儿童/病理语音适应性需用户自行验证。


# AdaptLingo: A Speech-to-Speech English Practice System with Fluency-Adaptive Responses

- 论文编号：3594
- 报告人：Zackary Rackauckas
- 程序：Tuesday 29 September 2026 / Speech and Language Learning Technologies
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rackauckas26_interspeech.pdf

## 问题
静态英语口语练习对初学过难、对高阶过简；需按流利度调节词汇与语速。

## 方法
AdaptLingo：Praat 提发音率/语速 → 随机森林分初/中/高；CrisperWhisper 转写；按 EIKEN 词表检索并 logit 加权约束生成；gpt-4o-mini-tts 语速 0.8×/0.9×/1.0×。Gradio+FastAPI，含毒性过滤与学习日志。

## 实验与结果
标注集宏 F1 95%，用户研究噪声语音准确率仅 47%。被试内对比：日语母语者 19 项中 15 项偏爱 AdaptLingo；普通话与西班牙语母语者更多偏爱非自适应基线，但认可其“把我当英语学习者”。

## 结论
流利度自适应口语练习可行但非万能；需按母语背景与对话目标个性化。

## 点评
三件套（分类–词表–语速）演示完整；野外流利度估计是短板，且自适应有时牺牲自然度。


# lisero: An interactive practice app for learning Romanian Sign Language

- 论文编号：3595
- 报告人：Anisia Popescu
- 程序：Tuesday 29 September 2026 / Speech and Language Learning Technologies
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/popescu26_interspeech.pdf

## 问题
罗马尼亚手语（LSR）2020 年获官方承认，但教育资源匮乏（认证译员仅约 77 人）；现有工具偏词典、缺结构化练习。

## 方法
免费移动应用 lisero（iOS/Android）：两名聋人母语者视频循环交替；约 1000 词词典；家长/通用两套课程，情景章节；练习含多选（语义/音系竞争）、视频–词匹配、组句；半速播放、前置摄像头镜像、收藏分享与积分/连续天数等游戏化。跨学科团队含聋人签名者与认证教师。

## 实验与结果
系统介绍，无大规模学习效果实验；面向听障婴幼儿照护者与一般学习者。

## 结论
为 LSR 提供可扩展的结构化互动练习，填补词典型资源空白；后续扩内容与他手语。

## 点评
资源建设导向明确、社区参与充分；尚缺成效评估与语法教学深度（相对纯词汇+短句）。


# SayCheck: Gamified Speech Practice and Attribute-Based Speech Analysis for Children

- 论文编号：3598
- 报告人：Mostafa Shahin
- 程序：Tuesday 29 September 2026 / Speech and Language Learning Technologies
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shahin26_interspeech.pdf

## 问题
儿童言语治疗需反复家庭练习，动机难维持；传统音素级误读检测难说明“错在哪些发音特征”。

## 方法
SayCheck = Say Bananas（马里奥式横版游戏，收星触发目标词录音）+ PhoneAid。治疗师可按音素/位置/词长配置目标。PhoneAid：澳大利亚儿童语料训的 wav2vec2 + 音系属性层，SCTC-SB 多标签序列预测；对齐后同时报音素替换/增删与属性（嗓音、鼻音、部位、元音高低前后等），汇总 PCC/PVC 与属性准确率。

## 实验与结果
演示工作流；强调属性级比纯对错更利于临床解读。正文未给新的大规模临床疗效数字。

## 结论
游戏化诱发与属性级分析可结合，支持可扩展儿童家庭言语练习与诊断反馈。

## 点评
产品闭环完整，属性分解贴临床；演示文性质，外部效度与儿童模型误差率待更多报告。


# A Speech-First Character Interface for Stylized Japanese Dialogue Practice

- 论文编号：3599
- 报告人：Zackary Rackauckas
- 程序：Tuesday 29 September 2026 / Speech and Language Learning Technologies
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rackauckas26b_interspeech.pdf

## 问题
日语练习需同时体验文字、发音、语体与句末助词；多数中性导师聊天把语音当附加，难感受角色语体差异。

## 方法
Jouzu 移动演示：选虚构角色 → 打字或说话 → 人设条件 LLM 生成日语 → Style-BERT-VITS2（专业演员微调）合成角色声；多角色同 prompt 对比；点击词显示假名/罗马字/英义。框定角色语为表达性练习，非正式场合万能模板。用户研究结果另文。

## 实验与结果
演示系统；引用 Style-BERT-VITS2 JP Extra 与母语真值平均无显著差异的先前评测。本文不重复学习成效数字。

## 结论
以语音为主通道展示人设、情感与语体对比，并嵌入轻量词汇支架，形成可展台运行的日语口语练习环。

## 点评
“同句多角色听差”教学设计清楚；依赖角色语，需防学习者误用到正式场景（作者已声明）。


# CodeVaani: A Multilingual, Voice-Based Code Learning Assistant

- 论文编号：3608
- 报告人：Jayant Havare
- 程序：Tuesday 29 September 2026 / Speech and Language Learning Technologies
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/havare26_interspeech.pdf

## 问题
印度等非英语语境编程教育默认英语与文本交互；口语编程问句语码混合、术语 OOV，标准 ASR 易错，下游代码助手失效。

## 方法
接入 IITB LMS 的 CodeVaani：Indic-Conformer（Indic）/Whisper（英语）→ Gemma-27B（DPO）做代码感知转写修正（如 ask key→ASCII）→ Codestral-22B 同语种答疑；React/Django + 双 H100。

## 实验与结果
28 名初学者：>89% 评 fair 及以上，26 人中 25 愿采用。500 条真人问句：相对 Saaras V3，各语 WER 大幅下降（如 Gujarati 45.3%→8.1%，English 70.5%→12.4%）。相对 Whisper/Qwen3-Omni/Phi-4，框架 WER/PER/WFED 最低（例 WER 8.1%）。

## 结论
语音优先、多语代码助手可降低英语门槛；转写精炼是关键。后续多轮对话与端到端低延迟。

## 点评
对准“代码混合 ASR + 纠错”真实痛点，评测扎实；规模仍偏小、多轮与延迟未解决。

