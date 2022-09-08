from django.shortcuts import render

# Create your views here.
def student(request):
    '''
    返回一个首页html
    :param request:
    :return:
    '''
    student_name = ["张三","李四","王五"]
    return render(request,"student.html",{"student_list":student_name})