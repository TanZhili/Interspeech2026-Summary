# Speech Emotion Recognition and Representation 1

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Oral
- Area：3
- 论文数：5

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场从可泛化 SER 综述切入，再到弱监督训练动态、轻量谱图架构、二阶几何聚合，以及音义冲突下的解耦。主线是：固定类别判别已成熟，但真实情绪理解要求跨语言/域/标签体系泛化，并处理声学与文本语义矛盾。

综述强调 foundation models 与 Speech LLMs 可能把 SER 推向开放式、零样本推理。实证研究则分别打在：早期硬标签强迫提交导致的不确定；SSL 过大难以上边缘而 mel CNN 表示不足；一阶池化丢掉特征相关；以及语义先验压倒矛盾声调（Semantic Dominance）。

方法上呈现“软化监督—蒸馏一致性—几何相关—对比解耦”光谱：PWS 逐步收紧 top-k 软监督；MSMC 用掩码卷积与 mean teacher 逼近 SSL；SOC 把协方差描述子映到切空间；ACR-Net 用跨模态注意力与对比解耦对抗 ASPIRE 冲突基准。

## 论文技术总结

# Generalizable Speech Emotion Recognition: Strategies and Trends

- 论文编号：
- 报告人：Chi-Chun Lee
- 程序：Monday 28 September 2026 / Speech Emotion Recognition and Representation 1
- 技术分类键：emotion
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
传统语音情感识别（SER）多在预定义情感类别上做判别学习，在固定范式下进展显著，但现实情感理解要求模型能跨语言、标签体系、说话人与领域泛化，超越训练中见过的设定。

## 方法
报告综述可泛化 SER 的策略与趋势：跨语言/跨领域迁移、适配不同情感表征与分类体系，以及从更多样语音数据中学习。随后讨论基础模型与 Speech LLM 如何改变 SER 范式，使其有可能在固定标签空间之外进行情感推理，并展望从任务特定 SER 转向灵活、多语言、乃至零样本/开放式情感理解。

## 实验与结果
摘要为调研型表述，未给出具体数据集名称、对比表或数值结果。

## 结论
SER 正经历从封闭类别判别走向更开放、可迁移情感理解的转变；基础模型与 Speech LLM 是推动这一转变的重要力量。

## 点评
问题设定清楚：泛化与标签空间开放是 SER 落地瓶颈。材料仅有程序摘要，点评只能停留在路线判断，无法核验具体迁移策略或 Speech LLM 用法的细节。


# Progressive Weak Supervision for Speech Emotion Recognition

- 论文编号：1587
- 报告人：Bao Thang Ta
- 程序：Monday 28 September 2026 / Speech Emotion Recognition and Representation 1
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/ta26b_interspeech.pdf

## 问题
情感标签固有模糊，SSL 编码器早期预测又高度不确定；硬 one-hot 交叉熵从一开始就强迫单类承诺，与数据与模型状态都不匹配。标签平滑又均匀放松、不感知当前预测。

## 方法
Progressive Weak Supervision（PWS）：若真标签落在当前 top-k，则构造软目标（真类质量 α，其余在 top-k 内均分），用 KL；否则硬 CE。k 三阶段：前 10% 固定 k_init → 10–75% 线性衰减至 1 → 末 25% 标准 CE。WavLM-Base + 注意力池化 + MLP；默认 α=0.7、E=200。

## 实验与结果
IEMOCAP（4 类，session 5-fold）与 ViSEC（越南语，说话人分层 5-fold）。k_init=3 时 UA：IEMOCAP 78.08%（相对 CE +4.66）、ViSEC 85.70%（+11.90），优于 CE/标签平滑等。α=0.7 最佳；去掉 warm-up 或过早收紧均掉分。

## 结论
使监督强度随模型成熟度渐进收紧，可同时应对标签模糊与早期不确定，并跨英越语言有效；无改结构、开销可忽略。

## 点评
把 curriculum 做到“监督信号本身”而非样本排序，且 top-k 软目标模型感知，比均匀平滑更贴 SER。k 上限受 4 类设置约束，多类细粒度情感是否同样单调增益未测；仍依赖单一金标，未直接建模标注者分歧。


# MSMC: Multi-Scale Masked Convolution network for Robust Speech Emotion Recognition

- 论文编号：951
- 报告人：Haoyu Song
- 程序：Monday 28 September 2026 / Speech Emotion Recognition and Representation 1
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/song26b_interspeech.pdf

## 问题
大型 SSL（HuBERT/WavLM）SER 效果好但参数与算力难边端实时；Mel 谱 + 传统 CNN 又难建模长程情感依赖，且对掩码谱直接卷积会泄漏。

## 方法
MSMC：学生分支对时—频掩码 Mel 谱做泄漏无关的 Masked Convolution Encoder（按可见掩码重归一化卷积）；教师为 EMA，看完整谱。条件位置编码 + 轻量 Transformer（学生仅保留可见 token）。多尺度一致性：MCE 中间层掩码区重建 + 全局向量余弦蒸馏；学生先自监督/蒸馏更新，再结合分类 CE；教师 EMA。

## 实验与结果
IEMOCAP 10-fold LOSO：全模型 WA 76.0%、UA 68.8%。消融显示 MCE、CPE、多尺度蒸馏逐步抬升。复杂度约 6.77M 参数、0.9G MACs/3s，相对文中 SSL 基线约少 16× 参数、23× MACs，同时逼近其准确率。

## 结论
泄漏无关掩码卷积 + 多尺度 mean-teacher 蒸馏，可在轻量谱图模型上逼近重 SSL 的 SER 表现，适合实时/边端。

## 点评
把视觉 MCMAE 思路改成“整频带时间掩码 + 按掩码重归一”，贴合谱图各向异性。双分支与 EMA 训练更复杂，部署可只留学生；与 SSL 对比的具体基线配置需对照原文表 2 解读，但效率叙事清晰。


# Geometric Second-Order Feature Correlation Learning for Self-Supervised Speech Emotion Recognition

- 论文编号：1210
- 报告人：Shuanglin Li
- 程序：Monday 28 September 2026 / Speech Emotion Recognition and Representation 1
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/li26u_interspeech.pdf

## 问题
SSL 帧级特征对 SER 很强，但一阶池化（均值/注意力）默认特征独立，丢掉通道间二阶相关；直接高维协方差又难算且在 SPD 流形上做欧氏操作会产生 swelling/伪熵。

## 方法
冻结 SSL 骨干提特征 X；SOC 层：可学习投影到低维子空间 → 中心化协方差 + 迹归一 → Log-Euclidean 映射到切空间 → 半向量化 → MLP 分类。作为可插拔模块，端到端可微。

## 实验与结果
在 ESD、RAVDESS（EmoBox 说话人无关协议）上，相对标准 GAP，SOC 分别提升约 4.68% / 4.42%；WavLM 上 ESD 峰值 WA 73.50%。去掉 LEM 分别掉约 1.45% / 1.65%。相对一阶注意力等基线持续更优。

## 结论
在子空间用 SPD + LEM 建模特征相关，可恢复一阶聚合丢失的判别信息，稳定聚合高维 SSL 特征用于 SER。

## 点评
把“情感在相关结构里”落到可插入的几何层，比盲目双线性池化更自洽。子空间维 d 与数值稳定仍是工程关键；效果依赖冻结骨干质量，未证明对端到端微调 SSL 同样必要。


# ACR-Net: Mitigating Semantic Dominance via Contrastive Acoustic-Semantic Decoupling

- 论文编号：2134
- 报告人：Mengke Zhang
- 程序：Monday 28 September 2026 / Speech Emotion Recognition and Representation 1
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26ca_interspeech.pdf

## 问题
多模态 SER / Audio LLM 在声学与文本情感冲突（讽刺等）时出现“语义主导”，盲目信文本；标准语料过滤不一致样本加剧该先验，融合重加权无法修复已塌缩的声学表征。

## 方法
提出对抗合成基准 ASPIRE（EmotiVoice，四类冲突：极性/唤醒/效价对立、情绪掩蔽）及指标 SOP（文本相对声学的过自信惩罚）、LDD（声学—语义潜空间正交度）。ACR-Net：冻结 Whisper + LoRA 双流，Cross-Modal Attention 检不一致，Contrastive Decoupling Loss 把冲突表征推入正交子空间。

## 实验与结果
ASPIRE 上 ACR-Net ACC 76.5%、SOP 0.128、LDD 0.864，显著优于朴素拼接/张量融合/MCR 与仅 CMA。极性冲突上融合法 ACC<45%、SOP>0.5；ACR-Net 维持高 LDD。一致场景（EmoDB 等）仍具竞争力（如 EmoDB 88.5%），未因解耦而崩。

## 结论
显式表征解耦优于决策层重加权，可在声学—语义冲突下保住声学保真并压低语义过自信。

## 点评
诊断（SOP/LDD）与解法对齐清楚，把“语义捷径”做成可测压力测试。ASPIRE 为 TTS 合成，真实讽刺边界更模糊；与并发 FAS/CASE 的差异在对抗合成与表征级解耦，落地仍需真实冲突数据验证。

