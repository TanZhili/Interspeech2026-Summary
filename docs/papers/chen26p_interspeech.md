# Bridging the Gap: A Hierarchical Framework for Cross-Modal Style Modeling in Expressive TTS

- 论文编号：1513
- 报告人：Jiale Chen
- 程序：Thursday 1 October 2026 / Flow Matching for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/chen26p_interspeech.pdf

## 问题
自然语言风格 prompt 控制表达式 TTS 时，文本与语音之间存在跨模态表征鸿沟，且同一 prompt 对应多种合理声学实现（one-to-many），点对点对齐不稳定。参考音频常不可得，粗粒度风格标签又缺乏描述细度；已有因子化/对比学习方法多依赖专用编码器或点式目标，难以显式处理分布级模态失配。

## 方法
提出 **OTAFlow** 三阶段层次框架：
1. **统一风格空间**：冻结 CLAP 文本/音频编码器，用对称轻量 adapter 映射到共享空间；用熵正则最优传输（Sinkhorn）做分布级对齐（余弦代价），再加对称 InfoNCE 保留实例级对应，并用 emotion/pitch/energy 多任务分类头增强表达因子可分性。
2. **Prompt-to-style 采样**：在统一空间上用条件流匹配（轻量残差 MLP）学习 \(p(z_s|z_t)\)，配合 classifier-free guidance，从噪声 ODE 采样多样音频风格嵌入，缓解残差模态间隙与一对多问题。
3. **下游 TTS**：将采样风格嵌入接到基于 Matcha-TTS、DiT 估计器与 AdaLN 条件的流匹配声学模型，再经声码器波形重建。

## 实验与结果
数据：Textrolspeech（约 330 小时，多说话人自然语言风格 prompt）；平衡测试集每情感随机 50 句（八类情感）。检索：联合 InfoNCE+OT 在 Text→Audio / Audio→Text 上 R@1 达 0.135 / 0.142，MedR=4，明显优于冻结 CLAP、仅 InfoNCE 或仅 OT。合成（Track-1 纯文本）：sMOS 3.88、ESIM 69.19 高于 EmoVoice、IndexTTS2、CosyVoice2；nMOS/UTMOS 有差距，作者归因于轻量 backbone 与训练规模。Track-2 音色参考下仍保持较高风格控制。消融：CFM 相对确定性回归头提升 sMOS/ESIM，同 prompt 多样本 Style Dist.=0.1279。

## 结论
OT+对比+多任务监督可构建兼顾对齐与因子可分的统一风格空间；条件流匹配能对同一 prompt 采样多样声学风格嵌入，并提升下游表达一致性。框架可即插即用到标准 TTS backbone。

## 点评
核心抓的是「prompt 风格控制」里分布失配与一对多采样两件事：先用 OT 稳住跨模态几何，再用嵌入空间 CFM 把剩余间隙做成可采样条件分布，而不是端到端硬吞变异。强在控制可解释、风格与音色解耦（Track-2 防参考音频风格泄漏）的设计动机清晰；脆弱点在下游声学模型仍偏轻量，自然度指标落后，且风格空间高度依赖 Textrolspeech 标签与冻结 CLAP 的表征上限。
