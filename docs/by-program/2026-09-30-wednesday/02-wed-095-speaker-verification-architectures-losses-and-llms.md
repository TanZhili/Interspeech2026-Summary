# Speaker Verification: Architectures, Losses, and LLMs

- **日期**：Wednesday 30 September 2026
- **时间**：09:00-11:00
- **形式**：Oral
- **Area**：4
- **论文数**：6
- **材料说明**：依据官方程序与 ISCA 归档中的题名、作者、报告人、时段与摘要整理；未补充摘要未给出的指标、数据或机制。来源：[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)、[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)。

## 技术趋势

本场覆盖说话人确认的架构缩放、离散音频 token、开集噪声标签学习、噪声稳健混合一致性，以及音频/语音感知大模型适配。架构侧 ReDimNet2 在一维通路做时间池化以更激进扩展通道而不成比例增加算力。离散编解码 token 虽隐式保留说话人线索，但需跨特征知识蒸馏才能接近 Fbank 教师。

标签噪声方面用时序集成阈值与邻域感知标签混合缓解开集噪声校正偏差。噪声稳健则用混合物一致性自监督对齐增强信号与输入，避免增强前端把非判别因素也“还原干净”。LLM 线把 SV 重述为音频问答：零样本能力有限，监督微调与难负对采样可改进；亦可注入冻结说话人嵌入并用 LoRA 赋予自然语言接口下的 ASV 能力。

## 技术内容

### 架构缩放、离散 token 与噪声标签

**ReDimNet2: Scaling Speaker Verification via Time-Pooled Dimension Reshaping**（论文 1447；Ivan Yakovlev）  
在 ReDimNet 维度重塑框架上，于一维通路引入时间维池化，使一维特征仍为二维特征的重塑形式，同时更激进扩展通道。提供 B0–B6 七种配置。在 VoxCeleb1 上摘要称各尺度计算—精度帕累托前沿相对 ReDimNet 改进，并给出 Vox1-O EER 与参数/算力示例。

**Text-Independent Speaker Verification Using Discrete Audio Tokens**（论文 1135；Zheng Liang）  
离散 NAC token 在 ASV 上常弱于频谱特征。提出跨特征知识蒸馏 CFKD，引导编解码学生模仿强 Fbank 教师嵌入空间。在 VoxCeleb 上摘要称显著提升编解码系统，使其接近 Fbank 教师精度。

**Temporal Ensembling Threshold and Neighbor-Aware Label Mixup for Speaker Verification with Open-Set Noisy Labels**（论文 11；Liang He）  
TET-LM：每轮用双成分 GMM 建模嵌入相似度，指数滑动平均集成阈值区分干净/噪声标签；邻域感知机制生成混合标签缓解开集噪声校正偏差，并配合多阶段训练。在 VoxCeleb 上摘要称多种噪声标签条件下 EER/minDCF 相对标准方法与最佳基线大幅下降。

### 噪声稳健与大模型适配

**Mixture Consistency Learning for Robust Speaker Verification in Noisy Environments**（论文 364；Seung-bin Kim）  
指出 SE 前端常重建仍含残留噪声与信道变异的“干净”参考，可能恢复非判别因素。MCL-SV 不依赖参考，强制分离说话人与背景表征之和匹配原始混合物。摘要称在多数据集上持续优于强基线，并在近期噪声稳健 SV 中达 SOTA。

**Adapting Audio Large Language Models for Speaker Verification**（论文 1117；Shuai Wang）  
将 SV 重述为音频问答并做零样本评估，显示当前 ALLM 零样本 SV 有限。监督微调配合基于规则的难负对采样；轻量微调显著改进但仍落后传统模型。扩展到文本相关 SV，联合查询说话人身份与所说内容，摘要称结果可与级联 ASR—SV 竞争。

**Speaker Verification with Speech-Aware LLMs: Evaluation and Augmentation**（论文 2670；Yuzhe Wang）  
提出模型无关打分协议，用 Yes/No token 置信或对数似然比得到连续验证分数。基准显示近期 speech-aware LLM 说话人判别弱（VoxCeleb1 上 EER 高于 20%）。轻量增强：经学习投影注入冻结 ECAPA-TDNN 嵌入并仅训 LoRA。在 TinyLLaMA-1.1B 上摘要给出接近专用系统的 EER，同时保留自然语言接口。

## 本场要点

- 时间池化维度重塑可改善 SV 架构的精度—算力帕累托前沿。
- 离散音频 token 含说话人线索，跨特征蒸馏可释放其 ASV 潜力。
- 开集噪声标签需集成阈值筛选与邻域感知混合校正。
- 混合物一致性学习避免 SE 前端恢复非判别因素。
- ALLM 零样本 SV 弱，监督微调与难负采样可改进并支持文本相关联合验证。
- 注入冻结说话人嵌入 + LoRA 可把 LLM 变为带自然语言接口的 ASV 系统。

## 覆盖核对

| id | title |
|---|---|
| 1447 | ReDimNet2: Scaling Speaker Verification via Time-Pooled Dimension Reshaping |
| 1135 | Text-Independent Speaker Verification Using Discrete Audio Tokens |
| 11 | Temporal Ensembling Threshold and Neighbor-Aware Label Mixup for Speaker Verification with Open-Set Noisy Labels |
| 364 | Mixture Consistency Learning for Robust Speaker Verification in Noisy Environments |
| 1117 | Adapting Audio Large Language Models for Speaker Verification |
| 2670 | Speaker Verification with Speech-Aware LLMs: Evaluation and Augmentation |
