# Dual-LoRA: Parameter-Efficient Adversarial Disentanglement for Cross-Lingual Speaker Verification

- 论文编号：2274
- 报告人：Qituan Shangguan
- 程序：Thursday 1 October 2026 / TidyVoice2026 Challenge: Cross-Lingual Speaker Verification
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/shangguan26_interspeech.pdf

## 问题
跨语种说话人确认存在严重的语言–说话人纠缠：最难场景是同说话人跨语种需正确接受、异说话人同语种需正确拒绝。标准对抗解耦（盲目语言判别器）会惩罚与语言相关的说话人区分线索，损害身份判别力。全量微调在有限目标数据上还易灾难性遗忘。

## 方法
Dual-LoRA：冻结预训练骨干，全局注入两路并行 LoRA——Speaker Branch（r_spk 较高，ResNet 为 16，w2v-BERT2 为 32）与 Language Branch（r_lang 较低，分别为 4/16），分别提 e_spk 与 e_lang。Language-Anchored Adversary：共享判别器 D；语言锚点流用 e_lang 做语言分类，对抗流经 GRL 把 e_spk 送入同一 D，使对抗梯度对准真实语言线索而非任意相关特征。损失 L_id（Sub-center ArcMargin）+ λ1 L_lang + λ2 L_adv。三阶段课程：先只训语言（λ2=0），再弱对抗，再加强对抗。推理时丢弃语言支路与 D，把 Speaker LoRA 合并进骨干，零额外开销。

## 实验与结果
单系统/消融仅用公开 VoxBlink/VoxCeleb 初始化，在 TidyVoice 上微调 3 epoch。开发集：官方 Full FT ArcFace 3.07% → Sub-center 2.05% → LoRA No Adv 约 1.6%；SamResNet100 Dual-LoRA 0.98%，w2v-BERT2 Dual-LoRA 0.91%。最坏条件 SS-DL vs DS-SL：基线 5.19% → Ours 1.62%。探针 LID：No Adv 72.71%、Std Adv 55.03%、Dual-LoRA 49.02%，同时 EER 最低。跨 ResNet293/SamResNet100/w2v-BERT2，Dual-LoRA 均优于 No Adv 与 Std Adv。最终提交用内部约 18k 小时/396 语种预训练三骨干，1:1:1 校准后融合：eval-A 2.43%、eval-U 2.84%，相对基线降错约 70%，官方第 3。

## 结论
作者认为双路 LoRA 可在冻结骨干上显式因子化说话人与语言；语言锚定对抗比盲目 DANN 更能去语言、保身份；融合系统在见/未见语种评测上均稳健，获挑战第 3。

## 点评
做法针对的是“对抗去语言时误伤说话人”：用独立语言 LoRA 给判别器提供真语言锚点，比直接从 e_spk 猜语言更可控。脆弱点在于课程 λ 与非对称秩需调参，且最终成绩依赖大规模内部多语预训练；若语言支路表征弱，锚定本身会偏，对抗仍可能抹掉有用相关特征。
