# MMGenre: Benchmarking Singing Voice Synthesis across Multiple Musical Genres

- 论文编号：137
- 报告人：Wenhao Feng
- 程序：Wednesday 30 September 2026 / Speech Synthesis Evaluation 2
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/feng26_interspeech.pdf

## 问题
歌唱合成（SVS）进步快，但公开数据与评测严重偏流行乐，难系统分析跨流派泛化。流派作为整体风格条件在 SVS 中几乎未被当作一等评测维度。

## 方法
提出 MMGenre：用 Suno V4.5 按层级流派提示生成音乐，Mel-RoFormer 分离人声，STARS 标注音素音高时长，经时长/流派一致性（MuQ-MuLan）过滤与少量人工核验，得到 10 大类、26 子类、3,152 段中文分数–音频对（约 4.36h）。评测 RNN、XiaoiceSing、VISinger/2、DiffSinger、StyleSinger、TCSinger、TechSinger 等；核心指标 GCS-5（Gemini 2.5 Pro 五分流派一致性，与人 Spearman ρ=0.85），辅以 SingMOS 等与 CER。

## 实验与结果
各模型流派剖面高度相似，强对齐集中在 Pop 及相关类，非 Pop（Rock/Rap/Classical 等）普遍低分；合成嵌入跨流派重叠（相对真值可分），呈现“流派坍塌”。零样本风格迁移/技巧控制对 Classical/Rock/Rap 仅小幅抬 GCS-5，远低于 GT。用约 2h Rock 继续训练后 GCS-5 从约 1.5 升至 4.9。整体伪 MOS/CER 仍反映合成质量进步。真/合成 Pop 上模型 MOS 排序相关 ρ=0.90，支持基准相对有效性。

## 结论
MMGenre 提供多流派 SVS 诊断框架；当前模型流派意识强依赖训练分布，而非分数条件可轻松迁移。有限流派专用微调远优于零样本控制。

## 点评
用 T2M 扩流派覆盖是务实数据策略；“坍塌 vs 真值可分 + 微调即大幅回升”把问题钉在数据先验而非符号可控性上，对社区很有诊断价值。GCS-5 依赖 Gemini，且微调后略超 GT 可能含“子类夸张”伪影；中文、AI 生成人声为主，外推到真人多语料库需谨慎，但相对排序在 Pop 验证上已站得住。
