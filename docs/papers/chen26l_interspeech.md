# Leveraging Audio-LLMs to Filter Speech-to-Speech Training Data

- 论文编号：1148
- 报告人：Qixu Chen
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/chen26l_interspeech.pdf

## 问题
端到端 S2ST 依赖大规模挖掘并行语音，噪声、切分错误与语义不一致会伤训练。启发式（时长比、ASR 长度比）或偏语义的 QE（如 BLASER）对声学劣化、合成伪影与语音对错位不够敏感；纯 ASR+文本 LLM 过滤又丢声学信息。

## 方法
两阶段 Rank→Distill：用 SNR、UTMOS、ASR 转写上的 LLM adequacy、BLEURT 等弱信号构造 clean/noisy 偏好对（含受控劣化），训 LambdaMART 排序器；对大池打分取 top-K/bottom-K 作 keep/drop 伪标签；再指令微调 Qwen2-Audio（4-bit+LoRA）直接对源/目标双音频判决 keep/drop。下游用 Fairseq S2UT（去掉辅助 CTC 等）在筛选数据上从头训练。

## 实验与结果
CVSS-C FR→EN + 20% SpeechMatrix：未过滤 ASR-BLEU 21.32；Audio-LLM 保留约 477k 对达 22.72（约 +1.4）。同预算下优于随机、BLEURT、BLASER、70B 文本 LLM。仅 Stage I 排序选 477k 得 21.91；去掉 Stage I 几乎不过滤。DE→EN 简化信号集上未过滤 13.27→过滤后 15.14。Audio Flamingo 3（单音频拼接）更弱。

## 结论
Rank→Distill 可把弱质量信号蒸馏成语音条件 keep/drop 模型，提升 S2ST；当前二值判决不便固定预算下灵活控量，未来可做概率/预算感知选择。

## 点评
把“排序比绝对打分更稳”做成伪标签流水线，再让 Audio-LLM 直接听双语音，针对 S2ST 挖掘数据里声学+语义耦合噪声。匹配预算的对比设计较干净。脆弱处是伪标签仍绑在手工阈值与劣化分布上，且二值过滤与实际保留量控制脱节；单作者稿还依赖特定 Audio-LLM 双音频能力。
