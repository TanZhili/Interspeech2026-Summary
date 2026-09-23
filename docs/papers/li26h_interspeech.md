# SRF-SVB: Style-Consistent Singing Voice Beautifying via Rectified Flow

- 论文编号：615
- 报告人：Wenhui Li
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26h_interspeech.pdf

## 问题
歌声美化需改正业余音高/节奏并提质，同时保歌词与原唱歌手风格；现有 APC 多只改音高，NSVB 依赖难采集的平行录音，扩散式方法质量–效率难兼顾，过度“专业化”易抹掉个人音色与表达。

## 方法
SRF-SVB：解耦音高（RMVPE）、内容（Conformer PPG）、音色（CAM++）；训练时对 Mel 连续掩码（α=0.5）做 DiT 参数化的 rectified flow 填补，损失只算掩码区。推理：业余段作上下文 Mel，专业音高+DTW 对齐内容作生成条件，音色仍取自业余；Euler 10 步，NSF-HiFiGAN 声码。

## 实验与结果
约 160 h 中英歌声训练；英测 617、中测 874 业余–专业对。RPA：英/中 0.57/0.50（业余 0.40/0.22）；SECS 0.85/0.82，显著高于 NSVB（0.58/0.40）；MOS-Q/S 英 3.91/4.47，中 3.62/4.06，风格相似领先。连续 α=0.5 掩码优于更小比例或随机碎片掩码。英测 CER 略高于仅改音高的 Diff-Pitcher。

## 结论
首个基于 rectified flow 的风格一致 SVB，可高效同时校正音高节奏并保住业余歌手个性；生成重构偶发影响发音清晰度。

## 点评
用上下文 Mel 填补把“风格一致”写成训练–推理同构的 inpainting，比事后音色约束更直接。相对 NSVB 不再强依赖平行训练对是实用优势；CER 代价说明生成式美化仍可能碰歌词保真，实时场景还需压采样步数。
