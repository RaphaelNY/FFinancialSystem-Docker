将`config_example.json`复制一份，把副本重命名为`config.json`, 并请将你的相关信息填入。
`config_example.json`文件请保留不要删除
# 注意：config.json默认在.gitignore中，防止被上传。

# config文件内容解释
```json
{
  "secret_key": "django secret_key", //django密钥，密码必须是一个较长的随机值，且被妥善保存。
  "db_name": "your_database_name", //你的数据库名称
  "mysql_usr": "user_name", //你的数据库登录用户名
  "mysql_pass": "user_password" //你的数据库登录密码
}
```

你可以使用以下命令创建数据库`accounting`：
```bash
mysql -uroot -p
create database accounting;
exit;
```
如果你使用root用户登录mysql，密码为12345，
则此时`config.json`文件中的内容应该为：
```bash
{
  "secret_key": "django secret_key",
  "db_name": "accounting",
  "mysql_usr": "root",
  "mysql_pass": "12345"
}
```

