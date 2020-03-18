# s2monitor
用于监控Structs2漏洞的小脚本

--Struts2 VulnMonitor--
Created on 2017-9-8
Update on 2017-11-21
Author: cahi1l1yn
Version:1.2

说明：
1.利用爬虫定时从Apache Struts2官方安全通告发布页面获取最新漏洞情况，一旦发现新漏洞，立即调用阿里云短信接口向管理员发送短信通知。  
2.需安装lib.zip中的两个阿里云短信接口python库。  
3.需安装fake_UserAgent库。  
3.每次手动执行脚本前需将变量i设置为最新的漏洞编号加1，如最新编号为S2-053，则i值为54。  
4.time.sleep()为爬虫监控频率。  
