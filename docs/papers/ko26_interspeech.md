# Mispronunciation Modeling via PPG-Based Phone Editing: A Data Augmentation Framework for Dysarthric Speech Recognition

- 论文编号：891
- 报告人：Tsai-Hsiu Ko
- 程序：Wednesday 30 September 2026 / Speech, Voice and Language Disorders
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/ko26_interspeech.pdf

## 问题
构音障碍 ASR 受数据稀缺与高度个体化误读影响；现有增强多改时长/音高/音色等全局特征，难刻画说话人特异的音素替换等细粒度发音缺陷。

## 方法
说话人依赖增强三件套：(1) 用 PPG 抽取器得到构音障碍与配对对照音素序列，规则对齐构建 40×40 语音映射矩阵 M；(2) 若对角准确率低于 α=70%，按替换概率 >β=5% 最多选两个音素，在 PPG 上交换概率分布（每句最多改一个音素）；(3) 改自 UUVC 的 PPG-to-speech（连续 PPG、去掉时长网络，源–滤波–能量+HiFi-GAN），先 VCTK 预训练再 UASpeech 微调；(4) 按音素时长比做 WSOLA 音素级变速。用增强数据微调 HuBERT Large。

## 实验与结果
UASpeech：对照+构音障碍 block 1/3 训练，block 2 测试。合成语音 MOSNet 2.55（真值 2.68），SES 0.71。相对同规模 GAN 基线 [6]，总体 WER 19.53% vs 21.88%（绝对降 2.35%）；低/极低可懂度分别降 3.69%/4.54%。消融显示映射编辑优于随机替换，风格转换与音素级变速均有贡献，三者合用最好。

## 结论
PPG 音素编辑可把个体误读模式注入典型语音，在 UASpeech 上优于 GAN 增强，尤其惠及重度构音障碍。

## 点评
用可解释映射矩阵驱动局部 PPG 编辑，比全局声学扰动更贴近「这个说话人怎么错」。插入被排除、每句只改一音素偏保守，可能低估复杂错读；强依赖配对对照与对齐质量，临床配对不足时扩展性受限。
