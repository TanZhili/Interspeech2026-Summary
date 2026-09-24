# Dr. SHAP-AV: Decoding Relative Modality Contributions via Shapley Attribution in Audio-Visual Speech Recognition

- 论文编号：417
- 报告人：Umberto Cappellazzo
- 程序：Tuesday 29 September 2026 / Audio-Visual and Multimodal Perception
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/cappellazzo26_interspeech.pdf

## 问题
AVSR 在噪声下靠唇动补声学，但干净条件下 ASR 与 AVSR 差距很小，模态消融显示去视频几乎不伤、去音频则崩溃——模型如何平衡音视频、受何因素驱动，缺少跨架构的形式化分析。

## 方法
Dr. SHAP-AV：用 Shapley 值做性能无关的模态归因。三项分析——Global SHAP（整体 A/V 贡献比）、Generative SHAP（解码窗口轨迹）、Temporal Alignment SHAP（输入时段与输出 token 对应）。覆盖六模型（AV-HuBERT、Auto-AVSR、Whisper-Flamingo；Llama-AVSR、Llama-SMoP、Omni-AVSR）与 LRS2/LRS3，扫描干净到 −10 dB 等多 SNR 与噪声类型。

## 实验与结果
主要发现（正文摘要）：噪声下会转向视觉，但 −10 dB 时音频贡献仍达 38–46%；生成过程中部分模型音频依赖上升，AV-HuBERT 更稳；时序对齐在噪声下仍保持；噪声类型影响视觉依赖幅度；句长效应因架构而异；SNR 是主导因素，同 SNR 内识别难度影响小。干净条件模态消融：去视频 WER 接近全 AVSR，去音频则升一至两个数量级；含显式 VSR 多任务训练的模型视觉单模态相对更强。

## 结论
存在持续音频偏置，作者主张把 Shapley 式归因作为 AVSR 诊断常态，并启发显式模态加权机制。

## 点评
把「模型到底听还是看」从消融轶事提升为可公理化的贡献分解，并扩展到 cross-attention 与 LLM 两系。强在多粒度与 SNR 扫描；脆弱点在 Shapley 计算成本与特征联盟定义敏感。全文后半模型细节处有截断，但不影响核心发现复述。
