# Accelerating End-to-End ASR via Semi-Autoregressive Speculative Decoding

- 论文编号：1953
- 报告人：Long Wu
- 程序：Monday 28 September 2026 / Search Methods and Inference Algorithms
- 技术分类键：asr-decoding
- 全文：https://www.isca-archive.org/interspeech_2026/wu26g_interspeech.pdf

## 问题
端到端 ASR 中，AED 的自回归解码精度高但难以并行；NAR 虽快但语义建模与对齐常受损。现有 attention rescoring 等混合解码依赖 CTC prefix beam search 或复杂 CTC prefix score，成为吞吐瓶颈，且与 streaming chunk 解码不够契合。

## 方法
提出 Semi-Autoregressive Speculative Decoding（SASD），基于 joint CTC-attention 框架、无需重训：
1. 用 CTC greedy search 得到初假设（draft）；
2. 以 CTC 峰值概率为置信度，低于阈值 \(P_{\mathrm{thres}}\)（实验取 0.99）的位置记为低置信 token；
3. 高置信位置直接采用 CTC 结果；低置信位置用 attention decoder 做 speculative beam search，将 attention 分数与 CTC 分数插值后选 top-\(k\)；
4. 注意 decoder 只在原索引上替换 token，输出长度与 CTC 假设严格一致。
该设计避免精确 CTC prefix scoring，并兼容 chunk-based streaming。

## 实验与结果
数据：AISHELL-1、WenetSpeech（TestNet / TestMeeting）、内部约 33 小时工业测试集。在 WENET 五个预训练中文模型上评测。
- AISHELL-1（u2++ conformer）：SASD CER 4.73%（full），与 attention rescoring 4.77% 相当，优于 CTC greedy 5.18%；GPU RTF 0.0188，约为 attention rescoring（0.0535）的约 2.8 倍加速；batch=8 时 RTF 0.0098。
- WenetSpeech：与 attention rescoring 接近（如 TestNet full：9.40 vs 9.26），chunk 减小时更稳。
- 工业模型：CER 4.58 vs E2E 4.57，约 3.5× 加速。
摘要称相对 SOTA attention-rescoring 约 2.8×–3.5× 加速且 CER 可比。

## 结论
SASD 在解码阶段对“易”token 走 NAR（CTC）、对“难”token 走 AR（attention），省去 CTC prefix scoring / CTC beam search，在公开与工业数据上取得接近 rescoring 的 CER 与更高推理速度。

## 点评
做法本质是 token 级 draft-and-verify：用 CTC 峰度当置信门控，把昂贵的 attention 算力集中在少数低置信位置，因而延迟可接近 CTC greedy。强在兼容已有 AED、无需额外 draft 模型、对 streaming chunk 友好；脆弱点在于依赖 CTC 置信阈值与假设“多数 token 已足够自信”——若低置信比例升高（难声学条件），AR 修正成本会上升，加速比缩小。
