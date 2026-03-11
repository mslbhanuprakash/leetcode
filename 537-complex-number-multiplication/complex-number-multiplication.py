class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        a,b=num1.replace("i","").split('+')
        c,d=num2.replace("i","").split('+')
        a=int(a)
        b=int(b)
        c=int(c)
        d=int(d)
        real=a*c-b*d
        img=a*d+b*c
        return str(real)+"+"+str(img)+"i"