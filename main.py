# pip install wmi
import wmi
import winreg


def set_proxy(proxy_address, proxy_port):
    try:
        reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        key = winreg.OpenKey(
            reg, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings", 0, winreg.KEY_WRITE)

        winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, f"{
                          proxy_address}:{proxy_port}")

        winreg.CloseKey(key)

        print("Proxy đã được thiết lập thành công.")
    except Exception as e:
        print("Đã xảy ra lỗi:", e)


wmi_obj = wmi.WMI()
wmi_sql = "select IPAddress,DefaultIPGateway from Win32_NetworkAdapterConfiguration where IPEnabled=TRUE"
wmi_out = wmi_obj.query(wmi_sql)


for dev in wmi_out:
    print("IPv4Address:", dev.IPAddress[0],
          "DefaultIPGateway:", dev.DefaultIPGateway[0])

proxy_address = dev.DefaultIPGateway[0]
proxy_port = "10809"

set_proxy(proxy_address,  proxy_port)
