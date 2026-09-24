# RIVET: Robust Idempotent Voice Attribute Editing

- 论文编号：395
- 报告人：Dareen Alharthi
- 程序：Wednesday 30 September 2026 / Voice Editing
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/alharthi26_interspeech.pdf

## 问题
属性条件嗓音编辑依赖年龄/性别等标签，大规模数据标注常噪声或不一致，易学到错误条件映射，导致编辑不稳、身份漂移；重复编辑会累积漂移。

## 方法
RIVET：ECAPA-TDNN 说话人编码 + 条件归一化流做属性编辑 + VITS 生成。在潜空间施加幂等约束：z_re=E(D(E(x))) 应接近 z，L_idemp=∥sg(z)−z_re∥²，总损失为 VITS + flow MLE + 年龄/性别分类 + λ_i L_idemp；对说话人与语音编码器均施加。相对 VoiceShop，端到端联合训练。对比同结构无幂等基线。

## 实验与结果
GLOBE（约 535 h、自然噪声标签）上，相对基线：还原编辑后 Titanet 余弦相似更高（年龄 0.66 vs 0.63，性别 0.55 vs 0.54），性别准确 85.9 vs 77.2；UTMOS/WER 相近。EARS OOD：相似与性别编辑更稳。受控标签翻转 10%–60% 时，RIVET 身份相似与属性表现更稳。重复重建 20 轮基线身份快速漂移，RIVET 保持更高相似。AMT 听感多数表决显示编辑成功率提升（尤其性别）。

## 结论
潜空间幂等正则在噪声标签下提升身份保持与编辑成功率，且不改架构；可推广到其他属性与编辑骨干。

## 点评
把“反复编辑应回到流形固定点”变成对噪声监督的隐式正则，比显式估标签置信度更轻。评测用“改再改回”的余弦相似直接对准稳定性。注意 GLOBE 年龄准确提升有限、EARS 上年龄准确略降，幂等不能替代干净监督；开源对可复现有帮助。
