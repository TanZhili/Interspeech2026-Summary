# Membership Inference Attacks against Large Audio Language Models

- 论文编号：514
- 报告人：Jia-Kai Dong
- 程序：Monday 28 September 2026 / Evaluation of Speech and Audio Analysis
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/dong26_interspeech.pdf

## 问题

LALM 训练于大规模音文数据，可能记忆敏感说话人—内容绑定，但音频域成员推断（MIA）标准缺失。常见基准训练/测试存在声学分布偏移，盲分类器即可近乎完美分开，导致 MIA “成功”可能只是域分类而非记忆。

## 方法

对 Audio-Flamingo 3 与 Music-Flamingo（训练数据可公开核对）做首个系统样本级 MIA 审计。三相框架：(1) 多模态盲基线：仅用元数据、文本 TF-IDF、声学低层统计训练逻辑回归，量化分布捷径；(2) 两阶段生成（自解码再自条件打分）聚合 PPL、熵、Min/Max-k%、Rényi、zlib、概率间隔等指标做 MIA；(3) 模态解耦：静音、噪声、TTS/TTA 重合成，检验跨模态绑定。在分布匹配（盲 AUC≈0.5）数据上解读真正记忆。

## 实验与结果

跨数据集配对可出现 AUC≈1.0 的域捷径；LibriSpeech 等 MIA 高分与声学盲基线高度相关（如声学盲 AUC 99.8，r≈0.78）。在 SPGISpeech、Clotho 等干净集上 MIA 塌向随机（约 50.7–52.4）。解耦实验中，原始条件存在的弱信号在静音/噪声/重合成后显著消失（p<0.05），支持记忆来自特定嗓音身份与文本的绑定而非孤立文本或声学指纹。

## 结论

报告 LALM 的 MIA 必须伴随盲基线诊断；控制分布偏移后，样本级 verbatim 记忆证据弱，但隐私风险集中在说话人—内容跨模态绑定。代码已公开。

## 点评

核心贡献是方法论纠偏：先证明“高 AUC 不等于高记忆”，再在干净数据上定位跨模态绑定威胁模型，对音频隐私审计很有建设性。脆弱点是仅两家具开放数据的模型、干净集上绝对泄露信号本就弱，外推闭源大规模 LALM 需谨慎。作为学术隐私审计综述式总结，不提供可复用攻击操作细则。
