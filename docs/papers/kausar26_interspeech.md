# DisenEEG-Net: Disentangling EEG features via sufficient information bottleneck and adversarial learning for cross-subject auditory attention detection

- 论文编号：1703
- 报告人：Tasleem Kausar
- 程序：Wednesday 30 September 2026 / Neurophysiology of Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kausar26_interspeech.pdf

## 问题
EEG 听觉注意解码（AAD）跨被试泛化难：注意相关与被试特异特征纠缠，域偏移使神经导向助听难以落地。

## 方法
DisenEEG-Net：并行时空 Transformer 提表征后正交分解为任务/被试子空间；充分信息瓶颈约束被试子空间保留身份信息并抑制任务泄漏；GRL 对抗使任务特征被试不变；重建损失保保真。在 KUL、DTU、AVED 上留一被试交叉评测。

## 实验与结果
跨被试：KUL 1 s 窗口 Acc 75.9%±13.3（超 DARNet 约 5+ 点），2 s 76.1%；DTU 约 57.8–58.7%；AVED 音/视频约 54–55%。消融中去时间支路掉约 8.5 点；正交+瓶颈、对抗+重建均有贡献。分析显示 z_task 可做注意分类，z_dom  alone 不能。

## 结论
信息论瓶颈与对抗联合解缠可提升跨被试 AAD，更长时间窗有助；为神经导向助听的域泛化提供可行框架。

## 点评
把正交、充分瓶颈、对抗、重建四约束叠在一起，针对“任务–被试纠缠”较完整。强在三数据集一致超基线；弱在 KUL 方差仍大、绝对准确率在 DTU/AVED 仍接近临界实用。
