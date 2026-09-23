# Cross-Lingual Compositional Learning for Code-Switched Lip Reading

- 论文编号：1163
- 报告人：Jeonghyeon Joo
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/joo26_interspeech.pdf

## 问题

语码转换在多语交流中普遍，但视觉语音识别（唇读）缺真实混合语料；CSLR 规模小、句式重复。多语 VSR 默认“一句一语”，难直接泛化到句内切换。

## 方法

提出 CoCoVSR：从中英单语视频拼接伪混合样本（双向顺序），与真实 CSLR 联合训练；在预训练 MultiVSR 上微调视觉前端，并用共享 LoRA adapter（非整语专家）适配 Transformer 编解码，利用跨语共同 viseme。

## 实验与结果

CSLR：CER/WER/MER 16.69/16.23/16.48，大幅优于先前 CTC/MoE 等方法（MER 约 37+）。MultiVSR 中文与未见 LRS2 英语仍保持可竞争水平。仅训 CSLR 混合集最好但单语崩；加入 CoCo 数据可在混合与单语间折中。共享 decoder adapter 优于多 adapter。

## 结论

作者认为无需额外采集或生成合成，跨语拼接 + 共享轻量适配即可让多语唇读获得语码转换能力，并尽量保住原多语性能。

## 点评

抓住视觉跨语 articulatory 重叠，故意不用 ASR 里常见的语言专家路由，参数更省。拼接伪混合边界生硬，与真实切换韵律/口型过渡有差距；CSLR 本身模式重复，SOTA 幅度需结合数据特性解读。单语保留与混合精度的权衡在消融中交代清楚。
