# WSG: Clinically-Informed Weighted Speech Graphs for Dementia Detection

- 论文编号：2266
- 报告人：Yao Xiao
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/xiao26b_interspeech.pdf

## 问题
传统 speech graph 把词当抽象节点，忽略语义/音系切换与图画描述中的空间信息，难以编码流畅任务切换与 CIU 空间组织等临床线索。

## 方法
提出加权语音图（WSG）：只从目标词建图（SVF 动物词、PVF 以 p 开头真词、CTD 的 CIU），边权编码语义（ConceptNet Numberbatch）、音系（SoundVectors）、空间（Cookie Theft CIU 坐标）与时间间隔的距离/相似度。提取直径、ASP、密度、ATD 等加权拓扑特征，用朴素贝叶斯分类；在 CognoMemory 上嵌套交叉验证做 SFS 特征选择，再迁移到 ADReSS。开源 PyWSG。

## 实验与结果
相对「全词+基线特征」，仅用目标词显著提升（如 CognoMemory PVF F1/AUC 0.55/0.56→0.75/0.75）。SFS 常只选 1–2 个加权特征即可与完整基线集相当：PVF 常选 diameter(phon)（痴呆组均值 2.8 vs HC 5.3）；SVF 偏时间加权直径；CTD 偏空间加权 ATD/ASP+WC。ADReSS CTD 上最终子集 F1/AUC 0.73/0.75，接近目标词基线全集。

## 结论
少量临床可解释的加权图特征即可达到与完整基线相当的检测性能，并与痴呆组切换减少、空间组织变差等观察一致。

## 点评
把临床上已强调的切换、CIU 空间与时间间隔直接写进边权，比纯拓扑计数更可解释。目标词过滤同时隐式编码正确词数，收益一部分可能来自任务相关词计数而非图结构本身；CognoMemory 依赖 WhisperX 转写，对齐误差会传导到时间权。
