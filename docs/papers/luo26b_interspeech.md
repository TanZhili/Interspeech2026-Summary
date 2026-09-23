# Visually-Guided Spatial Audio Generation for 360° In-the-Wild Speech Scenes

- 论文编号：2577
- 报告人：Qingyu Luo
- 程序：Tuesday 29 September 2026 / Spatial Audio 2
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/luo26b_interspeech.pdf

## 问题
野外 360° 语音场景常只有全向轨，缺可靠 FOA 方向分量；现有语音空间数据集多为双耳/仿真，且与全景视频配对稀缺，显式视频条件 FOA 重建研究不足。

## 方法
构建 YT-SPEECH（约 8.9 h、24 kHz、5 s 片段，197 源视频）：多阶段过滤（FOA 布局、语音主导、YOLO 可见说话人、音视频一致性与人工检查）。提出 Localizer–Renderer：冻结 AVS 骨干 + 可微调 Spatial Prior Head 生成 ERP 空间先验 \(P_t\)；复域 U-Net 用置信度门控 FiLM（峰值×熵）将 \(W\) 谱投影为 \(Y,Z,X\) 复掩码。损失为置信度加权 MRS/幅度/\(\ell_2\)。Sphere360 预训练后在 YT-SPEECH 微调，并做 yaw/翻转增强。

## 实验与结果
YT-SPEECH 上完整模型 \(\ell_2\)、角误差 \(\Delta_{ang}\)、PESQ、MOS-P 最优；冻结 Localizer 损害空间指标；解析 Ambisonics/Pyroom 峰值编码在部分幅度/MOS-Q 上强但空间误差更大。相对 SAG，在 YT-CLEAN/YT-SPEECH 等视觉可定位集上更稳。噪声与重叠源仍是主要失败模式。

## 结论
YT-SPEECH 与 Localizer–Renderer 可提升野外语音主导 360° 场景的 FOA 重建保真度、空间精度与感知语音质量；局限含数据规模与复杂声学场景稳定性。

## 点评
把 AVS 热图当可解释方向先验，并用置信度门控缓解歧义，比无监督分离更贴“方向先行”路线。强在语音向数据集与相位一致复域渲染；弱在噪声/多源时先验不可靠，且 8.9 h 规模仍偏小。
