from django.shortcuts import render


def course_index(request):
    """课程首页"""
    return render(request, "course/course_index.html")


def course_detail(request, course_id):
    return render(request, "course/course_detail.html")
