# Audio Hallucination Attacks: Probing the Reliability of Large Audio Language Models

- 论文编号：2448
- 报告人：Ashish Seth
- 程序：Wednesday 30 September 2026 / Speech and Audio Quality Assessment
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/seth26_interspeech.pdf

## 问题
LALM 在标准基准表现强，但可能跳过“声音是否真的存在”的 grounding，在隐式提问或注入虚假语音描述时产生幻觉。

## 方法
提出 AHA：AHA-Eval（约 6.5K QA）含查询侧（显式 vs 预设声音存在的隐式问）与音频侧（TTS 注入描述不存在事件的合成语音）攻击；事件含相关/对抗/随机。用攻击成功率（ASR）评 Audio Flamingo 3、Gemini 3 Pro、Qwen2.5-Omni 等。另释 AHA-Guard（120K）做后对齐缓解。

## 实验与结果
Audio Flamingo 3 / Gemini 3 Pro 等 ASR 分别高达约 95.35% / 79.65%；隐式与音频注入攻击远强于显式问。AHA-Guard 对齐可将部分模型 ASR 降低至约一半（文称最高约 49%）。

## 结论
标准基准掩盖 grounding 可靠性缺口；需专门幻觉攻击评测，后对齐可显著缓解但未根除。

## 点评
用“假定存在”的隐式问揭示模型先验压过听觉证据，问题设定尖锐。AHA 属安全评测而非质量 MOS；缓解依赖额外对齐数据，部署前应视任务再验。
