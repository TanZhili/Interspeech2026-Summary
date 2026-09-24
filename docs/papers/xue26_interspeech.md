# Imperceptible Voiceprint Protection via Human-Machine Perception Discrepancy Feature Disentanglement

- 论文编号：105
- 报告人：Haotian Guo
- 程序：Wednesday 30 September 2026 / Speaker Privacy Preservation and Anonymization
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/xue26_interspeech.pdf

## 问题
零样本声纹克隆易被滥用；波形/频域对抗扰动要么可听、要么经预处理后失效，嵌入空间方法若不解耦内容与说话人又会伤可懂度。

## 方法
两阶段：（1）AutoVC 式解耦–重建：内容编码器经 bottleneck 提 c，GE2E 提说话人嵌入 h，解码+postnet 重建，损失含重建、内容一致性与对抗熵最大化解耦；（2）冻结编解码，训练生成器在说话人嵌入加扰动 δ（幅度 α），解码得保护 Mel，经 HiFi-GAN 出波形；损失含 mel 重建、MPEG 心理声学掩蔽、LSGAN 真实性，以及模拟攻击者从保护语音偷嵌入克隆任意内容后压低与原说话人相似度的防御损失。数据 VCTK（80/10/20 说话人）。

## 实验与结果
白盒（AutoVC+GE2E）：DSR@τ=0.5 达 87.2%，MOS 4.18，WER 5.30%，Sim_prot 0.95、Sim_clone 0.13，优于 RoVo（79.2% DSR、MOS 3.72）等。消融：去掉 Lde 后 DSR 崩至 12.5%；去掉 Lmask 对质量伤害大于去掉 Lmel。黑盒迁移至 YourTTS、VALL-E、AdaptVC 时 DSR 最高且白→黑跌幅最小。t-SNE 显示保护嵌入仍近原簇，克隆嵌入则散开。

## 结论
在解耦说话人子空间注入扰动并加心理声学约束，可同时提升防克隆成功率与听感；未来拟考察自适应攻击与压缩/噪声退化。

## 点评
“人机感知差”落地为先解耦再扰动，解释了相对 RoVo 的质量–防御双赢。防御损失显式闭环克隆链路，转移性较好。评测仍依赖同一说话人编码器家族与固定阈值，对自适应去噪攻击的正文讨论有限。
