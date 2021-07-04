# Job-back-end
用flask写的Job-MiniProgram和Job-enterprise的后端API


### 开始项目
- 源码
    ```
    git clone https://github.com/Gang-bb/Job-back-end.git
    ```
- MySQL
  - 安装  
  https://www.cnblogs.com/xiaojianblogs/p/12728846.html
  - 启动
    ```
    net start mysql
    ```
- 本地数据库配置
    ```
    ./config/local_setting.py
    ```
- db相关操作
  - 数据库导入  
    https://www.cnblogs.com/xfgnongmin/p/10658575.html  
    job.sql
    ```
    python manage.py db upgrade
    ```
  - 数据库操作，如增加工作
    ```
    python manage.py db_tools add_job
    ```
- 运行项目
   ```
   python manage.py runserver
   ```

   

