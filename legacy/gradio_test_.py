import requests
import concurrent.futures
import time

# Gradio界面的URL
GRADIO_URL = "http://localhost:5000/api/predict/"

# 模拟的用户请求数据
data = {
    "data": ["这是一个测试文本。"]
}

# 发送请求的函数
def send_request(data):
    response = requests.post(GRADIO_URL, json=data)
    return response.json()

# 发送多个并发请求的函数
def run_load_test(requests_count, concurrent_requests):
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
        futures = [executor.submit(send_request, data) for _ in range(requests_count)]
        results = [f.result() for f in concurrent.futures.as_completed(futures)]
        return results

# 测试设置
number_of_requests = 100  # 总请求次数
number_of_concurrent_requests = 10  # 并发请求数

# 开始测试
start_time = time.time()
results = run_load_test(number_of_requests, number_of_concurrent_requests)
end_time = time.time()

# 输出测试结果
print(f"发送了 {number_of_requests} 个请求，耗时 {end_time - start_time:.2f} 秒。")
print("部分响应输出：", results[:3])  # 打印部分响应作为示例
