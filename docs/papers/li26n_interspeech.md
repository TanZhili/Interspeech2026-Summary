# Online Audio-Visual Target Speaker Extraction with Viseme-Guided Lightweight Visual Pretraining

- 论文编号：948
- 报告人：Zixuan Li
- 程序：Wednesday 30 September 2026 / Audio-Visual and Generative Target Speaker Extraction
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26n_interspeech.pdf

## 问题
多数 AV-TSE 非因果且计算重，难上边缘实时；现有工作多减音频分支，视觉仍常用重 VSR 预训练或联合学 mouth cue，部署成本高。

## 方法
以 viseme（不可分唇形音位组）识别预训练轻量视觉前端；教师（音视频、非因果）蒸馏到因果学生（仅视频、Emformer）。再接因果修改的 TF-SkiMNet 做在线 AV-TSE。对比 mouth+SkiM、viseme+SkiM、VSR+TF-SkiMNet。

## 实验与结果
总 MAC 约 7.7G，低于 VSR 方案（11.3G）。LRS2-Mix：SI-SNR 10.07、PESQ 2.07、ESTOI 0.81，优于各基线。LRS3/Vox2 亦具竞争力。因果学生 VER 28.90%（蒸馏），无蒸馏 33.93%。跨域仍领先多数基线。

## 结论
Viseme 级视觉线索比完整 VSR 更轻、比 VVAD 更细，可支撑强性能的最低算力在线 AV-TSE。

## 点评
把部署瓶颈对准视觉前端而非只砍分离器，方向务实。viseme 标签粗于音素但够做分离条件；因果蒸馏差距仍在，边缘机上还需再压延迟。
