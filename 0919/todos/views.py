from django.shortcuts import render

todo_list = []

# Create your views here.
# 함수는 input에 대한 어떤 처리 후, output을 내는 게 목적

# views.py에 만드는 모든 함수들의 목적은?
# 사용자의 요청(input)에 따라서 반환해야할 적절한 html(output)을 내는 게 목적
def main(request):
    # main view 함수가 할 일이 생김
    # 사용자가 요청을 보냈는데 그냥 todos/main으로 요청이 온게 아니라
    # todos/main?work=값을 담아서 보냄
    # 요청할 때 데이터도 보냄. 그걸 내 html에 표현해줘야 함
    
    # 사용자의 모든 요청 정보는 request인자에 들어있음
    # get 메서드는 찾는 key가 없으면 None을 반환함
    work = request.GET.get('work')
    
    if work:
        todo_list.append(work)

    # todo_list.append(request.GET.get('work'))

    context = {
        'todo_list': todo_list,
    }
    
    
    return render(request, 'todos/main.html', context)

def create(request):
    return render(request, 'todos/create.html')