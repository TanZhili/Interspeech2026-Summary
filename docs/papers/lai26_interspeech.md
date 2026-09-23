# Lung-CL: Spectrum-aware Distillation and Generative Replay for Continual Learning based buffer-free Respiratory Sound Classification

- 论文编号：1199
- 报告人：Qinben Lai
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 1
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lai26_interspeech.pdf

## 问题
跨医院、设备与人群部署呼吸音分类时，域增量学习易灾难遗忘；存真实样本的 replay 触碰隐私（GDPR/HIPAA），而通用 buffer-free 蒸馏又忽略呼吸音时频稀疏、病理线索集中在高能量窄带的特点，易把设备噪声当不变特征。

## 方法
Lung-CL：Teacher–Student、固定容量。AST 前 6 层冻结为特征提取器 G、后 6 层+分类头为可训 H。Class-Specific Latent Replay（CSLR）：每域结束后用对角 CS-GMM（BIC 选分量数，Kmax=10）拟合各类潜特征，新域训练时采样伪特征注入 H，无需缓存音频。Multi-Level Spectrum-Aware Distillation（MLSAD）：Energy-Gated Distillation 按谱能量加权中间特征差、全局余弦对齐语义方向、KL 蒸馏 soft logits。联合优化分类、LEGD、LCosine、LKD。输入 16 kHz、8 s mel（50–2000 Hz）；三数据集映射统一四类 Normal/Crackle/Wheeze/Both。

## 实验与结果
ICBHI→SPRSound→HF 等三条序列（S1–S3）。相对 buffer-free 基线（EWC/SI/LwF），Lung-CL 在 S1/S3 取得最佳或接近最佳 ACC（约 61.81%）与最强 BWT（S1 −4.0%，S3 −5.05%）；S2 严苛域移下 BWT −9.6%，仍优于 EWC/SI。消融：CSLR 将 BWT 从 −14.11% 提到 −8.20%；再加 LEGD 至 −4.0%。t-SNE 显示生成伪样本能复现原域流形。

## 结论
在无真实缓冲下，CS-GMM 潜空间重放加能量门控谱蒸馏可缓解呼吸音域增量遗忘，并兼顾隐私与稳定性–可塑性权衡。

## 点评
问题切在“医疗音频不能存样本 + 病理在高能量带”，CSLR 与 EGD 分别对准隐私与谱稀疏。强在 buffer-free 仍可比部分有缓冲方法；弱在依赖冻结底层假设分布不漂、三类映射与序列设计可能影响可复现泛化，且 HF 类重叠严重时伪样本质量仍需依赖可视化佐证。
