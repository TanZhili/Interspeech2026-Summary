# Scaling and Zero-Shot Speech Synthesis

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Oral（Area 7）
- 论文数：6
- 材料：官方程序中该场全部论文摘要。摘要写明问题、方法与主要结论；未在摘要中出现的数字与细节不写入。

## 技术趋势

本场聚焦零样本与大规模 TTS：一方面用扩散语言模型式离散 NAR 架构把文本直接映射到多码本声学 token（OmniVoice，覆盖 600+ 语言、581k 小时开源数据）；另一方面用 ElasticDLM 通过长度缩放训练与置信度引导推理摆脱对精确时长预测的强依赖。

效率与适配是第二主线。WAND 把预训练 AR-TTS 改为全局条件注意力 + 局部滑动窗，并以课程收紧窗口与知识蒸馏保持音质，降低 KV cache。VoiceTTA 在推理时用强化学习（GRPO）与 F0/能量风格奖励、说话人相似度与 Whisper WER 做 test-time adaptation，专攻相声、方言等少见风格提示。

数据稀缺个性化方面，ZeSTA 用域嵌入区分真实与零样本合成增强数据并过采样真实数据；DSC-TTS 则在说话人嵌入空间与脸—声对齐共享身份空间双重约束，缓解模块化脸部驱动零样本 TTS 的身份漂移。瓶颈从“会说”转向时长柔性、超多语覆盖、长序列算力、少见风格模仿与跨模态身份稳定。

## 技术内容

### 可变长度与超多语零样本合成

**Learning to Rescale: On-the-Fly Sequence Length Adaptation in Non-Autoregressive Speech Synthesis**（论文 1069；Jiawei Jin）
指出 NAR TTS 依赖准确字符级或全局时长预测是瓶颈。提出 ElasticDLM：引入两个功能 token，配合 Differentiated Length-Scaling Training Scheme（DLTS）与 Hierarchical Confidence-Guided Inference（HCGI），使模型学习长度缩放并在推理中自动调整序列长度，从而从任意长度输入生成高保真自然语音。

**OmniVoice: Towards Omnilingual Zero-Shot Text-to-Speech with Diffusion Language Models**（论文 3256；Han Zhu）
OmniVoice 为面向 600+ 语言的大规模多语零样本 TTS，核心是扩散语言模型式离散 NAR，直接映射文本到多码本声学 token。关键技术包括 full-codebook random masking 与从预训练 LLM 初始化以保障可懂度；基于 581k 小时开源多语数据，摘要称在中英及多语基准上达到当时最广语言覆盖与先进性能，并公开代码与模型。

### 高效 AR 推理与测试时风格适配

**WAND: Windowed Attention and Knowledge Distillation for Efficient Autoregressive Text-to-Speech Models**（论文 943；Hanna Lee）
针对 decoder-only AR-TTS 全注意力二次复杂度，提出 WAND：条件 token 保持持久全局注意力，生成 token 用局部滑动窗；课程式逐步收紧窗口，并以全注意力教师知识蒸馏恢复音质。在三个现代 AR-TTS 模型上保持原质量，最高降低 66.2% KV cache，并实现近恒定逐步延迟。

**VoiceTTA: Enhancing Zero-Shot Text-to-Speech via Reinforcement Learning-Based Test-Time Adaptation**（论文 1757；Li Liu）
针对零样本 TTS 难以模仿相声、方言等少见风格，且微调需大量高质量数据，提出 VoiceTTA：在 flow matching 模型推理时用 GRPO 优化可学习 prefix，奖励含 F0/能量变异系数差风格项、说话人相似度与 Whisper WER。实验称在非常见语音提示上相对先进基线有实质提升。

### 合成数据增强与脸部驱动身份约束

**ZeSTA: Zero-Shot TTS Augmentation with Domain-Conditioned Training for Data-Efficient Personalized Speech Synthesis**（论文 1269；Youngwon Choi）
研究用 ZS-TTS 合成数据增强低资源个性化合成，但朴素混合常损害说话人相似度。ZeSTA 以轻量域嵌入区分真实/合成语音，并过采样真实数据稳定适配，不改基座架构。在 LibriTTS 与内部数据集、两种 ZS-TTS 源上，相对朴素增强提升说话人相似度并保持可懂度与感知质量。

**Dual-Space Constrained Face-Based Zero-Shot Text-to-Speech Synthesis**（论文 409；Ju Zhang）
针对模块化脸部驱动零样本 TTS 在训练用语音嵌入、推理才引入脸部表示导致身份漂移，提出 DSC-TTS：在说话人嵌入空间与脸—声对齐共享身份空间双重约束声学模型训练。实验称相对现有脸部 TTS 有更高说话人相似度与更强身份一致性。

## 本场要点

- 离散扩散式 NAR（OmniVoice）与弹性长度 NAR（ElasticDLM）正在削弱对两阶段语义管道或精确时长的依赖。
- 超多语零样本覆盖已推进到数百语言与数十万小时开源数据规模。
- AR-TTS 效率重点转向窗口注意力 + 蒸馏，以恒定复杂度换长序列可行性。
- 少见风格模仿可用推理时 RL 适配（VoiceTTA），避免大规模微调。
- 合成数据增强需显式域条件化，否则易损说话人相似度。
- 脸部驱动 TTS 需在训练期做双空间身份约束，而非仅推理期替换嵌入。

## 覆盖核对

- 1069 | Learning to Rescale: On-the-Fly Sequence Length Adaptation in Non-Autoregressive Speech Synthesis
- 3256 | OmniVoice: Towards Omnilingual Zero-Shot Text-to-Speech with Diffusion Language Models
- 943 | WAND: Windowed Attention and Knowledge Distillation for Efficient Autoregressive Text-to-Speech Models
- 1757 | VoiceTTA: Enhancing Zero-Shot Text-to-Speech via Reinforcement Learning-Based Test-Time Adaptation
- 1269 | ZeSTA: Zero-Shot TTS Augmentation with Domain-Conditioned Training for Data-Efficient Personalized Speech Synthesis
- 409 | Dual-Space Constrained Face-Based Zero-Shot Text-to-Speech Synthesis
