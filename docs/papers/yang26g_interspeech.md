# Pitch-Injected Residual Adapter for Tonal Language in Neural Audio Codec

- 论文编号：1224
- 报告人：Chi-Chun Lee
- 程序：Monday 28 September 2026 / Neural Speech Codecs: Low-Bitrate and Disentangled Coding
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yang26g_interspeech.pdf

## 问题
神经音频编解码器多在非声调语料上按 PESQ/STOI 训练，对 F0 失真不敏感；声调语言中 F0 区辨词义，且有跨音节变调，端到端微调又易遗忘、数据不足。

## 方法
PIRA：冻结 NAC，在量化潜空间注入残差。WORLD Harvest 抽 F0/UV，F0 量化为 4 bit + 1 bit UV（≤0.4 kbps 开销）；膨胀卷积 Pitch Injector 建模长程变调；置信网络按帧门控（抑制入声/清音）。CREPE 嵌入损失提供音高梯度。参数约 1.25–1.65M，可完全移除以服务非声调场景。

## 实验与结果
闽南/粤/越三语 × EnCodec/DAC/Mimi/WavTokenizer/BigCodec：平均相对降低 codec 引入的 dTER 约 35.7%（如 EnCodec–闽南 dTER 0.267→0.171），F0-RMSE 等同步改善，英语质量基本保持。优于全量微调；消融证实膨胀卷积、置信门控与 CREPE 损失均必要。

## 结论
即插即用的音高残差适配可在不改预训练编解码器的情况下显著恢复声调可懂度，且对非声调部署零损伤。

## 点评
把“感知损失看不见音位 F0”转成显式侧信息注入，适配低资源声调语。依赖前端 F0 估计质量；对入声等非 F0 主线索声调的门控是否过抑需个案检验。
