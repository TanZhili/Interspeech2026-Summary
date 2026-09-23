# Task-Aware Joint Pruning and Distillation for Efficient Audio Deepfake Detection

- 论文编号：1766
- 报告人：Miao He
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/he26f_interspeech.pdf

## 问题
SSL deepfake 检测器（常 300M+ 参数）难上端侧；ASR 等面向内容任务的剪枝/蒸馏直接搬到伪造检测时，高稀疏度下尤其 OOD 掉点严重。需要任务感知地保住伪造判别结构并迁移跨域知识。

## 方法
三阶段框架：（1）微调预训练 SSL 并算结构单元 movement score（MHA/FFN/CNN）作重要性先验；（2）Hard Concrete 可微结构化剪枝 + 增强拉格朗日满足目标稀疏度，配合跨域无标签蒸馏（19LA train、21LA、21DF、ITW），按 CKA 选代表层（如 {5,14,24}）多层蒸馏；（3）剪枝后 SSL 与 AASIST 后端联合微调。主干为 XLSR-AASIST。

## 实验与结果
相对稠密基线 317M/146.3G，90% 稀疏时约 31.9M/23.3G（约 6.3× FLOPs）。75% 稀疏：ITW 8.43%、ASV5 17.75%、FoR 10.51%，优于 Finetune/HJ/Hybrid 剪枝，并在部分 OOD 上优于稠密基线（ASV5 19.92%、FoR 14.89%）。消融去跨域蒸馏后 21LA/ITW 等显著变差；去 movement 引导也有损失。摘要称多数据集平均掉点约 1.30%。

## 结论
作者认为任务感知剪枝与跨域蒸馏联合，可在激进压缩下保持伪造检测精度与泛化，具备端侧部署潜力。

## 点评
把“伪造相关结构”用 fine-tune movement 显式优先保留，并用无标签跨域蒸馏补监督，针对 deepfake 而非 ASR 压缩是关键点。部分 OOD 优于稠密模型提示过参数化过拟合，但极端 90% 稀疏在 FoR 等上仍明显回退，端侧部署仍需按场景选稀疏档。
