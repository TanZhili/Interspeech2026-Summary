# Speech and Audio Quality Assessment

- 日期：2026年9月30日（周三）
- 时间：16:30-18:30
- 形式：Oral
- Area：5
- 论文数：6
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。仅依据摘要表述，不补写未给出的实验细节。

## 技术趋势

本场覆盖端到端 MOS 预测增强、流式/多分辨率增量质量估计、FAD 编码器任务偏置分析、音高重音专用评测、多指标与偏好联合学习，以及对大音频语言模型幻觉可靠性的攻击评测。

趋势一是让质量表征在潜空间中按感知质量更好组织（对比学习），并支持前缀音频上的增量预测。趋势二是承认“评测器本身携带任务诱导偏置”，没有单一编码器可做万能 FAD。趋势三是把局部音高重音错误、异构绝对指标与成对偏好纳入统一建模，同时开始用对抗式音频幻觉探测 LALM 是否真正 grounding 到音频。

## 技术内容

### MOS 表征学习与增量多分辨率评测

**DNSMOS-C: Improving End-to-end Speech Quality Models via Contrastive Learning**（论文 342；Xinyu Liang）  
在 DNSMOS Pro 上加入 MOS 引导的三元组对比损失，直接作用于中间嵌入。摘要称在多个数据集上相关性优于 DNSMOS Pro，域外泛化更好，并出现可解释的低维质量排序，且不增加额外计算开销。

**ANCHOR: Autoregressive Non-intrusive Chunk-Ordered Refinement for Joint Multi-Resolution Speech Quality Modeling**（论文 927；Zhuoyan Tao）  
把增量质量评估重写为多分辨率自回归任务，在同一解码器中用双分辨率 token 与分辨率感知层级做粗到细精炼。摘要称在 2 秒前缀上 PLCMOS 误差降低 48%，并揭示约 4–6 秒有效感知上下文视界。

### 编码器偏置、重音评测与统一多指标学习

**An Empirical Analysis of Task-Induced Encoder Bias in Fréchet Audio Distance**（论文 1549；Wonwoo Jeong）  
将 FAD 评测分解为召回、精确与对齐（语义/结构），并跨六个编码器、两个数据集比较。摘要称重建型 AudioMAE、ASR 型 Whisper、分类型 VGGish 分别在不同轴占优，无单一万能编码器，未来需面向人类感知的评测原生编码器。

**PASQA: Pitch-Accent-Focused Speech Quality Assessment Model Trained on Synthetic Speech with Accent Errors**（论文 1662；Masaya Kawamura）  
用可控重音 TTS 构造日语重音错误数据并计算伪重音质量分，结合 mora 条件融合、排序损失、辅助错误定位与说话人不变训练。摘要称常规 MOS 模型难保持按错误严重度排序，而 PASQA 在已见/未见说话人上排序准确且更贴近人类重音正确性判断。

**URGENT-MOS: Unified Multi-Metric and Preference Learning for Robust Speech Quality Assessment**（论文 1671；Wei Wang）  
受 URGENT 多指标与偏好协议启发，在共享架构中联合建模多绝对质量指标与成对偏好。摘要称利用异构监督改善绝对质量与偏好预测及跨域稳健性。

### 大音频语言模型可靠性攻击

**Audio Hallucination Attacks: Probing the Reliability of Large Audio Language Models**（论文 2448；Ashish Seth）  
提出 AHA 攻击套件 AHA-Eval（约 6.5K QA），含查询结构攻击与向音频注入描述不存在事件的合成语音。摘要称 Audio Flamingo 3 与 Gemini 3 Pro 攻击成功率分别达 95.35% 与 79.65%；用约 120K QA 的 AHA-Guard 后对齐可将攻击成功率最多降低约 49%。

## 本场要点

- 对比学习可在不增大模型负担下改善 MOS 潜空间组织与域外泛化。
- 流式/生成系统需要前缀约束下的多分辨率增量质量建模。
- FAD 分数强烈依赖编码器训练任务，应避免单一编码器万能假设。
- 局部音高重音错误需要专用监督；多指标与偏好可统一学习。
- LALM 在标准基准高分下仍可对音频幻觉攻击高度脆弱。

## 覆盖核对

- 342 | DNSMOS-C: Improving End-to-end Speech Quality Models via Contrastive Learning
- 927 | ANCHOR: Autoregressive Non-intrusive Chunk-Ordered Refinement for Joint Multi-Resolution Speech Quality Modeling
- 1549 | An Empirical Analysis of Task-Induced Encoder Bias in Fréchet Audio Distance
- 1662 | PASQA: Pitch-Accent-Focused Speech Quality Assessment Model Trained on Synthetic Speech with Accent Errors
- 1671 | URGENT-MOS: Unified Multi-Metric and Preference Learning for Robust Speech Quality Assessment
- 2448 | Audio Hallucination Attacks: Probing the Reliability of Large Audio Language Models
