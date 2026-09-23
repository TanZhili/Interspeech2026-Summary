# VerAno: Speaker Anonymization via Self-Supervised Tokenization and Conditional Flow Matching

- 论文编号：497
- 报告人：Ngoc Hung Le
- 程序：Wednesday 30 September 2026 / Speaker Privacy Preservation and Anonymization
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/le26_interspeech.pdf

## 问题
说话人匿名化需在隐私与下游效用间权衡：ASR bottleneck 依赖语言且损副语言，连续 SSL 特征又会泄漏音色；合成阶段则在自回归误差与扩散采样复杂之间两难。

## 方法
VerAno：用受限码本的 VQ-VAE 量化 WavLM Large 第 18 层特征，迫使离散 token 优先保留音素/韵律而滤掉细粒度音色；token 与外部说话人池采样的目标 embedding（ReDimNet）条件化 Conditional Flow Matching Transformer，经 ODE（10 Euler 步）生成 Mel，再 HiFi-GAN 声码。码本大小 K 作为隐私–效用旋钮。训练数据为 LibriSpeech + CREMA-D；评测遵循 VPC 2024，并在 MLS（de/pt/it/es）测跨语。

## 实验与结果
相对 VPC B1–B6，CB128 与 CB8192 在 AVG/WTD 排名占前两名：CB8192 效用最好（平均 WER 2.20、UAR 57.51），EER 平均 23.13；CB128 隐私更强（EER 平均 31.73，接近 B5），WER 2.53、UAR 54.62。跨语上两者均使 ASV_Vox_orig EER 升至约 40%+；半知情 ASV_LS_anon 下 CB128 稳定性优于多语 B3-Mul，英语训练模型仍保持可用 WER。消融显示 K 增大效用升、隐私降，敏感应用更宜 K≈32–128。

## 结论
自监督 tokenization + CFM 可在官方基线整体排名上取得更好平衡，且对未见语言有一定泛化；未来拟蒸馏加速流匹配以支持端侧实时。

## 点评
把码本容量明确当成信息瓶颈旋钮，比“换更强转换器”更可解释地刻画隐私–效用曲面。CFM 相对扩散/自回归也更贴合高质量声学建模。跨语结果支持“声学–音素结构”而非语言特定 ASR 瓶颈；但训练仍以英语为主，且半知情攻击下隐私数字仍随 K 快速回落，部署时需按威胁模型选点而非默认大码本。
