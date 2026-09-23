# Is Speaker Identity a Unitary Construct? Neural Evidence for Distinct Trait Processing

- 论文编号：1018
- 报告人：Kaile Zhang
- 程序：Monday 28 September 2026 / Brain Studies and Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26r_interspeech.pdf

## 问题
说话人身份常被当作单一构念，主要定位于双侧 STG/STS（TVA）；但性别、年龄、口音等特质声学/音系线索不同，是否共享同一机制尚未分清。

## 方法
34 名普通话母语成人做 fMRI（3T Prisma）。刺激为 ChatGPT-4 生成、OpenAI TTS 合成的伪英语词，分性别（2 男 2 女成人）、年龄（儿童/成人）、口音（英式/印度英语）三任务，另有纯音高低基线。Block 设计：听刺激并按键判断特质。DeepPrep 预处理；表面 GLM 对比各特质相对纯音，簇置换检验；三特质 conjunction 定义共享 ROI，再对 ROI 内激活做重复测量 ANOVA。

## 实验与结果
行为：口音最难（准确率 86.76%，RT 约 1087 ms），性别最易（97.70%，约 854 ms），年龄居中。影像：三条件均激活双侧 STG/STS/HG；conjunction 得共享“voice core”。ROI 内口音激活显著强于性别与年龄；年龄额外招募左侧感觉运动/前运动区（PostCG/PreCG），口音额外招募双侧 IFG/MFG/SFG，性别主要停留在颞上听觉区。

## 结论
说话人身份加工非单一：共享听觉核心 + 特质特异扩展区（core-plus-extension）。口音认知负荷最高、额颞网络参与更多；性别依赖低层声学线索。提示未来说话人自适应模型可利用特质分层编码。

## 点评
用伪词弱化语义干扰、再用纯音基线剥离一般声学，设计上适于拆解身份维度；conjunction + ROI 幅度比较把“同一核心、不同负荷”说清楚。局限是合成伪词/固定口音对、任务判断本身引入决策网络，扩展区未必纯属“身份编码”。
