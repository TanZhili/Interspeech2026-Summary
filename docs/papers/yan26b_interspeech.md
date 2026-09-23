# Consistent and Coherent Audio-Visual Understanding with Cross-Frame Patch Differential Attention and Cross-Modal Temporal Alignment

- 论文编号：619
- 报告人：Lecheng Yan
- 程序：Monday 28 September 2026 / Audio-Visual Grounding, Synchronization & Video Understanding
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/yan26b_interspeech.pdf

## 问题
现有 MLLM 常把音视频分路处理，跨模态交互弱，难保证时间同步与语义一致；仅“能接音频”而不做对齐，收益极小（如 MiniCPM-v 与 o 变体差距约 0.04%）。

## 方法
在视觉–语言骨干 + Whisper 音频编码器上，引入：(1) 帧级 RoPE 与模态频率注入（视觉升序、音频降序）建立跨模态时间坐标系；(2) Cross-Frame Patch Differential Attention（CFPDA）对相邻帧 patch 差分做注意力，跟踪与音频相关的视觉变化；(3) Temporal Aligned Attention：按音视频长度比硬/软对齐掩码限制交叉注意，并用自适应质量分平衡模态内特征与跨模态上下文。训练为自回归 CE，参数高效微调（新模块可训、解冻末 4 层解码器等）。模型称 C2AVLM。

## 实验与结果
AVSD：ACC 50.30%、BERT-F1 89.87，全面优于含 Qwen-2.5-Omni（46.95 ACC）等基线。消融显示去音频、去 RoPE/频率、去 CFPDA 或仅交叉注意均掉点。域外：AVHBench 音频驱动幻觉 F1 80.2 领先；Video-MME 长视频无字幕 50.7% 强于 InternVL-3；LongVALE 描述类指标相对弱、但多超基座 Qwen-2.5-VL。

## 结论
作者认为成功的音视频理解依赖精确时间与语义对齐，而非仅多模态接入；所提编码与注意力机制在对话、幻觉检测与长视频时间推理上有效。

## 点评
问题诊断与消融一致：对齐机制比“加个音频塔”更关键。AVSD 与幻觉检测亮眼；长视频 caption 指标偏弱、且多数对比用 8 帧而 Omni 用全帧，作者已说明仍可赢，但跨设定解释需谨慎。依赖 LLM 评判准确率，主观偏置仍在。
