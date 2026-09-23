# Turning Speech Language Models into Multilingual Listeners

- 论文编号：2584
- 报告人：Tolúlọpẹ́ Ògúnrẹ̀mí
- 程序：Tuesday 29 September 2026 / Multilingual Speech 1
- 技术分类键：multilingual
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ogunremi26_interspeech.pdf

## 问题
开源 Speech Language Models（SLMs）多偏向英语及少数高资源语，根因是多语语音指令微调数据稀缺；现有 SLM 评测也几乎只有英语上的复杂生成任务，难以衡量多语听–答能力。

## 方法
基于英文 Voice Assistant 400K，用 SeamlessM4T v2 Large 译到 Aya Expanse 覆盖的 22 种目标语，再用 XTTS（15 语）、SeamlessM4T 或 MMS TTS（其余）合成问题语音，得到 MULTISPEECHQA：约 1080 万 spoken QA、9200 小时、23 种类型多样语言；人工评自然度平均约 3.0、内容理解约 4.1。测试集中每语 200 条经 Prolific 人工校对（约 72% 需改），并与 CommonVoice ASR、CoVoST-2 AST 拼成 MULTISPEECH-BENCH。评测用 Command-A / GPT-4o 作 LLM-as-a-judge 的成对偏好；级联基线为 Whisper Large v3 + Aya Expanse 8B。随后对 Qwen2.5-Omni 做 LoRA（rank 32）约 3 epoch 微调。

## 实验与结果
开源 SLM 中 Qwen2.5-Omni 最强，但多数在未见语上弱于 Whisper+Aya 级联；闭源中 GPT-Audio 领先，Gemini 2.5 Pro 次之，Flash Lite 未过级联。Qwen2.5-Omni 平均 ASR 错误率 49.7、BLEU 22.7、chrF 46.6，AST 可超级联。人机法官一致性：相对级联，Qwen2.5-Omni 约 75.6% 一致（κ=0.186），GPT-Audio 约 52.4%。微调后相对原 Qwen2.5-Omni 在 23 语上平均胜率约 60.6%，希伯来/希腊/波斯等更多打平；ASR WER 49.7→50.4、AST BLEU 22.7→21.0，核心识别/翻译基本不变。抽取文本在“训练数据配比如何影响 SLM”一节开头截断。

## 结论
高质量合成多语指令数据是廉价扩展 SLM 多语能力的路径；MULTISPEECHQA 微调显著抬升口语 QA，且不明显伤 ASR/AST。作者公开数据、基准与权重以服务更多语言使用者。

## 点评
核心假设是“有可用 MT+TTS 就能合成够用的指令数据”，用级联强基线压开源端到端模型，再证明 LoRA 微调主要补生成式听答而非刷 WER。强处是语言覆盖与人工校对评测子集；脆弱处在合成自然度偏低、LLM 法官 κ 低、以及希伯来等低 TTS 质量语上收益有限——多语听懂仍受合成链路质量上限约束。
