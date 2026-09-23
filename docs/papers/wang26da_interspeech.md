# GACA-DiT: Diffusion-based Dance-to-Music Generation with Genre-Adaptive Rhythm and Context-Aware Alignment

- 论文编号：2348
- 报告人：Jinting Wang
- 程序：Wednesday 30 September 2026 / Audio Foundation Models and Generation
- 技术分类键：generation
- 全文：https://www.isca-archive.org/interspeech_2026/wang26da_interspeech.pdf

## 问题
Dance-to-music（D2M）需节奏一致与帧级时间对齐。已有方法常用全局运动特征或二值化关节节奏，丢失细粒度运动、跨舞种鲁棒差；特征下采样还造成舞蹈节奏嵌入与音乐潜变量长度错位，对齐不足。

## 方法
GACA-DiT（约 56M）：(1) Genre-Adaptive Rhythm Extraction（GARE）：由姿态差分得运动幅度，多尺度 Gabor 小波建模时间动态，MLP+softmax 得关节自适应权重，再构多尺度相位直方图刻画空间运动分布，经时间注意力融成节奏嵌入 R。(2) Context-Aware Temporal Alignment（CATA）：将 R 切成 Tm 段，用可学习 context queries 对段内帧做注意力池化，得到与音乐潜变量同长的 ˜R。(3) I3D 视频语义特征 V 与 ˜R、时间步共同条件化 DiT，Conditional Flow Matching 学速度场；DiffRhythm VAE 编解码波形。训练 5 s/44.1 kHz，32 步 Euler，CFG=4。

## 实验与结果
AIST++ / TikTok 上相对 D2M-GAN、CDCD、LORIS、MotionComposer：AIST++ BCS 98.13、BHS 98.72、F1 98.47、FAD 20.14 等多项最优；TikTok BCS 91.55、F1 91.21 等亦领先。消融逐步加入小波、直方图、自适应加权与 CATA 指标递增；GARE 优于 ST-GCN 与 LORIS 式节奏特征。20 人 MOS：节奏一致性与整体质量中位数更高、分布更集中。

## 结论
细粒度、舞种自适应节奏表征 + 查询式跨模态时间对齐，使扩散式 D2M 在客观对齐/美学与主观评价上全面超过先前 SOTA。

## 点评
把“粗节奏”和“长度错位”拆成两个可模块化补丁，GARE 用时–空互补特征、CATA 用可学习查询对齐下采样，问题定位清楚。参数量远小于若干大基线却指标领先，说明条件表征质量比堆模型更关键。潜在脆弱点：依赖姿态检测质量与舞种覆盖；TikTok FAD 未全面领先；短 5 s 片段设定外的长视频对齐未充分验证。
