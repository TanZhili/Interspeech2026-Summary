# Exploiting EEG-based Gamma-Band Time Frequency Feature in WaveNet Decoder Framework for High-Fidelity Speech Reconstruction

- 论文编号：377
- 报告人：Rantu Buragohain
- 程序：Wednesday 30 September 2026 / Neurophysiology of Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/buragohain26_interspeech.pdf

## 问题
从侵入式神经信号直接合成可听语音仍难：噪声高、时序失配，线性/短时模型难抓长程依赖，既往谱重建 PCC 常低于 0.7。

## 方法
公开荷兰语 sEEG（10 名癫痫患者朗读 100 词）：提高 gamma（70–170 Hz）包络时频特征并堆叠时间上下文，映射到 logMel；用堆叠因果膨胀卷积残差块的 WaveNet 式解码器（门控激活、残差/跳跃连接）重建，再经全连接输出。按被试训练评估 MSE、PCC、STGI。

## 实验与结果
被试间 PCC 约 0.9014–0.9510，MSE 约 0.317–0.584，STGI 约 0.49–0.54；标准差小，显示相关强但存在被试差异。作者称相对既往线性/浅层非线性有更强相关与时序一致性。

## 结论
高 gamma 特征 + WaveNet 解码可从 sEEG 获得高相关谱重建，推进神经言语合成；仍受电极位置因临床而异与被试变异限制。

## 点评
用因果膨胀卷积对准神经–语音长程对齐问题，PCC 数字亮眼。强在公开数据可复现；弱在朗读词表、电极布局非统一、未充分报告可听合成听感/ASR 指标。
