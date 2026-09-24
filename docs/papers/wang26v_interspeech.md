# TC-DBI: A Plug-and-Play Trajectory Confidence-Guided Dynamic Block Inference Strategy for Speech Synthesis with Continuous Block Flow Matching

- 论文编号：1242
- 报告人：Ren Wang
- 程序：Thursday 1 October 2026 / Flow Matching for Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26v_interspeech.pdf

## 问题
连续 Block Flow Matching TTS 训练/推理常用固定块长，但语音信息密度不均：难区需要更强上下文，易区可大步并行；固定块在效率与质量间难兼顾，且连续 ODE 采样缺少离散模型那样的 token 置信度信号。

## 方法
定义 Trajectory Confidence（TC）：ODE 轨迹起终点位移范数 / 路径总长，越接近 1 越“直”、越可信。TC-DBI：先以 Lmax 并行生成候选块，按阈值 τ 找最长可靠前缀，截断低置信后缀并用更新后的上下文重生；每步至少保留 1 帧以防死循环。即插即用，无需改结构或重训。复现 BFM（DiT + 冻结 VoxCPM VAE，Emilia 中英约 100k 小时），推理 32 步 ODE，默认 τ=0.75。

## 实验与结果
Seed-eval：BFM+TC-DBI 相对无 DBI 降低 WER（zh 1.628→1.568%，en 1.921→1.798%），N-MOS 升至 3.809/3.973，SIM 基本持平。低 TC 句子错误率显著富集（阈值 0.65 时错误率约 35% vs 全局 21.4%）。τ=0.75 时相对 RTF 约 1.08× 且 WER 最优；过高 τ 使 RTF 升至 1.63× 收益递减。重生后 >90% 原低置信帧升到阈值以上。

## 结论
作者认为轨迹直线度可作为免训练可靠性指标，TC-DBI 能自适应块粒度，在相近效率下提升稳健性与感知质量。

## 点评
把 OT 直线流的几何性质变成可操作的动态解码信号，对连续块模型很贴切。阈值需折中；TC 是局部速度一致性代理，不等价于语义正确性，极端韵律/难文本是否总能被截断–重生修好仍依赖基座 BFM 能力。
