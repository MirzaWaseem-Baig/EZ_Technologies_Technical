def TOH(n,src,aux,des):
    if(n==1):
        print(f"I moved from {src} to {des}")
    else:
        TOH(n-1,src,des,aux)
        print(f"I moved from {src} to {des}")
        TOH(n-1,aux,src,des)
n=int(input())
TOH(n,"src","aux","des")