# Deep learning-based predictions of perceived listening effort and intelligibility across enhanced, synthetic, natural, and binaural speech

- 论文编号：1891
- 报告人：Dirk Eike Hoffner
- 程序：Monday 28 September 2026 / Model of Speech Perception
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hoffner26_interspeech.pdf

## 问题
听者实验测 listening effort（LE）与 speech intelligibility（SI）成本高；现有深度感知模型多针对特定任务。能否用原理不同的非侵入式模型 PHOBI 与 HASA-Net+，在双耳空间、助听器式增强、合成语音等训练未必覆盖的条件下同时预测 SI 与 LE。

## 方法
PHOBI：LibriSpeech 上训练的 hybrid ASR 前馈网，丢弃 HMM，用 triphone 后验的 Mean Temporal Distance（时间滞后上的平均 KL）作不确定性代理。HASA-Net+：WavLM-Large + 听力图特征 → BLSTM → 多头注意，教师–学生学 HASPI/HASQI；本文只用 HASPI 支路。三套听测：SI spatial（8 名正常听力，OLSA+SSN，三房间、噪声方位变化测 SRT）；LE enhanced（11 人，AdaptDRC 增强，SSN/CAF，Krueger ESCU 量表）；LE synthetic（23 人，Google TTS 德语句，多种噪声/SNR/空间配置）。LE 用独立 G¨ottinger 句子集做线性映射；SI 用模型心理测量函数取 50% 点作 SRT，双耳用 better-ear（取较高输出）；PHOBI/HASA-Net+ 均可用单参考条件校正偏移。

## 实验与结果
空间 SRT：无回声室相关最高（PHOBI/HASA-Net+ r=0.97/0.94；RMSE 1.0 vs 1.8/4.5 dB 校正/未校正）；办公室 0.91/0.88，食堂 0.94/0.91；PHOBI 平均 RMSE 约低 1.4 dB。LE enhanced：整体 r=0.98（HASA-Net+）与 0.94（PHOBI），RMSE 1.9 vs 1.2 ESCU；多数条件下增强降低实测与预测 LE，但 CAF 在 −10/−15 dB 上模型预测升、主观降。LE synthetic：全局 r≈0.94/0.96，噪声子集内相关更低（HASA-Net+ 0.43–0.75；PHOBI 0.62–0.91）。全文摘要称逾 10,500 条评分、相关总体 >0.88。

## 结论
两模型都能刻画空间释放掩蔽与增强带来的 LE 下降，并对合成语音有较好泛化；PHOBI 平均略优。局限：better-ear 简化双耳整合；嘈杂人声噪声下 PHOBI 难分目标/干扰；噪声簇内主观分差小导致簇内相关偏低。

## 点评
价值在“同一对 SI 代理模型跨 LE/增强/TTS/双耳”的压力测试，而不是提出新骨干。MTD 式不确定性与 HASPI 蒸馏代表两条可迁移路线；脆弱处是 LE 依赖事后线性标定、SRT 依赖参考偏移校正，以及 CAF 负 SNR 上增强方向预测反了，说明干扰语片段仍是盲预测瓶颈。
