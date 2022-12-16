from django.http import HttpResponse


class grid :
    def __init__(self, x, y) :
        self.x=x
        self.y=y
    def __len__(self) : 
        sum_x=self.x+self.y
        return sum_x ##__str__ 출력하라 이야기
       
    def __str__(self) :
        return ('({},{})'.format(self.x, self.y))
        
p1= grid (2,3)

a="""
<input type=button value={} 
style='color:{}'>
""".format('버튼','red')
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def lee(request):
    return HttpResponse(a + str(p1))


    