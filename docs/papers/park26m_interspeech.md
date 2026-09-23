# Listening to Motion in Space: Vision-Grounded Event-wise Video-to-Audio Generation and Rendering

- 论文编号：3574
- 报告人：Dayeon Ku
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/park26m_interspeech.pdf

## 问题
常规 V2A 输出单一单声道混音，难做按源编辑与空间控制；端到端双耳系统又依赖大规模视频–双耳配对数据。影视/游戏/AR 需要可分轨、可空间化的工作流。

## 方法
训练免费流水线 VisionSFX：Gemma 4-VL 将场景拆为事件列表（起止时间、听感提示、片段）并给环境提示；每事件用 MMAudio 在约 5 s 裁剪窗内独立生成，边界 raised-cosine 淡入淡出；环境音改用视频无关的 TangoFlux，避免混入事件声。定位：Farnebäck 光流去自运动后取质心，Depth Anything 3 给相对深度，再经 HRTF 渲染；环境声 Hilbert 解相关成立体声。演示约 1 分钟完成 10 s 片段分轨时间线，支持改提示、时间线注入、方位/仰角/深度实时重渲染。

## 实验与结果
本文为演示系统描述，未报告定量客观/主观分数；强调单源重生成不影响其他轨、空间重定位无需再生成音频。

## 结论
组合现成 VLM/V2A/深度与经典光流+HRTF，可不训练、无双耳配对地得到可编辑、深度感知的双耳 V2A 工作流。

## 点评
价值在组合式后期友好管线，而非新生成模型。事件分解质量依赖 VLM，光流质心对遮挡/多目标可能漂移；缺少听感评测，空间真实感与时间对齐精度仍待验证。
