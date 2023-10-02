# https://www.hackerrank.com/challenges/one-month-preparation-kit-two-arrays/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
def twoArrays(k, A, B):
    
    n = len(A)
    
    A = sorted(A)
    B = sorted(B, reverse=True)
    
    for i in range(n):
        if not((A[i] + B[i]) >= k):
            return "NO"
            
    return "YES"