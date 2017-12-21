敏捷软件开发的核心是敏捷思想:  
__以人为本，专注交付对客户有价值的软件。在高度协作的环境中，使用迭代式的方式进行增量开发，经常根据反馈进行思考、反省和总结，不停地自我调整和完善，让软件开发与交付轻量而敏捷。__

## 传统的团队协作/软件开发方式--瀑布模型
![瀑布模型]()

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
### 规则
- 计划
  用户故事：
- 管理
- 设计
- 代码
- 测试
### 价值
- 简单：只做必须做的、最小设计、持续重构
- 沟通：及时有效
- 反馈：严重承诺，尽快交付
- 尊重：互相尊重，通过努力工作获得认同
- 勇气：
### 过程
![XP的过程]()

Architectural Spike:架构刺探，根据需求要完成什么样的软件，采用什么业务架构、技术架构等  
User Stories:客户的需求，使用场景  
Release Planning:版本计划，根据用户故事、功能技术预估来作计划  
Iteration:有了版本计划后，开始迭代开发，产生一个最新版本  
Acceptance Tests:验收测试，发现Bug后，返回当前的迭代周期修改；客户有新的使用场景，添加到版本计划中  
Small Releases:验收测试通过后，客户认同，正式发布小版本
### XP的核心实践(Core Practices)
#### Whole Team
客户和开发人员形成一个完整的团队，随时面对面交流
#### Planning Game

#### Small Releases
频繁的、小量的发布，随时提供可运行的版本给用户，及时解决问题
#### Customer Tests
每次发版前，由用户进行验收测试
#### Code Standards
共同遵守统一的编码规范，全项目风格统一，提高可读性便于理解，方便工作
#### Collective Code Ownership
- 鼓励每个人贡献代码并对整体质量负责
- 任何人都能随时添加功能、修改问题、重构
- 增强了整体设计的结果来自合理可靠的技术决策的机会，而非来自社会结构
- 有利于技术知识扩散
- 减少进度缓慢的风险，不因某个开发者不到场而阻塞进度
#### Continuous Integration

#### Metaphor
#### Sustainable Pace
- 软件开发是一个可持续的活动
- 稳定合理的节奏，小步快跑
- 不提倡短期加班冲刺，特殊情况例外，这对生产不利
- 加班往往掩盖计划、管理或质量的缺陷
#### Test-Driven Development
#### Pair Programming
- 提倡经常轮换角色
- 有利于团队知识扩散与技能转移
