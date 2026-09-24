# Does Translation-Enhanced Speech Encoder Pre-training Affect Speech LLMs?

- 论文编号：3241
- 报告人：Tomoya Mizumoto
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/mizumoto26_interspeech.pdf

## 问题
Speech LLM 常用 ASR/SSL 编码器，表示偏语言特异，与 LLM 统一语义空间错位；Whisper 类预训练多为 X→en 单向翻译，英语输入侧未必学到跨语语义抽象。

## 方法
控制实验：Whisper-medium 式 Seq2Seq 编码器在 en/ja/zh/de（约 130k 小时，翻译目标由 Qwen2.5-32B 合成）上比较三种目标——仅 ASR、ASR+X→en、ASR+双向 X↔en（统一 75:25 转写/翻译比例，英文亦做 en→X）。丢弃解码器，接冻结 Llama-3.2-1B/3B，只训 CNN+线性 adaptor（约 6.2k 小时多任务），评 ASR/ST/意图/情感。

## 实验与结果
双向配置在 ASR 与 ST 上整体最优；1B 上日语 CER 29.2→19.7，en→X（含预训练未见的 fa/id/sv/tr）明显提升。3B 意图分类：双向使英语 57.3→64.5、德语 57.9→66.3；情感识别几乎不受预训练目标影响。解冻编码器时双向仍领先。

## 结论
编码器预训练加入双向翻译能改善与冻结 LLM 的跨模态对齐，并更好解锁其多语能力；增益对语义类任务明显，对依赖细粒度声学的情感任务有限。

## 点评
用“冻结 LLM、只换编码器目标”干净隔离因果，指出 Whisper 式不对称翻译对英语输入的盲区。合成平行数据规模与四语子集是现实折中，但也可能引入翻译噪声；情感无增益说明翻译目标主要塑形语义而非副语言表征。
