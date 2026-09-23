# Speaker Diarization 2

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Oral（Area 4 - Oral 5）
- Area：4
- 论文数：6
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。数字与方法仅取自摘要。

## 技术趋势

本场延续说话人日志（diarization）在会议、医患对话与远场多通道场景中的工程化。一条线把日志与 ASR 或角色标签联合：医患角色日志用双 transducer，并区分说话人日志与角色日志对声学/语言线索的依赖差异。

在线与多说话人扩展方面，延迟承诺式说话人跟踪取消显式人数上限，在 VoxConverse / VoxSRC-23 多至约 21–28 说话人时保持 DER 稳定；弱监督多说话人嵌入则去掉外部 VAD/分割依赖，给出窗内帧级多说话人边界。

远场与会议鲁棒性上，神经 FCASA 引入说话人活动的 beta 先验与变分下界，用正则化连续活动分数替代原交叉熵；会议场景则用两级不确定性抑制（语言上下文调制的分割 + 已知说话人种子引导聚类）对抗边界模糊与重叠传播。

端到端自条件（SC）EEND 侧则直面层级排列不一致（HPI）：用 Group-Wise / Continuous Influence PIT 在层次间约束或软正则排列，稳定训练并改善 2/3 说话人 DER。

## 技术内容

### ASR/角色联合与在线多说话人跟踪

**ASR-Synchronized Speaker-Role Diarization**（论文 880；presenter：Bongjun Kim）  
角色日志（如医生/患者）比通用说话人标签更实用，但单 transducer 串行预测词与角色会损害 ASR。工作将双 transducer ASR+SD 适配为 ASR+RD，论证 SD 与 RD 对声学/语言线索依赖不同，并提出任务专用 predictor、用更高层 ASR 编码器特征作 RD 输入，以及沿 1-best ASR 路径的交叉熵（替代完整 RNNT 损失）。在公开与私有医患对话上，相对最优基线 R-WDER 相对改进 6.2% 与 4.5%。

**Delayed-Commitment Online Speaker Tracking for Robust Many-Speaker Diarization**（论文 898；presenter：Youngki Kwon）  
在线聚类范式下，DC-OST 立即为嵌入打标签，但延迟注册新说话人直至证据充分，并以自适应距离阈值抑制虚假注册，无显式人数上限。系统 VAD 下，0.5 s 延迟在 VoxConverse 与 VoxSRC-23 上 DER 为 9.53% 与 9.12%（分别多至 21 与 28 说话人），优于 DIART 与 Sortformer；按说话人数分析显示精度随人数增长保持稳定，而基线下降。

### 弱监督嵌入、远场贝叶斯与会议不确定性抑制

**Multi-Speaker Embeddings With Weakly Supervised Speaker Activity Detection For Granular Speaker Diarization**（论文 2471；presenter：Jenthe Thienpondt）  
弱监督多说话人嵌入同时提取嵌入与帧级语音/说话人活动，去除流水线对外部 VAD 与说话人分割的依赖，并在每个窗内提供多说话人帧级边界且不依赖帧级标注训练数据。相对作者先前系统，在 AMI、VoxConverse、DIHARD III 上混淆错误率平均相对改进 13.7%。

**Neural Multichannel Distant Speaker Diarization and Source Separation with Beta Speaker Activity Prior**（论文 1248；presenter：Sicheng Mao）  
为增强模型驱动神经 FCASA 的鲁棒性，对说话人活动施加 beta 先验，并用可变分下界目标作为正则化连续说话人活动分数以替代原交叉熵训练日志模型。在 AMI 上相对基线，DER 至少改进 3%（相对 16%），Jaccard Error Rate 至少改进 4%（相对 20%）。

**Two-Level Uncertainty Suppression for Robust Meeting Diarization**（论文 1956；presenter：Shuhei Asaka）  
针对快速换人与重叠导致的边界不确定再传播到说话人分配，提出两级抑制：分割侧用 FiLM 将 OWSM-Encoder 语言上下文表征融入 WavLM，降低高活动区边界模糊；聚类侧 KSGC 用已知说话人嵌入稳定混有已知/未知说话人时的全局分配。AMI、AliMeeting、AISHELL-4 上 FiLM 相对 WavLM-large 最多降 DER 1.8 点；KSGC 在混合条件下最多再降 2.62 点。

### 自条件 EEND 的层级排列一致性

**Hierarchical Permutation Consistency Learning for Self-Conditioned End-to-End Speaker Diarization**（论文 1198；presenter：Bongsu Jung）  
SC-EEND 逐层细化说话人预测时，层独立 PIT 造成层级排列不一致，向自条件路径注入排列噪声。提出 GW-PIT（全局排列约束）与 CI-PIT（高斯加权聚合层代价矩阵的软正则），在保持局部表示灵活的同时促进层次排列一致。CALLHOME 上 CI-PIT 抑制排列噪声、稳定训练，并在 2/3 说话人场景改进 DER。

## 本场要点

- 角色日志与说话人日志任务属性不同，双 transducer + 任务专用预测器可兼顾 ASR 与 RD。
- 延迟承诺在线跟踪支撑无人数上限的多说话人会议日志，并抑制虚假新说话人。
- 弱监督多说话人嵌入把 VAD/分割内化到帧级活动估计。
- Beta 活动先验与两级不确定性抑制分别强化远场多通道与真实会议鲁棒性。
- SC-EEND 需显式处理层级 PIT 不一致，CI-PIT 提供软一致性约束。
- 评估覆盖医患、AMI/AliMeeting/AISHELL-4、VoxConverse/VoxSRC、CALLHOME 等场景。

## 覆盖核对

| 论文 id | 标题 |
| --- | --- |
| 880 | ASR-Synchronized Speaker-Role Diarization |
| 898 | Delayed-Commitment Online Speaker Tracking for Robust Many-Speaker Diarization |
| 2471 | Multi-Speaker Embeddings With Weakly Supervised Speaker Activity Detection For Granular Speaker Diarization |
| 1248 | Neural Multichannel Distant Speaker Diarization and Source Separation with Beta Speaker Activity Prior |
| 1956 | Two-Level Uncertainty Suppression for Robust Meeting Diarization |
| 1198 | Hierarchical Permutation Consistency Learning for Self-Conditioned End-to-End Speaker Diarization |
