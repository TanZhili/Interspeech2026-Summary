# Speech-to-See: End-to-End Speech-Driven Open-Set Object Detection

- 论文编号：2183
- 报告人：Xinyue Song
- 程序：Monday 28 September 2026 / Audio-Visual Grounding, Synchronization & Video Understanding
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/lu26d_interspeech.pdf

## 问题
语音驱动开放集目标检测（audio grounding）数据稀缺；先前 YOSS 等两阶段、经文本/CLIP 中介的管线易误差累积且难端到端优化，也难直接利用韵律等声学线索。

## 方法
Speech2See：在 Grounding DINO + HuBERT 上渐进训练。(1) 预训练：冻结视觉/语音骨干与检测解码器，用 Query-Guided Semantic Aggregation（可学习 query 对 HuBERT 序列交叉注意）压成紧凑语义 token，再经特征增强与 speech-guided query 选择做语音–视觉对齐；(2) 微调：仅训解码器 FFN 中的 Mixture-of-LoRA-Experts（Top-1 路由，K=2），加负载均衡损失。总损失为检测损失（L1、GIoU、对比对齐）+ λ·L_lb。训练语料由 COCO/Objects365/Flickr30k/LVIS 文本标注经 edge-TTS 多说话人合成语音。

## 实验与结果
COCO 闭集：相对 YOSS-large +17.0 AP（56.2 vs 39.2）。零样本 COCO：Obj365+Flickr+GQA 上 42.7 AP，超过 YOSS 闭集。LVIS 零样本：19.9 vs YOSS-large 16.3。相对 Whisper+G-DINO 级联：参数更少（197.8M vs 266.7M）、RTF 更低、AP 更高。消融：QSA 换 MLP 掉约 15.5 AP；K=2 优于 K=1，K=3 无额外收益。相对纯文本 Grounding DINO 仍有差距。

## 结论
作者认为端到端迁移文本–图像先验 + QSA/MoLE 可在合成语音设定下实现直接“听声定位”，并在效率与精度上优于级联与两阶段基线；未来需真实语音与噪声/长尾验证。

## 点评
抓住数据稀缺下“借文本–图像检测器先验、再适配语音”的务实路线；QSA 针对语音时序冗余是合理设计。主要边界是合成 TTS 语音与真实语音分布差，作者已承认；与文本驱动上界的差距也提示声学纠缠（说话人/韵律）仍是对齐难点。
