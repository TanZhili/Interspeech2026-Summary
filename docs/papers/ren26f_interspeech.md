# Can Hands Articulate? Kinematic, Acoustic, and Perceptual Analyses of Vowel Production via External Resonators in Kaxi

- 论文编号：1807
- 报告人：Jinyang Ren
- 程序：Tuesday 29 September 2026 / Perception and Appraisal of Prosody
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ren26f_interspeech.pdf

## 问题
源–滤波器模型通常假定声道为滤波器；喉切除等情形下可用电喉换源，但仍依赖内部声道塑形。外部工具能否独立充当滤波器产生可懂元音？中国北方民间艺术“咔戏”（Kaxi）以簧片为源、手势为外部共鸣器，且 f0 常高达约 300–700 Hz，对元音清晰度提出额外挑战。

## 方法
一名熟练咔戏表演者朗读 197 个普通话单音节（a/o/e/i/u）各 3 次，正常语音与咔戏对照；右手 MediaPipe 21 点骨架做 PCA（相对腕部归一化）。VoiceSauce/Praat 测 F0 与 F1–F3，高 f0 下人工调谐共振峰估计，Mahalanobis 去离群后用 Random Forest（500 树）做三共振峰元音分类。24 名听者做五选一元音辨认（正常 vs 咔戏分块，各 10 次重复），混合效应分析正确率与反应时。

## 实验与结果
PCA 前两成分解释约 60.83% 方差，手形在 PC 空间近似舌高/舌前后的元音空间。咔戏 F1/F2 整体抬升、前后对比压缩；RF 测试准确率由正常语音 96.4% 降至 84.1%（i 仍达 99.6%）。共振峰呈阶梯式谐音调谐（如 a 的 F1 在谐音间锯齿对齐）。听者咔戏整体正确率约 0.837（a≈0.996，o≈0.683），反应时显著变长（如 o 约 1522 ms）。

## 结论
作者认为手可作为有效的外部言语滤波器，通过类元音空间的手形与阶梯式共振峰调谐维持可区分性与相对稳健可懂度，并对言语康复中的非侵入外滤波器有启示。

## 点评
把民间咔戏做成可测的源–滤波案例，运动学–声学–感知三联证据较强。单说话人与高 f0 下共振峰估计仍依赖人工检查，泛化到临床装置需更多表演者与连续语流验证。
