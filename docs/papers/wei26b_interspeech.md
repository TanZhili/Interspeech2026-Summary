# Speaker Identity in Non-Verbal Vocalizations: Conditional Distillation and Mixture of Experts Approach

- 论文编号：77
- 报告人：Yi-Cheng Lin
- 程序：Wednesday 30 September 2026 / Speech and Language Representation
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/wei26b_interspeech.pdf

## 问题
表情 TTS/VC 越来越多生成笑声、咳嗽等非言语发声（NVV），需要说话人验证同时覆盖言语与 NVV。现有 SV 在 NVV 上泛化差，直接在 NVV 上微调又会灾难性遗忘言语验证能力。

## 方法
冻结 Data2Vec 前端 + ECAPA-TDNN，插入 MoE：Post-Fusion MoE 与 Inter-Layer Residual MoE（IR-MoE，每层后接适配器）。训练总损失含 AAM-Softmax、事件引导路由约束（负载均衡 + 事件内 KL + 事件间余弦间隔）、仅对言语样本生效的条件蒸馏（对齐冻结 WavLM-SV teacher）、以及跨域同说话人正样本的监督对比损失。数据用 NonverbalTTS（17 小时，10 类 NVV；1314/46/147 说话人划分），MFA 切分言语与 NVV。

## 实验与结果
- Zero-shot wavlm-base-plus-sv：SvS EER 5.60%，但 NvS/NvN 达 38.93%/39.13%。
- 自训基线中 Data2Vec+ECAPA NvS 23.33%；提出的 MoE-2（4 experts）NvS 22.66%、NvN 27.52%、SvS 9.24%。
- 消融：无蒸馏时 SvS 13.17%、NvS 24.95%；加条件蒸馏后分别到 9.24%/22.66%。专家数 4 时 NvS 最优，再增专家 NvS 略降但 SvS 可继续改善。

## 结论
条件蒸馏 + IR-MoE 在缩小 Speech–NVV 域差的同时显著缓解言语遗忘；中间层分离域、最终嵌入用对比统一说话人流形。局限：相对 VoxCeleb2 规模，NonverbalTTS 数据量小，SvS 仍不及 zero-shot WavLM-SV。

## 点评
核心洞察是“NVV 不是再加一类噪声，而是异构声学域”，用条件蒸馏只在言语上贴 teacher，避免把 NVV 硬拽进言语流形，设计干净。10 类 NVV 系统评估是贡献；但 Breath 占样本 67%+，稀有类（鼾声、喷嚏等）是否真正学到仍存疑，后续应看按类分解或合成 NVV 的零样本评测。
