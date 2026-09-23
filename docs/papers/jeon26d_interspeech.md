# ParaPairAudioBench: Paralinguistic Pairwise Audio Benchmark for LALM-as-a-Judge

- 论文编号：2021
- 报告人：Jisu Jeon
- 程序：Monday 28 September 2026 / Paralinguistics
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/jeon26d_interspeech.pdf

## 问题

大音频语言模型（LALM）已常被当作生成语音的自动评委，但先前多盯整体自然度，细粒度副语言属性是否判对、能否在模糊时弃权（Tie）、是否依赖文本线索与呈现顺序，仍缺乏可控诊断。自然度总分会掩盖“全局节奏强、局部强调弱”等行为差异。

## 方法

构建 PARAPAIRAUDIOBENCH：5175 对音频，覆盖 Style、Rate、Emphasis、Age、Gender 五维；每例三选一（A / B / Tie）。数据来自 Expresso、Sonos Voice Control Bias Assessment、LibriTTS、EARS 等官方测试切分，并按标签、转录控制与平衡约束筛选。Non-Tie 对比目标/非目标；Tie 在 Style/Age/Gender 上平衡 Both Good / Both Bad，Emphasis 仅 Both Bad，Rate 不含 Tie。约 47% same-transcript、53% cross-transcript，以区分声学依赖与词汇依赖。评测 Gemini 2.5 Flash、GPT-4o Audio、SpeechJudge-7B、Kimi-Audio-7B、Qwen2.5-Omni-7B；交换 A/B 顺序测位置偏置；人类基线为每准则 50 题、6 名评分者（Fleiss’ κ=0.67）。

## 实验与结果

人类平均准确率 79.2%，最强模型 Gemini 2.5 Flash 为 61.5%（平均落后约 17.7%p；摘要亦写相对人类平均落后约 32%p）。Rate 上模型相对较强，Emphasis 等局部韵律更弱。普遍校准失败：Non-Tie 可较高而 Tie 骤降（如 Gemini Emphasis NT 82.3% vs T 19.3%；SpeechJudge 多维 Tie 近乎从不选）。Style 在 same-transcript 明显高于 cross-transcript（Gemini 83.8% vs 36.6%），Emphasis 则相反，显示模型对局部突显敏感不足、对 Style 过度依赖词汇。位置偏置可达约 29.4%p（SpeechJudge）。Age 对人类也难（κ=0.365），Gemini 略超人类约 3.8%p。

## 结论

该基准把副语言评委能力拆成准则区分、Tie 校准、转录敏感性与顺序鲁棒性；现有 LALM 评委整体仍逊于人类，并暴露强制偏好、模态依赖不对称与位置偏置等系统性失效，单看自然度总分看不见这些点。

## 点评

贡献主要在评测协议设计：把“会不会判副语言”变成可分解诊断单元，尤其是 Tie 与 same/cross-transcript 对照，能把“看起来准”拆成真声学能力 vs 文本捷径。对 LALM-as-a-Judge 落地很有用。脆弱点包括 Rate 无 Tie、Emphasis Tie 仅 Both Bad、部分语料与模型可能预训污染虽已尽量用测试切分；人类子集仅 250 题，Age 本身主观噪声大，绝对数字需结合置信区间解读。正文末尾抽取有截断，结论以上述可读部分为准。
