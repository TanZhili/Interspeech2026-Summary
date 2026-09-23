# Pretrained self-supervised speech models can recognize unseen consonants

- 论文编号：2848
- 报告人：Chihiro Taguchi
- 程序：Monday 28 September 2026 / From Self-Supervised Pre-training to Phonetic Analysis of Speech Models
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/taguchi26_interspeech.pdf

## 问题
主流自监督 ASR 预训练语料偏高资源语言，点击辅音等类型学罕见音素几乎未出现；不清楚这些模型能否像普通音素一样识别点击音。作者构建点击丰富的 Khoisan 语数据并系统评估。

## 方法
构建 G|ui 与 West!Xoon 的 ASR 数据（去调、小写等规范化）。微调 Wav2Vec2 系列（xlsr-53、xls-r-300m/1b、mms-1b、mms-1b-all）与 HuBERT（large/xlarge，英语 Libri-Light 预训练），加 CTC 输出层；mms-1b-all 另试适配器。统一超参训练 10 epoch，报告 PER/CER，解码含贪婪、beam、3/5-gram LM。用 Needleman–Wunsch 对齐比较点击、非点击辅音与元音的错误率。

## 实验与结果
更大参数或更多预训练语言未必更好：常出现 300M 优于 1B；单语 HuBERT 在两语上整体最强或很强。仅训适配器、冻结底座时 G|ui PER 约翻倍。点击辅音错误率系统性低于非点击音素与元音（贪婪解码下 Wilcoxon \(W=0,p=0.016\)）；元音易混长度/鼻化等。图示显示按发音方式划分时点击也更稳。

## 结论
尽管预训练几乎不见点击音，全参数微调后模型对点击识别不差甚至更好，表明自监督范式对未见音素有较强适应性；模型规模与预训练语言数并非单调增益。

## 点评
这是音素层面的跨语言泛化检验，而非再推一套新架构：用点击 vs 非点击的对照直接回答“罕见音是否被欠表示”。强在实验设计清晰、统计检验到位。脆弱处在于数据量小、无验证集（G|ui）、点击声学显著性本身可能更容易识别，结论不宜过度外推到所有罕见音类。
