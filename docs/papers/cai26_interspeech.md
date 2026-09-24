# Relative Importance of Formants to the Intelligibility of Vocoded Speech in Cochlear Implant Simulation

- 论文编号：143
- 报告人：Ying Cai
- 程序：Wednesday 30 September 2026 / Assistive Technologies 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/cai26_interspeech.pdf

## 问题
CI 处理器频谱分辨率有限；共振峰对可懂度的相对权重在噪声声码器仿真中如何，以及通道数/包络截止频率是否改变该权重，尚缺系统证据。

## 方法
10 名正常听力普通话听者；MHINT 句经 LPC 提 F1–F3 轨迹生成正弦波语音，再设保留两共振峰条件（去掉 F1/F2/F3 之一）。噪声声码器：N=4/8，包络截止 100/200 Hz，另含宽带对照。单耳耳机听辨，报正确词率。

## 实验与结果
宽带：三共振峰 97.2%；去 F3→85.7%，去 F1→50.7%，去 F2→31.4%，F2 贡献最大。N=8、截止 200/100 Hz 时仍是去 F2 伤害最大。N=4、截止 200 Hz 时去 F1 伤害最大，说明通道数可改变相对重要性。声码化整体降低识别率，但共振峰排序模式与参数交互。

## 结论
CI 仿真下 F2 通常最关键、F3 最弱，与宽带结果一致；但声码器参数（尤其少通道）可重排权重，提示处理器设计应优先保住关键共振峰信息。

## 点评
用稀疏正弦波语音干净剥离共振峰贡献，再叠声码器参数，对 CI 策略有直接启示。听者均为正常听力仿真，真实 CI 用户与噪声/混响场景外推需谨慎；仅测普通话句子。
