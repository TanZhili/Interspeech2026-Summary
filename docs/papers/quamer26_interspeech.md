# Privacy and quality trade-off in real-time speaker anonymization via editing of age and sex attributes

- 论文编号：2741
- 报告人：Waris Quamer
- 程序：Wednesday 30 September 2026 / Voice Editing
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/quamer26_interspeech.pdf

## 问题
说话人匿名化常把变换当黑盒，不清楚改哪些属性、改多少才能在身份抑制与音质间取平衡。实时流式系统尤其需要可操作的属性级调参指引。

## 方法
流式合成：因果 CNN 内容编码器（HuBERT-Kmeans 单元）+ X-vector/ECAPA 说话人编码器 + AdaIN/FiLM 适配器 + 因果 HiFiGAN。对说话人嵌入做 PCA，按与年龄/女性度（连续 sex）的 Pearson 相关构造复合方向 V_attribute，Z′=Z+Σ λ_attribute V_attribute。年龄/性别标签由 wav2vec2 预测器在 LibriTTS 上生成。用线性回归量化 |λ| 对余弦相似度与 DNS-MOS 的影响，并做 AMT 听感验证。

## 实验与结果
女性度比年龄更能压低余弦相似（β≈−0.459 vs −0.309）；二者对 DNS-MOS 亦均显著负向，女性度更强。隐私（相似）下降斜率陡于质量下降，约 ±0.25 std 附近存在 sweet spot。匿名化不对称：推向分布对侧更有效（如女性降女性度）。听感：中等修改约 83% 判为不同说话人，极端约 94% 但自然度显著下降；中等仅改女性度分化率约 98%，综合建议 λ_fem≈0.25、λ_age≈0 附近。延迟约束约 <350 ms。

## 结论
通过可解释的年龄/性别嵌入编辑，可刻画隐私–质量权衡并标出中等修改的最优匿名区；框架可推广到语速、口音等属性，意在指导调参而非刷新匿名化 SOTA。

## 点评
贡献是属性级计量而非新模型：把“改多少”用回归与听感钉死，对工程调参很实用。PCA 不完美解耦年龄–性别（经音高相关），交互项与不对称性说明方向需按说话人人口统计定制。身份代理是嵌入余弦而非完整攻击者模型，与 VoicePrivacy 式评测仍有距离。
