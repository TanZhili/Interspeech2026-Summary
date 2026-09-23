# A Unified and Reproducible Experimentation Framework for Speech Understanding

- 论文编号：1225
- 报告人：Jing Peng
- 程序：Tuesday 29 September 2026 / Corpus Creation, Summerisation and Understanding
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/peng26e_interspeech.pdf

## 问题
语音理解评测常因后处理、归一化与打分不一致而不可比；现有基准模型族覆盖窄、少做真实应力场景；异构训练数据与流水线又使架构对比难复现。部署选型需要统一协议下的可复现实验框架。

## 方法
提出 SURE：统一预测格式、归一化与打分；引入相对性能分 RPS（相对同流水线当前最优归一化到 [0,1]）。三轨道——Track I：前端感知情景应力（噪声、混响、会议、码混、方言、热词等）；Track II：全栈理解横向对比（ASR、GR、S2TT、SER、SLU 等）；Track III：Agent 辅助把「论文+代码」转为可运行 SWIFT 配方，在匹配开放数据子集上从头训做受控架构比较。评测栈含 meeteval、sacrebleu 等固定后端。

## 实验与结果
Track I：会议 SA-ASR 上级联仍有竞争力（如 Diarizen+DiCoW 在 AMI 上 DER/cpWER 30.21/17.26，优于 VibeVoice-ASR 的 41.26/36.80）；不同系统在码混/方言/噪声/热词上各有长短。统一归一化可使 LibriSpeech 上某系统相对报告数字的 RPS 偏移约 0.3。Track II：级联在干净感知任务仍可竞争；情感识别普遍难；部分 Speech LLM 输出格式不遵从会拖垮自动指标。Track III：同协议下 Qwen2-audio 与 TASU(SFT)-2B 对比，后者在 GR/SER 等副语言任务落后，语义任务（SLU、S2TT）更接近。

## 结论
SURE 标准化评测并提供情景套件与受控训练转换流，开源可扩展，面向部署选型的可比与可复现。

## 点评
抓的是「评测协议与训练方差」而非新模型结构，对社区基建价值高。RPS 便于跨任务汇总但依赖动态榜单最优，解释时需看任务级指标。Track III 仍是初步，Agent 转换对非标准仓库可能需人工补丁，架构结论外推应克制。
