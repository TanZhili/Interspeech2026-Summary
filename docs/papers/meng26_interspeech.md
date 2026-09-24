# A Federated Learning-Based Speaker Recognition Method with Dual Classification Heads

- 论文编号：25
- 报告人：Liang He
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/meng26_interspeech.pdf

## 问题
机构级联邦说话人识别中，各客户端说话人集合互斥、分布异构；仅靠本地分类头训练时，模型只能经聚合间接获得全局知识，跨客户端信息融合不足。

## 方法
提出 FedDCH：本地同时维护局部分类头（C_k 类）与全局分类头（全体 C 类），联合损失 α L_global+(1−α)L_local 指导 ECAPA-TDNN 嵌入提取器；本地更新后按 speaker ID 将局部类向量写入全局头对应位（β 混合），上传提取器与全局头。服务器对提取器用数据量加权 FedAvg；对全局头按 speaker-ID 加权矩阵（含优势因子 μ）聚合后再下发。

## 实验与结果
VoxCeleb2 按说话人均分为 4 客户端：相对本地训练平均 EER 改善约 46.5%，相对 FedAvg 约 7.6%；Vox-O 上 FedDCH 各客户端 EER 约 2.31–2.54（FedAvg 约 2.52–2.73）。VoxCeleb 与 CN-Celeb 四客户端联合：相对本地约 68.8%、相对 FedAvg 约 5.4%。消融显示双头联合优于仅本地或仅全局头；全局损失用 CE / AM / AAM 均较稳。

## 结论
作者认为在更贴近“组织为客户端、说话人互斥”的设定下，双分类头能更直接注入全局分布知识并缓解异构；加权聚合进一步保留充分训练过的说话人判别信息。

## 点评
把“全局类空间”显式请进本地训练，比只在聚合后对齐更直观。全局头维度随总说话人数增长，通信与内存成本正文未细算；Vox-H 上并非所有客户端都最优，难例仍有优化空间。
