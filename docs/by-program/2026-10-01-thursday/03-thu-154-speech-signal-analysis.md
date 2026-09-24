# Speech signal analysis

- 日期：Thursday 1 October 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：5
- 论文数：5

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场以语音表征中的因子化与潜结构综述开场，随后聚焦对齐与音节级分析：多语种词级强制对齐、无声说话脸视觉强制对齐、语言无关音节工具包，以及时长感知软标签的监督音素切分。共同主题是把时间结构从硬边界假设推进到可学习动态规划、最优路径与不确定边界建模，并服务多语种/低资源场景。

综述对比自上而下施加结构（因子化目标、蒸馏、瓶颈/可控变量）与自下而上发现结构（探测、扰动、潜空间运算、重合成）及其在可控生成、声转换、域迁移等中的应用。实证工作则把 MMS 与无监督音素边界融合进可学习 DP，把视觉对齐写成帧—音素相容格上的单调最优路径，并用软高斯脉冲替代硬边界以刻画切分标注不确定性。

## 论文技术总结

# Factorization and Latent Structure in Speech Representations

- 论文编号：
- 报告人：Matthew Wiesner
- 程序：Thursday 1 October 2026 / Speech signal analysis
- 技术分类键：signal
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
语音表征中的结构有助于可控生成、向新领域迁移，以及分析模型行为。需要系统梳理如何向学习表征施加结构，以及如何发现并利用大模型中已有的潜在结构。

## 方法
自上而下：用分解式训练目标、模型蒸馏、显式瓶颈或可解释控制变量等，对学习表征施加结构，并讨论其优劣。自下而上：探测（probing）、受控扰动、潜空间算术与再合成等，用于发现并利用大规模预训练模型中已有结构。应用侧涵盖可控生成与编辑、声转换、领域迁移、高效语音建模，以及多说话人分离或归因。

## 实验与结果
调研型摘要，未给出具体数据集或定量对比。

## 结论
结构化表征是连接可控性、可迁移性与可分析性的关键；自上而下施加与自下而上发现是两条互补路线。

## 点评
「施加结构 vs 发现结构」二分法清楚，便于对照不同论文取舍。无 PDF，无法判断报告对各类技术的证据权重。


# Multilingual Word-Level Forced Alignment with Self-Supervised Representations and Learned Dynamic Programming

- 论文编号：296
- 报告人：Joseph Keshet
- 程序：Thursday 1 October 2026 / Speech signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/weber26_interspeech.pdf

## 问题
词级强制对齐对语言研究与 ASR/合成管线关键；HMM-GMM（如 MFA）仍强，但需 G2P；希望融合多语 SSL 表征并在未见语言上可迁移。

## 方法
对齐编码器融合 UnSupSeg（无监督音素边界）与 MMS CTC 词边界置信，经 Conformer 等预测帧级边界概率（focal loss）；对齐解码器为可学习动态规划，用边界距离、编码器转移分、区间内边界惩罚、MMS 字母发射和等特征求词结束帧。编码器与解码器分阶段迭代训练。无需音素/G2P。

## 实验与结果
英：TIMIT/Buckeye 上 MWA 全面优于 MFA、MMS、WhisperX、Canary（如 TIMIT ≤10 ms 58.0% vs MFA 41.6%）。未见语：希伯来、荷兰 IFA、德 PHONDAT 上 TIMIT 训练模型更可迁移；≤50 ms 及以上常优于或持平 MFA/MMS（德 ≤50 ms 84.7% vs MFA 82.1%）。

## 结论
融合 MMS 与 UnSupSeg 再加学习 DP，可在英语上超 MFA，并有望扩展到 MMS 支持的 1100+ 语而无需再训练。

## 点评
去掉 G2P、用多语 SSL 做零样本跨语对齐，工程价值高。编码器–解码器非端到端联合优化；荷兰整体偏低、希伯来宽容差下 MMS 仍更强，说明迁移并非处处压过基线。


# V-Align: Visual Forced Alignment via Phoneme to Video Optimal Path Traversal

- 论文编号：560
- 报告人：Souvik Ghosh
- 程序：Thursday 1 October 2026 / Speech signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ghosh26c_interspeech.pdf

## 问题
音频强制对齐在噪声/缺失音频时失效；视觉强制对齐（VFA）研究少，既有方法多靠音频派生边界监督，且难得到尖锐、时序一致的音素边界。

## 方法
V-Align 将 VFA 建模为帧–音素兼容格上的最优单调路径：冻结 VTP 唇动与 XPhoneBERT 音素嵌入，经卷积投影用高斯距离核建软遍历后验 Γ，Viterbi 式 DP 解码边界。Stage 1：forward-sum + 路径二值化，无边界标注；Stage 2：词级聚合后用 MFA 词边界监督细化。

## 实验与结果
LRS2/LRS3：Stage 1 已强于多数有监督基线；Stage 2 SOTA——LRS2 MAE 32.9 ms / ACC 91.2%，LRS3 56.9 ms / 88.5%，相对先前最优约降 17.3 / 13.6 ms。消融：最优路径解码优于贪心/帧 argmax；三损失合用最佳。噪声 MFA 监督下，保留路径目标比纯监督更稳健。

## 结论
结构化单调路径学习使无边界监督即可学出对齐结构，加词级 MFA 细化达视觉强制对齐 SOTA。

## 点评
把 TTS 对齐里的路径边际化迁到视听，Stage 1 对无可靠音频标注场景很实用。Stage 2 仍依 MFA，音素清单失配靠词级回避；评估指标相对 MFA 派生标签，噪声场景优势更有说服力。


# findsylls: A Language-Agnostic Toolkit for Syllable-Level Speech Tokenization and Embedding

- 论文编号：820
- 报告人：Héctor Javier Vázquez Martínez
- 程序：Thursday 1 October 2026 / Speech signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/martinez26_interspeech.pdf

## 问题
音节级表征利于口语建模与无监督词发现，但经典包络法与神经音节器分散在不同实现/数据/协议中，难复现、难公平对比与组件消融。

## 方法
开源工具包 findsylls：统一包络计算（RMS、Hilbert、SBS、theta 等）、特征提取（MFCC、HuBERT、VG-HuBERT、Sylber）与分割算法（peakdetect、余弦合并、MinCut、CLS 阈值），支持混搭与伪包络导出；提供音节嵌入池化与相对 TextGrid 的核/边界/跨度 F1 评测。

## 实验与结果
七语料（英/西成人与儿向、Kono 手标）：核检测易、跨度难。Sylber 默认核 F1 93.3；VG-HuBERT+MinCut 边界 F1 65.0。混搭增益明显：Sylber 余弦 + peakdetect 边界 F1 升至 69.9、跨度 47.0。token 率约 3.1–5.8/s；经典包络吞吐远高于神经配置。

## 结论
单一接口可支撑高资源与低资源（含 Kono）上可复现的音节实验；实际增益常来自表征与分割器的重组而非固定流水线。

## 点评
基础设施论文：价值在标准化与可组合性。参考音节边界多由词典规则从强制对齐派生，跨度指标有标注歧义；RTFx 仅单机相对比较。


# Duration-Aware Soft Targets for Text-Independent Supervised Phone Segmentation

- 论文编号：2568
- 报告人：Raghavan Ramesh
- 程序：Thursday 1 October 2026 / Speech signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ramesh26_interspeech.pdf

## 问题
文本无关监督音素切分惯用单帧硬边界，无法刻画渐变过渡的不确定性；既有工作多改特征或结构损失，较少改进监督目标本身。

## 方法
在硬边界两侧放置时长感知的半高斯软标签：左右 σ 与邻段时长成比例（spread ratio K=0.2），仅替换边界附近零值。基线为 39 维 MFCC + 双层 BiGRU + 加权 BCE；推理用 prominence 峰检测。强调正确实现 R-value（已访问真值边界不重复匹配）。

## 实验与结果
TIMIT：Soft R-val 91.53% vs Hard 89.50%，优于 SEGFEAT、SuperSeg（Non-AR）；Buckeye 86.23 vs 84.47。跨集与德/泰卢固/印地语上 Soft 多提升精度与 R-val。80% TIMIT 测试句伪峰减少，每句约少 40%。均匀/三角/高斯核表现接近，增益主要来自平滑。同源不同滤过渡相对 Hard +3.4%。

## 结论
更好设计的软监督可在不改架构下提升音素切分；未来可自适应 K 并扩展到发音数据。

## 点评
把问题焦点移到“目标质量”，改动轻、可复现。R-value 实现纠错对公平对比有贡献；多语对齐来自 Kaldi，标签噪声会与软标签效应纠缠。

