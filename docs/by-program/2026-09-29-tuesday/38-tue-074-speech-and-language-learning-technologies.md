# Speech and Language Learning Technologies

- 日期：Tuesday 29 September 2026；时间：14:00-16:00；形式：Show And Tell；论文数：9
- 材料：官方程序摘要。仅依据摘要归纳，不补写摘要未给出的数字或机制。

## 技术趋势

本 Show & Tell 场展示面向二语/手语/临床与编程教育的可运行系统。多套工具围绕音高可视化与实时反馈（Amadea、CARFAC/SAI pitchogram），把声调/音高重音学习从抽象规则转为可对齐轮廓比较。

另一类系统整合听说训练作者环境、流利度自适应对话、角色化日语口语练习，以及儿童言语治疗游戏化与音素/音系属性分析。手语应用 lisero 与印地语等母语语音编程助手 CodeVaani，把“学习技术”扩展出口语中心之外。

共同趋势是：即时反馈、自适应难度与教师/治疗师可配置流水线；演示强调端到端工作流而非单一模型分数。

## 技术内容

### 音高/声调可视化与听说训练平台

**Amadea: An AI Companion for Pitch-Aware Spoken Language Practice**（论文 3570；Mrigendra Agrawal）面向日语音高重音与普通话等声调语言：转写学习者语音、生成母语参考音频，对齐后比较归一化 F0 轮廓给音高模式分，并可视化分歧；支持结构化课程与开放对话。

**Real-Time CARFAC/SAI-derived Pitchogram for Seeing and Correcting Pronunciation in Mandarin Chinese Tones**（论文 3575；Yuka Maruyama）用 CARFAC/SAI 派生 pitchogram 替代常规谱图，双屏实时对照 Google TTS 参考，帮助 L2 学习者感知并产出普通话四声。

**AURORA: A Web-based Authoring System for Bridging Aural-Oral Language Training and Communicative Practice**（论文 3581；Nobuaki Minematsu）支持影子跟读等听训（听解不流畅 LD）、模仿重叠等口训（发音偏差 PD），以及与 ChatGPT 的任务型口语与提示评估；提供约两月课程与教师工作坊。

**AdaptLingo: A Speech-to-Speech English Practice System with Fluency-Adaptive Responses**（论文 3594；Zackary Rackauckas）开源语音到语音英语练习：由时域声学特征预测流利度，约束 EIKEN 对齐词表并调节 TTS 语速。初评显示标注数据上流利分类尚可，噪声用户语音仍难。

### 临床工具、手语、儿童与专业学习

**VoxKit: Desktop Phone Alignment and Goodness of Pronunciation Analysis**（论文 3591；Nina R Benway）桌面工作台整合强制对齐与发音优良度分析，服务临床人群研究者：注册数据、训练/比较对齐引擎并计算音素级 GOP。

**lisero: An interactive practice app for learning Romanian Sign Language**（论文 3595；Anisia Popescu）免费移动应用，课程、练习与增长中的手势词典，含游戏化与分享；面向听人及聋人/听障学习者，并支持双模态双语情境。

**SayCheck: Gamified Speech Practice and Attribute-Based Speech Analysis for Children**（论文 3598；Mostafa Shahin）整合 Mario 风格游戏 Say Bananas 与 PhoneAid 自动分析（音素与音系/发音属性级），供治疗师与照护者配置练习并获诊断式反馈。

**A Speech-First Character Interface for Stylized Japanese Dialogue Practice**（论文 3599；Zackary Rackauckas）Jouzu：选择虚构角色，经 Style-BERT-VITS2 听角色化回应，比较多人格措辞/语域/语音，并点词获读音支持。

**CodeVaani: A Multilingual, Voice-Based Code Learning Assistant**（论文 3608；Jayant Havare）嵌入 IIT Bombay LMS：Indic ASR、代码感知转写精炼与代码模型，文/音双模回答。28 名初学者中逾 89% 评分公平及以上。

## 本场要点

- 音高轮廓对齐与 pitchogram 可视化是声调/音高重音 CAPT 的核心交互。
- AURORA、AdaptLingo、Jouzu 分别覆盖作者课程、流利度自适应与角色化口语。
- VoxKit / SayCheck 把对齐—GOP—属性分析接到临床与儿童家练场景。
- lisero 与 CodeVaani 把学习技术扩展到手语与母语语音编程教育。
- 本场重点是可演示闭环：输入语音 → 反馈/自适应 → 教师或学习者可操作界面。

## 覆盖核对

| id | title |
|---|---|
| 3570 | Amadea: An AI Companion for Pitch-Aware Spoken Language Practice |
| 3575 | Real-Time CARFAC/SAI-derived Pitchogram for Seeing and Correcting Pronunciation in Mandarin Chinese Tones |
| 3581 | AURORA: A Web-based Authoring System for Bridging Aural-Oral Language Training and Communicative Practice |
| 3591 | VoxKit: Desktop Phone Alignment and Goodness of Pronunciation Analysis |
| 3594 | AdaptLingo: A Speech-to-Speech English Practice System with Fluency-Adaptive Responses |
| 3595 | lisero: An interactive practice app for learning Romanian Sign Language |
| 3598 | SayCheck: Gamified Speech Practice and Attribute-Based Speech Analysis for Children |
| 3599 | A Speech-First Character Interface for Stylized Japanese Dialogue Practice |
| 3608 | CodeVaani: A Multilingual, Voice-Based Code Learning Assistant |
