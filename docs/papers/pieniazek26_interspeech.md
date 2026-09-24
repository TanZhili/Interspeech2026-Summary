# Detection of Incorrect Place of Articulation in Polish Sibilants Using Convolutional Autoencoders

- 论文编号：2624
- 报告人：Wojciech Pieniążek
- 程序：Wednesday 30 September 2026 / Child Speech and Health
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pieniazek26_interspeech.pdf

## 问题
儿童齿擦音错误很常见，早期诊断依赖言语治疗师，资源有限。需自动检测波兰语清卷舌擦音/塞擦音 /ʂ/、/tʂ/ 的错误发音部位（尤其齿化相对规范卷舌）。

## 方法
4–8 岁儿童语料（/ʂ/：149 人 1746 次；/tʂ/：151 人 586 次），SLP 标注 PoA；中心麦 44.1 kHz，手切音段→64×64 语谱图。三种卷积自编码器（CAE / SCAE / MTCAE）学潜表示，SVM-RBF 分类；说话人独立 10 折；潜维 d∈{10…30}，类别加权处理失衡。

## 实验与结果
以敏感性为主。/ʂ/ 最佳 MTCAE 敏感性约 81–84%、准确率约 73%；顶尖配置多为 MTCAE/SCAE。/tʂ/ 顶尖十个敏感分类器均为 MTCAE，敏感性最高约 84%。Kruskal-Wallis 显示自编码器类型对性能有显著影响。约三分之二极端超参配置因退化被剔除。

## 结论
自编码器嵌入 + SVM 可在具挑战性的儿童语音上检测错误 PoA；多任务变体整体最有效。为儿科构音辅助筛查提供特征学习路径。

## 点评
小样本、说话人独立、以敏感性优先，设定符合筛查场景；多任务把类别信息压进瓶颈，比纯重构更贴诊断。类别严重失衡、仅二分卷舌 vs 齿化、手切语谱图，限制现场端到端部署；未与端到端 CNN 直接对照，贡献更偏表示学习比较。
