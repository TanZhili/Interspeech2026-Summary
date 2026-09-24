# From Tokens to Faces: Investigating Discrete Speech Representations for 3D Facial Animation

- 论文编号：1397
- 报告人：Pedro R. Corrêa
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/correa26_interspeech.pdf

## 问题
语音驱动 3D 面部动画常用 SSL 连续表征，但声学 codec、语义+声学混合、ASR 式 label-based 离散表征是否更合适尚不清楚；离散 token 对面部运动的信息内容也缺系统剖析。

## 方法
冻结比较四类编码器：HuBERT（semantic）、SpeechTokenizer（semantic+acoustic）、WavTokenizer（acoustic）、CosyVoice2（label-based），各接 GRU（扩散去噪，FaceDiffuser 复现为 Base）或 Transformer（L1+速度/加速度平滑）。在 BEAT2（约 27h，FLAME→51 维 ARKit blendshapes）上训解码器。指标：LVE、Jitter、自提 Bilabial Closure Score（BCS）；MUSHRA 式感知；对音素/viseme 做归一化条件熵探针与 Ridge 连续 blendshape R²。并给出 AVTTS 概念：CosyVoice2 TTS token 并行驱动语音与面部 Transformer。

## 实验与结果
LVE 上 HuBERT 最优（0.26），CV2+Transformer 接近（0.28）；Transformer 普遍降低 Jitter。BCS：Base 57.5%，CV2+T 47.0%，多数离散+GRU 接近 0。感知：CV2+T 与 Base 无显著差异，均优于 HB+T。探针：ST 音素熵最低（更好编码音素），但面部动画差；声学表征音素信息弱。AVTTS 可从文本共享 token 同步出语音与面部。

## 结论
semantic 与 label-based 表征均适合驱动 3D 面部动画且感知相近；编码音素类信息似必要但非充分，低结构声学信息可能有害。离散共享空间可支撑统一 AVTTS。

## 点评
把表征类型与「音素探针 vs 面部指标」对齐来看，比单纯刷 LVE 更有解释力；BCS 与感知更相关是有用的方法论提示。ST 音素好却动画差，说明「有音素信息」不等于「对面部解码友好」。
