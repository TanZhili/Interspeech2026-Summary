# LLM-HB: Language-Aware LLM-Guided Hotword Biasing for Code-Switching ASR

- 论文编号：1113
- 报告人：Yuxuan He
- 程序：Thursday 1 October 2026 / Code-Switching ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/he26c_interspeech.pdf

## 问题
码切换 ASR 易受跨语混淆；热词偏置多服务单语系统，CS 场景下较少与 LLM 自适应偏置结合。

## 方法
LLM-HB：Whisper-medium 编码器 + MoE adaptor（默认 2 experts、top-2）得到语言特化语音嵌入；Qwen3-4B 经 LoRA，输入拼接语音、热词与（训练时）转写嵌入，并用辅助语言头对 LLM 隐状态做 Mandarin/English/other 监督。训练目标 L = L_ASR + λ1 L_Bias + λ2 L_Lan（λ1=0.6，λ2=0.3）。热词经冻结 LLM tokenizer/文本编码器注入提示。

## 实验与结果
评测 ASRU2019-CS，每句 15 个干扰热词。全量约 2200h（ASRU+LibriSpeech+AISHELL-2）上，完整模型 MER 5.85（基线 7.34，相对降 20.30%），B-MER 8.99（基线 22.11）；CER/WER 4.94/13.21。仅 200h CS 数据时完整模型 MER 7.36（基线 9.59），热词提示单项收益最大。消融：2 choose 2 优于更多专家；λ1 增大使 CER/WER 更平衡，主实验取 0.6。

## 结论
语言特化 MoE、语言监督与 LLM 热词提示互补，可在码切换 ASR 上显著改善总体与热词相关错误率；作者称首次将 LLM 引导偏置引入 CS-ASR，并释放热词列表。

## 点评
把“分语表示”和“上下文热词”绑在同一 LLM 条件接口上，适合双语切换。热词损失权重调节英/中错误平衡；专家数不必多，双语场景两专家即可。小数据时单独加 MoE 可能略伤性能，需与语言/偏置信号联合才稳。
