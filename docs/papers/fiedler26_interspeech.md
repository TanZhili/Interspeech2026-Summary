# Contrastive Time-Proximity Pre-Training for Speech-Based Heart Failure Monitoring

- 论文编号：424
- 报告人：Nicholas Cummins
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 1
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/fiedler26_interspeech.pdf

## 问题
心衰（HF）急性失代偿（ADHF）需尽早发现；液体潴留可改变声道，但既往声学生物标志多依赖持续元音与患者主动配合，难以用于日常自然语音监测。手工声学特征对内容、时间与录音条件敏感，且缺乏直接刻画 HF 状态的特征。

## 方法
提出对比时间邻近（CTP）自监督预训练：在同一患者纵向录音上，≤3 天对拉近嵌入、≥100 天对推远（余弦 embedding loss，margin=0）。骨干改编 d-vector：mel 谱切 160 帧段，双向 LSTM + 帧注意力得段嵌入，再经段注意力聚成 256 维录音表示（约 4.5M 参数）。评估三档输入：A(16 kHz, 40 mel，可从说话人验证 checkpoint 初始化)、B/C 更高采样率与 mel 维。下游将入院（wet）相对出院（dry）作排序任务，用冻结特征的 XGBoost Ranker 或联合微调的 Neural Ranker；Level 1 为 Charité 留一患者交叉验证，Level 2 将 Level 1 集成测 Mayo。预训练数据为 Noah Labs 远程监测约 5.2 万条德语自然语音（392 人）；临床评估为 VAMP-HF 两中心共 68 名 ADHF 患者。

## 实验与结果
CTP 预训练上近端相似度明显高于远端。Level 1：经典 29 维声学特征 XGBoost 准确率最高 0.62，CTP-A 约 0.58–0.61，人类标注约 0.55。Level 2 跨中心跨语言：经典特征跌至 0.34，CTP-A 仍约 0.59–0.61；无 CTP 的 d-vector 接近随机。Level 2 差异因样本量小未达统计显著。注意力峰值常落在呼吸相关停顿，与人类“呼吸”线索一致。

## 结论
CTP 能从弱标注纵向自然语音学到对 ADHF 有预测力的表示，并较经典特征更利于跨中心泛化；注意力指向呼吸段，提示生理相关性。局限：N=68、探索性比较、无连续失代偿度量、代码未公开。

## 点评
用疾病渐进性把时间邻近变成对比监督，避开对临床终点的强依赖，抓的是“同人纵向状态变化”而非说话人不变性。强在跨语言诊所仍稳住、且段注意力可解释；弱在临床队列小、阈值未系统扫、预训练目标与下游最优配置不一致（B/C 预训练更好但下游更差）。
