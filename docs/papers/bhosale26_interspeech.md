# Echoes after Edits: Room Impulse Response Estimation for Geometry Update

- 论文编号：2514
- 报告人：Yoshiki Masuyama
- 程序：Tuesday 29 September 2026 / Spatial Audio 2
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/bhosale26_interspeech.pdf

## 问题
室内轻微几何编辑（挪移/移除家具）会显著改变 RIR；声学仿真要精细材料标注，场插值又要在编辑后重测多个参考 RIR，日常场景都不现实。

## 方法
提出 edit-conditioned RIR 估计与 PG-RIR：用编辑前后网格在 \(M\) 种全局均匀材料下仿真 proxy RIR，与实测编辑前 \(r_0\) 一起估计编辑后 \(r_1\)。ResNet-18 编码 log 幅度谱，融合 type/material 嵌入；上下文查询注意力 + 频带门控超网络预测残差谱，相位沿用 \(r_0\)。损失：谱 L1 + 带状衰减曲线。iGibson 14 场景、AcoustiX 仿真构建 143k 声源–接收对（训练以移除为主）。

## 实验与结果
Leave-one-scene-out：PG-RIR \(T_{60}/C_{50}/EDT\) 误差低于 identity 与 xRIR（K=4/8）；编辑幅度越大优势越明显。相对 DiffRIR 反演–前向渲染，在 9/34 表面场景均更优且无需每场景反演。仅训移除却可零样本推广到平移编辑；多步链式预测会累积谱平滑。

## 结论
用同质材料 proxy 把几何变化编码为声学线索，可在无新测量与无精细材料标注下更新 RIR；未来拟用课程学习加强平移序列。

## 点评
任务定义清晰：把“场景改了怎么办”从重测/重标注改成条件化残差预测。Proxy 差分解耦几何与材料是关键设计。目前证据主要在仿真；链式编辑的早期瞬态抹平是部署隐患。
