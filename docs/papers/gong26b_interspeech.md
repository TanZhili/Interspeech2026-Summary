# Bagpiper-Edit: Zero-Shot Open-Ended Audio Editing via Rich-Caption

- 论文编号：631
- 报告人：William Chen
- 程序：Wednesday 30 September 2026 / Voice Editing
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/gong26b_interspeech.pdf

## 问题
文本引导音频编辑常依赖配对数据、固定原子操作模板，或拼多专家管线，难统一覆盖语音/音乐/环境声的开放式自然语言指令。直接用 caption–音频基础模型做编辑易忽略原音频，导致风格与身份漂移。

## 方法
Bagpiper-Edit 把编辑改写为 rich-caption 变换：先从原音频抽详细 caption，再由文本 LLM 按用户请求改写 caption，最后以原音频为声学锚生成目标音频。自监督学锚：音频重复（同一 clip 复制）与相邻切段（共享说话人/房间/背景）构造 (a1,a2,c1,c2)；训练 Single-Turn（拼接 caption/音频）与 Multi-Turn（两轮对话，先 a1 再 a2）两种模式。数据约 50 万样本，无配对编辑数据；骨干 Bagpiper-Base（Qwen3-8B + X-Codec）。

## 实验与结果
语音编辑：MT 转写 Acc 79.76%、WER 14.01%、SpkSIM 0.83，优于 Base 的严重身份丢失；情感准确可比专家，风格略弱。事件增删：MT 在一致性与编辑成功间更平衡（增 editCLAP 更高，删 FAD 更低）。开放式 rich-caption：MT CapSIM/LLM 分最高，ST FAD 最低但语义对齐较弱。作者建议默认用 MT。

## 结论
无配对编辑数据即可通过 caption 重写 + 自监督声学锚实现跨域零样本开放编辑；MT 对话模式在多数任务上更稳。

## 点评
把“改什么”完全放到文本空间，避开原子操作与配对数据，统一多域是亮点。自监督相邻段锚很巧。代价是转写全句替换受 LLM 改写误差传播，稳定性不及大量配对训的专家模型；复杂多说话人场景仍受 base 能力限制。
