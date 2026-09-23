# Negation in Audio Generation Models

- 论文编号：1756
- 报告人：Bikash Dutta
- 程序：Wednesday 30 September 2026 / Generative Audio and Music
- 技术分类键：singing
- 全文：https://www.isca-archive.org/interspeech_2026/arora26_interspeech.pdf

## 问题
文本到音频（T2A）模型常忽略否定约束，生成被要求排除的声音；现有基准几乎不测否定理解，训练数据也几乎只描述“在场”事件，形成肯定偏置。

## 方法
构建 Audio Negation Benchmark：由 AudioCaps 派生约 100 万否定提示，覆盖四类否定与三种范围，人工抽检正确率 99.6%。提出音频问答（AQA）等协议探测生成音频中否定事件是否缺失；评测 AudioGen、AudioLDM2、TangoFlux，并辅以再描述验证。

## 实验与结果
所有模型、所有否定类型上，否定音频的 AQA recall 均 <0.05；否定与肯定提示产生近乎相同的声学输出，再描述亦显示系统默认肯定声景。

## 结论
否定处理是当前 T2A 的系统失败模式，需要否定感知训练目标与专用评测。

## 点评
把肯定偏置用大规模对照与 AQA 钉死，对生成音频可信度很关键。局限是基准由字幕改写而来、评价依赖问答模型本身，且未给出有效缓解方法（正文定位为问题界定）。
