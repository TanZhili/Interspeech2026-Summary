# VoiceQualityGUI: A Tool for Word-Level Voice Quality Modifications

- 论文编号：3579
- 报告人：Harm Lameris
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lameris26b_interspeech.pdf

## 问题
嗓音质量（吱嘎、气声、鼻化等）对语用功能重要，但研究工具少；既往用 VoiceQualityVC 需手写各时段属性，难快速试探词级局部调制假设。

## 方法
Streamlit GUI：先对原音频做零偏移 VC 作基线，再调全局音高/音高变化以贴合原句，然后按词选择并滑动调节 creakiness、breathiness、nasality。后端为改进的 VoiceQualityVC：在 FreeVC 上为 HNR35、CPPS、H1–H2、H1–A3 各加仿射编码器，45k 迭代微调；用户侧暴露为三种感知组合。训练用 Expressive Speech 英语子集约 17h20m（prosody score≤0.78），帧级声门特征与句级音高 z 标准化。输入需源音频、≥30 s 目标说话人音频与时间对齐转写。保存修改音频与对齐调节记录。

## 实验与结果
本文为工具/演示论文，未报告独立听感或语用实验数字；动机来自先前游戏配音后编辑中手工改参的成功与繁琐。

## 结论
提供首个支持词级嗓音质量对照刺激制作的工具，便于假设形成与筛选，并期望推动更可控、意图驱动的合成。

## 点评
把可控 VC 接到研究友好工作流，切中“局部语用–嗓音质量”实验痛点。鼻化与所选声门特征关联较弱属已知近似；效果依赖对齐转写与目标说话人样本，跨语种/极端音质外推未验证。
