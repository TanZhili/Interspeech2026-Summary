# Acoustic Event Detection 4

- 日期：2026年10月1日（星期四）
- 时间：14:00-16:00
- 形式：Oral
- Area：5
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场从资源高效 SED、Audio LLM 多事件定位可靠性、训练免费歧义消解，到注意力结构剪枝、鸟鸣发育可塑性无监督度量与音频主动学习。共同关切是：复杂场景下检测/理解既要准又要省，且模型在多事件与噪声下易幻觉或不确定。

效率侧，教师无关时间蒸馏与注意力通道二阶剪枝把大模型能力压到边缘预算。理解侧大规模敏感度分析显示事件数增加则真阳降、假阳升，提示词在两者间强权衡；RAISE 用选择性提取与听觉想象把预测锚定到显式声学证据。标注效率上 TSAL 用时—频谱模式引导采样；发育生物声学则用轨迹方差无标签量化可塑性。

## 技术内容

### 高效 SED、Audio LLM 定位与歧义消解

**Teacher-Agnostic Temporal Knowledge Distillation for Resource-Efficient Sound Event Detection**（论文 855；Gihun Son）  
TAT-KD 以教师 logits 为公共蒸馏空间，Conformer 时间上下文投影器传递时序，教师置信度感知损失下调模糊输出。家居环境 SED 基准 PSDS 0.574，4.548M 参数、3.668G MAC，远少于 SOTA 算力而具竞争力。

**A Sensitivity Analysis of Multi-Event Audio Grounding in Audio LLMs**（论文 1684；Taehan Lee）  
71K AudioCapsV2 片段、归一化（源,属性）事件，构建在场/缺席查询（缺席经音频对齐文本嵌入相似过滤负采样）；四 SOTA Audio LLM、12 提示、每模型约 50 万 yes/no。事件数增加则 TPR 降、FPR 升，提示词造成强权衡；多事件上模型更不确定。

**RAISE: Resolving Ambiguity in Audio Understanding with Imagination and Selective Extraction**（论文 1739；Yueqian Lin）  
训练免费框架：选择性提取隔离目标信号，听觉想象合成候选参考供比较推理，使预测基于显式声学证据。MMAR 与 MMAU 上最高约 12.4% 一致增益且无参数更新。

### 剪枝、发育可塑性与主动学习

**The silence of the weights: a structural pruning strategy for Attention-based audio signal architectures with second-order metrics**（论文 2026；Mathieu Fontaine）  
对注意力各头及 Q/K/V/输出投影矩阵解耦通道剪枝，用二阶度量打分。相对头剪枝与幅值打分，AST 与 Whisper 注意力块剪 50% 参数后性能大体保持。

**Trajectory Variance: An Unsupervised Measure of Developmental Vocal Plasticity in Birdsong**（论文 3557；Kanghwi Lee）  
位移模型预测自编码器潜空间中年龄条件位移，跨目标年龄预测方差作每声发音可塑性分。三只斑马雀（18.3–27.4 万发音）上轨迹方差区分习得音节与先天叫声（Cohen's d 0.29–0.57），并与谱平坦度负相关（r≈−0.48 至 −0.75）。

**Beyond Uncertainty and Diversity: Temporal-Spectral Guided Active Learning for Audio**（论文 1719；Qisheng Xu）  
TSAL 经软损失分布构造时—频谱信息模式，并以特征—梯度相似度选未标注样本。多音频基准上持续优于既有 AL，提升有限标注预算下的采样效率。

## 本场要点

- 教师无关时间蒸馏可在极少参数下逼近 SED SOTA。
- Audio LLM 多事件定位随复杂度恶化，提示词在敏感度与幻觉间权衡；想象+选择性提取可免训练消歧。
- 注意力解耦二阶剪枝与时—频谱引导主动学习分别服务推理与标注成本。
- 轨迹方差为发育发声可塑性提供无标签量化工具。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 855 | Teacher-Agnostic Temporal Knowledge Distillation for Resource-Efficient Sound Event Detection |
| 1684 | A Sensitivity Analysis of Multi-Event Audio Grounding in Audio LLMs |
| 1739 | RAISE: Resolving Ambiguity in Audio Understanding with Imagination and Selective Extraction |
| 2026 | The silence of the weights: a structural pruning strategy for Attention-based audio signal architectures with second-order metrics |
| 3557 | Trajectory Variance: An Unsupervised Measure of Developmental Vocal Plasticity in Birdsong |
| 1719 | Beyond Uncertainty and Diversity: Temporal-Spectral Guided Active Learning for Audio |
