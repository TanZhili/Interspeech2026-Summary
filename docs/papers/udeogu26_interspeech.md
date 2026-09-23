# From Continuous Speech to Subglottal Resonances: Automatic Signal Generation, Estimation, and Tracking Framework

- 论文编号：2464
- 报告人：Chigozie Uzochukwu Udeogu
- 程序：Monday 28 September 2026 / From Self-Supervised Pre-training to Phonetic Analysis of Speech Models
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/udeogu26_interspeech.pdf

## 问题
声门下共振（SGR）对说话人归一化、身高估计、ASR、肺健康等有用，但依赖颈加速度计等专用采集，且既有估计多为半自动、难以从连续语音同时跟踪 Sgr1–3。

## 方法
两段式框架：
1. **语音→加速度计波形**：基于 PrimeK-Net 的多尺度质数核 CNN（GPK）U-Net，spectrogram 到 spectrogram，在 WashU-UCLA seen 说话人上监督训练，再对 unseen 说话人生成加速度计信号。
2. **自动估计与跟踪**：VAD 取浊音段，能量×时长选最佳段，LPC 估参考 SGR；连续跟踪时用 pYIN 滤非浊音，自适应调整 LPC 阶与预加重，使估计相对参考偏差低于阈值，从而同时跟踪三阶 SGR。

下游用估计的 SGR 在 TIMIT 上线性回归估身高。

## 实验与结果
生成质量：seen 上核 (7,13,19,29) PESQ 3.55、LSD 0.75；unseen PESQ 3.53、LSD 0.77。SGR 估计：GT 与模型生成平均 RMSE 约 24 Hz，优于相对 Lulich 半自动法的若干对比。跟踪总体 RMSE 约 23–25 / 45–49 / 76–83 Hz（Sgr1/2/3，GT vs MG 接近）。TIMIT 身高：MAE 约 5.1–5.5 cm、RMSE 约 6.2–6.9 cm，与 Arsikere 等相当，训练说话人很少。

## 结论
可从普通语音生成类加速度计信号并自动估/跟踪三阶 SGR；跨数据集身高误差低于约 7 cm，显示实用潜力。说话人内 COV 低，支持 SGR 相对稳定。

## 点评
核心价值是打通“无加速度计也能用 SGR”的数据瓶颈，再用自适应 LPC 把估计做成可跟踪流水线。脆弱处：生成质量用 PESQ/LSD 作相对指标、LPC 对高音高女性略差、身高任务仍是线性回归小样本设定，下游更广任务尚未验证。
