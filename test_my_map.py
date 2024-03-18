# 示例：使用 map 将列表中的每个元素加倍
numbers = [1, 2, 3, 4, 5]
doubled_numbers_iterator = map(lambda x: x * 2, numbers)
a, b, c, d, _ = doubled_numbers_iterator
print(a, b, c, d)
# print(doubled_numbers_iterator)  #说明只是返回了一个地址
# 将迭代器转换为列表
doubled_numbers_list = list(doubled_numbers_iterator)
print(numbers)
print(doubled_numbers_list)
