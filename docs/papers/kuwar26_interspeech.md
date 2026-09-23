# VINAYAKA: Multilingual Audio-Visual Hate Speech Detection via Cross-Modal Fusion in Hyperbolic Space

- 论文编号：2262
- 报告人：Orchid Chetia Phukan
- 程序：Monday 28 September 2026 / Audio-Visual Grounding, Synchronization & Video Understanding
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/kuwar26_interspeech.pdf

## 问题
多语言/码混视频仇恨检测若依赖 ASR 文本，易受识别错误与跨语域漂移影响；仇恨意图也常在韵律、表情、场景等非词汇音视频线索中。需验证仅用 AV 线索能否在跨语/跨集设定下更稳健。

## 方法
VINAYAKA：冻结 WavLM（音频）与 ImageBind 视觉编码器抽特征，经 1D-CNN 后投影到 Poincaré 球；用双曲距离做双向交叉注意（音频引导视觉/视觉引导音频），Möbius 加和与标量乘聚合，再对数映射回欧氏空间分类。对比拼接、欧氏交叉注意、仅 Möbius 加以及文本依赖的 MM-HSD、ToxVidLM、MultiHateClip 复现。数据：HateMM、ToxCMM（Hi-En 码混）、MultiHateClip 英/中，五折交叉验证与跨集零微调迁移。

## 实验与结果
域内：VINAYAKA 全面最优（如 HateMM Acc/F1 0.914/0.901，ToxCMM 0.892/0.885）。曲率消融：双曲 c=−1 优于欧氏与球面。跨集迁移普遍优于文本依赖基线；跨语/跨文化仍有掉点但相对更稳，作者归因于避开 ASR 误差传播。

## 结论
作者认为仅靠副语言/行为 AV 线索 + 双曲跨模态融合，可比文本中心方法在多语言与分布外设定更稳健，并报告 M-AVHSD 上 SOTA。

## 点评
问题设定清楚：把“文本不可靠”当作一等公民约束。双曲几何假设行为线索有层级结构，曲率消融支持该选择。数据集规模中等、标签二值化（Offensive 并入 Hate）会简化任务；ImageBind/WavLM 语义层与“仇恨”标签的因果仍偏黑盒。
