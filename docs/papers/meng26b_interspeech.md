# Learning Global Key Knowledge for Federated Speaker Recognition via Fisher Information

- 论文编号：196
- 报告人：Liang He
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/meng26b_interspeech.pdf

## 问题
联邦说话人识别中客户端数据异构，全局模型聚合后仍残留冗余/偏置信息；本地若整嵌入对齐全局，易学到有害漂移，陷入局部最优。

## 方法
本地训练时用冻结的全局提取器与本地提取器分别得到 e_G、e_K；经临时分类器对 e_G 算对角近似 Fisher 信息，按尺度 s 取前 t=s·D 个高重要性维索引 I；在 I 上切片并归一化得 v_G、v_K，以 1−cos(v_K,v_G) 为 l_FI，与 AM-Softmax 分类损失相加。服务器仍按数据量加权聚合提取器。

## 实验与结果
ECAPA-TDNN（1024 通道）、D=512、s=0.2、E=5、R=20。VoxCeleb1→Vox-O：Ours 各客户端 EER 约 4.15–4.47，优于 FedAvg（约 4.90–5.42）与 FedFSS 等。VoxCeleb2→Vox-O/E/H 均为最优（如 Vox-O 约 1.91–2.18）。VoxCeleb1+CN-Celeb1：Vox-O 3.01、CN-Celeb.Eval 12.58（CN 略逊于 FedFSS 的 12.35，但不额外传额外信息）。消融：无 FIM 随机选维或无维选择均变差；s 在一定范围较稳。

## 结论
作者认为用 Fisher 筛出对任务判别关键的嵌入维，再约束本地向这些维对齐，可在保护隐私的同时减轻异构带来的冗余知识，提升联邦说话人识别。

## 点评
“对齐但只对齐关键维”比整向量蒸馏更贴异构场景。Fisher 经临时头与 CE 估计，重要性定义依赖该代理任务；跨语料上相对 FedFSS 互有胜负，说明维筛选并非处处碾压。
