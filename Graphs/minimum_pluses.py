from itertools import zip_longest
def combinations(li):
    li_rev=li[::-1]
    for i in range(1,len(li)):
        temp=[iter(li)]*i
        temp_rev=[iter(li_rev)]*i
        s=["".join(i) for i in zip_longest(*temp,fillvalue="")]
        t=["".join(i[::-1]) for i in zip_longest(*temp_rev,fillvalue="")]
        print(t,s)
combinations("1234")
