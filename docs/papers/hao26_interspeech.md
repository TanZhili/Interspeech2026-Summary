# YingMusic-Singer: Controllable Singing Voice Synthesis with Flexible Lyric Manipulation and Annotation-free Melody Guidance

- 论文编号：1547
- 报告人：Chunbo Hao
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hao26_interspeech.pdf

## 问题
改歌词保旋律的歌声编辑：上下文掩码法控制弱，商业 SVS 需手标 MIDI/时长；Vevo2 虽免对齐但可懂度与旋律贴合不足，SoulX 仍要字级时间戳。

## 方法
YingMusic-Singer：Stable Audio 式 VAE + MIDI 提取器中间表征作旋律、IPA 句级对齐歌词、DiT-CFM。课程：TTS 预训练 → 歌声 SFT（先无旋律再开旋律+CKA）→ GRPO（多奖励、组内相对优势）。输入为可选音色参考、旋律歌声片段、修改歌词，无需手标对齐。并提出 LyricEditBench（GTSinger 衍生，六类编辑×中英，7200 例）。

## 实验与结果
相对 Vevo2，跨六类任务在 PER、F0-CORR、Vocal Score 上全面更优（尤其翻译/语码混合）；主观 N-MOS/M-MOS 亦更高。消融：SFT Phase2 抬高 F0 但损 PER，GRPO 同时拉回 PER 并再提 F0/VS；去 CKA 略损旋律，去旋律扰动会导致模型“抄”旋律潜变量语义而 intelligibility 崩塌。

## 结论
免标注对齐的扩散课程+GRPO 可同时强化歌词忠实与旋律保持，并给出首个系统评测基准 LyricEditBench。

## 点评
问题设定贴产品（只给旋律片段+新词），CKA 与 GRPO 正面处理歌词–旋律权衡。单阶段 CFM 在 SIM 上不如 Vevo2 多阶段，但作者明确优先可懂度与旋律；大规模内部歌声数据与奖励模型细节对复现仍敏感。
