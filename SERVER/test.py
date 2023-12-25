import requests

BASE = "http://127.0.0.1:5000/"

# data = [
#     {"likes":10, "name":"tim", "views":100},
#     {"likes":9, "name":"linh", "views":1009},
#     {"likes":1, "name":"duong", "views":111}
# ]
# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())
# # response= requests.delete(BASE + "video/0")
# # print(response)
# input()
# response = requests.patch(BASE + "video/0" , {"views" : 99})
# print(response.json())

dataNew = {
    'amount' : 1025.5,
    'id' : 6,
    'payment_method' : "cash",
    'transaction_id' : 4,
    'transaction_id_number' : '4278967967896789'
}

response = requests.post(BASE + 'payments', data=dataNew)
# response = requests.put(BASE + 'payments/6', data=dataNew)
# response = requests.delete(BASE + 'payments/6')
print(response.json())


