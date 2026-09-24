# Harf-Speech: A Clinically Aligned Framework for Arabic Phoneme-Level Speech Assessment

- 论文编号：3472
- 报告人：Ehsan Hoque
- 程序：Thursday 1 October 2026 / Pathological Speech Assessment 4
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/azad26_interspeech.pdf

## 问题
阿拉伯语音素级发音评估对言语治疗重要，但经验证的工具稀缺；商业端到端系统（如 Azure）未针对阿拉伯音系本地化，也缺少与认证 SLP 判断的临床对齐证据。

## 方法
Harf-Speech 模块化流水线：(1) MSA phonetizer 生成参考音素序列并归一化；(2) 微调语音→音素模型（主用 OmniASR-CTC-1B-v2）预测发音；(3) LLM 做词级音素分段，Levenshtein 对齐得到替换/插入/删除；(4) 混合 LCS 比与基于编辑距离的 Accuracy/Completeness（0.6/0.4）得到 PronScore，再与 LCS（默认 0.6/0.4）融合并映射到 0–5 临床量表。在 IqraEval 等本土/合成/真实误发音数据上微调 Wav2Vec2、Qwen3-ASR、OmniASR，并与 Gemini 等零样本多模态对比。

## 实验与结果
音素识别：OmniASR-CTC-1B-v2 PER 8.92%、RTF 0.004，优于 Gemini-3-pro 零样本 15.07%（RTF 10.75）及其他微调模型。临床验证：3 名认证 SLP 独立评 40 句；SLP 间 PCC 0.858–0.927。Harf-Speech 对平均 SLP 分 PCC 0.791、ICC(2,1) 0.659、±1 一致率 76.9%，相对 Azure（PCC 0.635、MAE 0.94）相关更高、MAE 更低（0.79）。

## 结论
开放、本地化的音素级流水线可达到接近专家一致性的临床对齐，并显著优于通用专有评估；模块化便于替换未来 ASR 骨干并迁移到其他语言。

## 点评
把 PER 优化与 SLP 量表相关拆开验证，比只报识别率更贴近治疗场景。40 句临床子集偏小；评分权重与 LLM 分段是经验组件，可解释性依赖对齐错误类型是否被治疗师实际使用。整体路径对低资源语种临床评估有可复制模板价值。
