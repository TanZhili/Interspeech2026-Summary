# On the Robustness of Speaker Embeddings for Cross-Domain Speaker Retrieval

- 论文编号：1796
- 报告人：Chuanqi Huang
- 程序：Monday 28 September 2026 / Speaker Verification: Advances in Speaker Embeddings
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/huang26m_interspeech.pdf

## 问题
实际说话人检索（SR）是阈值无关的 1:N 排序，与依赖阈值的验证（EER）不同；跨信道、噪声、跨语、老化等域移下，低 EER 模型仍可能严重排位倒置。冻结预训练嵌入在检索约束下的排序稳健性与无训练后端校准是否有效，缺乏系统评测。

## 方法
六种 3D-Speaker 预训练模型（CAM++、ECAPA-TDNN、ERes2Net、x-vector、RDINO、SDPN）在 VoxCeleb2 上训练后直接部署。四类失配：信道（VoxCeleb2 宽带到电话/网络编解码）、声学环境（VOiCES 近场查询→远场库）、语言（TidyVoice 英↔非英）、年龄（voxAging 早期→中/晚期）。每场景随机 100 目标说话人，每人 10 查询+10 库内真值，其余说话人作库外干扰；余弦打分，报 P@10 与 mAP。另用 Adaptive Symmetric Normalization（ASN）：选高分伪冒认 cohort 估计局部分数统计，训练无关地标准化相似度。

## 实验与结果
信道：匹配 O→O 上 ECAPA P@10 达 92.72%；电话滤波下 ERes2Net 更稳（T→O mAP 62.96% vs ECAPA 43.44%）；O→T 普遍优于 T→O。环境：P@10 下降但 mAP 均 >95%，ERes2Net 最高 98.50%；自监督 RDINO（74.03%）可超监督 x-vector（71.79%）。跨语：非英→非英优于英→非英；ERes2Net 英→非英 P@10 54.69%，RDINO 仅 25.66%。老化：早期→晚期全面下降，ERes2Net 55.26%→50.41%。ASN 在 T→N 上普遍提升（如 ERes2Net P@10 40.70→43.76；SDPN mAP 17.48→28.59）。

## 结论
监督多尺度模型更抗信道与老化，但受英语预训练偏置易过拟合音系；自监督对房间声学更稳、跨语更弱。ASN 后端校准可恢复跨信道排序一致性，无需微调前端。

## 点评
把评测从验证阈值切到带干扰库的检索排序，切中工程痛点；方向性不对称（干净查询 vs 失真查询）观察有用。ASN 是实用补丁而非表示学习突破；评测说话人/句采样随机，跨论文复现时需注意协议细节。
