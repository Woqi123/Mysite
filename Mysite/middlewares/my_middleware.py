# @Description:
# 


# @Time : 2021/3/16 15:08 
# @Author : Woqi
# @File : my_middleware.py.py 
# @Software: PyCharm
import time

from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MD1(MiddlewareMixin):
    def process_request(self, request):
        print("process md1 request")
        # return HttpResponse('MD1 process_request')

    def process_response(self, request, response):
        print("MD1 response")
        return response


class MD2(MiddlewareMixin):
    def process_request(self, request):
        print("process md2 request")
        # return HttpResponse('MD2 process_request')

    def process_response(self, request, response):
        print("MD2 response")
        return response


visit_history = {
    # ip :[time1,time2..]
}


class Throttle(MiddlewareMixin):
    pass
    # def process_request(self, request):
    #     print("Throttle节流")
    #     # 获取当前请求访问IP
    #     ip = request.META.get('REMOTE_ADDR')
    #     print(ip)
    #     history = visit_history.get(ip, [])
    #     now = time.time()
    #     count = len(history)
    #     for i, t in enumerate(history[-1:]):
    #         # 限制5秒内访问次数不能超过3次
    #         if now - t <= 5 and count - i > 3:
    #             history.append(now)
    #             visit_history[ip] = history[i:]
    #             return HttpResponse("贵手速太快，需要歇息一会")
    #         elif now - t >= 5:
    #             visit_history[ip] = history[i:]
    #             break
    #     # 刷新当前IP访问记录
    #     history.append(now)
    #     visit_history[ip] = history
    #     print(visit_history)
