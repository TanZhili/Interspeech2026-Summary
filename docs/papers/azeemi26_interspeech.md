# Dissecting ASR Failures in Low-Resource South Asian Languages

- 论文编号：1382
- 报告人：Agha Ali Raza
- 程序：Tuesday 29 September 2026 / Multilingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/azeemi26_interspeech.pdf

## 问题
乌尔都语、旁遮普语、普什图语、信德语覆盖约 3.5 亿人，共享 Perso-Arabic/Gurmukhi 等邻近文字、正字不统一与混合脚本命名实体；现有多语 ASR 多只报聚合 WER，无法区分声学识别失败、脚本解码错误与评测伪影。

## 方法
在 Common Voice 22.0 与 FLEURS 上零样本评测五模型（Whisper-medium/large-v3、MMS-1b、SeamlessM4T-Medium/Large），共 4 语×2 集×多模型配置。用 jiwer 算 WER/CER，再按 11 类错误分类法事后分解：脚本混淆、正字变体、字符混淆、命名实体、OOV/低频词、句长、跨语污染、数字、转写、编辑操作、重复循环。命名实体用 LLM 标注（PER/LOC/ORG/MISC）；对 Whisper 错误脚本输出做基于规则的转写后处理；对 Perso-Arabic 做 Unicode 归一化后再算 WER。

## 实验与结果
SeamlessM4T-Large 在 8 个语–集对中 6 个最优（乌尔都 FL 16.3%、旁遮普 FL 22.1%）；MMS 在信德两集最优。Whisper 在三语大量输出错误脚本（如旁遮普 CV medium WER 104.7），剔除后普什图可降约 68 pp；转写后处理使旁遮普 medium WER 降 25.0 pp（104.7→79.7）。Unicode 归一化平均降普什图 3.1 pp WER。实体比非实体难 5–20 pp；低频词准确率仅 20–62%；短句（1–5 词）均值 WER 约 76% 高于长句约 46%；信德输出中 12–35% 字符来自相关语（主要为乌尔都）。

## 结论
聚合 WER 会误判南亚多脚本 ASR 失败主因：脚本混淆、Unicode/正字歧义与跨语干扰是结构问题；语言适配器架构更稳，转写后处理与归一化可无重训回收大量误差。局限含信德 CV 仅 40 句、仅零样本未微调。

## 点评
把“听错”和“写错/评测罚错”拆开，对 Perso-Arabic 与近亲脚本族很有针对性。强在 11 维 taxonomy 与可落地的后处理；弱在零样本设定与极低资源集规模，难以直接外推到真实口语与微调部署。
