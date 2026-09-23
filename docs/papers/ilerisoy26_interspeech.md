# Zero-Shot Respiratory Sound Classification through LLM-Augmented Audio-Text Alignment

- 论文编号：2235
- 报告人：Mustafa Talha İlerisoy
- 程序：Tuesday 29 September 2026 / Multimodal and Non-Speech Healthcare Applications
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ilerisoy26_interspeech.pdf

## 问题
自监督呼吸音编码器缺临床语义锚定，难零样本诊断；通用音频–文本模型（CLAP 等）缺医学用语，且真实音频–报告配对稀缺。

## 方法
REACH：用医学 LLM 由元数据合成结构化听诊报告作语义锚；冻结医学文本编码器，优化音频投影与骨干；sigmoid 对比损失 + 原生 SSL 重构损失防特征崩坏；FAISS 相似感知负采样拉远病理边界。在 6 数据集 9 任务上评零样本与线性探针。

## 实验与结果
零样本平均 AUC 61.3%，高于 CLAP 51.4% 与 Qwen2-Audio 54.9%；线性探针平均 AUC 71.6% 最高，且仅用全规模基线约 43% 的数据。对齐后仍保持单模态能力。

## 结论
结构化语义对齐可把领域呼吸编码器变为可零样本的多模态工具，效率与效果优于更大通用音频语言模型。

## 点评
关键洞察是“对齐而非从头训医学 CLAP”，LLM 合成报告缓解配对稀缺。强在数据效率与零样本；合成文本质量与元数据覆盖决定上限，临床部署仍需分布外病理与设备变异验证。
