# Should Robots Sound more like Machines than like Humans? User Expectations Affect the Perception of Prosody in TTS Voices

- 论文编号：3075
- 报告人：Ha Eun Shim
- 程序：Tuesday 29 September 2026 / Prominence, Stress and Focus
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/shim26_interspeech.pdf

## 问题
TTS/机器人语音设计常把自然度、情感、音色等与可懂度分开讨论；但对依赖韵律边界消歧的句法歧义句，这些“超语言学”线索可能改变理解。本文问：在机器人化身交互中，把声音做得更情感化/更单调，或更机器感/更人感，会如何影响听众对逗号所标韵律边界的感知与可懂度。

## 方法
刺激为 Direct Address 与 List 两类歧义句对（With/Without Comma），另有 tense/lax 元音 filler；每人听 40 句。基线用人声微调的 Matcha-TTS（Human-like Affective），再用 Praat 降 pitch 变异 40% 得 Monotonic，用 Delay 0.02 s + Amplitude 0.5 Pa 得 Machine-like，交叉共 4 种音色。被试间设计：160 名英语母语者（Prolific，19–30 岁）各听一种音色，与机器人化身做图片匹配“训练”任务（判断语音是否匹配目标图），再填 MOS-X2/Godspeed 类问卷。主要分析为混合效应逻辑回归（Picture Match × Voice Condition × Comma）及问卷累积链接模型。

## 实验与结果
训练任务：Picture Match、Comma 及二者交互均极显著；三维交互显著（χ²=9.93, p=.019）。整体上 Without Comma 更易判对（听众常听不出边界）；对比显示 Machine-like 相对 Human-like 在 With Comma 条件下准确率更高（β=−0.51, z=−2.29, p=.022），congruency 对比也有较小效应。Affective vs. Monotonic 对可懂度无实质影响。问卷：Voice Condition 主效应/与题项交互均不显著；事后看 Affective 更自然（p<.01），Human-like 略更“聪明”（p=.064）。

## 结论
对 TTS 句法歧义句，韵律边界本身很难被听出；单纯改变 pitch 情感幅度几乎不改善消歧可懂度，但使音色更机器感反而提高 With Comma 条件下的理解——作者认为这改变了用户对机器人语音能力的期望，从而偏置或促使听众去听那些本难察觉的边界。局限包括被试间设计无法直接比较音色、听努力等机制尚未测量。

## 点评
这篇把 HCI 里常见的“更自然人声更好”直觉反过来：与边界无关的 indexical 音色操纵，通过期望通道影响了本该由韵律决定的消歧。实验设计干净（同一 Matcha 输出上做正交操纵），也因此把效应锚定在期望而非额外韵律线索上。脆弱点在于机制仍是事后解释（期望 vs. 更仔细听），且 Without Comma 接近天花板，Machine-like 优势主要体现在 With Comma 一侧。
