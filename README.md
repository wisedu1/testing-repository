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

**github 访问慢的原因及解决方法：**

方法一：输入  `ipconfig/flushdns`  刷新 `DNS` 缓存即可

方法二：

 **1. 修改本地hosts文件**

```
windows系统的hosts文件的位置如下：C:\Windows\System32\drivers\etc\hosts
mac/linux系统的hosts文件的位置如下：/etc/hosts
```

**2. 增加 github.global.ssl.fastly.net 和[ github.com 的映射**

```sh
获取Github相关网站的ip
访问https://www.ipaddress.com，拉下来，找到页面中下方的“IP Address Tools – Quick Links”
分别输入github.global.ssl.fastly.net和github.com，查询ip地址
下面是我的配置
140.82.114.4	github.com
199.232.5.194	github.global.ssl.fastly.net
```

> 该方案参考链接：https://juejin.cn/post/6999271897057738789

#### 数据库

1. 查询每门课程成绩都大于80分的学生姓名

   ```sql
   SELECT name FROM stu
   GROUP BY name
   HAVING name NOT IN (
   SELECT name FROM stu
   WHERE score <80)
   ```

   > where 在聚合前根据条件筛选记录，然后用 group by 分组，group by 后面的字段作为分组依据，此时该字段不重复，having 只能用于 group by 后，对分组统计后的结果数据进行过滤。where 后不可用聚合函数，having 后可以用聚合函数
   >
   > 执行顺序：where -> group by -> having -> select

* join 用法：

  基于这些表之间的共同字段把来自两个或多个表的行结合起来

  * **inner join**（等价于 join）：左表行和右表行匹配，输出

    ```sql
    SELECT column_name(s)
    FROM table1
    INNER JOIN table2
    ON table1.column_name=table2.column_name;
    ```

  * **left join**：返回左表所有行，右表没有匹配则结果为 `NULL`

    ```sql
    SELECT column_name(s)
    FROM table1
    LEFT JOIN table2
    ON table1.column_name=table2.column_name;
    ```

  * **right join**：与 `left join`相反

    ```sql
    SELECT column_name(s)
    FROM table1
    RIGHT JOIN table2
    ON table1.column_name=table2.column_name;
    ```

  * **full outer join**: 结合 `left join`和`right join`的结果

    ```sql
    SELECT column_name(s)
    FROM table1
    FULL OUTER JOIN table2
    ON table1.column_name=table2.column_name;
    ```

* union 用法：

  合并两个或多个 `select` 语句的结果集，其中每个 `select`语句必须拥有相同数量的列，且列的数据类型和列的顺序相同

  **默认取不重复的值**

  ```sql
  SELECT column_name(s) FROM table1
  UNION
  SELECT column_name(s) FROM table2;
  ```

  允许重复用 `UNION ALL`

  ```sql
  SELECT column_name(s) FROM table1
  UNION ALL
  SELECT column_name(s) FROM table2;
  ```

  

#### 编程语言

#### 计算机网络

#### 操作系统

#### 数据结构和算法

1. 排序算法

   1. 堆排序 (平均时间复杂度 `O(nlogn)`，不稳定)

      堆（是一种特殊的完全二叉树），用数组表示，分为大顶堆和小顶堆，大顶堆是指每个节点的值都 ≥ 其子节点的值，在堆排序算法中用于升序排列，小顶堆相反

      **算法步骤**（以大顶堆为例）：

      1. 创建一个堆
      2. 将堆首（最大值）和堆尾互换
      3. 除堆尾剩下的 n - 1 个元素调整为新堆，重复步骤 2, 3，直到剩下 1 个元素

      首先要知道以下公式：

      给定某个结点的下标 `i`（从 0 开始），其父节点和左右孩子节点的下标分别为：

      * parent(i) = floor((i-1)/2)
      * left(i) = 2i + 1
      * right(i) = 2i +2

      然后关注两个重要问题：

      1. 如何将无序数组建立为堆？
      2. 将堆顶元素放在堆尾后，如何将除堆尾剩下的 n - 1 个元素调整为新堆？

      1. 筛选法：从第一个非叶子节点向上筛选，直到根元素筛选完毕（循环筛选 n / 2 个元素）
      2. 将新的根元素（标记为`f`）下沉，和它的子元素比较，如果`f`小于某个子元素，则互相交换位置，直到`f`大于其所有子元素

      ```java
      public class ArrayHeap {
          private int[] arr;
          public ArrayHeap(int[] arr) {
              this.arr = arr;
          }
          
          private void swap(int i, int j) {
              int temp = arr[i];
              arr[i] = arr[j];
              arr[j] = temp;
          }
      
      	public void sort() {
              int len = arr.length;
              // 初始化大顶堆
              buildMaxHeap(len);
              int lastIndex = len - 1;
              for (int i = lastIndex; i > 0; i--) {
                  swap(0, i);
                  len--;
                  adjustHeap(0, len);
              }
      	}
          
          // len / 2 取整的结果其实是第一个非叶子节点，换言之就是有孩子节点的节点
           private void buildMaxHeap(int len) {
               for (int i = (int) Math.floor(len / 2); i >= 0; i--) {
                   adjustHeap(i, len);
               }
           }
          
          /**
          * 该方法作用是：以下标为 i 的元素为根节点，往下的部分调整为堆结构
          * len 的作用只是防止越界，数组的下标最多为 len - 1
          */
          private void adjustHeap(int i, int len) {
              int left = 2 * i + 1;
              int right = 2 * i + 2;
              
              // 假定该节点是最大的节点
              int largest = i;
              
              // 左孩子节点大，记录新的最大节点下标
              if (left < len && arr[left] > arr[largest]) {
                  largest = left;
              }
              
              // 右孩子节点大，记录新的最大节点下标
              // 这两步就是找到该节点和它的两个子节点中最大的节点
              if (right < len && arr[right] > arr[largest]) {
                  largest = right;
              }
              
              // 不相等，说明子节点中存在比该节点大的节点，那么堆还未调整成功
              // 交换该节点和最大的子节点，那么父子关系交换，从新的子节点（原父节点）继续调整（递归操作），直到父节点大于等于两个子节点，则说明堆调整成功
              if (largest != i) {
                  swap(i, largest);
                  adjustHeap(largest, len);
              }
          }
      }
      ```

      

      

#### Web 自动化测试

* [基于 `Page Object` 设计模式的企业微信 `web`端自动化测试实战](./web自动化测试/selenium_wework_main)

**selenium 笔记**

1. selenium 的实现原理

   1. selenium client (python等语言编写的自动化测试脚本) 初始化一个service服务，通过Webdriver启动浏览器驱动程序chromedriver.exe
   2. 通过RemoteWebDriver向浏览器驱动程序发送HTTP请求，浏览器驱动程序解析请求，打开浏览器，并获得sessionid，如果再次对浏览器操作需携带此id
   3. 打开浏览器，绑定特定的端口，把启动后的浏览器作为webdriver的remote server
   4. 打开浏览器后，所有的selenium的操作(访问地址，查找元素等)均通过RemoteConnection链接到remote server，然后使用execute方法调用_request方法通过urlib3向remote server发送请求
   5. 浏览器通过请求的内容执行对应动作
   6. 浏览器再把执行的动作结果通过浏览器驱动程序返回给测试脚本

2. 显示等待和隐式等待

   * 显示等待的代码定义了等待条件，只有该条件触发，才执行后续代码，可以把 sleep() 看作一种时间人为固定的显示等待

   * 隐式等待是在尝试发现某个元素的时候，如果没能立刻发现，就等待固定长度的时间，也就是在没发现的这段时间还可以进行其它操作。默认设置是0秒。一旦设置了隐式等待时间，它的作用范围就是Webdriver对象实例的整个生命周期


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

#### 设计模式

#### 接口测试框架开发

#### 持续集成

#### 持续交付

#### 测试平台开发
