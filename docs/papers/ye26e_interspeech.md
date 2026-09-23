# OPERA-Net: Octave-aware Phase-sensitive Enhanced Recognition Architecture for Singing Voice Deepfake Detection

- 论文编号：3341
- 报告人：Fengwei Ye
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ye26e_interspeech.pdf

## 问题
歌声伪造检测（SVDD）上，语音反欺骗器易失效：背景音乐干扰强，且幅度谱忽略相位不连续等伪造线索。

## 方法
OPERA-Net 双流：Phase-Consistent CQT（PC-CQT）建模瞬时频率导数以捕相位异常；Semantic-Guided Gating 用预训练 WavLM 语义先验过滤 PC-CQT，抑制 BGM、突出人声伪造痕迹。在 CtrSVDD 与 SingFake（T01/T02/T03）上评测。

## 实验与结果
CtrSVDD pooled EER 1.54%（A09–A13），优于 Fosafer 等挑战系统且为单模型。SingFake overall EER 4.72%（T01 3.12 / T02 4.85 / T03 4.92），优于 SingGraph 6.05% 与 AASIST/W2V2 变体。

## 结论
作者认为相位敏感表征加语义门控可在有伴奏的野外歌声上更稳地检出伪造，无需堆叠多 SSL 集成。

## 点评
把 SVDD 难点明确落在“相位+伴奏”，PC-CQT 与 WavLM 门控分工清楚。CtrSVDD 控制集与 SingFake 野外差距仍大；对极端混响/翻唱重制等未见条件还需更多压力测试。
