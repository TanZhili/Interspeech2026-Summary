# Morphoacoustic Modeling of a Dynamic 3D Vocal Tract Using MRI-Constrained Deformations and FEM Acoustics

- 论文编号：1890
- 报告人：Tharinda Piyadasa
- 程序：Monday 28 September 2026 / Methods and data for vocal tract and articulation analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/piyadasa26_interspeech.pdf

## 问题
高分辨率体 MRI 给出持续发音的 3D 声道，rtMRI 给出连续言语的中矢面动态，二者如何结合成声学上合理的动态 3D 模型仍开放；1D 管模型难刻画卷舌等复杂过渡。

## 方法
澳大利亚英语女说话人：持续 [ɜ:]/[ɻ:] 体 MRI + [ɜɻɜ] 的 rtMRI。用 rtMRI 中矢轮廓约束的 LDDMM 在两端点网格间生成时变 3D 网格；在五声学/发音地标处采样网格，COMSOL FEM（Helmholtz、刚性壁、球外域 PML）估 F1–F3，与机外录音对比（每共振峰常数偏置对齐仅用于可视化）。

## 实验与结果
端点持续音 FEM 与直立录音在 F2/F3 较接近，F1 约高 110 Hz。动态轨迹上模拟共振峰系统偏高，但随地标跟踪参考轨迹，符合噪声环境下持续发音超调/过度清晰化的解释。地标 ±1 帧扰动不改定性结论。

## 结论
MRI 约束形变 + FEM 可连接动态 3D 几何与共振峰轨迹；绝对频率仍受姿态与边界假设影响，轨迹形状更可信。

## 点评
把几何 morphing 与声学仿真接到同一 VCV 卷舌例上，验证中间形是否“像样”。单说话人、五地标、机内外不对齐是边界；对卷舌 F3 对几何敏感的问题很有针对性。
