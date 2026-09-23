# MOS-Bias: From Hidden Gender Bias to Gender-Aware Speech Quality Assessment

- 论文编号：67
- 报告人：Wenze Ren
- 程序：Wednesday 30 September 2026 / Speech Synthesis Evaluation 2
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ren26_interspeech.pdf

## 问题
MOS 是语音质量金标准，但听者人口学偏差少被系统研究。若男女听者评分标准不同，简单平均会掩盖组间差异，并可能把某种性别的感知标准写进自动 MOS 模型。

## 方法
在 BVCC（含听者/说话人性别元数据）上分析性别差异；基线用 SSL-MOS。提出 gender-aware 架构：共享 SSL 编码器 + Mean Net（总体 MOS）与 Gender Net（条件于抽象二元组嵌入 0/1，不直接喂性别标签），输出 Avg / Male / Female MOS；多任务等权 MSE（L_avg + L_male + L_female）。

## 实验与结果
男性听者评分系统性高于女性（总体 2.988 vs 2.886，Welch t 检验显著）；差距随质量下降而增大（1–2 档差 0.167，4–5 档仅 0.030）。无性别信息的 SSL-MOS 预测更贴近男性 GT（句级 MSE 0.372 vs 女性 0.430）。Gender-MOS 相对 baseline：全听者句级 LCC 0.862 vs 0.853、MSE 0.239 vs 0.290；男性分支 MSE 0.332、女性 0.366，均优于 baseline。

## 结论
MOS 性别偏差是系统性、质量依赖、可学习的；平均标签与其上训练的模型隐含偏男性标准。抽象组嵌入可提升总体与性别特异预测。未来拟做偏差缓解并在更多数据集验证。

## 点评
把听者性别从“标注噪声”升格为可建模结构，并指出简单全局校准不够（差距随质量变），问题抓得准。抽象 0/1 组嵌入既保留基线“性别中立”接口，又逼模型从数据中挖出两组模式，是务实折中。局限是目前仅 BVCC 有完整性别元数据；且“更准预测各组”不等于“更公平的评估标签”，后续仍需明确公平目标（校准、再加权还是报告分组分数）。
