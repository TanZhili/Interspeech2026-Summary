# Cognitive-Heuristic Guided Multimodal Data Augmentation for Alzheimer’s Disease Detection Using LLM and TTS

- 论文编号：1724
- 报告人：Cheng Gong
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jiang26e_interspeech.pdf

## 问题
基于语音的阿尔茨海默病（AD）检测数据稀缺；常见文本/语音增广缺少认知相关约束，难以保持语言–声学一致的 AD 行为模式。

## 方法
从真实数据提取认知属性向量（流畅度填料、MATTR 词汇复杂度、停顿比/语速）；双源 RAG（临床知识+患者范例）约束 LLM 生成带 `<pause>`/`filler` 的脚本；CosyVoice2 属性引导 TTS 同步实现停顿与犹豫。在 ADReSSo 上以约 1:1 增广训练 ERNIE、MM-AD、CogniAlign 等，并对比传统文本/声学扰动与 VC/TTS。

## 实验与结果
多模态检测：CogniAlign Acc 0.789→0.831，MM-AD 0.732→0.803，ERNIE 平均指标亦升。文本侧相对删除/回译/GPT-2，认知约束文本 Acc 0.857 最优。作者报告认知驱动增广稳定提升检测表现；另有尺度敏感性实验（正文后续表）。

## 结论
以认知启发式锚定多模态生成，可合成更贴近 AD 语言–声学共变的训练样本并提升检测；样本已公开演示。

## 点评
把“填料–停顿–词汇贫乏”写成可检索约束再驱动 TTS，比盲目扰动更贴任务。强在跨模型一致增益与文本消融；弱在合成分布仍依赖有限真实种子、临床外推与幻觉风险需人工把关。
