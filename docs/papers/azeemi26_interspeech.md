# Dissecting ASR Failures in Low-Resource South Asian Languages

- 论文编号：1382
- 报告人：Agha Ali Raza
- 程序：Tuesday 29 September 2026 / Multilingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/azeemi26_interspeech.pdf

## 问题
Urdu、Punjabi、Pashto、Sindhi 使用相近 Perso-Arabic / Gurmukhi 脚本、正字法不统一且命名实体常跨脚本出现，现有多语 ASR 多只报聚合 WER，难以区分声学识别失败、脚本解码错误与评测伪影。

## 方法
在 Common Voice 22.0 与 FLEURS 上零样本评测 Whisper-medium / large-v3、MMS-1b、SeamlessM4T-Medium / Large（共 40 配置）。用 jiwer 计算 WER/CER，事后按 11 类错误 taxonomy 分解：脚本混淆、编辑操作、重复循环、数字、正字变体、字符混淆、命名实体、Latin 词、OOV/稀有词、时长、跨语言污染等。实体由 LLM 标注；并对 Whisper 错误脚本输出做音译后处理，对 Perso-Arabic 做 Unicode 归一化后再算 WER。

## 实验与结果
SeamlessM4T-Large 在 8 组中 6 组最优（Urdu FLEURS 16.3%、Punjabi 22.1%）；MMS 在 Sindhi 两集最好。Whisper 在 Punjabi/Pashto/Sindhi 上大量错脚本，WER 常超 100%；音译后处理可回收至多约 25 个百分点 WER。Unicode 归一化平均降低 Pashto WER 3.1 点。稀有词准确率约 20–62%；短句 WER 高于长句；Sindhi 输出中 12–35% 字符来自其他语言（多为 Urdu）。

## 结论
聚合 WER 系统性误判南亚低资源 ASR 失败性质：脚本混淆、Unicode/正字歧义与跨语干扰是主因；语言适配架构更稳，生产级仍远未达到。局限包括 Sindhi CV 仅 40 句、仅零样本未微调。

## 点评
把“听错了”与“写错脚本/评测过严”拆开，对多脚本低资源族很有诊断价值；音译与归一化是低成本可落地的补丁。弱在测试集方言信息缺失、Sindhi 样本极少，且未验证微调后失败模式是否仍以脚本为主。
