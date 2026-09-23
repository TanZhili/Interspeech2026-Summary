# DiffRhythm 2: Efficient and High Fidelity Song Generation via Block Flow Matching

- 论文编号：128
- 报告人：Yuepeng Jiang
- 程序：Wednesday 30 September 2026 / Generative Audio and Music
- 技术分类键：singing
- 全文：https://www.isca-archive.org/interspeech_2026/jiang26_interspeech.pdf

## 问题
全长歌曲生成需歌词–歌声对齐与结构连贯。纯 NAR（如 DiffRhythm）对齐难或依赖时间戳/REPA 约束损害乐感；多偏好 RLHF 常分模型再合并导致性能折中。

## 方法
DiffRhythm 2：半自回归块级 flow matching——块内 NAR、块间 AR，无需时长标签即可对齐；5 Hz 音乐 VAE 压缩长序列；随机块 REPA 提升结构/乐感；跨对偏好优化（交叉配对冲突/协同偏好）做多维 DPO，避免合并退化。支持最长约 210 秒可变长（EOP 帧）与块级 KV cache。

## 实验与结果
客观上 DiffRhythm 2 在开源模型中 PER 0.13、Mulan-T 0.40，SongEval 多项领先（如 CO 4.09）；相对 DiffRhythm+/ACE-Step/LeVo 整体更均衡。主观与客观均报告优于开源基线并保持高效（正文强调相对 AR 仍快）。

## 结论
块级半 AR flow matching + 跨对偏好优化可在效率与保真之间取得更好歌曲生成折中。

## 点评
用“块内双向上下文 + 块间因果”同时缓解 NAR 对齐与 AR 慢速，设计动机清楚。细节依赖训练注意力掩码与 EOP 设计；多偏好分组策略对冲突维度的稳健性仍需更多消融支撑。
