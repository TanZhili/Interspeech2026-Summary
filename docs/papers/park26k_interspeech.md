# MeloDISinger: Melody-Aware & Duration-Preserving Singing Voice Editing with Audio Infilling

- 论文编号：3285
- 报告人：Yoonjeong Park
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/park26k_interspeech.pdf

## 问题
文本驱动歌声编辑需改歌词同时严格保持总时长与旋律以对齐伴奏；既有方法或隐式控制无法硬性保时长，或复用原音素时长导致替换不自然，且常整段重生成破坏未编辑区。

## 方法
MeloDISinger：MeloDRP 在固定编辑跨度预算下预测时长比（span 内 softmax 归一），融合音素信息与伪 MIDI（由 F0 导出）经交叉注意，并用音素–音符时间重叠引导注意；FPIP 预测编辑区 F0；flow-matching mel 解码器只在编辑掩码区域做 infilling，未编辑帧原样保留。另用 WhisperX+LLM（含音节容量约束）生成可评估的编辑歌词。

## 实验与结果
GTSinger-En（13 h，三歌手）。相对 EditSinger、Vevo2：各编辑场景（替换/插入/删除/混合）DDUR≈0、DC≈99.93%，WER/CER 与 FPC 多数最优；主观 Lyric/Melody/Naturalness MOS 亦全面领先。消融去掉时长预算条件降幅最大，去旋律条件损害节奏相关编辑。

## 结论
时长比预测 + 旋律感知 + 掩码 infilling，可在保总时长与未编辑区的前提下做旋律一致的歌词编辑，并达 SOTA 主客观表现。

## 点评
把 SVE 的硬约束（跨度预算）直接写进时长建模，比事后裁剪更干净；伪 MIDI 交叉注意缓解“像说话的时长”。评测流水线本身也是贡献，但数据规模偏小、场景由 LLM 生成，真实制作流水线的编辑分布可能更杂。
