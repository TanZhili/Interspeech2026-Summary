# Scaling Properties of Continuous Diffusion Spoken Language Models

- 论文编号：2980
- 报告人：Eeshan Gunesh Dhekane
- 程序：Wednesday 30 September 2026 / Generative Audio and Music
- 技术分类键：singing
- 全文：https://www.isca-archive.org/interspeech_2026/ramapuram26_interspeech.pdf

## 问题
纯语音 SLM 多走离散 AR，语言能力远落后文本 LLM，且缩放代价极高；连续扩散是否更可行、其缩放律如何，尚缺系统证据。

## 方法
研究 continuous diffusion SLM：提出音素 Jensen–Shannon 散度（pJSD）度量生成“语言性”；拟合验证损失与 pJSD 的缩放律，并分析最优 token–参数比随算力变化。最终缩放至约 16B 参数、千万小时级对话数据。

## 实验与结果
验证损失遵循缩放律；最优 token–参数比随算力增大而下降；高算力下近最优区对 N/D 配置显著变宽（利于推理前沿）。pJSD 亦随规模可预测改善，类似离散 AR 的语言评测趋势。常规感知指标多不服从缩放律且易饱和；Audiobox Aesthetics 中部分维度可缩放。16B 模型可生成多说话人、多语、富情绪韵律对话，但长程语言连贯仍难。

## 结论
连续扩散 SLM 缩放轨迹与离散 AR 相似，未根本改写算力需求；在当前数据/算力下进一步纯语音缩放可能不切实际，或需新表示/范式或转文本–语音模型。

## 点评
把 pJSD 与“isoFLOP 平坦化”作为可操作发现很有价值。结论偏悲观但证据导向；生成样例与长程失败模式的细粒度诊断仍有限。
