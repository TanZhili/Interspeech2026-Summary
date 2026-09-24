# A Two-Stage Defence for Robust Federated Speech Emotion Recognition

- 论文编号：1125
- 报告人：Yi Chang
- 程序：Thursday 1 October 2026 / Emotion, Prosody, and Articulation
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chang26b_interspeech.pdf

## 问题
边缘设备上的 SER 同时面临数据隐私与对抗攻击脆弱性：集中上传语音有泄露风险，DNN 又易被 FGSM、PGD、DeepFool 等人不可感知扰动误导。现有联邦 SER 多偏隐私，对推理阶段白盒攻击的系统性防御不足。

## 方法
提出两阶段防御的联邦对抗学习框架。各客户端本地提取 log Mel spectrogram；训练阶段从第二轮起将本地数据对半拆分，一半生成白盒对抗样本后与干净半集联合做 vanilla adversarial training（损失为干净与对抗项的 α 加权）；服务器做联邦平均聚合。推理阶段对 log Mel 做随机缩放与随机 padding，以削弱单步与迭代攻击。

## 实验与结果
计划在意大利情感语料 DEMoS 上验证：排除中性类后保留 9,365 条、七类情感（anger、disgust、fear、guilt、happiness、sadness、surprise），68 说话人、平均时长约 2.86±1.26 秒。正文声称两阶段防御优于 vanilla FL 与任一单阶段防御。全文抽取在实验设置与数据集介绍处截断，具体 EER/准确率等数字未见。

## 结论
作者认为该框架可在本地保护语音数据，并对一系列白盒对抗攻击提升模型鲁棒性；随机化与对抗训练互补，覆盖单步与迭代攻击。

## 点评
把隐私（FL）与鲁棒性（对抗训练 + 测试时随机化）绑成同一流水线，针对 SER 边缘场景较贴切。全文抽取在结果段前截断，无法核验攻击强度与干净样本性能折损；随机化对干净数据的影响依赖 β、γ 调参，正文完整版中的消融未见。
