# PhonLLM: Joint Phone Recognition and Phonological Process Inference for Child Speech

- 论文编号：3378
- 报告人：Ilja Baumann
- 程序：Tuesday 29 September 2026 / Prosody, Pronunciation and Specialized Speech Processing
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/baumann26_interspeech.pdf

## 问题
儿童言语临床筛查需要音位级诊断反馈，ASR 转写 alone 不够；传统 MDD/CAPT 多针对 L2 或独立错误分类，缺少把期望发音与实现发音之间的音韵过程（如 fronting、backing、deletion）显式标出的结构化预测，且过程标注昂贵。

## 方法
提出 phonological process inference：输入声学 a 与由正字法经 eSpeak G2P 得到的期望 phone 序列 x，输出带过程标签的规范 phone 序列 y。PhonLLM：wav2vec 2.0（OmniASR，300M）音频帧每 r=5 帧下采样投影后，与期望 phone embedding 拼接，送入冻结 LLaMA-1B，仅训 LoRA（r=16, α=32）与音频投影。两阶段：先在成人多语数据（CommonVoice、MLS 等，约 9.8k 小时）做跨语种 phone 识别；再在儿童数据上联合预测 phone+过程标签。规则增强：对规范 IPA 施加 fronting/backing/deletion 改写得到训练用“期望”序列，目标仍为规范 phone 加过程 tag；采样概率 fronting 0.30、backing 0.60、deletion 0.12、仅识别 0.30。临床 PhonBank 数据仅用于评测。

## 实验与结果
基线平均：冻结 LLM 上下文 F1 50.2；精调文本 oracle F1 89.0；XLSR-53→精调 LLM 级联 F1 48.5（XLSR PER/AW-PER 58.0/26.2）。PhonLLM 平均 tagging F1 75.9（chance 19.2），PER/AW-PER 23.5/12.6，相对 XLSR PER/AW-PER 降约 59.5%/51.9%。Fronting 最稳（多数据集 F1 约 80+），backing/deletion 更难。去掉期望序列条件后模型不再输出过程标签。Másdóttir 按年龄分层：AW-PER 从约 18.83（2y）降至 9.54（7y），tagging F1 约稳定在 74 附近。

## 结论
轻量 speech–LLM 可联合恢复规范发音与音韵过程标签，规则增强可规模化注入监督；联合建模相对 ASR 级联提升 tagging 与降低 PER。局限包括过程库存仍窄（计划加 deaffrication、cluster reduction、stopping 等），backing/deletion 仍弱。

## 点评
把“纠错”改写成“相对期望发音的过程变换”，并用期望序列作触发条件，消融清楚说明过程标签不是无从声学无条件学出的。规则改写解决标注瓶颈，但训练过程分布与临床自然过程可能错位；临床集规模小、德语 recall 偏低，部署前需警惕增强规则与真实病理过程的覆盖差。
