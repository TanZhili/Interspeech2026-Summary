# Towards Dys-XAI: Influence-Based Explanations for Dysarthria Severity Assessment

- 论文编号：538
- 报告人：Xiaoliang Wu
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/wu26b_interspeech.pdf

## 问题
构音障碍严重度自动评估黑盒难获临床信任；常见谱图/声学特征归因不易转成临床可比对的证据，也难体现相邻等级的序数关系。

## 方法
在 TORGO 四类序数分类（typical/mild/moderate/severe）上，用训练轨迹梯度内积近似各训练样本对测试预测的影响 I_i→t，得到支持/对抗样本。按严重度聚合得类级影响矩阵 S，并按序数距离 d 统计 ¯S(d) 检验序数敏感。用控制删除（删高/低影响或随机 5–20%）验证影响分数因果性。基分类器为 80-dim FBank + 单层线性分类器，说话人分层 K-fold。

## 实验与结果
删高影响样本使准确率显著下降（如 moderate 36.8%→0.3%、severe 72.3%→43.1%）；删低影响反而提升（mild 5.5%→17.6% 等）；随机删除 |Δ|<2%。S 呈块对角：同级支持最强；typical 只受 typical 正影响，构音障碍等级间互相正支持。¯S(d) 随 d 单调衰减（13427→1028→−642→−2561）。案例显示影响排名可揪出近静音伪相关训练文件；相对 SHAP 的 OpenSMILE 分数列表，音频参考样本更可听验。

## 结论
基于训练实例影响的解释把决策连到可感知参考样例，并通过删除实验与序数衰减模式验证忠实性，适合临床审计与数据质检。

## 点评
案例式解释对准临床“与原型比较”的推理习惯，且能做数据集审计，比热图更可行动。当前骨干极简、数据以 TORGO 为主；影响计算依赖多 checkpoint，扩展到大模型与更细标注粒度仍需验证。
