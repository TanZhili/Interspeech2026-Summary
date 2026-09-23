# HaessigDB: A Database of Irritable Speech with Intensity Grading

- 论文编号：3304
- 报告人：Niklas Weller
- 程序：Tuesday 29 September 2026 / Datasets
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/weller26_interspeech.pdf

## 问题
客服语音机器人需按烦躁强度与时间轨迹做升级转接，但常用情感语料（Emo-DB、IEMOCAP 等）缺服务场景、序数强度与对话时间演化；二分类难以支撑早期干预。

## 方法
HaessigDB：合成银行客服脚本（客户逐渐烦躁）由 4 名英语演员棚录；切成约 3.91 s 句级片段；Prolific 众包对 annoyance/frustration/aggression 打 1–10 分。按维度迭代剔除低一致性项至 Krippendorff α≥0.80，得高一致子集。公开 Zenodo/Hugging Face。

## 实验与结果
原始有效片段 1068；高一致子集 annoyance/frustration/aggression 为 553/537/516；内外连接合并 250/832。轨迹显示前约 10 片段三维度平均上升。现成 HF 情感分类器在阈值扫描下召回曲线平坦，难分辨中间强度；LoRA 微调 HuBERT/XLSR 做攻击强度回归：MAE 1.502/1.333，Pearson r=0.607/0.710（80/20 非说话人分离划分）。

## 结论
提供带序数强度与时间顺序的烦躁语音资源，可支持分级检测与升级策略；初步证明预训练编码器可适配强度回归。

## 点评
把“烦躁=可升级的序数轨迹”做成数据规格，贴合客服场景。高一致子集与失败模式分析有用；局限为表演式合成脚本、微调划分未说话人分离，外推需谨慎。
