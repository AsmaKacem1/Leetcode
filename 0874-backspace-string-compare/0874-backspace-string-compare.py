class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        cout1,cout2=0,0
        point1,point2=len(s)-1,len(t)-1
        while point1>=0 or point2>=0:
            while point1>=0 and (cout1>0 or s[point1]=="#"):
                if s[point1]=="#":
                    cout1+=1
                else:
                    cout1-=1
                point1-=1
            while point2>=0 and (cout2>0 or t[point2]=="#"):
                if t[point2]=="#":
                    cout2+=1
                else:
                    cout2-=1
                point2-=1
            if (point1 >= 0) != (point2 >= 0):
                return False
            if point1>=0 and point2>=0 and s[point1]!=t[point2]:
                return False
            
            point1-=1
            point2-=1

        return True
            