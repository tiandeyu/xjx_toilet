## 小鲸洗智能坐便盖Pro


>xjx_toilet是一款ha自定义插件,通过miio协议接入到homeassistant
>目前已经实现获取落座状态，可以使用该状态进行联动，解决拉屎关灯的痛点


### 下载custom component
下载下面网址所有文件到如下目录/config/custom_components/
https://github.com/tiandeyu/xjx_toilet/tree/main/custom_components

```shell
//文件目录结构如下
/config/custom_components/xjx_toilet/__init__.py
/config/custom_components/xjx_toilet/binary_sensor.py
/config/custom_components/xjx_toilet/manifest.json
```

### configuration.yaml配置 
| 名称 | 可选 | 描述 |
| :---- | :---: | ----- |
| name | 否 | ha中显示传感器的名字 |
| host | 否 | 马桶盖IP地址，需要在路由器设为固定IP |
| token | 否 | 米家设备token |
| scan_interval | 是 | 刷新间隔s，默认30 |
 
```yaml
binary_sensor:
  - platform: xjx_toilet
    name: 'Toilet Seat'
    host: 192.168.2.55
    token: 5fef98a2990ba6068d3fa09c6f892eed
    scan_interval: 10


