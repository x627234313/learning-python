敏捷软件开发的核心是敏捷思想:  
__以人为本，专注交付对客户有价值的软件。在高度协作的环境中，使用迭代式的方式进行增量开发，经常根据反馈进行思考、反省和总结，不停地自我调整和完善，让软件开发与交付轻量而敏捷。__

## 传统的团队协作/软件开发方式--瀑布模型
![](http://i68.tinypic.com/1zdvebm.png)

SOW：statement of work/工作任务说明书 AR：acceptance requirement/验收要求 UI：user interface

PHB：process handbook/过程手册 PPL：project plan/制订项目计划 WBS：work breakdown structure/工作分解结构 RTM：requirements traceability matrix/需求追踪矩阵 RiskM：风险矩阵 TP：task plan/任务计划

SRS：software requirements specification/软件需求说明书 STC：system test cases/系统测试用例 STR：system testing report/系统测试报告  
HLD：high level design/概要设计 ITC：integration test cases/集成测试用例  
LLD：low level design/详细设计 UTC：unit test cases/单元测试用例  
SRC：source code/源代码

### 瀑布模型的问题
1. 流程冗长，需求变化响应慢，开发周期长，不适应现在互联网的快节奏
2. 文档繁多，几乎每一步流程中都会产生很多的文档。
3. 客户没有参与到开发过程中，开发团队对需求有理解不到位的地方，不能很快的发现，可能导致开发完成后与客户期望的相差很大。

## 敏捷开发实践--极限编程(extreme programming)
### 过程
![XP的过程](http://i64.tinypic.com/6szx93.png)

Architectural Spike:架构刺探，根据需求要完成什么样的软件，采用什么业务架构、技术架构等  
User Stories:客户的需求，使用场景  
Release Planning:版本计划，根据用户故事、功能技术预估来作计划  
Iteration:有了版本计划后，开始迭代开发，产生一个最新版本  
Acceptance Tests:验收测试，发现Bug后，返回当前的迭代周期修改；客户有新的使用场景，添加到版本计划中  
Small Releases:验收测试通过后，客户认同，正式发布小版本

### XP的核心实践(Core Practices)
#### Whole Team
客户和开发人员形成一个完整的团队，随时面对面交流，及时、有效
#### Planning Game
计划阶段，包括发版计划、迭代计划、验收测试、每日立会、单元测试等，所需的时间周期越来越短
#### Small Releases
频繁的、小量的发布，每完成一个功能发布一次，让用户可以马上使用
#### Customer Tests
每次发版前，由用户进行验收测试
#### Code Standards
共同遵守的编码规范，全项目风格统一，包括编码风格、命名风格、技术实现等各种风格的统一，提高可读性便于理解，方便工作
#### Collective Code Ownership
代码集体所有权，团队中的每个人都可以对整体代码添加功能，修改、重构，发表不同的意见，更可以促进个人成长
#### Continuous Integration
持续集成，保证代码是“最新”的、可用的；每次提交少量的内容，可以更容易发现错误、定位错误；频繁提交可以从时间等客观条件上促使开发者创建模块化的代码，降低复杂性
#### Metaphor
**隐喻**，类比常见的生活常识，更容易理解计算机相关的术语
#### Sustainable Pace
可持续的步伐，软件开发是一个可持续的活动，稳定节奏，不提倡加班，尽早揭露团队中的技术、管理、计划方面的问题
#### Test-Driven Development
测试驱动开发，先做出正确的，再实现高质量的，即只写“刚好够用”的代码先过测试，再通过重构提高代码质量
#### Pair Programming
结对编程，有“司机”“导航员”两种角色，提倡轮换角色，可以更容易发现个人编程的隐患，提高代码质量，也有利于团队知识扩散

## 敏捷开发实践--Scrum
### Scrum框架
![Scrum框架](http://i67.tinypic.com/jgnv45.png)

Product Owner：汇总各方面的需求，整理出一份Product Backlog/待开发列表，标明任务优先级  
Team：选择一个Sprint，进行冲刺计划会议，讨论这次Sprint期间需要完成的工作，产出Sprint Backlog。实施，每次Sprint周期一般为2~4周  
ScrumMaster：负责团队运转  
Daily Scrum Meeting and Artifacts Update：每日晨会，每人讲叙昨天做过的、今天要做的事情，遇到的困难，更新工件  
Review：评审会议，检查这次Sprint过程中，事情完成情况，探讨下一步工作计划  
Retrospective：回顾会议，审视团队中每个人的技术、沟通、合作能力

### Scrum自组织团队
由管理层确定团队组成和团队目标，之后在开发过程中，团队决定任务的分配，团队做技术决策，团队管理和监督开发过程和进度，在承诺的时间内交付正确的、可工作的软件

### Scrum vs XP
- 迭代周期：2\~4周 vs 1\~2周
- 需求变更：一个Sprint周期中不接受变更 vs 有条件接受
- 优先级定义权：自组织团队决定 vs 客户/产品主管决定
- 工程实践：无规定 vs 有一定要求(核心区别)

Scrum着重计划（分解任务、排优先级、迭代计划），没有规定工程实践的部分，虽然降低了要求应用更广泛，但是也会产生一些问题。  
团队选择一个Sprint开始开发，最终交付的商业价值不好预估；没有统一的编码规范，没有测试驱动开发，可能导致代码质量不高，容易出现问题，对于问题追踪不及时浪费时间、成本；一个Sprint过程中不接受需求变更，无法响应突发事件等

## 精益
起源于丰田TPS，当时丰田进入汽车产业，为了与传统以大规模生产的企业竞争，提出精益思想：以市场需求为目标，动态调整产量，保持市场平衡，只在有需求时生产并且持续改进。

软件开发中提倡：
- 每个人都要参与到整个项目周期
- 减少浪费，减少延误，仅选取最重要的项目
- 最终工作的是人，但引入管理方法（比如Scrum中，选取Sprint时，通过使用某种方法，选取商业价值最高的）
- 质量内建（在设计、开发、测试过程中，每一步都尽力高质量的完成）
- 限制同时进行的任务数，清晰地管理工作流（假如限制每个Sprint不能超过10个Task，迫使团队完成最核心的功能。通过最小的输入，产出最大的价值）

敏捷方法的具体实践还有`Feature Driven Development`(特性驱动开发)、`Kanban`、`DSDM`等，然而现在的互联网公司使用的都不是单一的某种方法，而是以一种方法为主体，结合自身的实际，借鉴其他方法中的工程实践混合而成，最终符合敏捷思想（以人为本、高度协作、增量开发、交付有价值的软件、不断完善）
