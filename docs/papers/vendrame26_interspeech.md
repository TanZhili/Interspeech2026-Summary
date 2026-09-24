# Joint Speech And Text Training For LLM-based End-To-End Spoken Dialogue State Tracking

- 论文编号：2769
- 报告人：Katia Vendrame
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：https://www.isca-archive.org/interspeech_2026/vendrame26_interspeech.pdf

## 问题
端到口口语 DST 依赖稀缺的带标注口语数据，跨域（尤其是地名/店名等槽值）泛化差。为每个目标域再采口语数据成本高，而文本 DST 数据更易获得。

## 方法
在 speech-encoder + connector + LLM（LoRA）E2E DST 上增加仅训练期使用的 text encoder：语音与文本经各自编码器后共用 connector/LoRA，联合训练。损失含：口语 DST、未配对文本 DST、以及口语批次转写上的文本 DST。先冻 LLM 做 ASR 预训练（Fisher/LS/CV/VoxPopuli），再微调 connector、text encoder 与 LoRA。推理丢弃 text encoder。对比无文本基线、无 text encoder 只训 LoRA、以及 Qwen3-TTS 合成语音。

## 实验与结果
SpokenWOZ ↔ Speech-aware MultiWOZ 交叉：源域语音 + 目标域文本可明显收窄与目标语音训练的差距（如 MW 验证上 SW 语音+MW 文本 15.1→19.0；SW 上 MW 语音+SW 文本 20.5→30.6）。混入 DialogStudio 仍有效；仅 DS 时主要帮含 MW 的场景。无 text encoder 有部分收益，完整流水线更好；调大文本损失权重可逼近 TTS 合成效果。更大 LLM（Gemma-3-12B）上联合文本甚至可使跨域 JGA 接近源域语音训练。分析显示跨域收益常来自槽键/实体错误率，而非一律降低 WER。

## 结论
用未配对文本做联合训练可实现“部分域有语音、其余域只有文本”的多域口语 DST，且无需 TTS。方法随 LLM 规模更稳，为文本侧槽增强等策略迁移到口语系统打开空间。

## 点评
共享 connector/LoRA 让文本监督回流到语音通路，比只给 LLM 看目标域 JSON 更实质性。MW 训练/测试城市不一致时值难直接迁移，正文也如实反映；实际部署仍需关心目标域槽值覆盖，而非仅槽键。
