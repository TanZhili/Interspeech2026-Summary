# SayCheck: Gamified Speech Practice and Attribute-Based Speech Analysis for Children

- 论文编号：3598
- 报告人：Mostafa Shahin
- 程序：Tuesday 29 September 2026 / Speech and Language Learning Technologies
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shahin26_interspeech.pdf

## 问题
儿童言语治疗需反复家庭练习，动机难维持；传统音素级误读检测难说明“错在哪些发音特征”。

## 方法
SayCheck = Say Bananas（马里奥式横版游戏，收星触发目标词录音）+ PhoneAid。治疗师可按音素/位置/词长配置目标。PhoneAid：澳大利亚儿童语料训的 wav2vec2 + 音系属性层，SCTC-SB 多标签序列预测；对齐后同时报音素替换/增删与属性（嗓音、鼻音、部位、元音高低前后等），汇总 PCC/PVC 与属性准确率。

## 实验与结果
演示工作流；强调属性级比纯对错更利于临床解读。正文未给新的大规模临床疗效数字。

## 结论
游戏化诱发与属性级分析可结合，支持可扩展儿童家庭言语练习与诊断反馈。

## 点评
产品闭环完整，属性分解贴临床；演示文性质，外部效度与儿童模型误差率待更多报告。
