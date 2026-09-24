# Improving streaming ASR with foundation models using emission policies

- 论文编号：3358
- 报告人：Gerard Mas Mollà
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/masmolla26_interspeech.pdf

## 问题
Parakeet、Canary 等语音基础模型离线 ASR 强，流式切块后质量明显下降；依赖内部特征的发射策略难迁移，需要不打开模型黑盒的流式包装。

## 方法
训练无关、模型无关流水线：滑动窗音频缓冲（块长 L_c、最大窗 L_max）增量喂入；用 token 级时间戳过滤早于 T_last 的重复输出；文本侧发射策略控制提交时机——静态 Wait-K、Hold-N，动态 LocalAgreement（连续两假设最长公共前缀）及基于编辑距离阈值 τ 的 LA-Lev。仅要求模型能产时间戳。

## 实验与结果
Open ASR Leaderboard：VoxPopuli、TedLium-v3、Earnings22；模型 Parakeet-tdt-0.6b-v3、Canary-1b-v2。窗参：L_c=2、L_max=20 较稳。相对 NeMo 流式基线，各策略均降 WER；高延迟下 Parakeet+LA 接近离线（如 Earnings22 11.45% vs 离线 11.19%，延迟约 2.25 s）。L_c=1 低延迟设定下 Parakeet+LA 优于或接近 SimulStreaming Whisper（如 Earnings22 12.07%/1.32 s vs 14.92%/1.01 s），延迟略高约 0.4 s。

## 结论
滑动窗 + 时间戳去重 + 纯文本发射策略，可使带时间戳的 SFM 在实时/近实时下接近离线质量，且无需访问内部张量。

## 点评
把“黑盒+时间戳”做成可插拔流式层，利于换模型。LA 等策略用稳定性换延迟，与 AlignAtt 类模型感知策略比更易移植、延迟略逊。图文中部分抽取噪声不影响主结论；多任务 ST 等扩展作者留作未来工作。
