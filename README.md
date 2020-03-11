## 项目环境说明

本项目的目标网站：<https://www.xfz.cn/> ，具有以下模块：新闻、在线课程、付费资讯、搜索等模块。

其中涉及到的技术要点有：`Django`、`ajax`，`Restful API`，`arttemplate.js`、在线视频播放，支付，`haystack`搜索，`UEditor`富文本编辑器，第三方分享等。

前端技术要点：

- `nvm`：用来管理`node.js`的工具
- `node.js`：自带有`npm`包管理工具
- `npm`：类似于`Python`中的`pip`。可以非常方便的管理一些前端开发的包
- `gulp`：用来自动化开发流程。比如`sass`转`css`，`css`和`js`压缩等

后端技术要点：

- `Python`：开发语言
- `Django`：开发框架
- `MySQL`：数据库

虚拟环境：

- `pipenv`



## 前端开发环境安装

### nvm 安装

`nvm（Node Version Manager）`是一个用来管理`node`版本的工具。我们之所以需要使用`node`，是因为我们需要使用`node`中的`npm(Node Package Manager)`，使用`npm`的目的是为了能够方便的管理一些前端开发的包！`nvm`的安装非常简单，步骤如下：

1. 到这个链接下载`nvm`的安装包：`https://github.com/coreybutler/nvm-windows/releases`。
2. 然后点击一直下一步，安装即可！（避免安装在中文路径下）
3. 安装完成后，还需要配置环境变量，把`nvm`所处的路径填入进去即可！
4. 打开`cmd`，然后输入`nvm`，如果没有提示没有找不到这个命令。说明已经安装成功！

`nvm`常用命令：

1. `nvm install node`：安装最新版的`node.js`，`nvm i == nvm install`。
2. `nvm install [version]`：安装指定版本的`node.js` 。
3. `nvm use [version]`：使用某个版本的`node`。
4. `nvm list`：列出当前安装了哪些版本的`node`。
5. `nvm uninstall [version]`：卸载指定版本的`node`。
6. `nvm node_mirror [url]`：设置`nvm`的镜像（提高下载速度）：`nvm node_mirror https://npm.taobao.org/mirrors/node/`
7. `nvm npm_mirror [url]`：设置`npm`的镜像（提高下载速度）：`nvm npm_mirror https://npm.taobao.org/mirrors/npm/`

### node 安装

安装完`nvm`后，可以通过`nvm`来安装`node`。本项目使用`6.4.0`版本的`node.js`

安装命令：`nvm install 6.4.0`

安装完成后，也要配置环境变量

### npm 安装

`npm(Node Package Manager)`在安装`node`的时候就会自动的安装了，使用 `nvm use 6.4.0`切换 node 的版本

建议使用淘宝镜像，因为 镜像源在国外，下载安装速度超慢，操作方法：

`npm install -g cnpm --registry=https://registry.npm.taobao.org`

上面这条命令，在网速不佳的情况下，也是需要有耐心等待安装完成的。

**安装完成后，以后就可以使用 `cnpm uninstall [package]`来安装各种包了，而且速度提升非常明显**

### gulp 安装与使用

1、创建本地包管理环境

使用`npm init`命令在本地生成一个`package.json`文件，`package.json`是用来记录你当前这个项目依赖了哪些包，以后别人拿到你这个项目后，不需要你的`node_modules`文件夹（因为`node_moduels`中的包实在太庞大了）。只需要执行`npm install`命令，即会自动安装`package.json`下`devDependencies`中指定的依赖包。

2、安装 gulp

- 全局安装：`cnpm install gulp -g`
- 本地安装：`cnpm install gulp --save-dev`
- 指定安装版本：`cnpm install gulp@版本号 --save-dev`
- 开发项目时，全局和本地都需要安装 gulp

`--save-dev`是将安装的包的添加到`package.json`下的`devDependencies`依赖中。以后通过`cnpm install`即可直接自动完成所有所需要的包的安装。`devDependencies`这个是用来记录开发环境下使用的包，如果想要记录生产环境下使用的包，那么在安装包的时候使用`npm install xx --save-dev`就会记录到`package.json`下的`dependencies`中，`dependencies`是专门用来记录生产环境下的依赖包的！

```python
"devDependencies": {
    "browser-sync": "^2.24.4",
    "gulp": "^3.9.1",
    "gulp-autoprefixer": "^5.0.0",
    "gulp-cache": "^1.1.1",
    "gulp-concat": "^2.6.1",
    "gulp-concat-folders": "^1.3.1",
    "gulp-connect": "^5.5.0",
    "gulp-cssnano": "^2.1.3",
    "gulp-imagemin": "^4.1.0",
    "gulp-rename": "^1.2.3",
    "gulp-sass": "^4.0.1",
    "gulp-sourcemaps": "^2.6.4",
    "gulp-uglify": "^3.0.0",
    "gulp-util": "^3.0.8"
  }
```

以上的包，重点留意版本搭配，`"gulp": "^3.9.1"`尽量使用4.0以前的版本，因为4.0以后的版本，容易发生不兼容的问题。

3、创建 gulp 任务

要使用`gulp`来流程化开发工作。首先需要在项目的根目录下创建一个`gulpfile.js`文件。然后在`gulpfile.js`中填入以下代码：

```javascript
var gulp = require("gulp")
```

4、创建处理 css 文件的任务

需要使用`gulp-cssnano`来处理 css 文件的压缩：`cnpm install gulp-cssnano --save-dev`

在`gulpfile.js`中代码：

```javascript
var gulp = require("gulp")
var cssnano = require("gulp-cssnano")

// 定义一个处理css文件改动的任务
gulp.task("css",function () {
    gulp.src("./css/*.css")
    .pipe(cssnano())
    .pipe(gulp.dest("./css/dist/"))
});
```

5、修改文件名

需要使用`gulp-rename`来修改文件名：`cnpm install gulp-rename --save-dev`

在`gulpfile.js`中代码：

```javascript
var rename = require("gulp-rename")
gulp.task("css",function () {
    gulp.src("./css/*.css")
    .pipe(cssnano())
    .pipe(rename({"suffix":".min"}))
    .pipe(gulp.dest("./css/dist/"))
});
```

6、创建处理 js 文件的任务

需要使用到`gulp-uglify`插件来压缩 js 文件：`cnpm install gulp-uglify --save-dev`

在`gulpfile.js`中代码：

```javascript
var uglify = require('gulp-uglify');
gulp.task('script',function(){
    gulp.src(path.js + '*.js')
    .pipe(uglify())
    .pipe(rename({suffix:'.min'}))
    .pipe(gulp.dest('js/'));
});
```

7、合并多个文件

在网页开发中，为了加快网页的渲染速度，有时候我们会将多个文件压缩成一个文件，从而减少请求的次数。需要用到`gulp-concat`插件：`cnpm install gulp-concat --save-dev`

```js
var gulp = require('gulp');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
gulp.task('vendorjs',function(){
    gulp.src([  // 合并哪些文件
        './js/nav.js',
        './js/index.js'
    ])
    .pipe(concat('index.min.js'))  // 合并到那个文件
    .pipe(uglify())  // 压缩 js 文件
    .pipe(gulp.dest('dist/js/'));
});
```

8、压缩图片

图片是限制网站加载速度的一个主要原因。图片越大，从网站上下载所花费的时间越长。因此对于一些图片，我们可以采取无损压缩，即在不改变图片质量的基础之上进行压缩。可以使用`gulp-imagemin`来处理；

同时，为了避免重复压缩，要搭配`gulp-cache`来缓存那些压缩过的图片：

```javascript
var imagemin = require('gulp-imagemin');
var cache = require('gulp-cache');
gulp.task('image',function(){
    gulp.src("./images/*.*")
    .pipe(cache(imagemin()))
    .pipe(gulp.dest('dist/images/'));
});
```

9、检测代码修改，自动更新

可以使用`gulp`内置的`watch`，只要在终端执行`gulp watch`命令即可自动监听所有的`css`文件，然后自动执行`css`的任务，完成相应的工作：

```JavaScript
// 定义一个监听的任务
gulp.task("watch",function () {
    // 监听所有的css文件，然后执行css这个任务
    gulp.watch("./css/*.css",['css'])
});
```

10、更改文件后，自动刷新浏览器

使用`browser-sync`插件，可以实现浏览器同步更新：`cnpm install browser-sync --save-dev`

```js
var bs = require("browser-sync").create()

gulp.task("bs",function () {
    bs.init({
        'server': {
            'baseDir': './'   // 确定浏览器中 url 的根目录地址
        }
    });
});

// 定义一个监听的任务
gulp.task("watch",function () {
    gulp.watch("./css/*.css",['css'])
});

// 执行gulp server开启服务器
gulp.task("server",['bs','watch'])  // 默认启动 bs watch 这两个任务
```

如果将 `gulp.task("server",['bs','watch'])` 改为 `gulp.task("default",['bs','watch'])` ，则可以直接在终端中输入 `gulp` 直径自动刷新任务



## 前端开发

编写 `gulpfile.js`  文件中的前端监控程序，分别监控html、scss、js、图片文件的更新。

### sass 语法

`css`不是一门编程语言，没法像`js`和`python`那样拥有逻辑处理的能力，甚至导入其他的`css`文件中的样式都做不到。而`Sass`就是为了解决`css`的这些问题。它允许你使用变量、嵌套规则、 `mixins`、导入等众多功能，并且完全兼容`css`语法。`Sass`文件不能直接被网页所识别，写完`Sass`后，还需要专门的工具转化为`css`才能使用。

需要使用`gulp-sass`插件将 sass 转换为 css：`npm install gulp-sass --save-dev`

```js
var gulp = require("gulp");
var sass = require("gulp-sass");
// 处理css的任务
gulp.task('css',function () {
    gulp.src(path.css + '*.scss')
        .pipe(sass().on("error",sass.logError))
        .pipe(cssnano())
        .pipe(rename({"suffix":".min"}))
        .pipe(gulp.dest(path.css_dist))
});
```

区别于 css ，新增的功能：嵌套，引用父选择器（`&`），定义变量，运算，@import语法，@mixin语法。

### 前端开发测绘工具

markman：<http://www.getmarkman.com/>

### 网页结构分析

网页头部、主体、尾部的结构分析；

分析哪些可以重复利用，例如头部、底部，可以通过网页的继承方式，进行重复利用。

### 要点

图标可以使用阿里矢量图标库中的图标：<https://www.iconfont.cn/>

首页轮播图实现：

- JavaScript + jQuery 通过控制轮播图的 left 样式，实现轮播图的滚动，部分代码如下：

  ```javascript
  Banner.prototype.initBanner = function(){
      var self = this;
      var firstBanner = self.liList.eq(0).clone();
      var lastBanner = self.liList.eq(self.bannerCount-1).clone();
      self.bannerUl.append(firstBanner);
      self.bannerUl.prepend(lastBanner);
      self.bannerUl.css({"width": self.bannerWidth*(self.bannerCount+2), "left": -self.bannerWidth});
  };
  ```

使用 flex 实现多个课程自动布局

概念：`CSS3`弹性盒子(`Flexible Box`或 `Flexbox`)，是一种用于在页面上布置元素的布局模式，使得当页面布局必须适应不同的屏幕尺寸和不同的显示设备时，元素可预测地运行。对于许多应用程序，弹性盒子模型提供了对块模型的改进，因为它不使用浮动，`flex`容器的边缘也不会与其内容的边缘折叠。

相关属性：

1. `flex-direction`：确定主轴的方向。默认是横向的。
   - row：横向布局。
   - row-reverse：横向反转布局。
   - column：纵向布局。
   - column-reverse：纵向反转布局。
2. `justify-content`：属性定义了项目在主轴上的对齐方式。
   - flex-start：主轴的起始点对齐（默认）。
   - flex-end：主轴的结束点对齐。
   - center：居中排列。
   - space-between：两端对齐，项目之间的间隔相等。
   - space-around：每个项目两侧的间隔相等。所以，项目之间的间隔比项目与边框的间隔大一倍。
3. `align-items`：确定项目在纵轴上如何对齐。
   - flex-start：纵轴的起始点对齐。
   - flex-end：纵轴的结束点对齐。
   - center：纵轴的中点对齐。
   - stretch：默认值。如果没有设置高度。弹性元素被在侧轴方向被拉伸到与容器相同的高度或宽度。
4. `flex-wrap`：指定子元素在一行排列不下的时候，该如何表现。
   - nowrap：不换行，被挤到一行。
   - wrap：被打断到多行中。
5. `align-content`：确定纵轴的轴线如何对齐。只有在多行的情况下才有效。
   - flex-start：纵轴的起始点对齐。
   - flex-end：纵轴的结束点对齐。
   - center：纵轴的中点对齐。
   - stretch：默认值。在没有给元素设置高度的时候（假如纵轴使用的是竖向的），弹性元素被在侧周方向被拉伸到与容器相同的高度。

项目中具体代码：

```scss
.course-list{
  margin-top: 20px;
  display: flex;
  flex-direction: row;  \\ 横向布局
  flex-wrap: wrap;  \\ 被打断到多行中
  justify-content: space-between;  \\ 两端对齐，项目之间的间隔相等
```

#### Django 前端模板的继承

设置好模板文件

在其他 HTML 文件中，通过 `{% extends '模板文件路径' %}` 来继承模板

修改的部分，在 `{% block xxx %} 修改的内容 {% endblock %}` 进行编辑

部分可引用的，可通过 `{% include xxx %}` 进行继承

#### SweatAlert 插件

SweetAlert2是一款功能强大的纯`JavaScript`模态消息对话框插件。SweetAlert2用于替代浏览器默认的弹出对话框，它提供各种参数和方法，支持嵌入图片，背景，HTML标签等，并提供5种内置的情景类，功能非常强大。

SweetAlert2是SweetAlert-js的升级版本，它解决了SweetAlert-js中不能嵌入HTML标签的问题，并对弹出对话框进行了优化，同时提供对各种表单元素的支持，还增加了5种情景模式的模态对话框。

使用方法参考：<https://blog.csdn.net/qq_37214567/article/details/88062772>

#### 富文本编辑器 UEditor

官方链接：<http://ueditor.baidu.com/website/>

使用步骤：

1. 做好前后端文件配置后

2. 配置 主文件下的 `urls.py` 和 `settings.py` 文件

   ```python
   # 富文本编辑器配置
   UEDITOR_UPLOAD_TO_SERVER = True
   UEDITOR_UPLOAD_PATH = MEDIA_ROOT
   UEDITOR_CONFIG_PATH = os.path.join(BASE_DIR, "front", "dist", "ueditor", "config.json")
   ```

## 后端开发

#### Django配置工作

1. 配置数据库：使用 `MySQL` 数据库，可视化工具 Navicat；

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',  # 选择数据库类型
           'NAME': "xfz2",  # 数据库名称
           "HOST": "127.0.0.1",  # IP地址
           "PORT": "3306",  # 端口号
           "USER": "root",  # 数据库用户
           "PASSWORD": "123qwe"  # 数据库密码
       }
   }
   ```

2. 配置模板文件的路径

   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [os.path.join(BASE_DIR, 'front', "templates")]  # 修改模板文件路径
           ,
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   ```

3. 配置静态文件的路径

   ```python
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, "front", "dist")
   ]
   ```

4. 配置时区

   ```python
   TIME_ZONE = 'Asia/Shanghai'
   
   USE_I18N = True
   
   USE_L10N = True
   
   USE_TZ = True
   ```

5. 配置模板的 `static` 标签：可以直接在 HTML 文件中使用静态文件路径，不需要每次都写 `{% load static %}`

   示例：`<link rel="stylesheet" href="{% static 'css/news/index.min.css' %}">`

   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [os.path.join(BASE_DIR, 'front', "templates")]
           ,
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
               "builtins": [
                   "django.templatetags.static",  # 配置 static 标签
               ]
           },
       },
   ]
   ```

6. **创建 Django 应用**：`python manage.py startapp news`

7. 配置应用

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'apps.news',
   ]
   ```

视图函数示例：

```python
def index(request):
    return render(request, "news/index.html")
```

主 `urls.py`

```python
from django.conf.urls import url, include

urlpatterns = [
    url("", include("apps.news.urls")),
]
```

应用程序中的 `urls.py`

```python
from django.conf.urls import url
from . import views

app_name = "news"

urlpatterns = [
    url("", views.index, name="index"),
]
```

#### 后台管理系统开发

使用 adminlte 进行开发：

- 官网：<https://adminlte.io/>
- GitHub： <https://github.com/ColorlibHQ/AdminLTE>

登陆页面样式：<https://adminlte.io/themes/AdminLTE/pages/examples/login.html>

#### 用户系统开发

重新定制 Django 内置的 User 系统（继承自 AbstractBaseUser），并且前后台使用同一个 User系统。

##### `xfzauth/models.py`

- 使用 ShortUUIDField 作为用户主键：不使用自增长 id 主键，容易造成安全隐患，或者泄露公司机密

  - 需要安装对应的包：`pip install django-shortuuidfield`

- 建立 User 模型

  ```python
  class User(AbstractBaseUser, PermissionsMixin):
      """用户模型"""
      uid = ShortUUIDField(primary_key=True)
      telephone = models.CharField(max_length=11, unique=True)
      email = models.EmailField()
      username = models.CharField(max_length=100)
      is_active = models.BooleanField(default=True)
      is_staff = models.BooleanField(default=False)
      date_join = models.DateTimeField(auto_now_add=True)
      
      USERNAME_FIELD = "telephone"  # 默认使用username
      REQUIRED_FIELDS = ["username"]  # 指定创建超级用户时需要填写 username 字段
      objects = UserManager()  # 将重写的 UserManager() 添加到 objects 中
  
      def get_full_name(self):
          return self.username
  
      def get_short_name(self):
          return self.username
  ```

  ```python
  class UserManager(BaseUserManager):
      """重写 UserManager """
      def _create_user(self, telephone, username, password, **kwargs):
          """创建用户"""
          if not telephone:
              raise ValueError("请输入手机号码！")
          if not username:
              raise ValueError("请输入用户名！")
          if not password:
              raise ValueError("请输入密码！")
  
          user = self.model(telephone=telephone, username=username, **kwargs)
          user.set_password(password)
          user.save()
          return user
  
      def create_user(self, telephone, username, password, **kwargs):
          kwargs["is_superuser"] = False
          kwargs["is_staff"] = True
          return self._create_user(telephone, username, password, **kwargs)
  
      def create_superuser(self, telephone, username, password, **kwargs):
          kwargs["is_superuser"] = True
          kwargs["is_staff"] = True
          return self._create_user(telephone, username, password, **kwargs)
  ```

- 配置 `settings.py` 

  ```python
  # 配置用户模型
  AUTH_USER_MODEL = "xfzauth.User"
  ```

##### `xfzauth/forms.py`

表单验证

```python
from django import forms


class LoginForm(forms.Form):
    """登陆表单"""
    telephone = forms.CharField(max_length=11)
    password = forms.CharField(max_length=20, min_length=6)
    remember = forms.IntegerField(required=False)
```



##### `xfzauth/views.py`

```python
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.http import require_POST

from utils import restful
from .forms import LoginForm


@require_POST
def login_view(request):
    """登陆视图"""
    form = LoginForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get("telephone")
        password = form.cleaned_data.get("password")
        remember = form.cleaned_data.get("remember")
        user = authenticate(request, username=telephone, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                return restful.ok()
            else:
                return restful.un_auth(message="您的账号已被冻结~")
        else:
            return restful.params_error(message="手机号码或者密码错误~")
    else:
        errors = form.get_errors()
        return restful.params_error(message=errors)
```

**在模板中判断是否有用户登录**

```html
{% if user.is_authenticated %}
    <a href="#" class="authenticated-box">{{ user.username }}</a>
{% else %}
    <a href="#" class="signin-btn">登陆</a> /
<a href="#" class="signup-btn">注册</a>
{% endif %}
```

##### 图形验证码的生成

主要使用 PIL 模块

通过生成画布，生成验证码文字，绘制干扰线，干扰点等形成验证码图片。

具体使用可参考连接：<https://www.cnblogs.com/6324TV/p/8811249.html>

**视图函数代码**

```python
def img_captcha(request):
    """图形验证码"""
    text, image = Captcha.gene_code()
    # 通过BytesIO()， 存储图片的流数据
    out = BytesIO()
    # 调用image的save()，将 image 对象保存到 BytesIO 中
    image.save(out, "png")
    # 将 文本指针 移动到最开始的位置
    out.seek(0)
    response = HttpResponse(content_type="image/png")
    response.write(out.read())
    response["Content-length"] = out.tell()

    return response
```

##### 短信验证码

选择阿里通信来作为短信服务平台。通过这个平台，中小企业及开发者可以在最短的时间内实现短信验证码发送、短信服务提醒、语音验证码、语音服务通知、IVR及呼叫中心、码号、后向流量、隐私保护相关的能力，实现互联网电信化。

**官方文档：**https://help.aliyun.com/document_detail/59210.html

**主要步骤：**

1. 获取 AccessKey 和 ACCESS_KEY_SECRRET
2. 创建应用
3. 创建验证码
   1. 创建签名
   2. 添加短信模板
4. Python 发送短信验证码：详见安装指导文档：<https://help.aliyun.com/document_detail/112147.html?spm=a2c4g.11186623.6.653.6b882e79gqjmkm#section-o1m-f3b-fhb>

##### 验证码缓存：`memcached`

``Memcached`是一个高性能的**分布式**的**内存对象缓存**系统，全世界有不少公司采用这个缓存项目来构建大负载的网站，来分担数据库的压力。`Memcached`是通过在内存里维护一个统一的巨大的 hash 表，`memcached`能存储各种各样的数据，包括图像、视频、文件、以及数据库检索的结果等。将数据调用到内存中，然后从内存中读取，从而大大提高读取速度。

`Memcached`应用场景：存储验证码（图形验证码、短信验证码）、登录session等所有不是至关重要的数据。

安装与启动 `Memcached`

1. windows：

   - 安装：`memcached.exe -d install`。
   - 启动：`memcached.exe -d start`。

2. `settings.py` 配置

   ```Python
   # 缓存配置
   CACHES = {
       "default": {
           "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
           "LOCATION": "127.0.0.1:11211"
       }
   }
   ```

##### Django 高级功能

判断用户是否为内部员工：

```python
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required(login_url="index")  # 如果不是内部员工，跳转到网站首页
def cms_index(request):
    return render(request, "cms/cms_index.html")
```

##### 配置文件上传路径

**settings.py**

```python
# 配置图片上传路径
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```

**配置主文件下的 urls.py**

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("news/", include("apps.news.urls")),
    path("cms/", include("apps.cms.urls")),
    path("account/", include("apps.xfzauth.urls")),
    path("course/", include("apps.course.urls")),
    path("payinfo/", include("apps.payinfo.urls")),
    path("search/", views.search, name="search"),
    path("", views.index, name="index"),
]

urlpatterns += static(settings.MEDIA_URL, 
                      document_root=settings.MEDIA_ROOT)  #文件路径
```

##### 将图片上传到七牛云

**操作步骤**

1. 准备工作：到七牛官网：`https://www.qiniu.com/`。创建账号。然后到个人面板->秘钥管理处获取`access_key`和`secret_key`
2. 后端配置：
   1. 下载 Python SDK ：通过命令`pip install qiniu`即可下载七牛的`SDK`
   2. 创建一个获取 `token` 的 `url`
3. 前端配置
   1. 在模板中引入最新版的`JavaScript SDK`
   2. 监听一个`type=file`类型的按钮的`change`事件，一旦选择了文件，那么就会执行`change`事件，在`change`事件的处理函数中，我们就可以获取到当前选中的文件。通过七牛的`SDK`发送给服务器

##### Django REST framework

官网链接：<https://www.django-rest-framework.org/>

实现数据的序列化

安装：

- `pip install djangorestframework`

- 将 `'rest_framework'`  添加到  `INSTALLED_APPS` 中

  ```python
  INSTALLED_APPS = [
      ...
      'rest_framework',
  ]
  ```

##### django-debug-toolbar

`django-debug-toolbar` 是一组可配置的面板，可显示有关当前请求/响应的各种调试信息，并在单击时显示有关面板内容的更多详细信息。

Git 地址：<https://github.com/jazzband/django-debug-toolbar>

文档：<>

安装及相关配置：

安装：`pip install django-debug-toolbar`

`settings.py` 文件配置：

```python
INSTALLED_APPS = [
    # ...
    'django.contrib.staticfiles',
    # ...
    'debug_toolbar',
]
```

```python
MIDDLEWARE = [
    # ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # 中间件配置，尽量放第一位
    # ...
]
```

```python
INTERNAL_IPS = [
    # ...
    '127.0.0.1',  # 配置ip地址
    # ...
]
```

主 `urls.py` 文件中配置：

```python
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
```



##### 视频云存储：百度云点播VOD服务（未实现）

百度云：`https://cloud.baidu.com`



##### 订单支付功能：paysapi（未实现）

官方网站：https://www.paysapi.com/

相关文档：https://www.paysapi.com/docindex



##### 权限管理

`Django` 可以通过自定义命令来实现权限管理

在创建数据库表时，`Django` 已经创建好了用户的权限分配表，保存在 `auth_permission` 表中

在 `django_content_type` 表中，记录了创建的`app`下的`models`表进行`app_label-models`一一映射

```python
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission, ContentType

from apps.news.models import NewsCategory, News, Banner, Comment
from apps.course.models import Course, CourseCategory, CourseOrder, Teacher
from apps.payinfo.models import Payinfo, PayinfoOrder


class Command(BaseCommand):
    def handle(self, *args, **options):
        # 编辑组：管理新闻、课程、评论、轮播图等
        edit_content_types = [
            ContentType.objects.get_for_model(News),
            ContentType.objects.get_for_model(NewsCategory),
            ContentType.objects.get_for_model(NewsCategory),
            ContentType.objects.get_for_model(Banner),
            ContentType.objects.get_for_model(Comment),
            ContentType.objects.get_for_model(Course),
            ContentType.objects.get_for_model(CourseCategory),
            ContentType.objects.get_for_model(Teacher),
            ContentType.objects.get_for_model(Payinfo),
        ]
        edit_permissions = Permission.objects.filter(content_type__in=edit_content_types)
        edit_group = Group.objects.create(name="编辑")
        edit_group.permissions.set(edit_permissions)
        edit_group.save()
        self.stdout.write(self.style.SUCCESS("编辑分组创建完成~"))

        # 财务组：课程订单、付费咨询订单
        finance_content_types = [
            ContentType.objects.get_for_model(CourseOrder),
            ContentType.objects.get_for_model(PayinfoOrder),
        ]
        finance_permissions = Permission.objects.filter(
            content_type__in=finance_content_types
        )
        finance_group = Group.objects.create(name="财务")
        finance_group.permissions.set(finance_permissions)
        finance_group.save()
        self.stdout.write(self.style.SUCCESS("财务分组创建完成~"))

        # 管理员：编辑组 + 财务组
        admin_permissions = edit_permissions.union(finance_permissions)
        admin_group = Group.objects.create(name="管理员")
        admin_group.permissions.set(admin_permissions)
        admin_group.save()
        self.stdout.write(self.style.SUCCESS("管理员分组创建完成~"))
```

使用 `python manage.py initgroup` 完成分组创建

前后端均需要进行用户权限判断

- 前端判断方式

  ```html
  {% if perms.course.change_course %}
      <li class="header">课程管理</li>
      <li>
          <a href="{% url 'cms:pub_course' %}">
              <i class="fa fa-tv"></i>
              <span>发布课程</span>
          </a>
      </li>
  {% endif %}
  ```

- 后端使用装饰器进行判断

  ```python
  # 对于类视图
  @method_decorator(permission_required(perm="news.add_news", login_url="/"), name="dispatch")
  class EditNewsView(View):
      
  # 对于视图函数
  @require_POST
  @permission_required(perm="news.add_news", login_url="/")
  def delete_news(request):
  ```



## 项目部署（使用虚拟机）

### 在开发机上的准备工作：
1. 确认项目没有bug。
2. 用`pip freeze > requirements.txt`将当前环境的包导出到`requirements.txt`文件中，方便在部署的时候安装。
3. 使用 `Git` 进行项目版本管理
    * `git init`：将目录初始化，成为一个 `git` 仓库
    * `git remote add origin 远程仓库地址`：将项目连接到远程仓库
    * `git add .`：将目录下的文件添加到暂存区
    * `git commit -m 'first commit'`：提交到本地库
    * `git push -u origin master`：把项目文件推送到远程仓库，`-u` 表示远程仓库是空的
    
    [git操作详细说明](https://blog.csdn.net/Lucky_LXG/article/details/77849212?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)


### 在服务器上的准备工作：
1. 安装好项目用到的`Python`。
    * sudo apt install python
    * sudo apt install python-pip
    * pip install --upgrade pip
2. 安装`virtualenv`以及`virutalenvwrapper`。并创建虚拟环境。
    * pip install virtualenv
    * pip install virtualenvwrapper
    * sudo apt install vim
    * vim ~/.bashrc 进入文件中，填入以下两行代码：
        ```python
        export WORKON_HOME=$HOME/.virtualenvs
        source /usr/local/bin/virtualenvwrapper.sh
        ```
    * source ~/.bashrc
3. 安装`git`：
    ```shell
    sudo apt install git
    ```
4. 为了方便XShell或者CRT连接服务器，建议安装`OpenSSH`：
    ```shell
    sudo apt install openssh-server openssh-client
    service ssh restart
    ```
5. 安装`MySQL`服务器和客户端：
    ```shell
    sudo apt install mysql-server mysql-client
    sudo apt-get install libmysqld-dev
    ```
6. 进入虚拟环境中，然后进入到项目所在目录，执行命令：`pip install -r requirements.txt`，安装好相应的包。
7. 在`mysql`数据库中，创建相应的数据库。
8. 执行`python manage.py migrate`命令，将迁移文件，映射到数据库中，创建相应的表。
9. 执行`python manage.py runserver 0.0.0.0:8000`，然后在你自己电脑上，在浏览器中输入`http://你的服务器的ip地址:8000/`，访问下网站所有页 面，确保所有页面都没有错误。
10. 设置`ALLOW_HOST`为你的域名，以及ip地址。
11. 设置`DEBUG=False`，避免如果你的网站产生错误，而将错误信息暴漏给用户。
12. 收集静态文件：`python manage.py collectstatic`。


### 安装uwsgi
1. uwsgi是一个应用服务器，非静态文件的网络请求就必须通过他完成，他也可以充当静态文件服务器，但不是他的强项。uwsgi是使用python编写的，因此通过`pip install uwsgi`就可以了。**(`uwsgi` 必须安装在系统级别的Python环境中，不要安装到虚拟环境中**)。
2. 使用命令`uwsgi --http :8000 --module zhiliaoketang.wsgi --vritualenv=/root/.virtualenvs/django-env-py2`。用`uwsgi`启动项目，如果能够在浏览器中访问到这个页面，说明`uwsgi`可以加载项目了。

### 编写uwsgi配置文件：
在项目的路径下面，创建一个文件叫做`zhiliaoketang_uwsgi.ini`的文件，然后填写以下代码：
```shell
[uwsgi]

# Django相关的配置
# 必须全部为绝对路径
# 项目的路径
chdir           = /srv/zhiliaoketang
# Django的wsgi文件
module          = zhiliaoketang.wsgi
# Python虚拟环境的路径
home            = /root/.virtualenvs/django-env-py2

# 进程相关的设置
# 主进程
master          = true
# 最大数量的工作进程
processes       = 10
# socket文件路径，绝对路径
socket          = /srv/zhiliaoketang/zhiliaoketang.sock
# 设置socket的权限
chmod-socket    = 666
# 退出的时候是否清理环境
vacuum          = true
```
然后使用命令`uwsgi --ini zhiliaoketang.ini`，看下是否还能启动这个项目。


### 安装nginx：
1. nginx是一个web服务器。用来加载静态文件和接收http请求的。通过命令`sudo apt install nginx`即可安装。
2. `nginx`常用命令：
    * 启动nginx：service nginx start
    * 关闭nginx：service nginx stop
    * 重启nginx：service nginx restart

### 收集静态文件：
静态文件应该让nginx来服务，而不是让django来做。首先确保你的`settings.py`文件中有一个`STATIC_ROOT`配置，这个配置应该指定你的静态文件要放在哪个目录下。那么我们可以执行以下命令：`python manage.py collectstatic`来收集所有静态文件，将这些静态文件放在指定的目录下。

### 编写nginx配置文件：
在`/etc/nginx/conf.d`目录下，新建一个文件，叫做`zhiliaoketang.conf`，然后将以下代码粘贴进去：
```python
upstream zhiliaoketang {
    server unix:///srv/zhiliaoketang/zhiliaoketang.sock; 
}

# 配置服务器
server {
    # 监听的端口号
    listen      80;
    # 域名
    server_name 192.168.0.101; 
    charset     utf-8;

    # 最大的文件上传尺寸
    client_max_body_size 75M;  

    # 静态文件访问的url
    location /static {
        # 静态文件地址
        alias /srv/zhiliaoketang/static_dist; 
    }

    # 最后，发送所有非静态文件请求到django服务器
    location / {
        uwsgi_pass  zhiliaoketang;
        # uwsgi_params文件地址
        include     /etc/nginx/uwsgi_params; 
    }
}
```
写完配置文件后，为了测试配置文件是否设置成功，运行命令：`service nginx configtest`，如果不报错，说明成功。
每次修改完了配置文件，都要记得运行`service nginx restart`。

### 使用supervisor配置：
让supervisor管理uwsgi，可以在uwsgi发生意外的情况下，会自动的重启。
1. `supervisor`的安装：在系统级别的python环境下`pip install supervisor`。
2. 在项目的根目录下创建一个文件叫做`zlkt_supervisor.conf`。内容如下：
    ```python
    # supervisor的程序名字
    [program:mysite]
    # supervisor执行的命令
    command=uwsgi --ini zlkt_uwsgi.ini
    # 项目的目录
    directory = /srv/zhiliaoketang 
    # 开始的时候等待多少秒
    startsecs=0
    # 停止的时候等待多少秒
    stopwaitsecs=0  
    # 自动开始
    autostart=true
    # 程序挂了后自动重启
    autorestart=true
    # 输出的log文件
    stdout_logfile=/srv/zhiliaoketang/log/supervisord.log
    # 输出的错误文件
    stderr_logfile=/srv/zhiliaoketang/log/supervisord.err

    [supervisord]
    # log的级别
    loglevel=info

    # 使用supervisorctl的配置
    [supervisorctl]
    # 使用supervisorctl登录的地址和端口号
    serverurl = http://127.0.0.1:9001

    # 登录supervisorctl的用户名和密码
    username = admin
    password = 123

    [inet_http_server]
    # supervisor的服务器
    port = :9001
    # 用户名和密码
    username = admin
    password = 123

    [rpcinterface:supervisor]
    supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
    ```
然后使用命令`supervisord -c zlkt_supervisor.conf`运行就可以了。
以后如果想要启动`uwsgi`，就可以通过命令`supervisorctl -c supervisor.conf`进入到管理控制台，然后可以执行相关的命令进行管理：
    * status                # 查看状态
    * start program_name    #启动程序
    * restart program_name  #重新启动程序
    * stop program_name     # 关闭程序
    * reload                # 重新加载配置文件
    * quit                  # 退出控制台