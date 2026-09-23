# Plan and Double-Check: Streaming Multimodal Q-Former for Online Robot Action Generation

- 论文编号：2999
- 报告人：Chiori Hori
- 程序：Monday 28 September 2026 / Multimodal Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/hori26_interspeech.pdf

## 问题
基于演示视频的机器人动作规划与确认生成多依赖离线、预切分片段；真实交互需对未切分音视频流式处理。直接流式化易引入延迟与对齐困难，且缺少合适的人–机器人对话级时序标注。

## 方法
将 AVBLIP（音频–视觉 Q-Former + 冻结 OPT-2.7B）扩展为流式：
- 按约 1 秒 chunk 提取 Omnivore/CLIP/AST 特征并交错送入 Q-Former；查询嵌入可 attend 历史 chunk（左上下文），不看未来；
- LLM 对当前 chunk 自回归生成：输出 \(\langle S\rangle\) 及后续 token，或 \(\langle /S\rangle\) 表示本 chunk 无输出；
- 训练用注意力掩码实现并行：因果自注意力、chunk 级 cross-attention、流式 LLM 的 chunk 自注意力；
- 对齐策略对比：固定 clip 末、采样提前响应时刻、基于 CE loss 的 loss-based 选择（采样损失相对末 chunk 损失足够小时采用采样对齐）。
在线用 greedy 解码。未使用字幕（在线难以获得）。

## 实验与结果
YouCook2，验证集对半交叉验证。动作微步短语集来自既有标注。
- 离线基线 action BLEU-2 / METEOR：0.357 / 0.251；流式模型作离线使用时性能接近。
- 在线流式（loss-based）：平均延迟约 −2.92±2.20 s（相对 clip 结束提前），漏检率 4.40%；action BLEU-2 / METEOR 0.328 / 0.228，description 0.212 / 0.145；相对基线质量下降但文中称各序列指标相对降幅 <10%。
- loss-based 优于 clip-end 与单纯 sampling（延迟波动更小、指标更好）。

## 结论
通过 chunk 化 Q-Former、左上下文掩码与响应时刻对齐，可在接近离线并行训练效率下实现低延迟流式动作序列与确认句生成；loss-based 对齐优于其它对齐策略。准确率相对离线有可接受损失。

## 点评
把流式 ASR 的 chunk/interleave 思路迁到 Q-Former–LLM 动作规划，并用掩码保住并行训练，工程路径清晰。强在显式生成确认句以支持执行前人工复核；脆弱在依赖启发式对齐阈值、greedy 相对 beam 已有损失、且未接入流式 ASR 字幕——复杂厨房场景下漏检与错时触发仍是主要风险。
