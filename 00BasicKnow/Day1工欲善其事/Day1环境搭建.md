# Day1:环境搭建

## 0x0 前言

​	病毒分析时一些 病毒样本会损坏机器、窃取信息等风险，使用虚拟机搭建测试环境是必要的。

接下来，我们要搭建的是Windows10和Ubuntu20，使用的虚拟机是Vmware。

​	对于病毒分析来说，工具亦是必不可少的，今天就只部署这两个：Flare-VM，REMNux。

## 1x0 Vmware搭建Windows10和Ubuntu

​	首先，下载Vmware，参考文章：[安装虚拟机（VMware）保姆级教程（附安装包）_vmware虚拟机-CSDN博客](https://blog.csdn.net/weixin_74195551/article/details/127288338)，推荐使用官方包，避免第三方塞东西。

​	然后，下载Windows10镜像文件[VMware 安装 Windows10（各种版本）【保姆级】_vmware win10镜像-CSDN博客](https://blog.csdn.net/qq_44001404/article/details/130885077)，仍然推荐官方包，第三方纯净版也可以考虑。

​	最后，下载Ubuntu镜像文件，我用的是清华大学的镜像站[Index of /ubuntu-releases/ | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/ubuntu-releases/)，挑选一个稳定的版本下载即可。

## 2x0 Windows10部署Flare-VM(武器库)

windows10需求大小：100G

链接如下：[mandiant/flare-vm：适用于 Windows 系统的软件安装脚本集合，允许您轻松地在 VM 上设置和维护逆向工程环境。](https://github.com/mandiant/flare-vm)

跟着官方教程来即可。

提醒一下：在运行install.ps1时，会出现ping google.com 不通的情况，这是因为google服务器未开放接收icmp协议，所以ping不通，而这一步只是为了能够访问外网，从而可以下载需要的工具。

解决方法：在保证能够访问外网的前提下，替换install.ps1中所有google字样，替换为baidu即可进行下一步。

部署花费时间依赖于网络速度，如果是宿主机连接外网，要想办法让虚拟机也能访问外网，在Flare-VM下载内置软件库时，会出现电脑自动重启的现象，故外网连接会断开，我的解决方案：多运行几遍即可安装成功，由于没那么多时间，我花了两天(主要是重启后就要重新跑一下)。

参考命令：`install.psl -password yourpassword -nowait`

Flare-vm工具结构树见 flareVM_tools_tree.txt

## 3x0 REMnux搭建

直接下载REMnux：[获取虚拟设备 |REMnux 文档](https://docs.remnux.org/install-distro/get-virtual-appliance)

打开VMware，导入ova文件即可

开箱即用，十分便利。

REMnux工具结构树见 remnux_tools_report





















