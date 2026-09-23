# Acoustic Event Detection 1
- 日期：Tuesday 29 September 2026 / 时间：09:00-11:00 / 形式：Oral（Area 5）/ 论文数：6
- 材料：官方程序论文摘要。未出现的数字与细节不写。

## 技术趋势

本场从异常声音检测的局部密度归一化，到呼吸音分类的 SSM 骨干，再到大规模自动标注管线、语音声学 landmark 检测，以及生物声学的任务向量合成与嵌入可解释性。共同主题是：在密度不均、标注稀缺、分类体系分散的条件下，如何让嵌入距离、频谱敏感性与生态约束真正服务检测/分类。

方法分歧清晰。距离法 ASD 用 cluster exit 自适应邻域，避免跨簇破坏局部密度假设；呼吸音工作用光谱响应分析论证 SSM 相对 AST 的中高频保持，并加谱感知正则与 Dual-Axis Patch-Mix；TriA 则把场景音频自动变成带事件标注的训练数据。Landmark 检测强调软标签时间展宽与冻结 HuBERT 特征。生物声学两篇分别回答“机构不共享原始数据时如何合成多类群分类器”和“预训练嵌入编码了哪些类语音特征、对任务是否有用”。

瓶颈包括邻域大小敏感、全局自注意力低通行为、标注成本、landmark 元音类难度，以及任务向量合成在 domain negation 等边界条件失效。

## 技术内容

### 异常检测、呼吸音与自动标注

**Mind the Gap: Detecting Cluster Exits for Robust Local Density-Based Score Normalization in Anomalous Sound Detection**（论文 177；presenter：Kevin Wilkinghoff）
局部密度分数归一化对邻域大小敏感：邻域跨簇会破坏局部性。提出 cluster exit detection，识别距离不连续并据此选邻域。摘要称跨多种嵌入模型与数据集提升对邻域选择的鲁棒性并有一致增益。

**Lung-SRAD: Spectral-Aware Regularized Audio DASS with Dual-Axis Patch-Mix Contrastive Learning for Respiratory Sound Classification**（论文 550；presenter：June-Woo Kim）
AST 等 CLS 自注意力可能低通、削弱局部异常模式。分析 Distilled Audio State Space 中间表征的光谱响应后，引入高斯卷积谱感知层正则与面向 SSM 的 Dual-Axis Patch-Mix 对比学习。ICBHI 上摘要报告相对 AST 基线的分数提升。

**TriA Pipeline: A Large-Scale Automatic Audio Annotation Pipeline For Audio Classification In Specific Scenarios**（论文 995；presenter：Hong Lyu）
多数场景标注数据有限。TriA Pipeline 自动生成带音频事件标注的训练数据，并构建覆盖多小时、多类别的 TriA；再划分先验知识引导子集 TriAGK。三类家庭场景 AC 上，摘要称相对纯人工标注有平均相对准确率与 Macro-F1 增益。

### Landmark 检测与生物声学表征

**Acoustic Landmark Detector based on Conformer and HuBERT**（论文 1386；presenter：Mateo Cámara）
在 14 种 Conformer 配置上研究 landmark 检测，提出每类时间展宽的高斯软标签。冻结 HuBERT 特征无细调表现最佳；塞音擦音可靠、元音更难。摘要给出 F1@20 ms 与 LER，并说明与 AutoLandmark / SpeechMark 因语料与指标不同不可直接比。

**Ecologically-Constrained Task Arithmetic for Multi-Taxa Bioacoustic Classifiers Without Shared Data**（论文 2629；presenter：Ragib Amin Nihal）
独立细调的 BEATs 编码器可用任务向量算术合成统一多物种分类器而无需共享数据。生物声学任务向量近正交，分离与谱分布距离相关；简单平均优于符号冲突法。摘要讨论物种丰富度不对称、零样本跨区迁移及 domain negation 失败边界。

**Beyond task performance: Decoding bioacoustic embeddings with speech features**（论文 2759；presenter：Ines Nolasco）
用 88 个 eGeMAPS 特征对六类群做线性/非线性探测，把评价框为可解释性。结果显示无单一模型覆盖全特征空间，拼接嵌入最好；响度易恢复、F0 最难。结合每物种特征显著性给出模型选择假设。

## 本场要点
- ASD 局部密度归一化需自适应邻域，避免跨簇。
- 呼吸音分类探索 SSM 骨干与谱感知正则，回应自注意力低通疑虑。
- 自动标注管线是特定场景 AC 数据瓶颈的工程解。
- Landmark 软标签与 SSL 特征提升检测，难度随事件突变性变化。
- 生物声学可用近正交任务向量在隐私约束下合成多类群模型。
- 嵌入“编码了什么”与任务显著性交叉，可指导选型而非只看任务分数。

## 覆盖核对
`177 | Mind the Gap: Detecting Cluster Exits for Robust Local Density-Based Score Normalization in Anomalous Sound Detection`
`550 | Lung-SRAD: Spectral-Aware Regularized Audio DASS with Dual-Axis Patch-Mix Contrastive Learning for Respiratory Sound Classification`
`995 | TriA Pipeline: A Large-Scale Automatic Audio Annotation Pipeline For Audio Classification In Specific Scenarios`
`1386 | Acoustic Landmark Detector based on Conformer and HuBERT`
`2629 | Ecologically-Constrained Task Arithmetic for Multi-Taxa Bioacoustic Classifiers Without Shared Data`
`2759 | Beyond task performance: Decoding bioacoustic embeddings with speech features`
