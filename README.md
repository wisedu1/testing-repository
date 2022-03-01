# TestingRepository

#### 介绍
这是一个关于计算机、测试开发相关的知识库，包含但不限于一个资深测试开发工程师应当掌握的全部内容

#### 测试理论

#### Linux

#### Git

github 更新后的 push 方法:

```shell
git push https://<GITHUB_ACCESS_TOKEN>@github.com/<GITHUB_USERNAME>/<REPOSITORY_NAME>.git
```

【解决pull push等慢或报错的问题】

```shell
git config http.sslVerify "false"
git config --global http.postBuffer 524288000
```

1.更新本地代码库

```shell
git pull
```

2.对需要删除的文件、文件夹进行如下操作

**删除文件:**

```shell
git rm <file>
```

**删除文件夹:**

```shell
git rm -r <directory>
```

3.提交修改

```shell
git commit -m <"Delete files">
```

4.将修改提交到远程仓库的xxx分支:

```shell
git push origin <branch>
```

#### 数据库

1. 查询每门课程成绩都大于80分的学生姓名

   ```sql
   select name from stu
   group by name
   having name not in (
   select name from stu
   where score <80)
   ```

   > where 在聚合前根据条件筛选记录，然后用 group by 分组，group by 后面的字段作为分组依据，having 只能用于 group by 后，对分组统计后的结果数据进行过滤。where 后不可用聚合函数，having 后可以用聚合函数

#### 编程语言

#### 算法


#### Web 自动化测试


#### 移动端自动化测试

#### 自动化测试框架

##### UI 自动化测试框架

##### 接口测试框架

#### 客户端测试平台

#### 客户端专项测试

#### 服务端接口测试

#### 服务端性能测试

#### 接口安全测试

#### docker

#### 接口测试框架开发

#### 持续集成

#### 持续交付

#### 测试平台开发
