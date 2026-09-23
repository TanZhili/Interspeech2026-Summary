# Unified Prosody Restoration Using Diffusion Models for Controllable Text-to-Speech Synthesis

- 论文编号：2942
- 报告人：Yuki Ito
- 程序：Wednesday 30 September 2026 / Speech Synthesis: Speech Features, Codec and Representations
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ito26_interspeech.pdf

## 问题
显式韵律可控 TTS 常要帧级 pitch/VUV/energy，用户难指定又要符合语言（尤其日语音调）的合法结构。已有工作只覆盖局部补全或平滑细化等单一场景，且常预测音素平均韵律、损失帧内细节。

## 方法
把韵律恢复统一为线性逆问题：由退化算子 `H` 从干净韵律得到易指定的退化输入。覆盖五类任务：Inpainting、从平滑/分段平均细化（Ref-S/Ref-A），以及掩码+粗化组合（InpRef-S/InpRef-A）。提出两类扩散韵律恢复器（DPR）：监督版按模拟退化训练并条件于退化 ID；无监督版只在干净韵律上训条件 score，推理用 DDRM（非盲）或 GibbsDDRM（盲平滑核）。恢复结果再送入可条件于 pitch/VUV/energy 的 FS2+flow-matching 声学模型与 HiFi-GAN。

## 实验与结果
日语情感语料 IH（约 31h）与 JVNV。相对 Det/CVAE 基线，Diff-S 与 Diff-U 在多数任务上降低 log F0/energy 误差并改善 PA-ER；主观韵律自然度上 Diff-U-B（InpRef-S）达 4.74、Diff-S 约 4.21–4.22，明显高于基线约 3.4–3.5。JVNV 上趋势一致。盲任务中已知真实退化时 Diff-U-NB 作 oracle 更优。

## 结论
扩散先验可在统一框架下从部分/粗化/二者兼有的输入恢复帧级合法韵律，监督与无监督 DPR 均优于非扩散基线，并更好保持口音相关结构。

## 点评
把多种用户交互统一成线性退化+扩散求解，对可控 TTS 产品流程很实用；无监督路线用逆问题采样扩展未见退化模式。脆弱点在于评价多用 GT duration、日语情感数据规模有限，且盲设定仍假设平滑核参数化，复杂非结构化用户输入未必覆盖。
