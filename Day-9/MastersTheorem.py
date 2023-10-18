'''Masters Theorem:
    T(n) = a T(a/b) + theta(n^klog(2) to base n)
    a>=1, b>=1, k>=0, P is a real number
    3 cases
    i) if a > b^k then T(n) = theta(n^log(a) base b)
    ii) if a = b^k :
        (a) if P > -1 then T(n) = theta(n^klog(P+1) base n)
        (b) if P = -1 Then T(n) = theta(n^klog(logn))
        (c) if P < -1 Then T(n) = theta(n^k)
    iii) if a < b^k:
        (a) if P >= 0 then T(n) = theta(n^klog(P) base n)
        (b) if P < 0 then T(n) = theta(n^k)'''