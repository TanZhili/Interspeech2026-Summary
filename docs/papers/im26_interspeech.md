# PF-D2M: A Pose-free Diffusion Model for Universal Dance-to-Music Generation

- 论文编号：248
- 报告人：Jaekwon Im
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/im26_interspeech.pdf

## 问题
现有 dance-to-music 多依赖单人人体姿态（SMPL/2D 关键），难覆盖多人舞、非人类角色，且姿态估计抖动；公开数据（如 AIST++）歌曲少、背景简单，易过拟合、难泛化到真实视频。

## 方法
提出 PF-D2M：用 Synchformer 视觉特征代替姿态，条件 DiT（初始化自 Stable Audio Open 的 VAE/DiT）生成音乐 latent；文本用 T5-base 交叉注意力；视觉特征上采样后与 DiT 输入通道拼接，并经 AdaLN 调制；速度预测 + CFG。渐进训练：Stage 0 保留文本–音频生成能力；Stage 1 在 VGGSound 上学视听同步；Stage 2 按 2:4:1 混合 AIST++、FMA/MoisesDB（无演唱过滤后约 191h）、VGGSound 微调，文本侧用空视觉 embedding。推理 DPM-Solver++ 100 步、CFG=5。

## 实验与结果
AIST++（按未见曲目切测试集）客观节奏指标：PF-D2M (S2) BHS 99.8、HSD 1.9、F1 94.3，多数指标 SOTA，BCS 略低于 Text-Inv/LORIS。主观（20 人、四类野外视频：单/多人 × 人/非人）：对齐与音质均明显优于 LORIS、Text-Inv，多人与非人场景差距更大。Stage 2 相对 Stage 1 结构更连贯、更少“现场收录感”。

## 结论
无姿态、用视频视觉特征 + 渐进训练，可在多样舞姿视频上生成对齐且音质更好的音乐；局限是生成时长较短，且缺合适客观评测集。

## 点评
用 Synchformer 视听同步特征绕开姿态管线，再靠 Stable Audio 初始化与多模态混合微调缓解 AIST++ 过拟合，路线清晰。节奏指标相对 GT 对齐，难反映“另有合理节奏”的感知质量，作者也强调主观评测更关键。脆弱处是短片段生成、依赖文本标签质量，以及野外场景仍可能受视觉噪声与剪辑影响。
