try:
    n,m,k=input("Enter Number of objects, boxes, Box size: ").split()#count object , #count box , #Size box
    a=[]#declare empty list
    list1=[]#declare empty list
    b=input("Enter {} objects (1 to {}): ".format(n,k)).split()
    if(len(b)>int(n)):
        print("number is more than" , n)
    if(len(b)<int(n)):
        print("number is less than" , n)
    try:
        a = [int(ir) for ir in b]#get n number
        try:
            list2=a#equal a
            list1=[0]*int(m)
            def behineh(a,k,list1,c):
                b=['']*len(a)
                i=0
                for i in range(len(a)):
                    r=-1*(i+1)
                    if -r<=int(n):
                        if(list1[c]+a[r]<=int(k)):
                            list1[c]+=a[r]
                            b[i]=a[r]
                        elif c+1<int(m) and a[r]<=int(k):
                            c=c+1
                            list1[c]=a[r]
                            b[i]=a[r]
                        else:
                            i=i-1
                            break
                    else:
                        print("false")
                return c,i,b,list1
            cc,ii,b,list1=behineh(a,k,list1,c=0)
            while '' in b:
                b.remove('')
            b.reverse()
            list1.reverse()
            print(len(b))
        except:
            print("ErRoR to fill boxes!!")
    except:
        print("input number for objects must be integer!!")
        
except:
    print("ErRoR to get input!!")
    
