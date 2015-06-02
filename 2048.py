# -*- coding: utf-8 -*-
"""
2048基础设计
"""


def merge(line):
    """
    返回左移后的列表
    """
    new_list = list(line)
    length = len(new_list)
    # 移除0
    for each in range(length):
        try:
            new_list.remove(0)
        except ValueError:
            pass

    # 末尾补充0
    for each in range(length-len(new_list)):
        new_list.append(0)

    # 合并
    for each in range(length-1):
        if new_list[each] == new_list[each+1] and new_list[each+1] != 0:
            new_list[each] *= 2
            new_list[each+1] = 0

    # 全部往最左移动
    for each in range(length):
        try:
            new_list.remove(0)
        except ValueError:
            pass

    for each in range(length-len(new_list)):
        new_list.append(0)

    return new_list


def check_over(line):
    length = len(line)
    for i in range(length-1):
        if line[i] == line[i+1] and line[i+1] != 0:
            return False
    return True
