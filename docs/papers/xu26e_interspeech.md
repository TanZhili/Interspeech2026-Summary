# SCNet: Enhancing GAN-based Speech Generation with Subband Condition Network and Magnitude-aware Phase Loss

- 论文编号：843
- 报告人：Nan Xu
- 程序：Wednesday 30 September 2026 / Speech Enhancement and Restoration
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/xu26e_interspeech.pdf

## 问题
GAN 声码器常黑盒生成，细粒度谱信息易丢；全带 iSTFT 相位连续性差；现有相位损失等权对待所有时频点，忽视大幅值区相位误差对听感更关键。

## 方法
以 iSTFTNet 为骨干（Snake 激活），旁路 CondNet 用 ConvNeXtV2 预测低频子带幅度/相位并 iSTFT 生成约 6 kHz 子带波形，再经 STFT+耦合块注入骨干上采样层。提出幅度感知抗卷绕相位损失：sin²(Δθ/2) 乘目标幅度 M。判别器用 MPD/MRD（同 BigVGAN）；重建含全带/子带 mel 与相位项。

## 实验与结果
LibriTTS train-clean-100（24 kHz）训练；域内与 VCTK 域外各 500 句。SCNet PESQ ID/OD 4.02/3.78，MOS 4.21/4.14，优于 BigVGAN、Vocos、HiFTNet 等；约 15.86M 参数。CosyVoice 声学特征上 MOS 4.09。dev 子集 2M 步 PESQ 4.007，接近更大 BigVGAN。

## 结论
子带条件先验与幅度加权相位损失可提升 GAN 声码器客观与主观质量，并保持有竞争力的推理速度。

## 点评
用低频子带先验替代易错 F0/NSF 路径，更稳地注入谱结构；幅度加权直接对准「大能量相位更重要」的听感直觉。子带仅到 6 kHz，高频细节仍依赖骨干黑盒，跨采样率部署需重设 hop/ISTFT 配置。
