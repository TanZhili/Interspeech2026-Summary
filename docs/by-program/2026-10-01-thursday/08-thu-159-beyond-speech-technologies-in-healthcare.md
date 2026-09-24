# Beyond Speech Technologies in Healthcare

- 日期：Thursday 1 October 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：13
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场面向医疗与辅助沟通：电子喉（EL）语音转换的个性化与新设备、舌超声到语音合成及其信息来源检验，以及构音障碍 ASR 的零样本声克隆增广。共同约束是术前/病理数据极少、设备声学特异、以及评测需超越谱失真走向可懂度。

ELVC 线从单句术前音色保留（级联优于伪目标）、鼻部电子喉（NEL）特征选择与增广，到用合成数据做一对多时间对齐 EL→自然语音。超声线提出时空 Transformer 框架并用 WER 评测；对照实验意外发现去除舌区未必显著伤 MSE，提示基线可能利用更广图像线索，而双编码器可把激活聚焦舌区。构音障碍侧用零样本克隆绕过说话人专用采集瓶颈。

## 论文技术总结

# Personalized Electrolaryngeal Voice Conversion with a Single Pre-operative Utterance

- 论文编号：1942
- 报告人：Devin Chang
- 程序：Thursday 1 October 2026 / Beyond Speech Technologies in Healthcare
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/chang26e_interspeech.pdf

## 问题
个性化电子喉语音转换（ELVC）通常需要大量术前自然（NL）录音；临床往往只有极少甚至一句参考。直接对 EL 做零样本 VC 因域失配失败，需在仅一句 NL 参考下同时恢复可懂度与说话人音色。

## 方法
基准前端为 LLE-ELVC（HuBERT 邻域搜索 + WavLM 权重/重建 + HiFi-GAN）。对比：(1) 伪目标：用 FreeVC/Vevo/Seed-VC 把 240 句 NL 音色转到单句术前参考，再监督 LLE-ELVC；(2) 级联：先 LLE-ELVC 恢复可懂度，再零/一次样本 VC 转音色；并做特征级级联（跳过波形重编码）及对 Seed-VC 的监督精炼（LOUO 中间特征 + 伪目标，DTW 对齐）。用健康说话人模拟 EL/NL 对（4 对，TMHINT 320 句，240/40/40）。

## 实验与结果
直接零样本 SER 往往高于原始 EL（如 FreeVC >100%）。级联优于伪目标（Seed-VC 波形级联相似度 0.82 vs 0.74）。特征级 + Seed-VC 精炼：SER 59.65%、相似度 0.84、UTMOS 2.30，优于假设有 240 句术前数据的监督 LLE-ELVC（61.98%、0.75、1.86）。主观 ABX：精炼级联 77.71% 胜、监督基线 9.38%。

## 结论
一句参考下，先 EL 域可懂度再音色迁移的级联更有效；特征级联与监督精炼可进一步压 SER、抬相似度。未来需更大说话人集与真实患者数据、延迟评估。

## 点评
用模拟术前数据把“one-shot 个性化”立成可复现基准，并证明直接零样本不可行。级联把 intelligibility 与 timbre 解耦，与 DSR 两阶段思路一致；真实喉切除术前录音稀缺，当前结论依赖健康人 EL 模拟，迁移到患者仍是关键未解。


# A Preclinical Study of Electrolaryngeal Voice Conversion for a Novel Nasal Electrolarynx: Feature Choice and Data Augmentation

- 论文编号：1882
- 报告人：Ming-Chi Yen
- 程序：Thursday 1 October 2026 / Beyond Speech Technologies in Healthcare
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/chen26t_interspeech.pdf

## 问题
新型鼻式电子喉（NEL）声学异于颈式电子喉（CEL）：中高频共振、低频衰减、元音共振峰抬高；既有 ELVC 多针对 CEL，特征选择与数据稀缺下 NEL-to-NL 是否可直接套用尚不清楚。

## 方法
在统一 seq2seq 框架比较 VTN-VC 与带额外 VC 预训练的 ETN-VC，输入分别为 80 维 Mel 或 WavLM-Large 第 6 层特征。数据增强：F5-TTS 由 TWnews 生成 sNL，再用 LLE-VC（WavLM 邻域搜索，可选重建 WavLM 或对应 Mel）合成配对 sNEL，供 ETN 预训练后在真实 NEL–NL 上微调。预临床设置：同一健康说话人录 320 句 TMHINT（NL/CEL 录音棚，NEL 病房），240/40/40。

## 实验与结果
特征偏好设备相关：CEL-to-NL 更宜 WavLM（VTN SER 57.5%），NEL-to-NL 更宜 Mel（VTN SER 58.8% vs WavLM 62.0%）。ETN+Mel+10k 增强：CER/SER 降至 63.0%/53.8%（相对 VTN Mel 的 72.0%/58.8%）。A/B 可懂度：Mel 优于 WavLM，ETN Mel 优于 VTN Mel。UTMOS 等神经质量分则偏向 WavLM，与可懂度指标存在折中；零样本 SeedVC/Vevo 等对 CEL/NEL SER 仍很高。

## 结论
NEL 的设备特异频谱使 Mel 比通用 SSL 特征更保声学线索；LLE-VC 增强可稳定提升 NEL 转换。单健康说话人预临床，需真实患者 NEL 与自然度 MOS 验证。

## 点评
把“特征是否通用”做成 CEL/NEL 对照实验，结论清晰：SSL 预训练偏 NL，可能抹掉 NEL 共振。医疗场景优先 CER/SER 与听测而非 UTMOS 的取舍合理；病房噪声与单说话人设计限制了对外推广的强度。


# One-to-Many Electrolaryngeal Voice Conversion with Synthetic Data

- 论文编号：2150
- 报告人：Carlos Toshinori Ishi
- 程序：Thursday 1 October 2026 / Beyond Speech Technologies in Healthcare
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/wu26l_interspeech.pdf

## 问题
电子喉到自然语音（EL2NL）的时间对齐 VC（保节奏）数据极缺；多数用户无术前录音，需要一对多目标音色。仅压平 F0 的伪 EL 频谱不像真 EL，限制转换质量。

## 方法
三步：在 JVS 上预训练日语 QuickVC（QVC）；用 1 名喉切除患者约 13 分钟（100 句）EL，冻结 Whisper 编码器微调得 NL2EL，把 JVS 约 12998 句转为合成对齐 EL；再用合成对监督微调预训练 QVC 做一对多 EL2NL——Whisper 编码器吃合成 EL、说话人编码器吃对应 NL，只更新内容编码器与 flow，冻结说话人编码器以防从目标句偷语调。对比 QVC、QVC-mix、flat-F0 及 ours-100/1k/10k。

## 实验与结果
合成 EL 相对真 EL 的 MCD：ours 5.942 vs flat-F0 11.916。EL2NL：ours-10k 在 F0 RMSE/CORR、CER、音色相似度上优于基线（如 CER 0.366、Sim 0.923）；更多合成数据更好。主观（97 人）：相对 QVC / flat-F0 的 N-CMOS、I-CMOS 显著为正；S-MOS 3.03（真值对 4.51）。局限：/h/ 等难发音、仅中性语调。

## 结论
从小规模真 EL 学出频谱匹配的合成 EL，再规模化监督一对多 EL2NL，可同时提升语调自然度与可懂度，并保留多目标音色选择。未来需改进音素与表情语调。

## 点评
“先 NL→EL 造对齐数据，再 EL→NL”把稀缺瓶颈转成可扩展合成，比 flat-F0 更贴 EL 频谱。冻结说话人编码器以防语调泄漏是细腻设计。单患者日语数据与中性语调限制了跨语言/个性化表达；S-MOS 与真值差距说明一对多音色仍有空间。


# Tongue2Speech: Real-Time Speech Synthesis from Tongue Ultrasound Videos via Spatiotemporal Transformers

- 论文编号：3023
- 报告人：Yash Sonkar
- 程序：Thursday 1 October 2026 / Beyond Speech Technologies in Healthcare
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/sonkar26_interspeech.pdf

## 问题
仅用舌部超声（UTI）重建可懂语音时，既有方法多依赖 CNN/LSTM，长距协同发音建模不足；评价常停在 MSE/MCD，对词汇可懂度洞察有限；跨说话人零样本因解剖与探头放置差异极难。

## 方法
Tongue2Speech：原始 scanline（64×842）经极坐标到笛卡尔楔形（64×64）；四层 3D Conv 时空编码 → 自适应平均池化得每帧 256 维；六层 Transformer（8 头，FFN 1024）建模长距动态；MLP 预测 80 维 mel，HiFi-GAN 声码。总参 19.17M（不含声码器 6.25M），L1 mel 损失。在 TaL1/TaL80 上对比 Conformer-U2S、STN-CNN、多种 3D/2D+BiLSTM 变体；多说话人后对未见说话人短时微调。

## 实验与结果
单说话人 TaL1：整体 WER 15.93%、MSE 0.594，优于最强基线 3D-CNN+BiLSTM+Skip（WER 24.15%）；Conformer-U2S/STN-CNN 近饱和不可懂。多说话人 TaL80：WER 31.64%（Skip 变体 33.23%）。对说话人 78–81 微调后 WER 约 27.62–46.07%。评价用 Whisper Medium ASR。

## 结论
3D 时空编码 + Transformer 可在仅舌部超声下得到可懂合成；MSE 不能可靠反映词汇正确性。跨说话人泛化仍难，个性化微调是实用路径。

## 点评
把可懂度（WER）提到主指标，纠正了 U2S 过度依赖谱失真的习惯。单说话人到多说话人 WER 翻倍，说明几何可变性仍是瓶颈；探头摆放敏感在会话间仍有约 9 点 WER 波动。


# On the Role of the Tongue Region in Ultrasound-to-Acoustic Mapping

- 论文编号：1071
- 报告人：Ibrahim Ibrahimov
- 程序：Thursday 1 October 2026 / Beyond Speech Technologies in Healthcare
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/ibrahimov26_interspeech.pdf

## 问题
超声到声学映射常默认舌面是主要声学信息源，但帧内还有周围组织、阴影与伪影；标准 2D-CNN 是否真在用舌区特征尚未被严格检验。

## 方法
在 UltraSuite-TaL80 四名说话人上，帧到 80 维 mel 的说话人专用网络。自动舌区提取：ROI 掩膜 + 自适应高斯阈值 + 连通域，并以 IoU/质心位移做时序稳定。输入操纵：把舌区像素换成同帧背景采样（无舌轮廓）。再提出双编码器 + 交叉注意力门控，显式注入舌掩膜。基线为 13×13 核 2D-CNN；HiFi-GAN 合成后评 MCD/PESQ/MOSnet；Grad-CAM 可视化关注区。

## 实验与结果
去掉舌区后 MSE 略升但四说话人均无统计显著（p>0.05）。双编码器相对基线在 MSE 与感知指标上亦无一致显著增益（个别说话人基线更好）。Grad-CAM：基线激活散落在组织/阴影，提议模型稳定集中在舌区。整体合成质量仍远低于 vocoded original。

## 结论
在帧级 2D-CNN 设定下，预测并不 critically 依赖显式舌区像素，网络可能依赖更广图像统计；交叉注意力虽不抬客观分，但使表征更解剖可解释。未来需在时序模型中再检验舌动态的作用。

## 点评
用“挖掉舌区也不掉分”的操纵实验挑战领域默认假设，负结果本身有价值。局限在帧独立映射——协同发音与舌轨迹本该是时间结构；点评中应记住：可解释性改进 ≠ 当前指标提升。


# Low-Burden Data Augmentation for Dysarthric ASR via Zero-Shot Voice Cloning

- 论文编号：1501
- 报告人：Satwinder Singh
- 程序：Thursday 1 October 2026 / Beyond Speech Technologies in Healthcare
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/singh26_interspeech.pdf

## 问题
构音障碍 ASR 数据稀缺且说话人差异大；合成增强常需多句注册或说话人特调，再次落入采集瓶颈。需检验零样本声纹克隆能否用极低负担数据改善识别。

## 方法
用 Higgs Audio V2，对 TORGO 每位构音障碍说话人仅取一句参考（平均 7.2s，“The quick brown fox…”），以 LibriSpeech 100h 去重/过滤文本为提示生成 TORGO-Synth（8289 句，约 18h，训练 15h）。严格剔除与 TORGO/SAP-1102 词表重叠的提示。微调 Whisper-medium：Zero-shot / Real / Clone / Hybrid，仅在留出真实 TORGO 上评 WER；并用 SAP-1102 子集做跨库测试。TitaNet 嵌入做说话人相似分析；另扫 5–50h 合成量。

## 实验与结果
总体 WER：Zero-shot 31.62%，Real 24.44%，Clone 26.00%，Hybrid 25.12%。中重度组 Clone/Hybrid 优于 Real（39.95%/37.49% vs 42.19%）。合成量在约 15h 为最优点，再增易过拟合伪迹。SAP-1102：Clone 整体约 12.8%（Zero-shot 14.5%），CP 组从 54.7% 降至 41.6%。t-SNE 显示多数说话人克隆簇紧、M05 较散。

## 结论
单句注册的零样本克隆可提供可扩展训练信号，接近真实微调并在中重度与跨库上有时更优；存在合成量“甜点”与对中度说话人可能引入分布偏移的代价。

## 点评
把“低负担”落到单句注册与词表隔离，实验控制清楚。中重度受益、中度恶化提示克隆并非普适补丁；TORGO 以 CP 为主，跨库 CP 增益更大符合源分布偏置。全文结论段抽取不完整，跨库细表以正文已给数字为准。

