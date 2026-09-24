# Beyond Two-stage Diffusion TTS: Joint Structure and Content Refinement via Jump Diffusion

- 论文编号：2875
- 报告人：Jiabao Ai
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ai26b_interspeech.pdf

## 问题
扩散/流匹配 TTS 中，两阶段固定对齐易塌向平均韵律；单阶段无显式时长又易对齐不稳。需要在同一过程中联合演化离散时序结构与连续频谱内容。

## 方法
跳跃扩散：前向同时删帧（保护各音素首帧）与加噪；反向用 Location Predictor 选插入槽、Content Predictor 填内容，再做标准去噪。提出 Upsample–Diffuse–Downsample（UDD）以复用固定维预训练 U-Net；One-shot 退化为用分类时长替代 Grad-TTS 回归时长预测。冻结 Grad-TTS 编码器与扩散骨干，在 LJSpeech 训练跳跃预测器。

## 实验与结果
One-shot：WER 3.37% vs Grad-TTS 4.38%，UTMOSv2 略升。直接变维 TDD 最差。UDD 在匹配目标时长下 MCD/F0 有竞争力。0.75× 慢速 OOD：Grad-TTS 近似均匀拉伸，UDD 提高静音占比（如 Argmax 静音比 9.63% vs Grad-TTS 6.38%）并略降 WER，呈现自适应停顿。

## 结论
分类时长与跳跃–扩散联合细化可缓解均值韵律，并在非常规总时长下更自然地插入停顿；UDD 使变长结构与固定维网络兼容。

## 点评
把“时长多模态”写成插入槽分类，比 MSE 时长更贴停顿等稀有事件。主表最优往往是 One-shot 而非完整迭代 UDD，说明联合细化收益仍场景依赖；实验限 LJSpeech 与 Grad-TTS 骨干，对更强单阶段流匹配基线的相对优势待证。
