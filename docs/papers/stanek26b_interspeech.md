# Ethical and Technical Limits of Deepfake Speech Datasets

- 论文编号：124
- 报告人：Vojtěch Staněk
- 程序：Tuesday 29 September 2026 / Safeguarding Synthetic Speech: Ethical, technical and legal perspectives
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/stanek26b_interspeech.pdf

## 问题
深度伪造语音检测器的鲁棒性与公平性声明，取决于训练/评测数据集质量；现有基准多服务准确率竞赛，与 EU AI Act 等对文档、可追溯与偏置监测的要求错位。跨数据集评测常被当作域外测试，但可能共享真实语音源。

## 方法
审计 39 个同行评审报告的深度伪造语音数据集：可及性、许可、语言、人口统计元数据、合成工具披露、规模，并绘制 bona fide 源语料重叠图（交互浏览器公开）。属性对照论文与官方仓库交叉核对。

## 实验与结果
仅约 49%（19/39）同时报告男女说话人计数/标签；口音、年龄、族裔等几乎缺失，公平评测基本不可行。语言：64% 单语（多为英/中），多语仅约 21%。23% 仅单一合成器或未披露工具。15% 受限访问；部分许可不清或禁商用。源侧大量依赖 LJSpeech、VCTK、AISHELL、LibriVox 衍生资源，跨集评测可能泄漏语料特异伪影。无一数据集同时满足作者所列“无偏检测”全部属性。

## 结论
缺失人口/语言元数据使公平评估受阻；共享真实源削弱跨集泛化叙事。建议发布时报告人口与语言元数据、详细合成管线、真实语音来源、清晰许可与可靠获取。

## 点评
把批评落在数据集基础设施而非再刷榜，对领域很及时。强在系统表与源重叠可视化；弱在重叠无法从公开文档精确量化（作者已声明），结论偏审计清单而非因果实验。
