# TTBA: Spatial Prompted Text to Binaural Audio Generation Using Transformer

- 论文编号：602
- 报告人：Changjun He
- 程序：Tuesday 29 September 2026 / Spatial Audio 3
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/he26_interspeech.pdf

## 问题
现有 text-to-audio 多生成单声道，即使有立体声也缺乏可控空间信息；近期可控双耳/空间生成仍易出现空间漂移与定位误差。作者希望从文本与显式空间提示直接生成方向可控的双耳音频。

## 方法
TTBA：用预训练单声道 EnCodec 对左右声道编码后做 codebook 维交叉排列；空间提示编码器将各声源的起止方向（五扇区量化）与速度编成嵌入，经多头注意力与 T5-large 文本特征融合；解码器式 Transformer ALM 自回归生成双耳离散 token。训练上从更深的单声道教师蒸馏内容，并用 CE + KD 损失与 CFG。推理时拆开交叉 token 再解码波形。

## 实验与结果
在 BEWO-1M 的 SS/SD/DS/Mix 子集上对比 Stable-audio-open 与 SpatialSonic。多源场景（DS、Mix）上 FD/FAD/CLAP 等多数指标最优；DILD 常优于 SpatialSonic。主观（20 人）OVL/REL/SPQ 多数最高。消融：无蒸馏损害内容指标；无 SPE 主要恶化空间指标（尤其 DILD）。

## 结论
交叉排列离散表征 + 空间提示条件 + 单声道教师引导，可在复杂多源条件下生成语义与空间均较可控的双耳音频；未来拟提升空间真实感并扩展到更复杂环境。

## 点评
把“内容”与“耳间差异”拆成教师蒸馏与交叉 token，对文本驱动双耳生成是合理归纳。方向被粗量化到五扇区，精细轨迹与距离控制仍有限；定量上单静/单动态子集并非全面领先，主观优势与客观不完全一致，说明空间评价仍依赖听感。
