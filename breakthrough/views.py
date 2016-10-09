# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from breakthrough.models import *
from django.core.exceptions import ObjectDoesNotExist
import random


# 数据库查找用户
def find_user(user_id, user_name):
    try:
        Participant.objects.get(p_id=user_id)
    except ObjectDoesNotExist:
        # p_class = set_class(user_id)
        p_class = 1
        Participant.objects.create(p_id=user_id, p_name=user_name, p_class=p_class, p_key=1, score1=100, p_count=0)
        return True
    if Participant.objects.get(p_id=user_id).p_alive:
        return True
    else:
        return False


# 随机数设置试题类型
def set_class(user_id):
    p = Participant.objects.get(p_id=user_id)
    p.p_class = random.randint(1, 6)
    p.save()
    return p.p_class


# 设置题数
def set_count(user_id, count):
    p = Participant.objects.get(p_id=user_id)
    p.p_count = count
    p.save()


# 设置HP
def set_hp(user_id, hp, key):
    p = Participant.objects.get(p_id=user_id)
    if key == 1:
        p.score1 = hp
        p.save()
    if key == 2:
        p.score2 = hp
        p.save()
    if key == 3:
        p.score3 = hp
        p.save()


# 设置是否存活
def set_alive(user_id):
    p = Participant.objects.get(p_id=user_id)
    p.p_alive = False
    p.save()


# 设置关卡数
def set_key(user_id, key):
    p = Participant.objects.get(p_id=user_id)
    p.p_key = key
    p.save()


# 登陆
def login(requests):
    if requests.method == 'GET':
        return render_to_response('login.html')


# 游戏介绍界面
def start(requests):
    if requests.method == 'POST':
        user_id = requests.POST['id']
        user_name = requests.POST['name']
        requests.session['user_id'] = user_id
        if find_user(user_id, user_name):
            # 判断是否为二次登陆
            if Participant.objects.get(p_id=user_id).p_key > 1 or Participant.objects.get(p_id=user_id).p_count > 0:
                # 如果通关后再次访问
                if Participant.objects.get(p_id=user_id).p_key == 4:
                    info = Participant.objects.get(p_id=user_id)
                    return render_to_response('sorry.html', {'user_id': user_id, 'info': info})
                # 因为意外退出后再次访问
                else:
                    info = Participant.objects.get(p_id=user_id)
                    return render_to_response('restart.html', {'info': info})
            else:
                return render_to_response('start.html', {'user_id': user_id})
        # 挑战失败的挑战者
        else:
            info = Participant.objects.get(p_id=user_id)
            return render_to_response('sorry.html', {'user_id': user_id, 'info': info})
    else:
        return render_to_response('error.html')


# 第一关
def data_bank1(requests):
    # GET方法获取第一关第1题
    if requests.method == 'GET':
        # 如果已经死亡跳转到error页面
        if Participant.objects.get(p_id=requests.session['user_id']).p_alive:
            if requests.GET.get('message') == 'yes':
                hp = Participant.objects.get(p_id=requests.session['user_id']).score1
                p_class = Participant.objects.get(p_id=requests.session['user_id']).p_class
                question = DataBank1.objects.get(q_id=requests.GET.get('q_id'), q_class=p_class)
                return render_to_response('data_bank1.html', {'q_id': requests.GET.get('q_id'), 'question': question, 'HP': hp})
            else:
                p_class = Participant.objects.get(p_id=requests.session['user_id']).p_class
                question = DataBank1.objects.get(q_id=1, q_class=p_class)
                return render_to_response('data_bank1.html', {'q_id': 1, 'question': question, 'HP': 100})
        else:
            return render_to_response('error.html')
    # POST方法获取除了第一题的其他题目
    else:
        # 第一关题数常量
        const_count = 10
        user_id = requests.session.get('user_id')
        q_id = requests.POST['q_id']
        result = requests.POST['result']
        p_class = Participant.objects.get(p_id=user_id).p_class
        answer = DataBank1.objects.get(q_id=q_id, q_class=p_class).answer
        hp = Participant.objects.get(p_id=user_id).score1
        count = Participant.objects.get(p_id=user_id).p_count
        # 如果结果正确,hp加10,最高100
        if answer == result:
            hp += 10
            if hp >= 100:
                hp = 100
                set_hp(user_id, hp, 1)
            else:
                set_hp(user_id, hp, 1)
            count += 1
            set_count(user_id, count)
            # 下一关
            if count == const_count:
                p = Participant.objects.get(p_id=user_id)
                p.sum_score = p.score1 + p.score2 + p.score3
                p.save()
                set_hp(user_id, 100, 2)
                set_count(user_id, 0)
                set_key(user_id, 2)
                return render_to_response('trans1.html')
            # 下一道题目
            else:
                question = DataBank1.objects.get(q_id=count + 1, q_class=p_class)
                hp = Participant.objects.get(p_id=requests.session['user_id']).score1
                return render_to_response('data_bank1.html', {'q_id': count + 1, 'question': question, 'HP': hp})
        # 如果错误,hp减20
        else:
            hp -= 20
            # hp<=0死亡
            if hp <= 0:
                set_hp(user_id, 0, 1)
                set_alive(user_id)
                info = Participant.objects.get(p_id=user_id)
                return render_to_response('sorry.html', {'user_id': user_id, 'info': info})
            # hp>0
            else:
                count += 1
                set_count(user_id, count)
                set_hp(user_id, hp, 1)
                # 下一关
                if count == const_count:
                    p = Participant.objects.get(p_id=user_id)
                    p.sum_score = p.score1 + p.score2 + p.score3
                    p.save()
                    set_hp(user_id, 100, 2)
                    set_count(user_id, 0)
                    set_key(user_id, 2)
                    return render_to_response('trans1.html')
                # 下一道题目
                else:
                    question = DataBank1.objects.get(q_id=count + 1, q_class=p_class)
                    hp = Participant.objects.get(p_id=requests.session['user_id']).score1
                    return render_to_response('data_bank1.html', {'q_id': count + 1, 'question': question, 'HP': hp})


# 第二关
def data_bank2(requests):
    # GET方法获取第二关第1题
    if requests.method == 'GET':
        # 如果已经死亡跳转到error页面
        if Participant.objects.get(p_id=requests.session['user_id']).p_alive:
            if requests.GET.get('message') == 'yes':
                p_class = Participant.objects.get(p_id=requests.session['user_id']).p_class
                question = DataBank2.objects.get(q_id=requests.GET.get('q_id'), q_class=p_class)
                hp = Participant.objects.get(p_id=requests.session['user_id']).score2
                return render_to_response('data_bank2.html', {'q_id': requests.GET.get('q_id'), 'question': question, 'HP': hp})
            else:
                p_class = Participant.objects.get(p_id=requests.session['user_id']).p_class
                question = DataBank2.objects.get(q_id=1, q_class=p_class)
                return render_to_response('data_bank2.html', {'q_id': 1, 'question': question, 'HP': 100})
        else:
            return render_to_response('error.html')
    # POST方法获取除了第二题的其他题目
    else:
        # 第二关题数常量
        const_count = 2
        user_id = requests.session.get('user_id')
        q_id = requests.POST['q_id']
        result = requests.POST['result']
        p_class = Participant.objects.get(p_id=user_id).p_class
        answer = DataBank2.objects.get(q_id=q_id, q_class=p_class).answer
        hp = Participant.objects.get(p_id=user_id).score1
        count = Participant.objects.get(p_id=user_id).p_count
        # 如果结果正确,hp加20,最高100
        if answer == result:
            hp += 20
            if hp >= 100:
                hp = 100
                set_hp(user_id, hp, 1)
            else:
                set_hp(user_id, hp, 1)
            count += 1
            set_count(user_id, count)
            # 下一关
            if count == const_count:
                p = Participant.objects.get(p_id=user_id)
                p.sum_score = p.score1 + p.score2 + p.score3
                p.save()
                set_hp(user_id, 100, 2)
                set_count(user_id, 0)
                set_key(user_id, 3)
                return render_to_response('trans2.html')
            # 下一道题目
            else:
                question = DataBank2.objects.get(q_id=count + 1, q_class=p_class)
                hp = Participant.objects.get(p_id=requests.session['user_id']).score2
                return render_to_response('data_bank2.html', {'q_id': count + 1, 'question': question, 'HP': hp})
        # 如果错误,hp减30
        else:
            hp -= 100
            # hp<=0死亡
            if hp <= 0:
                set_hp(user_id, 0, 2)
                set_alive(user_id)
                info = Participant.objects.get(p_id=user_id)
                return render_to_response('sorry.html', {'user_id': user_id, 'info': info})
            # hp>0
            else:
                count += 1
                set_count(user_id, count)
                set_hp(user_id, hp, 2)
                # 下一关
                if count == const_count:
                    p = Participant.objects.get(p_id=user_id)
                    p.sum_score = p.score1 + p.score2 + p.score3
                    p.save()
                    set_hp(user_id, 100, 3)
                    set_count(user_id, 0)
                    set_key(user_id, 3)
                    return render_to_response('trans2.html')
                # 下一道题目
                else:
                    question = DataBank2.objects.get(q_id=count+1, q_class = p_class)
                    hp = Participant.objects.get(p_id=requests.session['user_id']).score2
                    return render_to_response('data_bank2.html', {'q_id': count + 1, 'question': question, 'HP': hp})


# 第三关
def data_bank3(requests):
    # GET方法获取第三关第1题
    if requests.method == 'GET':
        # 如果已经死亡跳转到error页面
        if Participant.objects.get(p_id=requests.session['user_id']).p_alive:
            if requests.GET.get('message') == 'yes':
                p_class = Participant.objects.get(p_id=requests.session['user_id']).p_class
                question = DataBank3.objects.get(q_id=requests.GET.get('q_id'), q_class=p_class)
                hp = Participant.objects.get(p_id=requests.session['user_id']).score3
                return render_to_response('data_bank3.html', {'q_id': requests.GET.get('q_id'), 'question': question, 'HP': hp})
            else:
                p_class = Participant.objects.get(p_id=requests.session['user_id']).p_class
                question = DataBank3.objects.get(q_id=1, q_class=p_class)
                return render_to_response('data_bank3.html', {'q_id': 1, 'question': question, 'HP': 100})
        else:
            return render_to_response('error.html')
    # POST方法获取除了第一题的其他题目
    else:
        # 第三关题数常量
        const_count = 2
        user_id = requests.session.get('user_id')
        q_id = requests.POST['q_id']
        result = requests.POST['result']
        p_class = Participant.objects.get(p_id=user_id).p_class
        answer = DataBank3.objects.get(q_id=q_id, q_class=p_class).answer
        hp = Participant.objects.get(p_id=user_id).score1
        count = Participant.objects.get(p_id=user_id).p_count

        # 如果结果正确,hp加30,最高100
        if answer == result:
            hp += 30
            if hp >= 100:
                hp = 100
                set_hp(user_id, hp, 3)
            else:
                set_hp(user_id, hp, 3)
            count += 1
            set_count(user_id, count)
            # 下一关
            if count == const_count:
                p = Participant.objects.get(p_id=user_id)
                p.sum_score = p.score1 + p.score2 + p.score3
                p.save()
                set_count(user_id, 0)
                set_key(user_id, 4)
                return render_to_response('success.html')
            # 下一道题目
            else:
                question = DataBank3.objects.get(q_id=count + 1, q_class = p_class)
                hp = Participant.objects.get(p_id=requests.session['user_id']).score3
                return render_to_response('data_bank3.html', {'q_id': count + 1, 'question': question, 'HP': hp})
        # 如果错误,hp减40
        else:
            hp -= 100
            # hp<=0死亡
            if hp <= 0:
                set_hp(user_id, 0, 3)
                set_alive(user_id)
                info = Participant.objects.get(p_id=user_id)
                return render_to_response('sorry.html', {'user_id': user_id, 'info': info})
            # hp>0
            else:
                count += 1
                set_count(user_id, count)
                set_hp(user_id, hp, 3)
                # 下一关
                if count == const_count:
                    p = Participant.objects.get(p_id=user_id)
                    p.sum_score = p.score1 + p.score2 + p.score3
                    p.save()
                    set_count(user_id, 0)
                    set_key(user_id, 4)
                    return render_to_response('success.html')
                # 下一道题目
                else:
                    question = DataBank3.objects.get(q_id=count+1, q_class = p_class)
                    hp = Participant.objects.get(p_id=requests.session['user_id']).score3
                    return render_to_response('data_bank3.html', {'q_id': count+1, 'question': question, 'HP':hp})
