#Online Bookshop

成员

- 71Y12111 姚逸云
- 71112202 沈多

##1 系统设计

###1.1 实验目的
能够使用已学到的数据库的知识开发一个完整的系统。能够从数据库系统的角度详细分析并讨论系统的设计。通过该实验学会从数据库设计、查询性能、系统维护、备份方案设计等各 方面对整个系统进行分析和考虑。

###1.2 平台

- 项目框架：Django 1.7.1
- 数据库管理系统：Postgres
- 部署：Heroku
- 使用了：
 - OSX
 - git, pip, bower, virtualenv, tastypie

###1.3 任务分工

过程 | 时间 | 目标 | 任务分配
---|---|---|---
需求阶段 | 2014/12/20 | 分析用户需求、完成需求分析文档 | 所有组员一同完成
设计阶段 | 2014/12/21~25 | 进行系统架构分析、界面设计、数据库设计、完成详细设计文档 | 数据库一同设计，沈多：界面设计，姚逸云：文档整合
编码阶段 | 2014/12/26~30 | 实现功能 | 姚逸云：用户系统、购物系统、商品系统；沈多：帮助系统、搜索系统、管理系统
测试阶段 | 2014/1/1~6 | 功能性测试 | 所有组员一同完成
部署阶段 | 2014/1/7~9 | 发布系统到heroku平台 | 姚逸云

##2 功能说明
网上书店主要分为6个部分：用户系统，商品系统，帮助系统，购物系统，搜索系统和管理系统.

###2.1 用户系统
创建用户账号并保存用户信息，包括基本信息、订单信息，为用户做更好的书籍推荐。

- 用户登录- 用户注册- 用户历史购物记录
- 推荐书籍

###2.2 商品系统
显示书籍信息，帮助用户筛选更合适的书籍。

- 网站导航
- 首页
- 书籍详细页面
- 相关书籍

###2.3 购物系统
帮助用户方便地购买书籍，并且保证支付的安全。

- 加入购物车
- 生成订单
- 支付
- 评价书籍

###2.4 搜索系统
为用户提供更快捷的途径定位书籍，找到真正想要的书籍。

- 搜索
- 搜索结果展示

###2.5 帮助系统
帮助用户更好，更快捷地使用网站所提供的服务。

- 查看帮助- FAQ- 联系我们


###2.6 管理系统
为网站的维护人员提供友好的用户接口，可以更快捷方便地维护书籍。

- 书籍管理
- 订单管理

##3 使用说明

网站已经发布到了Heroku平台上([http://online-bookshop.herokuapp.com](http://online-bookshop.herokuapp.com))，用户可以注册体验。
###匿名用户使用说明

- 浏览最新上架的图书和热销书籍：进入[网站首页](http://online-bookshop.herokuapp.com/)，或者点击网站图标“Bookshop”，可以浏览新书上架和热销书籍。横幅为数据库内的新入书籍。用户可以更具自己的喜好选择相关的书籍进行浏览。

![index](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/index.png)

- 使用网站导航栏：在用户的每个页面左部都设置了一个导航栏方便用户的使用，用户可以更具自己的需求请求响应的页面,如下图:

![navbar](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/navbar2.png)

- 登录：已经拥有该网站的会员资格的匿名用户可以点击页面右上方的“Account”进入登录页面，输入自己的用户名和密码，登录到该系统，任何会员需要的功能都会直接跳到登陆页面，登陆成功后返回原先页面。登录页面如下：

![login](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/login.png)

- 注册会员：没有该网站会员权限的用户可以点击登陆页面中的“Register”按钮进入用户注册页面，如下图：

![register](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/register.png)

在该页面填写相关的信息后即可注册为本网站的会员。（用户名必须是没有注册过的用户名，若你填写的用户名已注册过则会提示你输入另一个用户名）

- 搜索书籍：用户可点击导航栏中的“Books”进入搜索书籍页面，如下图：

![search](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/search.png)

用户可以同过搜索书名进行搜索

![search1](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/search1.png)

- 浏览书籍：用户可点击任意页面中存在的书籍图片查看该书籍（书名的链接或图片的链接），如下图：

![book](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/book.png)

- 查看书籍详细信息：该页面中有书籍的详细信息，在下部的“Book Info”中，如下图：

![book_info](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/book_info.png)

- 查看与该书籍相关的书籍：在下部的“Related”中，如下图：

![related](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/related.png)

如果用户想要查看相关书籍的详细信息，也可以直接点击进入查看。

- 查看用户对书籍评论：在下部的“Comments”中，如下图：

![comments](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/comments.png)

评论由用户购买后评价生成，将在后面的购买系统中做详细介绍

- 查看网站帮助：点击导航栏中的“Help”，显示网站的使用说明，如下图：

![help](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/help.png)

###会员用户使用说明
会员用户除了拥有匿名用户的所有功能之外，还包括以下功能。

- 购买书籍：用户点击书籍详情页面的“Buy”或者点击导航栏中的“Checkout”，进入生成订单页面，如下图: 

![checkout](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/checkout.png)

该页面中，可以任意的增加或减少书本的数量，并且可以将书本从订单中删除。

- 加入购物车：用户点击书籍详情页面的“Add to Cart”将书籍加入购物车。购物车中商品的数量将在导航栏中的“Checkout”条目的右侧显示。如下图：

![cart](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/cart.png)

- 购买：用户点击订单页面的“Go to Pay”进行支付，网站将立刻确认订单，并且跳转到用户界面。如下图

![pay](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/pay.png)

- 确认收货并且评论：用户点击Uncomment orders中的“comment”，可以确认收货并且为书本添加评论。如下图：

![make_comment](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/make_comment.png)

用户可以输入评论，点击确定，该订单就会被确认，并且相应的评论就会添加到相应的书籍上。

![make_comment1](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/make_comment1.png)

![make_comment2](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/make_comment2.png)

- 查看推荐：我们会根据用户的订单，推测用户的看书喜好，给出相应的推荐，推荐的范围很广，每次会随机选出4本。推荐可以在多个地方看见，比如：Account，Index。如下图

![recommend1](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/recommend1.png)

![recommend2](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/recommend2.png)

- 登出：用户可以点击“Account”中的“logout”登出。

###管理员使用说明
管理员能够增加，删除，修改，查询网站内的所有实体对象。

![admin](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/admin.png)

这里以Book为例。

- 增加Book：点击Bookshop栏目下Book条目的“Add”按钮，填写相应信息。

![add](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/add.png)

- 查询或者修改Book：点击“Change”按钮，选择相应的Book，在详情页中修改内容。

![change](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/change.png)

- 删除Book：点击“Change”按钮，在复选框中选中相应Book，选择Action下拉框中的“Delete selected books”，点击“Go”，删除Book。

![delete](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/delete.png)

###API
网站提供了一套可供应用程序调用的web API

![api](https://raw.githubusercontent.com/yyypasserby/OnlineBookshop/master/INTRO_IMAGE/api.png)

## 实验体会
- 项目需求非常明确，而且也是比较普通的一个电商网站，所以前期设计上并未太多困难。为了在编码过程中不致于反复修改，所以在数据库设计时组内花了一些时间来讨论，并设计了较多的关系表以提高查询效率。
- 可能还不是很习惯以文档的为主来编码，所以其实此次系统设计的文档和编码过程仍旧比较分离。不过由于系统不是很复杂，所以思路逻辑比较清晰，不依赖于文档也不会遇到太多困难。
- 在姚逸云同学的推荐下，这次系统采用了Python写后台，数据库采用了Postgres，均是以前没有尝试过的，算是学习了一些新技术。
- 此次实验其实时间还是比较紧张的，在期末面对很多考试加上小组只有两名成员的情况下，有一些功能和效果还可以有待改善。
- 在实战过程中，体会到了数据库在一个OLTP系统中的重要性，熟练掌握数据库功能在未来的学习工作中是十分重要的。
- 在书籍数据的获取中，采用了爬虫技术，快速高效地获取了数据。

##5 改进方案
1. 购物车只为会员用户开放，匿名用户也应当可以使用。增加购物车支持，可以提升匿名用户的用户体验，让用户更有可能转化为会员用户。2. 搜索书籍中，方式比较单一，在没有搜到结果时没有提示或者推荐。可以根据搜索结果，给出更人性化的加护方式。3. 用户的推荐系统任然不够智能，并且性能较差。可以使用数据表将推荐暂时存在数据库中，不用每次请求时，都去计算。4. 用户的基本资料无法修改。可以添加修改的功能，让使用更加方便。