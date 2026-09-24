# ES-3DF: Editable Speech-Driven 3D Face Reconstruction via Geometry Texture Disentanglement

- 论文编号：433
- 报告人：Ju Zhang
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/wang26i_interspeech.pdf

## 问题
现有语音驱动人脸多为 2D 合成，缺显式 3D、跨视角几何不一致，也难精细编辑；级联「先 2D 再 3D」会误差累积。

## 方法
ES-3DF 直接从短语音重建可编辑带纹理 3D 脸。Disentangle：用 3DDFA V3 抽几何（3DMM 系数）与 StyleGAN2 式 UV 生成器分离纹理。Align：ECAPA-TDNN 提语音特征，ShapeMLP 回归 α_id，TexMLP 对齐纹理；用 Class-Aware Multi-Slot Memory Bank（每说话人 K=4 原型，EMA 更新）与 Multi-Slot InfoNCE 桥接语音–纹理模态差。可微渲染合成 3D 脸，3DMM 系数支持形状/表情/姿态/平移编辑。

## 实验与结果
VoxCeleb1∩VGGFace，1225 人（训练 F–Z 共 924，验证/测 301）。对比 CMP、VoiceStyle：Landmark L1/L2 1.33/19.65，α_id L1/L2 37.56/5.25，优于基线；面部部位 IoU（如 nose 84.55%、skin 87.94%）更高；FaceNet Feature Cos 31.04%（w/ GT α 达 47.15%）。消融显示去掉 3D 解耦或对比学习均下降。

## 结论
几何–纹理解耦 + 多槽对比对齐可直接从语音得到高保真、可编辑 3D 脸，几何与身份一致性优于级联/纯 2D 方法；未来拟加强高维身份特征的跨模态对齐。

## 点评
把「可编辑」落到显式 3DMM+UV，比潜空间粗控更可解释；多槽 Memory Bank 针对纹理高维、身份多原型的设定合理。嘴唇 IoU 仍偏低，作者也承认静态唇形从动态语音反推是病态问题。
