# Endpoint Anticipation for Low-Latency Spoken Dialogue

- 论文编号：2196
- 报告人：Sathvik Udupa
- 程序：Thursday 1 October 2026 / Turn-taking
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/udupa26_interspeech.pdf

## 问题
级联口语对话系统（如 Unmute）依赖反应式 endpointer，ASR→LLM→TTS 串行导致 TTFA 常达 1–2 s，难以接入推理/工具等重计算。需要在用户话轮结束前主动预判终点，以便投机执行下游流水线，并量化延迟收益与无效计算的折中。

## 方法
提出 Endpoint Anticipation（EPA）：双流 Transformer 分别编码 User/System 音频（Mimi 前 8 码本特征，12.5 Hz，骨干冻结），拼接后对多个固定前瞻窗口 h∈{320,…,2560} ms 做二值分类（若 t_EOT−t∈[0,h] 则为正）。EPA-S 每窗口独立模型；EPA-M 共享骨干、多头多任务。阈值用 Silero VAD 精修，短于 2 s 的 turn/backchannel 掩码。部署时首次超过阈值 θ 触发投机：fork LLM 短前缀并预合成 TTS 缓存；若在 h 内真实终点确认则释放缓存并续写，否则丢弃。引入 MRA、PAR、ERC、HEA 等指标刻画“实现的前瞻”与“过早触发”。

## 实验与结果
在 SpokenWOZ 与 Switchboard 上相对适配后的 VAP 基线，EPA-M 在 MRA–PAR、HEA–ERC 曲线上更优。约 33% ERC 工作点、h=640 ms 时 EPA-M 的 MRA 达 640 ms（VAP 160 ms）；约 15% ERC 时仍有 480 ms MRA。任务型 SpokenWOZ 整体优于开放对话 Switchboard。接入 Unmute（Gemma 3 4B，h=960 ms）平均延迟从 1195 ms 降至 690 ms（降 505 ms），ERC 28.4%。EPA-S 与 EPA-M 指标接近，后者可一模型覆盖多 h。

## 结论
固定视界的语音端点预判可使级联系统投机掩蔽串行瓶颈；EPA-M 持续优于 VAP 式基线，并在 Unmute 上验证约半秒级平均延迟下降。未来关注中途改口、晚到关键信息等语义边界情况。

## 点评
把“能提前多久”与“浪费多少算力”拆成可调阈值曲线，比单一 precision/recall 更贴近系统工程。强项在任务型对话；开放对话更难，说明声学预判对结构松散话轮仍脆弱。投机策略依赖原有语义 VAD 做最终确认，预判模块本身不处理打断等其它全双工能力。
