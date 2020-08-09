# coding:utf-8

#455.分发饼干
def findContentChildren(children, cookies):
    cookies = sorted(cookies)
    children = sorted(children)
    cookie_num, child_num = 0, 0
    while child_num < len(children) and cookie_num < len(cookies):
        if children[child_num] <= cookies[cookie_num]:
            child_num += 1  # 指向下一个小孩
        # 指向下一块饼干（包含2中种情况，当前饼干不满足小孩胃口，取查看下一个更大的饼干；或者当前饼干满足，则准备分发下一个）
        cookie_num += 1
    return child_num

print('findContentChildren:', findContentChildren([1,2,3], [1,1]))