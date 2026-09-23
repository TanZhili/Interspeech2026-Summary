# SingFox: A Multi-Lingual Singfake Detection Corpus

- 论文编号：2573
- 报告人：Arth J. Shah
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shah26_interspeech.pdf

## 问题
现有 singfake 数据多偏英语、生成范式单一，缺少多语、替代假唱（假人声+真伴奏）与源追踪设定；语音反欺诈模型难迁移到含节奏/旋律的歌声伪造检测。

## 方法
构建 SingFox：20 语种（14 国际+6 印度）、113,802 片段、约 126.32 小时、1150 歌手；六轨 T1–T6 分别覆盖全球语、Indic、乐器类、合集、替代假、源验证。真唱来自开放资源，假唱由 GAN（HiFi-GAN/BigVGAN/UnivNet）、扩散（DiffSinger/DiffRhythm）、VC（RVC/So-VITS-SVC）、TTM（MusicGen）等生成；4 s 切片、峰值+RMS 归一、不做源分离。约 30% 子集用部分生成器训练，其余含未见生成器测试。

## 实验与结果
LFCC+ResNet 等声学特征与 SSL 基线；跨数据集时 FMC 训练在 SingFox T4 上准确率最高达 77.84%，CtrSVDD/WildSVDD 训练迁移较差。T5 替代假上 LFCC+ResNet 准确率可低至 45.13%。源追踪上 LFCC 准确率 89.06%。生成器侧 BigVGAN/RVC 极难检（准确率约 1%），UnivNet 相对易检（71.17%）。人类 MOS：假唱约 3.47，真唱约 4.03。

## 结论
提供多语、多范式、含替代假与源追踪的 singfake 评测资源，暴露现有检测器在跨语/跨生成器与混合真假伴奏上的脆弱性。

## 点评
贡献是基准与威胁面设计，而非新检测器；T5/T6 特别贴近真实攻击（假声真伴、可解释溯源）。正文注明为高度压缩版、细节在 arXiv，部分表与结论表述略乱，使用时需对照完整版协议。
