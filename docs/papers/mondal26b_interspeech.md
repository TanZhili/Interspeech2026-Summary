# Spontaneous Dialect-Aware Speech Corpus for Low-Resource Dakhini, A Southern Indo-Aryan Language: Methods, Challenges, and Insights

- 论文编号：2640
- 报告人：Anindita Mondal
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mondal26b_interspeech.pdf

## 问题
Dakhini（德干接触变体）口语资源匮乏；无标准书面语、声望低，录音场景易触发向标准 Hindi/Urdu 的语码切换（观察者效应），若缺乏结构清单，采集到的可能是“干净但不地道”的数据。

## 方法
先做结构与社会语言学预研形成诊断特征清单；电话场景、熟人男女配对对话，非对称知情（仅 anchor 知情，对方事后告知并知情同意）；Hyderabad 约 160 说话人（17–50 岁，约 70% 男），每通约 20 分钟取约 5 分钟。pyannote 说话人日志后保留未知情说话人；IndicConformer Hindi ASR 预转写，将与标准形式的偏差当作方言信号，规则标签 PA/PV/MAUX/MP-KO/MP/SF/LD，按标签密度分流人工复核。

## 实验与结果
正文以方法与案例为主：预调研中弱势群体在正式场合更常用 Dakhini（如劣势背景男 10/15、女 11 使用），受教育群体更常转向标准语（男 6/15、女仅 2）。给出标准–Dakhini 对应表（如 itnaa→ittaa、aadmii→admii、省略 hai、kaiku/nakko 等）。未报告大规模 ASR 词错误率等下游基准数字；结论段在抽取文本中截断。

## 结论
作者强调真实方言建库依赖结构知识、社区嵌入招募与降低监控感的采集设计，而非仅录音设备；方言感知规则标注可把 ASR 标准化错误转化为有用信号，为方言敏感 ASR/对话建模奠基。

## 点评
把社会语言学观察者效应直接写进采集协议（电话 + 非对称知情），对非声望变体很关键。强在诊断清单驱动的 QC 与半自动标注 triage；弱在正文几乎无量化语料/系统评测、伦理上的隐蔽录音需严格事后同意执行，且全文尾部截断限制对最终规模声明的核对。
