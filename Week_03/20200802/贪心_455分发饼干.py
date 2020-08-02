# coding:utf-8

#455.分发饼干
def findContentChildren(children, cookies):
    cookies = sorted(cookies)
    children = sorted(children)
    cookie_num, child_num = 0, 0
    while child_num < len(children) and cookie_num < len(cookies):
        if children[child_num] <= cookies[cookie_num]:
            child_num += 1
        cookie_num += 1
    return child_num

print('findContentChildren:', findContentChildren([1,2,3], [1,1]))