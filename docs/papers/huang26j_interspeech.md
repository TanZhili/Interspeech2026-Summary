# SignMatch: Aligning Pose Latent Diffusion via Multi-dimensional Rewards for Sign Language Video Generation

- 论文编号：1546
- 报告人：Rongjie Huang
- 程序：Tuesday 29 September 2026 / Prosody, Pronunciation and Specialized Speech Processing
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/huang26j_interspeech.pdf

## 问题
手语视频生成（SLVG）要从口语文本与参考签名者图像合成写实签名视频，但文本与细粒度时空动作对齐弱；似然训练往往同时兼顾不好语义忠实与视觉真实，RL/偏好优化在手语生成中尚未充分利用。

## 方法
SignMatch 两阶段：(1) LLM 赋能的 pose latent 扩散（flow-matching），文本骨干默认 T5-Large（也试过 Qwen3-8B），将句子映射为运动条件潜变量 C（身体+手部）；(2) 参考引导的签名视频扩散（参考 SignViP：SD v1.5 U-Net + AnimateDiff 时序，条件编码器注入运动、参考编码器保身份）。随后仅对 pose latent 规划器用 LoRA（rank 64）做 Flow-GRPO 后训练，冻结视频渲染器；对每句采样 G=8 候选，在潜变量上计算多维奖励：语义 R_BLEU（pose→text 回译 BLEU）与视觉 R_SSIM（相对真值 pose），组内标准化后加权（λ_sem=λ_vis=0.5）得 advantage，随机单步做 clipped GRPO+KL（β≈0.04）。回译奖励模型与评测用 BLEU 评估器来自不同训练 run，以减轻 reward hacking。

## 实验与结果
数据：RWTH-2014T（德语手语）、How2Sign（ASL）。视频回译语义（Table 1）：SignMatch 在 RWTH 上 BLEU-4 11.3、ROUGE 27.1、COMET 0.62，优于最强基线 SignViP（7.9/25.4/0.54）；How2Sign BLEU-4 5.1 vs 4.5。视频质量（Table 2）：RWTH FVD 914、IDS 0.60、SSIM 0.70；How2Sign FVD 2009、IDS 0.61、SSIM 0.65，均优于 SignViP 等。消融：无 RL BLEU-4/FVD=9.2/936；仅 BLEU→10.7/978；仅 SSIM→9.7/901；组合→11.3/914。T5-Large 优于 Qwen3-8B（pose 级 BLEU-4 14.26 vs 11.04）。

## 结论
在中间运动潜空间做多维 RL 对齐可同时提升语义与视觉，且不必更新视频渲染器。作者称在两基准上达到语义与视频质量的 SOTA；正文未展开更多失败模式边界。

## 点评
把对齐点压到 pose latent、奖励也算在潜变量上，避免每步渲染多视频，工程上合理；BLEU 与 SSIM 互补的消融也支持“语义奖励 alone 会伤 FVD”。脆弱处在于回译 BLEU 与 SSIM 相对真值 pose 是否覆盖手语语言学正确性，以及冻结渲染器时潜空间对齐对最终手形细节的上限。
