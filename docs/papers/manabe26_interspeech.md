# ProLAP: Probabilistic Language-Audio Pre-Training

- 论文编号：845
- 报告人：Toranosuke Manabe
- 程序：Wednesday 30 September 2026 / Acoustic Signal Analysis and Generation
- 技术分类键：signal
- 全文：https://www.isca-archive.org/interspeech_2026/manabe26_interspeech.pdf

## 问题
CLAP 类方法默认音–文一对一确定性嵌入，但真实关系是多对多、有粗细粒度层级；音频源叠加重叠使视觉域层级建模难以直接迁移。

## 方法
ProLAP 将输入建模为对角高斯 \(N(\mu,\sigma^2)\)：PPCL 用校正相似度（CSD）做对比；跨模态/模态内 inclusion loss 编码包含关系；再提出层次化 inclusion loss，用递归随机掩码构造多级更不确定表示。编码器 HTS-AT + GPT-2，自 CLAP 权重微调。发布诊断集 AudioCaps-HC（四级抽象字幕）与 AudioCaps-EC（事件级音文），评测检索、audio traversal、inclusion 测试。

## 实验与结果
- AudioCaps/Clotho 检索与确定性 CLAP 相当或略优（如 AC 上 T→A R@1 42.70）。
- Traversal：加 \(L^h_{\mathrm{inc}}\) 后 Precision 26.83、R@1 15.67，显著高于 InfoNCE/SigLIP CLAP。
- 文本长度–不确定性相关：层次损失使 \(r_{\mathrm{TLU}}\) 达 −0.43；EC inclusion 测试文本/音频约 83.5%/91.7% 满足假设。

## 结论
概率嵌入 + 层次 inclusion 能更好刻画语义层级与不确定性，且不明显牺牲检索。音频侧层次级数过高会略伤检索，文本侧加深更利于不确定性校准。

## 点评
把 ProLIP 思路迁到音频，并用 HC/EC 与 traversal 把“学到层级”变成可测指标，比只报 R@1 更有信息量。字幕由 LLM/事件分割合成，inclusion 是否部分依赖掩码捷径需警惕；作者用 EC 测试试图排除纯 MASK 伪相关，方向对但诊断集质量仍是方法天花板。
