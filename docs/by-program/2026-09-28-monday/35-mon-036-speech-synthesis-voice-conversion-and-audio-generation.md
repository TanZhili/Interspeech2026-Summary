# Speech Synthesis, Voice Conversion and Audio Generation

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Show And Tell
- Area：
- 论文数：8

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

Show & Tell 场以可交互演示为主，覆盖听端流式语音转换、视觉锚定的可编辑视频到音频、漫画有声化、机械可编程语音合成、词级嗓音质量编辑、TTS 指纹溯源、低资源民族语言 TTS 工具与评测，以及可扩展房间声学场景生成。共同特点是把研究能力做成可切换、可拖拽、可批量生成的工作流，而不是只报告离线分数。

鲁棒性与可控性是两条并行线索。Coco-VC 面向电话退化在听端做实时转换；VoiceQualityGUI 把 creakiness / breathiness / nasality 控到词级以探索语用含义；VisionSFX 则把“每源可编辑 + 双耳空间化”作为影视/游戏/AR 需求，走训练无关管线以避免成对双耳数据依赖。

低资源与可信生成同样突出：EveryVoice 与评测设计服务听者稀缺场景；DsNA 把密码学签名分片嵌入 TTS 音频以做内在溯源且号称无明显 SNR 下降；Treble SDK 用轻量 recipe 延迟渲染，支持手工与批量随机场景。机械声道模型则提醒：可编程合成不必依赖计算机。

摘要对客观/主观结果多点到为止（如电话退化下仍高质量、约一分钟生成时间线、MOS 或 SNR 无可见劣化），细节以各条自述为限。

## 论文技术总结

# Coco-VC: Degradation-Robust Streaming Voice Conversion System on the Listener Side

- 论文编号：3571
- 报告人：Ryo Kato
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kato26_interspeech.pdf

## 问题
电话场景中说话人难以知晓己方音色/信道/噪声导致听感差；传统 VC 多在说话人侧且假设较干净输入。需要听者侧、流式、对电话降质鲁棒的实时转换。

## 方法
Coco-VC：因果 ConvNeXt 学生内容编码器（零前瞻、20 ms 帧，重叠相加后算法延迟 40 ms）+ 轻量 Vocos 解码器。多教师蒸馏融合 ContentVec（说话人不变韵律）与 Whisper 编码器（语言内容）。非对称训练：教师看干净 16 kHz，学生看经编解码、失真、混响、噪声等管线破坏的 8 kHz，预测干净融合特征。演示在消费级笔记本上运行（如 M2 约 80 ms 端到端），GUI 可开关 VC 与切换目标说话人。

## 实验与结果
与同解码器的 StreamVC 比：FLEURS-8k 上 WER 0.338 vs 0.451（UT-MOS 略低 3.214 vs 3.271）；VCTK 上 UT-MOS 4.041 vs 3.701。私有投诉电话仿真：61840 h 域内数据 vs 960 h 公开数据，WER 0.125 vs 0.363，UT-MOS 3.35 vs 3.08。

## 结论
电话增强 + 多教师蒸馏可得到降质不变表示，使听者侧流式 VC 在标准硬件上可用，并改善严重电话条件下的可懂度。

## 点评
把场景从“说话人美化自己”翻转到“听者侧补救”，工程闭环（延迟、GUI、域内数据）完整。核心是非对称蒸馏当联合增强器；局限是私有数据不可复现，且噪声极端时 MOS 未必优于基线，需在可懂度与自然度间权衡。


# Listening to Motion in Space: Vision-Grounded Event-wise Video-to-Audio Generation and Rendering

- 论文编号：3574
- 报告人：Dayeon Ku
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/park26m_interspeech.pdf

## 问题
常规 V2A 输出单一单声道混音，难做按源编辑与空间控制；端到端双耳系统又依赖大规模视频–双耳配对数据。影视/游戏/AR 需要可分轨、可空间化的工作流。

## 方法
训练免费流水线 VisionSFX：Gemma 4-VL 将场景拆为事件列表（起止时间、听感提示、片段）并给环境提示；每事件用 MMAudio 在约 5 s 裁剪窗内独立生成，边界 raised-cosine 淡入淡出；环境音改用视频无关的 TangoFlux，避免混入事件声。定位：Farnebäck 光流去自运动后取质心，Depth Anything 3 给相对深度，再经 HRTF 渲染；环境声 Hilbert 解相关成立体声。演示约 1 分钟完成 10 s 片段分轨时间线，支持改提示、时间线注入、方位/仰角/深度实时重渲染。

## 实验与结果
本文为演示系统描述，未报告定量客观/主观分数；强调单源重生成不影响其他轨、空间重定位无需再生成音频。

## 结论
组合现成 VLM/V2A/深度与经典光流+HRTF，可不训练、无双耳配对地得到可编辑、深度感知的双耳 V2A 工作流。

## 点评
价值在组合式后期友好管线，而非新生成模型。事件分解质量依赖 VLM，光流质心对遮挡/多目标可能漂移；缺少听感评测，空间真实感与时间对齐精度仍待验证。


# Automatic generation of audio comic from manga images

- 论文编号：3577
- 报告人：Sota Koshino
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/koshino26_interspeech.pdf

## 问题
有声漫画需为角色配适合剧情的表情语音，人工成本高；希望从漫画页图像（半）自动生成对应朗读/演技语音，兼顾制作降本与视障可及。

## 方法
流水线：检测分镜/文字/角色 → OCR → 阅读顺序 → 人脸与预存姓名–人脸库匹配并关联说话人，产出 XML；VLM（GPT-5.2）据文本上下文、脸与分镜图预测八类情绪，组成 “角色名's voice is Emotion with very clear audio” 提示；ParlerTTS 在约 9 小时 MangaVox 日语有声漫画数据上微调后按行合成。检测理解对比 Magiv2+Yomitoku（v1）与 Magiv3+MangaOCR（v2）。

## 实验与结果
约 700 页/8 部 Manga109+MangaVox 测试：v2 在面板/文本/角色检测、身份、说话人关联、TOER、CER 全面优于 v1，故采用 v2。主观：150 人、五分制整体印象；GT 真人约 4.0，v2+TTS 与 manual+TTS 均约 2.5，自动与半自动接近，但仍低于真人。

## 结论
自动检测–理解–提示 TTS 可生成一定质量的有声漫画，瓶颈更在 TTS 表现力而非理解流水线。未来改进提示设计与角色音色合成。

## 点评
把漫画理解与风格化 TTS 串成可演示闭环，客观任务齐全。主观上自动≈人工校正说明前端够用，差距主要在演技合成；情绪仅八类离散标签、依赖角色脸库，跨风格/无脸分镜时可能脆弱。


# Programmable Speech Synthesis without Computers

- 论文编号：3578
- 报告人：Takayuki Arai
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/arai26b_interspeech.pdf

## 问题
机械声道模型（VTM-UT 系列）可用滑块改变构型，但固定凸轮只对应单一短语；不用电脑/执行器时如何“可编程”地合成多短语动态语音。

## 方法
在 VTM-UT30-D6/D9（六块自下插入的构音滑块，D9 含鼻腔支路）上，用线性凸轮与旋转凸轮两种机构抬升滑块。可编程化：底板/基轴插入可互换异形板片（直角三角形/矩形/梯形等，或对应的斜坡/环扇），拼出任意凸轮轮廓；板片可拆装以换短语。目标高度以主声道高度 20 mm 为上限。

## 实验与结果
用两类凸轮合成同一英语短语 “I love you”；给出归一化时间上的六凸轮位移轨迹与频谱图，两侧共振峰轨迹大体相似。

## 结论
无需计算机即可用可编程机械凸轮驱动声道模型合成短语；线性与旋转方案输出相近。若有 Articulatory Phonology 轨迹，可扩展到任意短语；未来需更系统的轨迹设计。

## 点评
演示向工作，强调物理可解释的动态声道控制与“可插拔编程”。科学贡献在机构可复用性，而非语音质量评测；单短语、无听感/可懂度指标，与数字合成路线互补但规模扩展依赖手工轨迹设计。


# VoiceQualityGUI: A Tool for Word-Level Voice Quality Modifications

- 论文编号：3579
- 报告人：Harm Lameris
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lameris26b_interspeech.pdf

## 问题
嗓音质量（吱嘎、气声、鼻化等）对语用功能重要，但研究工具少；既往用 VoiceQualityVC 需手写各时段属性，难快速试探词级局部调制假设。

## 方法
Streamlit GUI：先对原音频做零偏移 VC 作基线，再调全局音高/音高变化以贴合原句，然后按词选择并滑动调节 creakiness、breathiness、nasality。后端为改进的 VoiceQualityVC：在 FreeVC 上为 HNR35、CPPS、H1–H2、H1–A3 各加仿射编码器，45k 迭代微调；用户侧暴露为三种感知组合。训练用 Expressive Speech 英语子集约 17h20m（prosody score≤0.78），帧级声门特征与句级音高 z 标准化。输入需源音频、≥30 s 目标说话人音频与时间对齐转写。保存修改音频与对齐调节记录。

## 实验与结果
本文为工具/演示论文，未报告独立听感或语用实验数字；动机来自先前游戏配音后编辑中手工改参的成功与繁琐。

## 结论
提供首个支持词级嗓音质量对照刺激制作的工具，便于假设形成与筛选，并期望推动更可控、意图驱动的合成。

## 点评
把可控 VC 接到研究友好工作流，切中“局部语用–嗓音质量”实验痛点。鼻化与所选声门特征关联较弱属已知近似；效果依赖对齐转写与目标说话人样本，跨语种/极端音质外推未验证。


# DsNA(Digital sigNature for Audios): A Unique Method to Fingerprint Audio Files Generated by Text to Speech

- 论文编号：3590
- 报告人：Vishal Gourav
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gourav26_interspeech.pdf

## 问题
高质量 TTS 加剧合成语音溯源与滥用风险；传统音频指纹偏内容检索，难把可验证出处嵌进生成语音本身，且不宜改 TTS 内部结构。

## 方法
后处理框架 DsNA：TTS 波形与元数据经哈希/数字签名（启发自 RSA）生成紧凑签名，切成三片；音频切成两等份，与签名分片交错拼成“自带指纹”文件。验证走反向流水线抽取分片校验。不改声学模型或声码器。

## 实验与结果
250 条 TTS 样本：指纹前后 SNR 均为 45.2 dB；MOS 4.51→4.48；CER 1.8%、WER 2.6% 不变。作者称无可观测保真度损失。

## 结论
交错嵌入可使合成语音自含可验证出处且保持质量。仍需检验压缩/噪声/对抗篡改鲁棒性与更强安全保证。

## 点评
思路是容器级交错签名而非感知水印，实现轻、对波形改动理论上可逆抽取。当前评测几乎无失真可能因嵌入对听感影响极小或指标粗；对重编码、剪切、重采样等常见变换是否仍可验证，正文未给出证据，安全声明需谨慎。


# Two Lessons Learned from the SGILE project: Efficient Building and Evaluation of TTS Voices

- 论文编号：3596
- 报告人：Korin Richmond
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pine26_interspeech.pdf

## 问题
绝大多数语言属低资源，难以按高资源范式用海量数据与大模型建 TTS；听者稀缺时传统 MOS 评测代价高。SGILE 项目需同时解决高效建声与高效评测。

## 方法
展示开源 EveryVoice TTS Toolkit：面向有限算力与少量音频（常仅数小时）从零建高质量音色，带向导降低非专家门槛。评测侧推广 Best-Worst Scaling（BWS）等相对选择范式，对比 AB：四刺激选最好/最差可等价约五对成对判断。演示为网页听测：盲评样本后揭示所用音色与数据量，并与其他用户跨语言偏好对照。

## 实验与结果
本文为 Show & Tell，不报告新的定量 TTS 分数；强调演示样本覆盖不同数据量与多语言，并引用项目前期工作称 BWS 更高效稳健。

## 结论
低资源 TTS 可用适度数据与工具链实现；BWS 等范式可在听者稀缺时提高评测信息量。后续 Own Your Voice 项目将把 EveryVoice 部署到强调数据主权的云环境。

## 点评
价值在社区工具与评测方法论的可体验展示，而非新声学模型。强项是把“少数据可建声”与“少听者可评测”绑在同一交互界面；局限是本文本身缺少对照实验数字，说服力依赖现场听感与已发表配套论文。


# Scalable Audio Scene Generation with the Treble SDK

- 论文编号：3609
- 报告人：Georg Götz
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gotz26b_interspeech.pdf

## 问题
真实共享空间录音难控、难扩展；仅有孤立 RIR 不足以支撑增强/分离等需要混音、目标轨、标签与背景噪声的任务。需要把声学仿真资产变成可复现、可规模化的完整场景数据集。

## 方法
Treble SDK Scene Generator：输入 RIR 集合、干净音频与场景/设备规则。场景以轻量 recipe 表示（轨道、源–IR 映射、听者配置、元数据、目标定义），卷积与混音仅按需渲染（lazy）。支持手工搭场景与规则驱动批量随机化（位置、说话人、重叠、电平、朝向、噪声等）。演示用 Jupyter：多说话人对话 + HVAC 噪声、时间线与 3D 房间视图、渲染混音/分轨/转录/JSON 元数据，再批量生成 SceneCollection。

## 实验与结果
演示系统描述，无独立下游 ASR/分离基准数字；强调 recipe 可序列化、共享、过滤与对齐监督信号。

## 结论
把物理接地仿真接到 ML 友好的场景配方与按需渲染，填补 RIR/干净音频与训练脚本之间的工程缺口，便于共享环境语音系统的数据生成与评估。

## 点评
贡献是工作流与数据工程抽象，而非新仿真算法。lazy recipe 对大规模数据集生成实用；可复现性依赖 SDK/仿真引擎与规则设计，本文未给出与真实录音下游性能的直接对比。

