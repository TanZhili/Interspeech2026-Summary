# Phonetic evidence for contrastive length in Nakanamanga monophthongs

- 论文编号：1597
- 报告人：Shubo Li
- 程序：Wednesday 30 September 2026 / Diphthongs and Monophthongs
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26z_interspeech.pdf

## 问题
瓦努阿图中部大洋洲语 Nakanamanga 是否有音系性元音长短对立、且是否覆盖全部五个元音音色，此前仅有最小对立对论证，缺少时长声学证据。

## 方法
14 名母语者（8 女 6 男）朗读 50 词表（双音节 CV.CV，目标在首音节），载体句中五次重复；Praat 手工切分，EMU/emuR 提取时长。共 2,622 token。线性混合效应模型：Duration ~ VowelLength + VowelQuality + WordLength + (1|Speaker)+(1|Word)，并检验 Length×Quality 交互。

## 实验与结果
短元音均值 85 ms，长元音 177 ms，比值 2.08；Length 主效应约 +82.6 ms（p<.001）。五音色比值 1.88–2.24，各对均显著；Length×Quality 交互不显著，说明长短差距跨音色稳定。闭元音本征更短、词长有轻微压缩，但不掩盖长短对立。

## 结论
时长为 Nakanamanga 全系统短–长对立提供清晰语音证据，支持十元音（五对）音系分析，并与同区域 Nafsan（约 1.91）等数量语言可比。

## 点评
用受控词表 + 混合模型把“词典里的冒号”落到可重复的声学比率，对低资源大洋洲语描写很关键。词表中短元音多落在动词、诱发略偏，但效应量足够大；后续应补感知实验与自然语流/社会语言学变异。
