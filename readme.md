## 简介
pytest-mongodb插件
## 安装

`pip install pytest-mongodb -i http://*:8082/private_repository/ --trusted-host *`

## 使用
### 测试用例可使用mongodb fixtrue

```python
def test_mongodb(mongodb):
    data = mongodb['rvs'].find('vehicle_position', {"_id": '74361e94a61846e2a690d2e2a9bf591d'})
```
### 运行测试
需编写pytest.ini文件，置于项目内的根目录上，用于指定mongodb配置路径。
默认在项目内的根目录下寻找环境对应配置(./config/config.yml)

####pytest.ini
```ini
[mongodb]
config = config/config.yml
```
或在命令行中通过--config_mongobd参数指定路径
```bash
pytest --config_mongobd config/config.yml
```
####test_config.yml配置如下:
```yaml
mongodb:
  rvs:
    username: *
    password: *
    host: *
    port: *
    database: *
```
## 打包
`python setup.py sdist bdist`  
`twine upload -r my_nexus dist/*`