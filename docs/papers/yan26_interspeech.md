# UniSE: A Unified Framework for Decoder-Only Autoregressive LM-Based Speech Enhancement

- 论文编号：192
- 报告人：Chengwei Liu
- 程序：Tuesday 29 September 2026 / Language-Model and Codec-Token Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yan26_interspeech.pdf

## 问题
神经音频编解码推动了 LM 在语音任务上的应用，但自回归 LM 能否在统一框架内覆盖语音恢复（SR）、目标说话人提取（TSE）与语音分离（SS）仍探索不足；现有 LM-SE 多限于单失真或单任务，且 RL 在 SE 中的感知对齐较少被系统使用。

## 方法
UniSE：冻结 WavLM（层均特征）+ 可训线性 adapter 提供参考/受损连续条件；BiCodec 将目标语音编成固定长全局 token（32）与变长语义 token（50/s）；LLaMA 式 decoder-only LM 自回归预测目标离散 token。用任务 token 区分 SR / TSE / 反向 TSE（rTSE）三种模式，组合模式做两说话人 SS（先 SR 取较响说话人，再 TSE/rTSE）。监督训练后用渐进强化学习（PRL）：DPO 阶段 1 以 DNSMOS 定胜负，阶段 2 再混入 WavLM 特征距离作相似度准则，并保留 CE 项（α=0.4）。训练数据来自 VoxBox 清洁语音与多种噪声/RIR 仿真多失真。

## 实验与结果
DNS 2020：UniSE+PRL 在 With Reverb 上 SIG/BAK/OVRL 达 3.83/4.26/3.64，No Reverb 3.76/4.23/3.57，优于 MaskSR、GenSE、LLaSE-G1 等。URGENT 2025 盲测 OVRL/NISQA/UTMOS 为 3.34/3.83/2.95。Libri2Mix TSE 上 +PRL 的 OVRL 3.45；SS 上 Libri2Mix/WSJ0-2mix OVRL 3.55/3.49。消融：NAR 明显变差；换 Qwen2 骨干相近；X-codec2 因码本过大下降；α 过低会导致 OVRL 虚高而 SIM 崩塌。

## 结论
任务 token + AR 离散建模可把 SR/TSE/SS 统一到同一 decoder-only LM，PRL 进一步抬升感知质量且多任务不伤单任务。局限：全句条件不利于严格流式，解码效率低于 NAR。

## 点评
工作抓住“多任务 SE 的条件前缀可组合性”，用模式切换而非多头网络实现统一，方向清晰。PRL 的粗到细偏好有助于缓解单一奖励与相似度冲突。脆弱点在 BiCodec 重建上限（正文亦用干净语音过编解码说明瓶颈）以及 SS 依赖多轮推理，错误会级联。
