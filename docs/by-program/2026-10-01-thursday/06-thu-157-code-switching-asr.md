# Code-Switching ASR

- 日期：2026年10月1日（星期四）
- 时间：09:00-11:00
- 形式：Oral
- Area：9
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场专攻语码转换（CS）ASR：LLM 引导热词偏置、合成语音的语码混合保真、数据高效 RL 适配 Audio LLM、DPO 纠正转录失败模式、贝叶斯因子化适配保护单语能力，以及低资源黏着语流式 CS。核心矛盾是语言边界快速切换、真实 CS 数据稀缺，以及适配常损害强多语基线。

合成与偏好学习成为主路径：用 Code Mixing Index 偏好优化 TTS、用可验证奖励 RL（错误率 + 文字系统保真）与 DPO 偏好对纠正省略/翻译/幻觉。部署侧强调把切换知识高效注入预训练模型（MoE 适配器、贝叶斯因子化），并在黏着语场景用动态块在线与形态感知指标处理后缀跨边界问题。

## 技术内容

### LLM 偏置、合成与 RL/DPO 对齐

**LLM-HB: Language-Aware LLM-Guided Hotword Biasing for Code-Switching ASR**（论文 1113；Yuxuan He）  
提出语言感知 LLM 引导热词偏置：MoE 适配器与辅助语言预测头区分多语表示，热词经 LLM 提示注入。ASRU2019 测试集相对基线 MER 相对降 20.30%，15 干扰热词设置下 MER 5.85%；据称首个将 LLM 引导偏置接入 CS-ASR，并发布提取的热词列表。

**Improving Code-Switching ASR with Code-Mixing Guided Synthetic Speech**（论文 642；Yue Heng Yeo）  
指出既有 CS TTS 偏重建保真、未显式强制语言边界一致。提出以 Code Mixing Index 引导的偏好学习框架提升合成对 ASR 微调的效用。SEAME 上微调 Whisper Large，DevMAN/DevSGE 的 MER 由 12.1%/17.8% 降至 8.9%/14.2%。

**Reinforcement Learning for Data-Efficient Code-Switched ASR**（论文 2667；Ziwei Ye）  
对 Audio LLM 用 GRPO 式可验证奖励 RL：错误率奖励 + 惩罚错误文字系统的脚本保真奖励，及两遍草稿—精炼。以 Qwen2-Audio 为可复现测试床、10 对语言、仅 TTS CS 语音训练；用 10% 数据的 RLVR 匹配全量 LoRA SFT，类型距离远的语对增益最大；可零样本迁移到真人录制 CS 语料。

**Direct Preference Optimization for English-Mandarin Code-Switching Speech Recognition in Audio LLMs**（论文 110；Minh Duc Pham）  
识别英—汉 CS 三类失败：语言省略、翻译代替转录、幻觉。用 DPO：chosen 保留混合语言内容，rejected 模仿失败模式；三款 Audio LLM 在 100K 对（570 小时）上训练后学会保留语言组成而非翻译。MER 最高相对降 89.6%（分布内）与 20.0%（分布外）。

### 保护单语能力与低资源流式

**Adding Robust Code-Switching Capabilities to High Performance Multilingual ASR**（论文 1099；Enes Yavuz Ugan）  
合成 CSW 微调常损害强单语基线。提出贝叶斯因子化适配，少量合成数据高效注入切换相关知识而不覆盖既有能力：码切换词转录错误降 32.87%，总体 WER 改善 5.31%，并保持单语性能。结论：有效 CSW 适配更依赖知识整合而非数据复杂度。

**Dynamic Block-Online Streaming ASR for Low-Resource Agglutinative Code-Switching Speech with Morphology-Aware Evaluation**（论文 3334；Nabeel Mohammed）  
据称首个全面研究句内孟加拉—英语流式 CS ASR，指出严格因果流式与长程形态依赖失配。提出动态块在线 + VAD 对齐推理，允许全局双向注意力保形态完整；用脚本锚定借词注入增强音位过渡；引入 CS-WER 诊断切换/词根/后缀错误，并显示灵活时延预算有助黏着与混合语言识别，可迁移到月经医学域。

## 本场要点

- LLM 热词偏置与语言专家适配可显著降 CS MER。
- 合成 CS 数据需显式优化语码混合边界保真，而非仅重建质量。
- 可验证奖励 RL 与 DPO 能以少数据纠正 Audio LLM 的 CS 失败模式。
- 扩展 CSW 能力应避免覆盖强单语基线（贝叶斯因子化适配）。
- 低资源黏着语流式 CS 需动态上下文与形态感知评测。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 110 | Direct Preference Optimization for English-Mandarin Code-Switching Speech Recognition in Audio LLMs |
| 642 | Improving Code-Switching ASR with Code-Mixing Guided Synthetic Speech |
| 1099 | Adding Robust Code-Switching Capabilities to High Performance Multilingual ASR |
| 1113 | LLM-HB: Language-Aware LLM-Guided Hotword Biasing for Code-Switching ASR |
| 2667 | Reinforcement Learning for Data-Efficient Code-Switched ASR |
| 3334 | Dynamic Block-Online Streaming ASR for Low-Resource Agglutinative Code-Switching Speech with Morphology-Aware Evaluation |
