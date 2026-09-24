# Explainable and Trustworthy Speech Emotion Recognition Using Confidence Score and Reinforcement Learning Rectified Speech Emotion Descriptors

- 论文编号：1683
- 报告人：Youjun Chen
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26r_interspeech.pdf

## 问题
可解释 SER 依赖音高/音量/语速/性别/年龄等 SED，但自动标注阈值统一、不可靠，且训练中无法据情绪标签纠错，解释可信度不足。

## 方法
基于 VIB-Emo 类 SER-SLM：MLP CEM 用最后隐状态估各 SED 置信并均值池化，按阈值筛可靠子集做 SFT；RNN SED Controller 采样保留/修改策略，交替更新——用情绪 CE 变化作奖励（类 GRPO 组归一）在线校正 SED。SpeechCraft 预训，IEMOCAP/MELD 自动 SED 后训。

## 实验与结果
置信筛选 + RL 校正优于无筛选/无校正；最佳（约保留 90% + RL）IEMOCAP 80.98%、MELD 64.11%，相对全量无校正基线绝对 +2.9%/+3.3%。单独筛选最优约 80% 保留；策略数 M=6 整体最佳。t-SNE 显示情绪簇更清晰。

## 结论
置信筛选与在线 SED 校正可同时提升 SER 精度与解释可信度。

## 点评
直面自动 SED 噪声，用“先选再纠”闭环贴合部署现实。信任主要靠准确率与可视化间接论证，缺少人工 SED 正确率评测；奖励仅看情绪 token，可能放过语义上仍错的 SED。
