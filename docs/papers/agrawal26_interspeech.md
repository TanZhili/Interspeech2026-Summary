# Amadea: An AI Companion for Pitch-Aware Spoken Language Practice

- 论文编号：3570
- 报告人：Mrigendra Agrawal
- 程序：Tuesday 29 September 2026 / Speech and Language Learning Technologies
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/agrawal26_interspeech.pdf

## 问题
日语音高重音、普通话声调等对音高敏感语言，现有 CAPT 多固定 prompt 与机械重复，难在自由对话中给韵律反馈。

## 方法
Amadea：课堂模式预写短语 + 对话模式与 AI 同伴闲聊。Whisper 转写推断意图 → gpt-4o-mini-tts 生成母语式参考 → pYIN 提 F0 → 强度轮廓 DTW 对齐 → z 归一化后以 100/(1+d) 得 pitch-pattern score，并可视化分歧。反馈按整句而非单 mora。

## 实验与结果
系统演示文，尚无与专家评分相关或纵向学习增益的定量结果；作者列局限为 ASR 错、F0 噪声、对齐失败及单一参考轨迹。

## 结论
把韵律反馈嵌进结构化与开放对话，使学习者可对自选短语练习音高。

## 点评
设计抓点准（自由对话也能出参考），工程闭环清晰；当前缺外部效度验证，参考单一也可能误罚可接受变体。
