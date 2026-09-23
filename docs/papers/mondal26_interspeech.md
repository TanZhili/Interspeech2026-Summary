# Probing LoRA-to-LoRA Cross-Lingual Transfer for Unseen Low-Resource Conditions in Whisper-Based ASR

- 论文编号：1133
- 报告人：Spandan Dey
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mondal26_interspeech.pdf

## 问题
低资源 ASR 中，先前 LoRA-to-LoRA 迁移多针对 Whisper 预训练已覆盖的语种；对基座几乎未见、零样本 WER≈100% 的真正低资源语，捐赠语选择与迁移是否仍有效尚未知。

## 方法
两阶段捐赠选择：先限同语系，再在候选中最小化 Jensen–Shannon 正字法（词元分布）散度。在 Whisper-small 上先训捐赠语 LoRA（r=32，Q/V/Out/FFN），再以其权重初始化接收语 LoRA。捐赠：Hindi/Marathi/Bengali（IndicVoices）；接收：Bhojpuri Rural Woman、Konkani、Assamese（40–100 h）。

## 实验与结果
捐赠初始化相对仅接收语 LoRA 一致更优，相对增益约 9–17%（Hindi→Bhojpuri 40 h 达 17%）。JS 选中的捐赠优于同文字其他候选。零样本极高 WER 确认属未见设定，增益主要来自结构对齐而非强预训练先验。

## 结论
即便捐赠与接收均弱覆盖预训练，基于谱系+正字法相似度的 LoRA-to-LoRA 仍可提供更优优化起点，适合参数高效扩展低资源语。

## 点评
把“未见语”从高资源锚点迁移中拆出，并用可测正字法散度替代启发式配对，方法清晰可复用。绝对 WER 仍偏高（方言/数据少/仅 LoRA），贡献在相对迁移而非刷榜。
