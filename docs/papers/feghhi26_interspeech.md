# Lightbeam: An Accurate and Memory-Efficient CTC Decoder for Speech Neuroprostheses

- 论文编号：2947
- 报告人：Ebrahim Feghhi
- 程序：Monday 28 September 2026 / Assistive Technologies 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/feghhi26_interspeech.pdf

## 问题
Brain-to-Text ’24/’25 领先方案依赖 WFST CTC 解码器，峰值 RAM 约 320 GB，难本地部署；直接多模态 LLM 在小神经数据上又弱于 WFST。

## 方法
LightBeam：非 WFST 的 GPU CTC beam search（源自 FlexCTC），用较小 4-gram 浅融合处理同音词；按固定间隔（约 1–1.25 s）对正交假设做 delayed fusion（Llama 3.2 1B 替换 N-gram 分），终局再 LLM 标点。配基线 GRU 或因果 time-masked Transformer；可选生成式纠错（Llama 3.1 8B）。开源 Python 实现。

## 实验与结果
基线 GRU：B2T’24 WER 9.37 vs WFST 重实现 9.71；B2T’25 公开/私有 5.77/6.47 vs 6.31/6.72；RAM ~10 GB vs ~320 GB，RTF 仍 <1。Transformer 上同样显著优于 WFST；配合 GEC 达已发表 SOTA。

## 结论
作者认为将 LLM 纳入一阶段 delayed fusion 可在大幅降内存下提升神经语音解码精度，适合临床本地部署。

## 点评
工程痛点极具体（320→10 GB）。delayed fusion 避开 WFST 大图与纯端侧 LLM 微调的弱势。仍需 GPU 与周期性 LLM 调用；RTF 高于 WFST 但峰值仍实时。对神经解码工具链可访问性贡献大。
