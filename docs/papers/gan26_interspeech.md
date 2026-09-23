# L2 Speakers Accommodate Differently to AI and Human Voices Across Phonetic Features

- 论文编号：2605
- 报告人：Elisa Pellegrino
- 程序：Tuesday 29 September 2026 / Cross-Linguistic and L2 Phonetic Studies
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/gan26_interspeech.pdf

## 问题
语音调节（phonetic accommodation）已在人–人与人–设备互动中被研究，但 L2 群体是否对 AI 与人类声音表现出同样模式、以及不同语音特征上是否一致，仍不清楚。这对 TTS 用于 L2 发音训练有直接意义。

## 方法
28 名女性汉语母语、英语 L2（CET-6）被试，交叉设计两场影子跟读（间隔 10 天）：Microsoft Azure neural TTS（en-US-LunaNeural）与 ALLSSTAR 女性母语人类声音，外加基线朗读。分析归一化 VOT、/i/–/ɪ/ 时长比（DR）与频谱距离（SD），以及时长类与强度类节奏指标；用 difference-in-distance（DID）量化向模型收敛，线性混合效应比较 AI vs Human。

## 实验与结果
VOT：人类声音收敛更强（p=.008）。DR：AI 条件调节更大（p<.001）。SD：无显著差异。时长类节奏两场均无稳健模型差异；强度类节奏 AI 优势显著（p<.001）。会话效应大体不显著。

## 结论
作者认为 L2 对 AI/人类声音的调节也是特征依赖的：人类更利于 VOT 等细粒度连续线索，AI 更利于相对时长对比与强度节奏；二者在发音教学中可能互补。未来应扩展更多声音/特征、互动任务，并加入母语对照组。

## 点评
研究把现代 neural TTS 与人类声音直接对比，并用 DID 跨多特征统一操作化，对 L2 教学场景贴近。解释偏依赖“AI 更规律、人类更自然变异”的事后叙事；未盲测时被试是否能区分声音身份虽有访谈，但声学上人类优势也可能来自该具体说话人的显著送气等特质，外推到一般 TTS 仍需谨慎。
