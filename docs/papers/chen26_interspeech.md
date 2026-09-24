# MoVE: Translating Laughter and Tears via Mixture of Vocalization Experts in Speech-to-Speech Translation

- 论文编号：42
- 报告人：Szu-Chi Chen
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/chen26_interspeech.pdf

## 问题
现有 S2ST 语义准确但常抹掉笑声、哭泣等非言语发声（NV），损害语用；真实 NV 数据稀缺，且单一适配器难同时建模冲突情感。

## 方法
合成管线：IndexTTS2 + 情感/NV 提示（CREMA-D/MSP-IMPROV/IEMOCAP、笑声检测、JVNV 哭泣），属性解耦投影稀有 NV 到多样说话人，再经静音/WER 过滤得 En⇔Zh 对。在冻结 Kimi-Audio 上：五路 LoRA 专家（Happy/Sad/Angry/Laugh/Cry）分阶段专训，再训 token 级 soft router 混合专家；并微调 detokenizer 以重建极端 NV。宣称约 30 分钟精选数据即可接近全量情感保真。

## 实验与结果
相对 Seamless/gpt-4o-audio/Kimi 等，MoVE NV Match 76%（基线最高约 14%），Nat. MOS 3.85、Emo. SMOS 3.79 最高；en→zh ASR-BLEU 32.5。同数据单 LoRA NV Match 仅 26%；A/B 偏好 MoVE 60%。自建数据 50h 单 LoRA 已优于 SynStard/SeamlessAlign 子集。路由无显式标签仍达约 63.7% 主专家对齐。

## 结论
合成表达数据 + AudioLLM 上的 MoE-LoRA，可高效保留笑声/哭泣等 NV；数据效率主要来自预训练先验而非 LoRA 本身。

## 点评
把 S2ST 的“表情塌缩”拆成数据与干扰两大瓶颈，用分专家再 soft 混合直接对症。NV Match 相对商业/开源基线跃升鲜明。脆弱处是依赖 IndexTTS2/Kimi 的 En–Zh 中心设定、合成–真实域差，以及主观评测规模较小。
