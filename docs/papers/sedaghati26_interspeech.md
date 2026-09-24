# VoxWatermark: A Large-Scale Benchmark for Audio Watermark Detection under Perturbations

- 论文编号：1771
- 报告人：Farnaz Sedaghati
- 程序：Thursday 1 October 2026 / Audio Watermarking and Source Verification
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/sedaghati26_interspeech.pdf

## 问题
TTS 大规模部署后亟需可验证溯源，但缺少统一、面向检测器的大规模基准：现有基准覆盖水印方法少、扰动有限，且缺乏在未知嵌入方法与真实分布偏移下的通用检测基线。

## 方法
构建 VoxWatermark：在多语多源语料上统一注入 10 种水印（6 传统：LSB、QIM、Patchwork、Echo、Phase Coding、DSSS；4 神经：AudioSeal、WavMark、Timbre、Perth），约 91,090K 样本 / 126,513.89 小时。扰动分 no-box（17 类信号处理/编解码等）、black-box（HSJA、Square）、white-box（可微伪造/去除）。提出 AudioWMD：基检测器对 log-mel 打分，再对 K=8 随机查询分数聚合为 5 维稳定性特征（均值、标准差、极差、正类占比、翻转率），经逻辑回归做最终判决；对比单查询 WMD（ConvNeXt-V2）。

## 实验与结果
训练见 6 种水印、无扰动增强；OOD 含跨语（非英中 Common Voice）与跨口音（VCTK），并含未见水印（Patchwork、Echo、WavMark）。验证集上 AudioWMD AUROC 88.3% 高于 WMD 72.0%；OOD Test1/2 为 63.8%/63.2% vs 57.1%/57.9%。no-box 下两者多接近随机；white-box 上 AudioWMD 明显更稳（如 T1 AUROC 77.15 vs 48.63）；black-box 表现依赖攻击类型，HSJA-spec 上 AudioWMD 大幅掉点而 WMD 更强。

## 结论
作者认为注入方法多样性与分布偏移显著影响检测稳定性；AudioWMD 在多场景下更稳/可扩展，开源数据与代码以推动标准化评测。

## 点评
贡献重心在检测向大规模基准与三档威胁模型，暴露“干净域高分、真实扰动崩塌”的常见假象。AudioWMD 的查询稳定性建模对 white-box 有帮助，但对强自适应 black-box 并不万能——正好说明基准设计的价值。数据规模宏大，但检测器训练仅见部分水印、无扰动增强，OOD 数字仍偏低，实用部署需继续加强。
