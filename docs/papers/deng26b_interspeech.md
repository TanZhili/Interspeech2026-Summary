# Codec-induced Mismatch, Speech Duration, and Speaker-dependent Effect in a DNN-based Forensic Speaker Recognition System

- 论文编号：1004
- 报告人：Guangmou Deng
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/deng26b_interspeech.pdf

## 问题
法医自动说话人识别中，质疑语音常经有损编解码且时长有限，与高质量已知样本失配；系统级指标可能掩盖个体说话人表现差异。

## 方法
102 名年轻香港粤语男性跨会话 HQ 录音；仅对质疑侧施加 G.711 A-law、AMR-NB 12.2/6.7 kb/s、Opus（16 kHz, 128 kb/s）。前端 ResNet34-MHA（VoxCeleb1+2 训）提 512 维嵌入，后端 LDA-PLDA + 双高斯化校准出 LR。质疑时长 5–90 s（5 s 步进）；报告系统 C_llr 与按说话人 C_spk_llr。

## 实验与结果
系统级：AMR-NB 6.7 kb/s 劣化最大，Opus≈HQ；C_llr 随时长下降，约 30 s 后平台。个体级：短时长与低码率下部分说话人 C_spk_llr>1 或波动大；90 s 时跨条件均值与标准差正相关（R²=0.43），表现差者对编解码更敏感。

## 结论
作者认为系统级“尚可”不保证每个说话人都可靠；编解码失配与时长效应存在显著说话人依赖，个体级验证对法医解读必要。

## 点评
把 FASR 评测从平均 C_llr 推进到个体轨迹与敏感性回归，切中个案证据解释。语料为实验室 HQ→仿真编解码，真实多级级联信道仍待扩展；C_spk_llr 样本少、方差大，正文亦强调看系统模式而非单人诊断。
