# Speaker Verification: Advances in Speaker Embeddings

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Oral（Area 4）
- 论文数：6
- 材料：官方程序中该场全部论文摘要。摘要写明问题、方法与主要结论；未在摘要中出现的数字与细节不写入。

## 技术趋势

本场围绕说话人嵌入的获取、增强与下游用途展开。短时语音信息不足推动 VAM-ECAPA（TVAMSP + WavLM+ECAPA-TDNN）用可学习 Vector Archive 补全稀疏特征；声学失配则推动无标签嵌入增强，以 von Mises-Fisher profile likelihood 给出闭式自适应加权，强调“不必过度结构化”。

跨域说话人检索评估六种预训练嵌入，发现多尺度监督模型更抗信道与老化漂移，但多数架构在跨语条件下对语言特异音变过拟合；adaptive symmetric normalization 作为免训练后端可恢复排序一致性。噪声鲁棒方面，NoiseLoRA-SV 用噪声条件化 LoRA 与 CRN 分层表示在推理时动态生成权重，并以 InfoNCE 对比蒸馏对齐干净嵌入。

嵌入的“用途分化”也很清晰：面向生成的工作用 sub-center 建模保留说话人内变异以改善零样本语音转换；面向属性预测的工作则把 LLM 嵌入与 keyword-appending、top-k negative loss 结合，走向 open-set 语义属性空间。瓶颈集中在短时、失配、噪声与跨域排序；方向是档案映射、几何似然、后端校准、动态适配与任务专用嵌入目标。

## 技术内容

### 短时与失配条件下的嵌入增强

**Beyond Short Segments : Expanding Speaker Embeddings with Vector Archives**（论文 3192；Hyunku Kang）
针对短时语音说话人验证性能显著下降，提出 VAM-ECAPA：以 Transformer-based Vector Archive Mapping with Statistical Pooling（TVAMSP）把信息稀缺特征映射到可学习的典型说话人特质档案。集成到 WavLM+ECAPA-TDNN 基线后，在 VoxCeleb1 的 1 秒测试段上达到 8.334% EER，相对常规训练基线相对错误率降低 54.8%。

**Revisiting Label-Free Speaker Embedding Enhancement with vMF Profile Likelihood**（论文 1146；Seunghwan Kim）
在冻结主干的无标签嵌入增强设定下，将干净目标建模为 von Mises-Fisher 似然并 profile 掉样本浓度参数，得到带自适应加权的闭式目标。在 VoxCeleb1、VoxSRC23、CN-Celeb、VOiCES、VC-Mix 上大体保持基线并在困难失配集上更清晰增益；在宽泛 single-view 配方下比近期扩散基线更稳定，表明该设定下不必采用高度结构化配方。

### 跨域检索、开放属性与生成导向嵌入

**On the Robustness of Speaker Embeddings for Cross-Domain Speaker Retrieval**（论文 1796；Chuanqi Huang）
评估六种预训练嵌入在多跨域检索场景的排序稳定性。监督多尺度模型更抗信道滤波与老化漂移，但多数架构在跨语失配下对语言特异音变过拟合。提出免训练的 adaptive symmetric normalization：用高分背景 cohort 估计局部分数统计以校正信道导致的全局偏移，从而恢复各模型排序一致性。

**Toward Open-Set Speaker Attribute Prediction with Keyword-Appended LLM Embeddings**（论文 3203；Byoungjun So）
用 LLM 嵌入在连续语义空间表示说话人属性，以 keyword-appending 压缩判别流形，并用 top-k negative loss 在拥挤语义区建立决策边界。在 LibriTTS-P 上优于闭集基准，并可泛化到未见同义词；几何分析表明策略可正则化嵌入流形。

**Rethinking Speaker Embeddings for Speech Generation: Sub-Center Modeling for Capturing Intra-Speaker Diversity**（论文 942；Ismail Rasim Ulgen）
指出识别训练会压制说话人内变异，不利于自然生成。提出 sub-center 建模：每位说话人多个原型，使话语对齐不同原型以保留结构化说话人内变异同时保持可分性。零样本语音转换中改善可懂度、音高变异与自然度评分，并保持较强说话人验证性能。

### 噪声条件化动态适配

**NoiseLoRA-SV: Hierarchical Noise-Conditioned Adaptation with Embedding Distillation for Robust Speaker Verification**（论文 64；Dai Gao）
针对静态推理参数难以应对非平稳噪声，提出 NoiseLoRA-SV：CRN 提取分层噪声表示，全局嵌入经超网络生成 LoRA 矩阵，局部嵌入控制帧级时变门控，并以 InfoNCE 对比蒸馏对齐噪声—干净说话人嵌入。在 VoxCeleb1 配合 MUSAN 与未见 NonSpeech100 噪声上，EER 低于静态基线。

## 本场要点

- 短时 SV 可用 Vector Archive 映射（VAM-ECAPA）显著降低 1 秒段 EER。
- 无标签嵌入增强可用简单 vMF profile 目标，不必追求高度结构化扩散配方。
- 跨域检索瓶颈常在跨语音变过拟合；自适应对称归一化可作免训练后端校准。
- 生成任务需要保留说话人内变异（sub-center），与识别目标存在张力。
- 开放集属性预测正把 LLM 语义空间与说话人表征桥接。
- 噪声鲁棒走向推理时动态 LoRA 与对比蒸馏，而非仅静态微调。

## 覆盖核对

- 3192 | Beyond Short Segments : Expanding Speaker Embeddings with Vector Archives
- 1146 | Revisiting Label-Free Speaker Embedding Enhancement with vMF Profile Likelihood
- 1796 | On the Robustness of Speaker Embeddings for Cross-Domain Speaker Retrieval
- 3203 | Toward Open-Set Speaker Attribute Prediction with Keyword-Appended LLM Embeddings
- 942 | Rethinking Speaker Embeddings for Speech Generation: Sub-Center Modeling for Capturing Intra-Speaker Diversity
- 64 | NoiseLoRA-SV: Hierarchical Noise-Conditioned Adaptation with Embedding Distillation for Robust Speaker Verification
