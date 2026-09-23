# Toward Open-Set Speaker Attribute Prediction with Keyword-Appended LLM Embeddings

- 论文编号：3203
- 报告人：Byoungjun So
- 程序：Monday 28 September 2026 / Speaker Verification: Advances in Speaker Embeddings
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/so26_interspeech.pdf

## 问题
说话人属性预测若用闭集多标签分类，无法刻画语义渐变，也难泛化到未见属性。把属性放进 LLM 连续语义空间可开放集预测，但原始词义宽泛、流形拥挤，音–文对齐易糊。

## 方法
ECAPA-TDNN 输出对齐 GPT-OSS-20B 的 2880 维属性嵌入；强度加权余弦损失 Lwcos（very/normal/slightly→1.5/1.0/0.5，三标注均值）。关键词拼接（如 “cute speech”）压缩域歧义；top-k 负样本损失 Lnegk：以正样本加权余弦为锚 a，惩罚最相似的 k 个负属性越过 a−m（softplus），总损失 Lwcos+λLnegk（默认 m=0.2, λ=0.5, k=1）。数据 LibriTTS-P（2443 说话人、44 属性）。闭集与同义词零样本（Gemini 生成）上用余弦阈值 τ∈{0.2,0.4,0.6,0.8} 报 micro-F1；几何指标含 Center Sim、Total Variance、PCA Log-det。

## 实验与结果
闭集：提案在最优阈值约 0.7625 F1，优于基准约 0.7286。同义词零样本：speech/voice 等关键词下 F1 接近闭集；无关键词在 τ=0.8 崩溃（约 0.0018）。几何上关键词使流形收缩（如 speech Center Sim 0.8557 vs 无关键词 0.7385）；Lnegk 在更挤的 speech/voice/face 上带来正 ∆F1，在更宽的 man/apple 上增益弱或负。超参见消融：默认配置最优。

## 结论
LLM 嵌入 + 关键词拼接 + top-k 负惩罚可把属性预测做成开放集，闭集也更强；性能与流形紧凑度相关。局限：单语料、单一 LLM，结论句抽取截断。

## 点评
把“可解释说话人关键词”接到开放语义空间，并承认 apple 等无关词也有效——收益更像流形正则而非语义接地。同义词由 LLM 生成、且与训练属性强相关，开放集难度被软化；但对闭集基准的提升仍说明连续目标可行。
