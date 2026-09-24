# Decoupling Search and Evaluation: Efficient Beam Decoding for Language Model-Based Text-to-Speech Synthesis

- 论文编号：1531
- 报告人：Chenlin Liu
- 程序：Thursday 1 October 2026 / LLM Based Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/liu26l_interspeech.pdf

## 问题
LM-based TTS 多依赖采样解码，存在随机不稳定；beam search 虽是最大化解码，但在语音生成中易出现时间坍塌（长时间静音/噪声循环），且推理延迟过高。作者分析发现 beam search 约 98% 时间花在搜索扩展上，评估只占很小比例。

## 方法
提出 SaVE-Beam：将假设扩展与序列打分解耦。轻量 student（自蒸馏，温度 τ=2，强调高概率 token 排序）做 chunk 级 beam 树构建；原 teacher LM 做精确评估与最终选择。Chunk 长度 L，学生扩展后由教师树解码、top-K 过滤，并用类似 speculative decoding 的接受比 rt 与阈值 α 做确定性验收，按接受长度与教师对数概率选路径。搜索阶段对近期窗口 w 内已出现 token 做硬屏蔽（概率置零再归一化），避免软惩罚在最大化解码下仍坍塌。另用动态剪枝保留 top-N 节点。

## 实验与结果
在 CosyVoice 2 上实现，训练集 LibriTTS 与 WenetSpeech4TTS premium，评测 SeedTTS-Eval。相对 TRAD-BS，LM 解码加速约 3.9×–5.1×；相对采样 baseline，en/zh 的 W/CER 分别可降约 50%/33%，速度接近 baseline（如 SaVE-Beam-2h：en TPS 22.21、WER 1.83；zh TPS 23.92、CER 0.84）。RTF 从 TRAD-BS 的 4.95 降到约 1.18–1.19。消融表明硬重复约束对抑制时间坍塌关键；去掉动态剪枝可在 test-hard 上进一步改善 CER。

## 结论
通过搜索–评估解耦、chunk 扩展与硬重复约束，SaVE-Beam 可在接近采样系统实时性的前提下，使最大化 beam 解码在 LM-TTS 中实用，并显著降低生成错误。

## 点评
核心洞察是把昂贵的 beam 扩展交给小模型，把目标函数仍交给原 LM，并用硬结构约束补救语音 token 低信息密度带来的坍塌。与把解码完全交给蒸馏学生不同，质量门槛仍由 teacher 决定；学生引入的受控随机性在 hard 集上甚至可能帮助逃离局部最优，这是设计上的有趣副效应。脆弱点在于 chunk/窗口/α 等超参与 student 容量：太弱会频繁拒收而抵消加速，软惩罚替代硬约束则会重新坍塌。
