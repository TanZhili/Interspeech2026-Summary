# Audio2Tool: Speak, Call, Act - A Dataset for Benchmarking Speech Tool Use

- 论文编号：2857
- 报告人：Ramit Pahwa
- 程序：Tuesday 29 September 2026 / Audio & Speech Language Models: Evaluation, Representations, and Emerging Capabilities
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/pahwa26_interspeech.pdf

## 问题
语音助手需从语音直接做 tool/function calling，但现有基准域窄、声学单一、缺少分层组合难度；级联 ASR–LLM 会传播识别错误并丢掉副语言，而音频侧工具调用缺少可诊断失败模式的大规模评测。

## 方法
发布 Audio2Tool：约 3 万查询，覆盖 Smart Car / Smart Home / Wearables，152 个已校验函数、23 类。八层难度：Direct、Parametric、Multi-Intent、Implicit、Needle-in-a-Haystack、Correction、Conversation、Intent Blending。查询由 GPT-5.2/Gemini 2.5 Pro/Claude Opus 生成并经多模型裁判与人工抽检。用 Qwen3TTS、CosyVoice-3 零样本克隆，结合 Emilia-Yodas、3D Speaker、VoxPopuli 说话人与车载/室内噪声混合，模拟 in-the-wild。指标：Tool Accuracy、Exact Match、Slot F1。

## 实验与结果
评估端到端 SpeechLM（含 Qwen-3-Omni-30B、Kimi-7B、Qwen-2.5-Omni-7B、Step-Audio2-7B、Audio-Flamingo-8B 等）与 Whisper v3 + Qwen/Gemma 级联。简单 Tier-1 准确率可很高（如 Qwen-3-Omni-30B 92.4%），但 Multi-Intent/Implicit 的 EM/F1 常低于 35%；长文、纠错、多轮与意图混合（Tier 7–8）准确率多低于 56%。更大模型总体更好；端到端尚未稳定优于强 ASR–LLM。噪声消融（babble/机械/脉冲，+15/+5/−5 dB SNR）显示性能随噪声显著下降。

## 结论
Audio2Tool 在真实工具分类与分层声学挑战下暴露：简单指令已较强，组合推理、参数精确匹配与嘈杂/多说话人场景仍是主要瓶颈；公开数据与代码以推动稳健语音工具调用。

## 点评
把“听懂意图”升级为可执行 schema 约束（工具名顺序 + 参数精确匹配），并用八层课程隔离失败模式，比扁平 SLU 意图准确率更贴部署。汽车域占比高、合成 TTS+噪声仍是分布近似；Tier-8 对纯文本工具模型不适用，突显说话人分离是音频特有难点。端到端未系统性赢级联，说明当前瓶颈仍大量在组合与参数 grounding，而非只差一个更大 SpeechLM。
