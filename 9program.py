a,b=map(int,input().split())
l=list(map(int,input().split()))
tie=0
for i in range(b):
  tie=tie+l[i]
print(tie)
