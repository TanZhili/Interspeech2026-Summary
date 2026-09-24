# Dynamic Block-Online Streaming ASR for Low-Resource Agglutinative Code-Switching Speech with Morphology-Aware Evaluation

- 论文编号：3334
- 报告人：Nabeel Mohammed
- 程序：Thursday 1 October 2026 / Code-Switching ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/rafat26_interspeech.pdf

## 问题
低资源黏着语（Bangla–English）句内码切换 ASR 中，固定前瞻的因果流式注意力无法回头修正词根–后缀与脚本重排依赖，易在切换点截断形态；码切换数据稀缺，标准 WER 也难以区分切换、词根与后缀错误。

## 方法
以非自回归 Paraformer（SAN-M + CIF）为骨干：离线用全局双向注意力训练；推理改为 Dynamic Block-Online——VAD 在自然停顿（>200ms）切语义宏块（上限约 3s），块内恢复全局注意力以事后绑定词根与后缀。数据侧用 Script-Anchored Loanword Injection：用约 750 个英–孟语义对，将孟加拉词根替换为英语词根并保留孟加拉后缀，诱导句内 CS。提出 CS-WER，分解为 Eswitch / Eroot / Emorph。

## 实验与结果
训练约 750h Bangla（Common Voice、OpenSLR 53、IndicVoices、KathBath 等）+ 250h Gigaspeech 子集；注入后约 20% 句含 CS。Common Voice 上：因果流式即便扩到 3s（WER 37.20%）形态仍平台（Eroot≈0.35、Emorph≈0.42）；Dynamic Block（3s）WER 38.73%，但 CS-WER 达 .53/.29/.35，接近离线 topline。月经/更年期医疗 TTS 适应后，Block-Online 在噪声留出集上 WER 27%、Eroot 22。

## 结论
对黏着语 CS，灵活延迟预算上的双向块注意力比单纯拉长因果窗口更能保住形态与切换语义；脚本锚定注入与 CS-WER 分别解决数据与诊断。局限：依赖可靠 VAD，词表仅覆盖常见借词。

## 点评
核心洞见是“因果不可逆提交”与黏着 CS 的长距依赖不匹配，用 VAD 宏块换回全局注意力，比硬堆 lookahead 更对症。CS-WER 把切换/词根/后缀拆开，解释了为何 Global WER 接近时语义仍差。医疗域“无损迁移”叙事有吸引力，但合成 TTS 适应与真实临床声学差距仍需谨慎解读。
