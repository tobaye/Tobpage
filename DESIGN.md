# Tobpage 主题设计说明（普客网 · Hugo）

> 工作名 **Tobpage**（TobPress 的姊妹命名）。骨架取 Butterfly + AnZhiYu（张洪 Heo 设计血统），皮肤为普客网专属的「暗黑西游」。
> 本文档记录：设计来源拆分、暗黑西游视觉规范、资产可替换设计、上线不可破坏清单、构建方式。
> 状态：仅本地开发与试构建，未上线、未推送。

## 1. 设计来源拆分（谁的底子、谁的增改）

参考对象：

- **Butterfly**（jerryc127/hexo-theme-butterfly，Apache-2.0，源流为 hexo-theme-melody）——老牌 Hexo 主题，结构底盘。
- **AnZhiYu 安知鱼**（anzhiyu-c/hexo-theme-anzhiyu，GPL-3.0，主题设计：张洪 Heo）——README 明示「一款基于 hexo-theme-butterfly 修改的主题」，在蝴蝶骨架上做 Heo 式视觉与功能增改。

### 1.1 蝴蝶的底子（Butterfly 原生，Tobpage 沿用其布局骨架）

| 设计件 | 说明 |
| --- | --- |
| 双栏布局 | 文章流（左/主栏）+ 粘性侧栏（右），移动端收起为单栏 |
| 卡片式文章流 | 封面 + 标题 + 摘要 + 元信息（日期/分类/标签）的横向卡片 |
| 侧栏组件群 | 作者卡（头像/简介/社交/统计）、分类卡、标签云、归档/最新文章 |
| 文章页 TOC | 右侧粘性目录、滚动高亮（scrollspy）、阅读进度百分比/进度条 |
| 元信息体系 | 字数统计、预计阅读时长、发布/更新日期 |
| 页脚信息区 | 多行信息页脚：版权、驱动、框架/主题署名、自定义文本 |
| 暗色模式 | 一键切换 + 本地记忆 |
| 本地搜索 | 主题内置本地搜索方案（Butterfly 支持 Algolia/本地/DocSearch 三选其一） |
| 归档/分类/标签页 | 时间线式归档、分类与标签索引页 |
| 回到顶部按钮 | 右下角悬浮按钮组（含阅读进度） |
| 404 页 | 主题自带错误页 |

### 1.2 安知鱼 / Heo 的增改（AnZhiYu 在蝴蝶之上的招牌件，Tobpage 取其神）

| 设计件 | 说明 |
| --- | --- |
| 首页 Hero | 顶部大图/大标题区：站名大字 + 副标题 + 主题色氛围，安知鱼首页的门面 |
| 清爽卡片风 | 更大的圆角（12–16px 级）、更柔和的扩散阴影、卡片 hover 上浮+阴影加深 |
| 主题色体系 | 主色 `#49B1F5`（安知鱼蓝）为核心的 CSS 变量体系；进阶有「主色随文章封面取色」 |
| 全局中控台 | 右下角聚合控制台（搜索/暗色/回到顶部等一处收纳）——Tobpage 以简化版悬浮按钮组落地 |
| 沉浸式状态栏 | 滚动后顶栏收起/毛玻璃化，阅读时标题居中显示 |
| AI 摘要卡 | 文章顶部 AI 摘要（需外部服务，Tobpage 不落地，仅记录） |
| 人生进度/说说/相册等页型 | Heo 生活化页面组件（与普客网定位无关，不落地） |
| 细节动效 | 卡片封面 hover 缩放、标签胶囊、加载过渡等微交互 |

### 1.3 Tobpage 的落地取舍

- **取骨架**：双栏卡片流、粘性侧栏组件群、TOC+阅读进度、字数/时长、归档时间线、页脚信息区、本地搜索、回到顶部——全部按蝴蝶骨架实现（Hugo 模板手写，不移植 Hexo 代码）。
- **取神韵**：Hero 门面、大圆角柔和阴影卡片、hover 动效、主色变量体系——按安知鱼/Heo 的审美尺度实现。
- **不取**：PJAX、评论系统、AI 摘要、说说/相册、中控台全量版、任何外部 CDN 与第三方服务（普客网是纯静态个人站，保持零外部依赖）。
- **换皮肤**：见第 2 节「暗黑西游」。安知鱼蓝仅作为设计史记录，Tobpage 的主色变量默认是鎏金（见 2.2）。

## 2. 暗黑西游视觉规范（普客网专属皮肤）

### 2.1 气质

深色为默认气质（首次访问、无本地偏好时进暗色）；浅色可用但保持沉稳。文案克制：全站仅 Hero 副标题一处可点题（如「花果山福地，水帘洞洞天」类自撰短句默认不启用，见 2.5），其余界面文案照常是博客语言，不堆砌西游词。

### 2.2 配色（CSS 变量，theme/static/css/tobpage.css 顶部统一管理）

| 变量 | 暗色（默认） | 浅色 | 用途 |
| --- | --- | --- | --- |
| `--gold` | `#c9a24b`（鎏金·金箍金） | `#9a7a2e` | 主色：链接 hover、激活态、边框点缀、按钮 |
| `--gold-bright` | `#e8c268` | `#b8912f` | 渐变高光、Hero 大字渐变 |
| `--red` | `#c8402a`（朱砂赤红） | `#b23a24` | 点缀：火眼金睛光点、进度条尾、徽标 |
| `--bg` | `#0c0b09`（玄黑） | `#e9e2d0`（深灰纸面） | 页面底 |
| `--bg-soft` | `#14110c` | `#efe8d8` | 次级底（代码块、引用底） |
| `--card` | `#1a1712`（墨褐卡面） | `#f6f1e3`（宣纸卡面） | 卡片面 |
| `--text` | `#e8e0cd`（宣纸灰白） | `#29241a` | 正文 |
| `--text-dim` | `#a79c86` | `#6f6450` | 元信息文字 |
| `--border` | `rgba(201,162,75,.20)` | `rgba(122,94,32,.25)` | 金色系描边 |

阅读进度条：鎏金 → 朱砂的横向渐变（火眼金睛意象）。Hero 大字：鎏金渐变字。

### 2.3 母题元素（全部 CSS/SVG 实现，不依赖图片素材）

- **卷云纹（筋斗云）**：内联 SVG 螺旋云纹，用作 Hero 底部衔接、章节分隔线、页脚顶部纹带、404 装饰。可在 CSS 中以 data-URI 背景复用。
- **金环（紧箍/金箍）**：作者卡头像的金色双环描边、TOC 激活项的金环圆点、回到顶部按钮的环形进度意象（简化为金环边框）。
- **水墨烟雾**：页面顶部与 Hero 的多层径向渐变雾气（黑/灰/淡金），纯 CSS 渐变。
- **残旗意象**：仅保留在 Hero 大圣图中（图中披风即残旗），界面不再另加旗帜图形。

### 2.4 字体

- 标题与站名：`"Noto Serif SC","Songti SC","STSong","SimSun",serif`（系统宋体回退，不引外部字体）。
- 正文：系统无衬线栈（`-apple-system,"PingFang SC","Microsoft YaHei",sans-serif` 等），保证中文阅读。
- 诗词正文（blockquote）：宋体、字号略大、字距微宽、行高 1.9–2.0（见 2.6）。

### 2.5 Hero

- 结构：全宽 Hero 区（约 62vh，上限 560px）：背景大圣图 + 玄黑渐变罩，居中站名大字（宋体、鎏金渐变）、副标题（取站点 `params.homeInfoParams.Content`，无则用站点 description）、下方一排统计胶囊（文章/分类/标签数）与「开始阅读」金钮，底部卷云纹衔接到正文区。
- 大圣图：AI 生成的暗黑水墨图（侧影、金箍、火眼金睛赤光、金箍棒、卷云、水墨烟雾），存 `theme/static/img/hero-wukong.jpg`（1920×1280，约 514KB）。
- 副标题点题短句：模板预留 `params.tobpage.heroMotto`，默认空——不填则不显示，保持克制。

### 2.6 诗词正文（深色可读性专项）

- blockquote：宣纸灰白字（暗色 `#ece3cd`）、宋体、行高 2.0、字距 0.02em；底色为极淡金雾 `rgba(201,162,75,.06)`，左侧 3px 鎏金竖线，圆角 12px，内边距宽松；浅色下底色换宣纸深一阶、字色近墨。
- 正文图片：大圆角（14px）+ 柔和深影 + 1px 金边；点击新窗口打开原图（沿用现站习惯）。
- 二级/三级标题：宋体 + 标题前一枚金色云纹小标记（CSS 生成）。

## 3. 资产可替换设计（换皮不动骨）

| 资产 | 换法（任选其一，均不动模板/CSS 结构） |
| --- | --- |
| Hero 大圣图 | ① 直接替换文件 `themes/tobpage/static/img/hero-wukong.jpg`（同名覆盖）；② 站点 `static/img/hero-wukong.jpg` 放同名文件（站点 static 优先于主题 static，构建自动盖住）；③ 在 hugo.toml 设 `params.heroImage = "/images/你的图.jpg"` 指向任意站内路径（相对路径以 `/` 开头） |
| 主色/全部配色 | 只改 `tobpage.css` 顶部 `:root` 与 `[data-theme="light"]` 两组 CSS 变量 |
| 站点 Logo/头像 | 沿用现站参数 `params.label.icon` 与 `params.assets.favicon`（现为 `/images/logo.webp`），换站级文件即可 |
| 起算日（运行天数） | `params.tobpage.startDate`，默认 `2026-10-29` |
| 萌ICP 文案/链接 | `params.tobpage.moeIcp` / `params.tobpage.moeIcpURL`，默认 `萌ICP备20269123号` / `https://icp.gov.moe/?keyword=20269123` |

## 4. 上线不可破坏清单（切换主题时逐项守住）

源自现站（PaperMod）实况核查，Tobpage 已按此设计，切换前须逐项复验：

1. **文章 URL**：`/posts/<文件名>/` 不变（Hugo 默认 section+slug 规则，主题不改 permalink 配置）。
2. **`/admin/` 后台**：`static/admin/`（Sveltia CMS）为站级 static，主题无关，原样保留。
3. **图片路径**：`/images/uploads/*` 与 `/images/logo.webp` 为站级 static，主题模板只引用不搬动；文章封面 frontmatter `cover.image` 相对路径沿用。
4. **RSS**：`/index.xml` 保持可用（站点 outputs home 含 RSS；主题不覆盖 rss 模板，用 Hugo 内置）。
5. **Sitemap**：`/sitemap.xml` 保持（Hugo 内置，主题无关）。
6. **本地搜索**：`/search/` 页可用；依赖 home 的 JSON 输出（hugo.toml `[outputs] home = ['HTML','RSS','JSON']` 不得删），主题提供 `index.json` 模板产出标题/正文/链接/分类/标签。
7. **页脚三件套**：© 年份+站名、页脚文案（`params.footer.text`）、「由 Hugo 驱动」署名、萌ICP备20269123号（链 icp.gov.moe）、本站已运行 X 天（起算 2026-10-29，上线当天记为第 1 天，JS 按本地日期算——与现站 extend_footer 脚本同口径）。
8. **归档页**：`/archives/` 按年 → 中文月份（一月…十二月）分组，沿用现 `layouts/archives.html` 的分组口径（主题内提供同名布局接管，站级 layouts 若保留会优先于主题——切换时二选一，别双份打架）。
9. **导航与社交**：主导航为主题内建的固定结构（首页 + 五大栏目下拉 + 归档 + 关于 + 搜索，见 §7），不读 `menu.main`；页脚/作者卡社交图标取 `params.socialIcons`（github/rss/mail，内联 SVG，不引外部图标库）。
10. **分类体系**：已由 §7 的「五大栏目 + 14 个叶子分类」取代旧五类（技术/诗词/日常/工具/随笔）；`/categories/<名>/`、`/tags/<名>/` 路径规则不变。切换影响面见 §7.3 清单。
11. **日期格式**：`params.DateFormat = 2006年1月2日` 沿用；字数/阅读时长沿用现站开启状态。
12. **深浅色**：现站 PaperMod 有主题切换；Tobpage 保留切换（localStorage 键 `tobpage-theme`，与 PaperMod 的 `pref-theme` 不同名，互不干扰；默认暗色为有意变更，切换方案里需向用户明示）。

## 5. 构建与试用

- Hugo 版本与线上工作流一致：**0.169.0 extended**（`.github/workflows/hugo.yml` 的 `HUGO_VERSION`）。
- 本地试构建：站点副本的 hugo.toml 仅改 `theme = 'tobpage'`，主题目录置于 `themes/tobpage/`（即本仓库 `theme/` 的内容）。
- 零外部依赖：无 CDN、无网络字体、无第三方 JS 库；CSS/JS 各一个文件（`static/css/tobpage.css`、`static/js/tobpage.js`，外加 baseof 内一段防闪烁的主题引导脚本）。

## 6. 已知取舍

- 搜索索引为全量 JSON（现站 9 篇，体积无压力；文章量大后可再分片）。
- 「主色随封面取色」（安知鱼招牌）未落地：与暗黑西游的固定金色体系冲突，且需取色脚本，暂不做；主色走 CSS 变量手改。
- 评论、AI 摘要、说说/相册等 Heo 页型与普客网定位无关，不做。

## 7. 分类体系（栏目 + 二级分类 + 彩色图标）

2026-11-08 用户拍板：文章组织改为「五大栏目（父）→ 叶子分类（子）」两层。**父栏目不是 Hugo 分类**——文章只挂叶子分类，父层只存在于导航与分类索引页的分组里。呈现方式参考 TobPress（合林驿站）的胶囊 + 大图标徽章。

### 7.1 体系表（图标为内联 SVG sprite 名，描边风格）

| 父栏目 | 图标 | 色 | 叶子分类 | 图标 | 色 |
|---|---|---|---|---|---|
| 文章 | feather | `#8b5cf6` | 古诗词 | scroll | `#7c3aed` |
|  |  |  | 现代诗 | pen-nib | `#06b6d4` |
|  |  |  | 散文随笔 | leaf | `#22c55e` |
|  |  |  | 小说故事 | book-open | `#f59e0b` |
| 技术 | code | `#3b82f6` | 运维部署 | server | `#0ea5e9` |
|  |  |  | 编程开发 | terminal | `#6366f1` |
|  |  |  | 经验教程 | lightbulb | `#f97316` |
| 软件 | layout-grid | `#14b8a6` | 软件推荐 | star | `#10b981` |
|  |  |  | 开源项目 | package | `#64748b` |
|  |  |  | 工具分享 | wrench | `#84cc16` |
| 资讯 | newspaper | `#ef4444` | 科技新闻 | rss | `#f43f5e` |
|  |  |  | 站务公告 | megaphone | `#eab308` |
| 日常 | coffee | `#fb923c` | 生活随记 | sun | `#f59e0b` |
|  |  |  | 见闻杂记 | camera | `#ec4899` |

导航固定项：首页（home，鎏金 `#c9a24b`）、归档（archive）、关于（user）、搜索（图标按钮）。父栏目链接指向 `/categories/#g-<父名>` 分组锚点；下拉子项链向各叶子分类 term 页（该分类尚无文章时回退到同一分组锚点）。

### 7.2 实现方式（改一处全站生效）

- **元数据唯一定义处**：`layouts/partials/category-meta.html`，以 `return` 返回 dict：`parents`（父栏目有序列表，含 icon/color/children 有序名录）+ `cats`（叶子分类名 → parent/icon/color）。页眉下拉、分类索引分组、卡片/文章页胶囊、分类页徽章、侧栏分类列表全部读它。
- **图标**：`layouts/partials/icon-sprite.html`（隐藏内联 SVG sprite，26 个符号，路径取自 feather/lucide 开源图标，描边风格、零外部资源）+ `layouts/partials/icon.html` 引用助手（`{{ partial "icon.html" (dict "name" "scroll" "size" 16 "color" "#7c3aed") }}`）；sprite 在 baseof 的 `<body>` 后注入一次。
- **胶囊**：`layouts/partials/cat-chip.html`（输入分类名）：按元数据上色（CSS 变量 `--cat` + `color-mix` 描边/底色），链接用 term 页真实 RelPermalink（兼容子路径 baseURL）；未登记的分类回退 tag 图标 + 鎏金，不报错。
- **导航**：header 内建（不读 menu.main）；桌面端 CSS hover/focus 展开下拉，移动端（≤720px）由 tobpage.js 做手风琴（首击展开、再击跳转、同时只开一个）；term 页与文章页按分类自动高亮所属父栏目。
- **分类索引**：`/categories/` 按父栏目分组（锚点 `g-<父名>`），子分类卡含大图标、名称、篇数；暂无文章的叶子分类显示为不可点卡片（暂无文章），不产生 404 链接；未登记的现存分类单列「其他」组兜底。单个分类页头部带彩色大图标徽章 + 「所属栏目：X · 共 N 篇文章」。

### 7.3 正式站切换时清单（分类相关）

1. **Sveltia 后台选项**：`static/admin/config.yml` 的 categories 选项由旧五类换成上表 14 个叶子分类（只列叶子，不列父栏目）。
2. **存量文章同步**：正式站文章的 categories 做 `诗词 → 古诗词` 改名（2026-11-08 时为 9 篇诗词帖）；其余如有个别旧分类（技术/日常/工具/随笔）需人工逐篇归位到新叶子分类。
3. **旧地址失效**：切换后 `/categories/诗词/` 不复存在（Hugo 不为改名自动留别名）。站内链接以新地址为主、影响小；是否给旧分类地址留跳转页（aliases），切换时再议。
4. **预览站的 about 页是副本独有**：测试副本 `content/about.md` 为给「关于」导航项凑落点而加；正式站切换时需正式补一篇关于页（或改导航），别把副本那篇短文直接当正式内容。
5. **主旨语参数**：正式站 `hugo.toml` 须配 `[params.tobpage] heroMotto = '普天之下，皆为客'`（2026-11-08 用户定版，见 §9）；Hero 区与开场动画共用此参数，不配则两处都不显示主旨语。同段的 `startDate`、`moeIcp`、`moeIcpURL` 也须照预览副本的值显式配好。

### 7.4 正式切换完成记录（2026-11-08）

§7.3 五项已全部落实，普客网正式站已由 PaperMod 切换为 Tobpage：

1. ✅ Sveltia `static/admin/config.yml` 分类选项换成 14 个叶子分类。
2. ✅ 9 篇存量文章分类 `诗词 → 古诗词`（date 与正文未动；站内无其他旧分类文章）。
3. ✅ 旧地址 `/categories/诗词/` 线上实测 404（未留 aliases 跳转页，如实记录）。
4. ✅ 正式站新写 `content/about.md`（非预览副本短文）：主旨、五大栏目、联系邮箱、自 2026 年 10 月起运行。
5. ✅ 线上 `hugo.toml` 已配 `[params.tobpage]`：`heroMotto = '普天之下，皆为客'`、`startDate = '2026-10-29'`、`moeIcp`、`moeIcpURL`，与预览副本一致。

- **切换提交**：tobaye/tobaye.github.io `db940563`（2026-11-08 23:39 CST，增量树提交，父提交 `03cfd1ec` 即回滚点；themes/PaperMod 保留在仓内未删）。Actions「Deploy Hugo site to Pages」一次成功，线上逐项验活全过（首页/文章/分类/归档/搜索/关于/RSS/JSON/后台/图片 200，不存在路径 404，页脚 © · Hugo · 萌ICP备 + 运行天数组件齐全）。
- **附带修复**：切换后发现 `/robots.txt` 404。实测定位：Hugo 0.169 在站点配了 `[languages]` 块时不生成 robots.txt（与模板位置无关，最小站点对照验证；PaperMod 时期同样受此影响，非本次切换引入）。正式站改用 `static/robots.txt` 静态文件（内容与主题模板的生产输出一致），修复提交 `398595f0`（23:42 CST），线上已 200。主题内的 `layouts/robots.txt` 模板保留，供未配 `[languages]` 的站点使用。
- **主题源码仓**：tobaye/Tobpage（主题文件 + 本文档），与站点仓内的 `themes/tobpage/` 同源；今后改主题先动源码仓再同步进站。

## 8. 移动端二级菜单 bug 根因（2026-11-08 修复）

- **现象**：手机上展开父栏目后，子菜单文字与图标全部出屏，只剩右对齐的彩色圆点留在屏内（用户实机截图）。
- **根因**：桌面下拉的显示规则 `.has-drop:hover .nav-drop, .has-drop:focus-within .nav-drop { …; transform: translate(-50%, 0); }` 特异性为 0,3,0；移动端重置只写在 `.site-nav .nav-drop`（0,2,0）上，压不住该 transform。移动端子菜单 position 已改 static，但点父栏目后链接保持 `:focus-within`，漏进来的 `translate(-50%, 0)` 把子菜单左移自身宽度的一半（无头 Chromium 实测 rect x = -163），文字图标出屏，唯圆点（margin-left:auto 贴右）还留在屏内。
- **修法**：在 `@media (max-width: 720px)` 内把 transform 的重置提到同等特异性：`.has-drop:hover .nav-drop, .has-drop:focus-within .nav-drop { display: none; transform: none; }` 与 `.has-drop.open .nav-drop { display: flex; transform: none; opacity: 1; visibility: visible; }`。顺带：移动抽屉底色由半透 `--header-bg`（依赖 backdrop-filter，个别浏览器兜不住会透出正文）在移动端改为近实底 `background: var(--bg)`，桌面端不动。
- **验收**：无头 Chromium 390×844 实测，展开后第一个 `.nav-drop` rect x ≥ 0、首个子链接文字 span 在视口内。

## 9. 开场动画（大圣驾筋斗云 preloader）

学蝴蝶主题的 preloader，换成本主题的大圣视觉：

- **资产**：`static/img/loader-wukong.jpg`（黑金水墨风，纯黑底；CSS 用 `mix-blend-mode: screen` 让黑底与 overlay 底色无缝融合）。初版为大圣侧身驾金色卷云（720×691，约 98KB，配径向遮罩羽化边缘）。
- **定版图（2026-11-08 用户挑定）**：loader 大圣图定为候选 **v10「动静之间」**——大圣端坐螺旋云峰之巅（v7 式称王构图），棒身斜贯画面、棒尖在右上拖出大弧金光（v6 的动势），原版金线笔意。自高清原图（1120×2240）裁上半幅（0,40–1120,1360：保全主体、全棒斜贯与棒尖弧光，裁掉下半云柱与云海）缩至 660×778、约 140KB。因棒尖弧光与棒尾贴近画面边缘，`.pl-wukong` 已去掉原径向遮罩（遮罩会把弧光裁没），仅靠 screen 混合融合黑底；显示宽 `min(74vw, 320px)`，模板宽高属性同步为 660×778。高清原图存 `~/workspace/tobpage/candidates/v10-fusion-dynamic-hires.jpg`。
- **结构**：baseof `<body>` 开头 `#preloader` 全屏 overlay（背景 `#0c0b09`）：缓慢旋转的 SVG 卷云纹（`.pl-swirl`，26 秒一圈）垫底，大圣图自左腾入（`.pl-fly`）后上下浮沉（`.pl-bob`），站名宋体字淡入（站名读 `site.Params.label.text | default site.Title`，不写死），站名下方一行主旨语小字（`.pl-motto`，晚站名半拍淡入），下方一条金→赤渐变细进度线往复扫过。
- **主旨语定版（2026-11-08 用户定）**：普客网主旨语为 **「普天之下，皆为客」**。单一数据源 `params.tobpage.heroMotto`：首页 Hero 区（`.hero-motto`）与开场动画站名下方（`.pl-motto`）共用同一参数，没配则两处都不渲染；别的站点接入时填自己的主旨语即可。
- **主旨语样式定版（2026-11-08 用户定）**：两处主旨语与上下元素拉开古朴差别，同一套处理——字体走楷体栈 `--font-kai`（`"Kaiti SC", "STKaiti", "KaiTi", "楷体", var(--font-title)`，系统字体零外部引入）；颜色走朱砂变量 `--motto: var(--red-bright)`（暗底 `#e2543a` 提亮赤、浅色模式随变量变深为 `#c0452c` 保证纸面可读），与上方鎏金渐变标题、下方灰白副标题明显区分；两侧配黯金细线（`::before/::after` 渐隐短横线，Hero 34px / 动画 26px），字尾缀一个 7px 朱砂小方印点（`.motto-seal`，模板内 span，似印章一角）；字号 Hero 17px、动画 16px，字距 `.5em`，动画淡入节奏不变（晚站名半拍）。
- **两段式定版（2026-11-08 用户拍板）**：loader 改为两段式叙事——第一段 v11「在飞」寓意「网站正在飞速加载赶来」，收尾切第二段 v12「棍指南天门」寓意「门就在前面、内容马上出现」；上一版定版图 v10「动静之间」自此留档 candidates、不再用作 loader。两图均为 660×778 纯黑底定版（`loader-wukong.jpg` = v11，约 111KB；新增 `loader-arrive.jpg` = v12，约 144KB），处理口径：黑阶压实（黑点 22）+ 边缘 34px 柔和压暗，消除融合时图块边缘的极淡矩形界。**形象统一**：v12 大圣以 v11 为角色基准重新生成对齐版（`candidates/v12-nantianmen-harmonized-hires.jpg`）——脸型口鼻、图案金紧箍、蜷曲尾巴、深色袍服的云纹镶边 panels、向左拉满的披风飘带、螺旋云纹与人物占比均向 v11 看齐，构图仍是立云海、棒斜指南天门于右上云气；剩余细微差异：发箍中央纹饰略有不同、姿态一飞一行（构图使然）。结构：baseof 里两图同位叠放（`.pl-img-a` / `.pl-img-b`，B 图绝对定位、初始 opacity 0），切到收尾时 `.pl-arrive` 令 A 淡出 B 淡入（crossfade 约 300ms），`.pl-inner` 同时 scale 到 .97 做「落定」收束。
- **退场纪律（硬性，两段式口径）**：① head 引导脚本先行判定——`prefers-reduced-motion` 时不播、sessionStorage 有 `tobpage-loaded` 标记时同会话不再播，才给 `<html>` 加 `.show-preloader`，CSS 仅在该类下显示 overlay（不播则 DOM 里虽有节点但永不显示，主脚本随即移除）；② 时序：第一段至少展示 **800ms**（load 更早到也要等满，保证两拍都看得见）→ window `load` 触发即 crossfade 进收尾拍 → 收尾图停留约 **500ms** → 整体淡出（0.55s）并从 DOM 移除；③ load 迟迟不来时最迟 **1.9s** 强制进收尾拍，全局硬上限 **3s** 必开始退场（因此原 2.5s 兜底改 3s：给「800ms 最短展示 + 收尾拍」留出完整时序，baseof 内联兜底与 tobpage.js 同口径双保险，主脚本加载失败也不会挡住正文）；④ 退场后元素已移除，不存在 pointer-events 残留问题。

## 10. 通用性（别的站点接入本主题时）

主题不得带出普客网专属信息，以下逐项区分「读站点配置」与「主题内置」：

**读站点配置（`hugo.toml` 的 params，各站填自己的，没配就不渲染对应项）：**

| 内容 | 参数 | 没配时 |
|---|---|---|
| 站名（页眉品牌、Hero 标题、开场动画站名、页脚） | `site.Title` / `params.label.text`（品牌与动画优先 label.text） | 回退 `site.Title` |
| 备案号与链接 | `params.tobpage.moeIcp` / `params.tobpage.moeIcpURL` | **整项不渲染**（无默认值，主题不内置任何备案号）；有号无链接则纯文本 |
| 运行天数起算日 | `params.tobpage.startDate`（如 `2026-10-29`） | **整项不渲染**（页脚元素不带 data-start 就不存在，JS 无兜底日期） |
| Hero 图 | `params.heroImage` | 回退主题内置 `img/hero-wukong.jpg`（见下） |
| Hero  motto / 副标题 | `params.tobpage.heroMotto` / `params.homeInfoParams.Content`，副标题再回退 `params.description` | motto 不渲染；副标题为空则空 |
| 页脚简介、社交图标、站标、favicon | `params.footer.text` / `params.socialIcons` / `params.label.icon` / `params.assets.favicon` | 对应块不渲染 |

**主题内置（随主题走，各站如需更换按 §3 资产可替换方式覆盖）：**

- 栏目分类元数据：`layouts/partials/category-meta.html`（栏目名、父子关系、图标名、色值都在这一处；别的站栏目不同就改这一份文件，全站导航/分组/胶囊随之变）。
- 大圣视觉资产：`static/img/hero-wukong.jpg`（Hero 默认图）、`static/img/loader-wukong.jpg` + `static/img/loader-arrive.jpg`（开场动画两段图）；站点在自己的 `static/img/` 放同名文件即可覆盖，或用 `params.heroImage` 换 Hero 图。
- 暗黑西游配色与母题（CSS 变量与 SVG 云纹，见 §2）：属主题皮肤本身，非站点信息。

## 11. 全站自检记录（2026-11-08，正式切换前最后一遍）

方法：Playwright 无头 Chromium，390×844 与 1280×800 双视口，本地服务实测预览构建产物（首页/文章《望庐山瀑布二首》/分类索引/古诗词分类/归档/搜索/关于/404），含交互与浅色全量复看。验收图存 `audit-20261108/`。

**查出并已修（3 处真问题）**
1. **页脚/作者卡 GitHub 图标路径数据损坏**：social-icons.html 的 GitHub path 有一处数字粘连（`1.27.35.83`），每页控制台报错、图标渲染残缺。已换成 simple-icons 官方标准路径，复验全站控制台零错误、图标正常。
2. **Hero 背景图默认路径写死根绝对**：index.html 默认值 `/img/hero-wukong.jpg` 在子路径部署（预览站）下 404、Hero 无画。已改走 `relURL`（站点仍可用 `params.heroImage` 自定义），预览与根域两种部署都成立。
3. **搜索索引 fetch 写死 `/index.json`**：子路径下会拉到别站的索引（预览站上等于搜正式站的数据且链接跳正式站）。已改：search.html 的输入框带 `data-index="{{ "index.json" | relURL }}"`，JS 读该属性。复验预览内搜「李白」得 9 篇、链接指向预览自身。

**美化（1 处）**：Hero 内容区衬底加一层暗色径向渐变（680×320 @50% 46%），提升鎏金大标题与朱砂主旨语压在水墨画上的可读性，深浅两态都受益（浅色下 Hero 保持暗色画带，为既定设计）。

**性能**：loader 两图同尺寸重编码瘦身（arrive 148→119KB、wukong 115→96KB，画质目检无损）；Hero 图 526KB 试压仅省 5%，不动原图。CSS 34.8KB（gzip 8.8KB）、JS 8.8KB（gzip 3.6KB）、搜索索引 87KB（按需加载）、卡片封面已带 lazy，首页无重复加载。

**逐项结论**：8 类页面双视口全 200（404 为主题页直开核验，GitHub Pages 上线后以 404 状态 serve 同一文件）；每页恰 1 个 h1、标题层级零跳级；零横向溢出、零出界元素、零裂图；图标引用 23 种与 sprite 定义逐一对账零缺失；文章页导航高亮「文章」、分类页高亮所属栏目、面包屑 首页/古诗词/文正确；TOC 7 锚点全部点达；手风琴复测 rect x=16、transform none（§8 的 bug 未复发）；桌面 hover 下拉、深浅切换刷新持久、正文图新窗大图、回到顶部均正常；loader 两段式复测 arrive ≈1.0s、整体 ≈2.1s 退场，浅色首访 overlay 仍为 #0c0b09 暗底不突兀；浅色首页+文章页完整复看，对比度与诗词引文块均合格。

**上线前状态**：主题与预览已同步，预览仓 commit `02f4e25`（父 a9e073b）。正式站切换仍按 §7.3 清单执行（站级 layouts 移除/改名、Sveltia 分类名单、存量分类改名、参数显式配置），切换后线上再复验 robots 与 404 状态码。
