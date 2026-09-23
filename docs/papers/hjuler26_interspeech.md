# Listenability of Synthetic Speech: On the Effect of Linguistic Registers in Text-to-Speech Input

- 论文编号：894
- 报告人：Maja Jønck Hjuler
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/hjuler26_interspeech.pdf

## 问题

LLM 文本越来越多直接送入 TTS，但其语域是否适合听读未知。既有评测多关注自然度/可懂度，较少测听者加工与记忆负荷；可读性指标也不等于可听性。

## 方法

被试内设计（N=47）：四类输入经同一 Google TTS（澳式口音）合成——ART 对谈广播转写、Wikipedia Simple English（WSiE）、标准维基（WStE）、GPT-4o-mini 生成。测 AIME、NASA TLX 主观努力与线索回忆；并用可读性指标与 Biber MDA 刻画语域。

## 实验与结果

ART 努力显著最高（AIME 62.9、TLX 46.8），书面与 GPT 显著更低且彼此接近（约 25–29 / 15–18）。回忆上 WStE 最高（94.3%），ART 最低（78.7%）。MDA：ART 偏互动口语，WStE 偏正式信息文，GPT 与 WSiE 居中且接近。可读性上 WSiE 最易读，WStE 最难，GPT 居中。

## 结论

作者认为合成语音中，书面/维基源比广播对谈转写更易听；LLM 文本与维基源可听性相当，支持其作为合成输入。研究属初步，语域与话题样本有限。

## 点评

把焦点从“合成器好不好听”转到“输入语域好不好听”，对 agent/播客管线很有现实意义。对谈转写难听可能来自口语纠缠结构经 TTS 朗读后更吃力，而非“口语更自然”的直觉。样本与音色单一，外推需谨慎；也提示“为说话而写”可能比直接喂聊天转写更重要。
