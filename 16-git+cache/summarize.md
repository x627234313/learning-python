#
## Docker Registry
Registry是一个存储和内容交付系统，存储并允许你分发Docker images，可以使用不同的标记版本。

用户使用docker pull/push和Registry进行交互。

## GitFlow
![](http://i65.tinypic.com/3149wdv.jpg)
![](http://i65.tinypic.com/wtw0sk.jpg)

- `develop branch`：用于整合各个功能分支，也是开发过程中代码主要提交分支之一。
- `feature branch`：有新功能需求时，从`develop`上分出，开发完成后再合并到`develop`上，而且只能合并到`develop`上。
- `release branch`：发版日期临近或`develop`上有了足够的功能用于发布，就从`develop`上分出，为发布作准备。如果`release`测试发现bug，直接在`release`上修复，完全准备好后合并到`master`上，也要合并到`develop`上，
  - 命名规则：`release-*`  eg：`release-1.4.2`
  - 版本号命名规范：N[.N]+[{a|b|rc}N]  N为阿拉伯数字
  - 版本阶段
    - `Alpha`(内测版)
    - `Beta`（公测版）
    - `Release Candidate`（候选版）
    - `Final`（正式版）
    - 主版本号.子版本号.修正版本号  eg: 1.2a1、2.3.2b4
- `hotfix`：用于快速修复生产环境中的发行版代码，它是唯一从`master`上分出来的分支，主要是因为：
  1. 生产环境和测试环境不同，比如数据量相差较大，导致代码出现bug
  2. 确定出现bug的最原始的代码是`master`上

  修复完成后合并到`master`上，也要合并到`develop`上。
  
- `master`：记录正式发版历史，要保证这上面的代码是干净的。

## Cache
