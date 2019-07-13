from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from db.models import User, Blog, Topic


# TODO
# Создать пользователя first_name = u1, last_name = u1.
# Создать пользователя first_name = u2, last_name = u2.
# Создать пользователя first_name = u3, last_name = u3.
# Создать блог title = blog1, author = u1.
# Создать блог title = blog2, author = u1.
# Подписать пользователей u1 u2 на blog1, u2 на blog2.
# Создать топик title = topic1, blog = blog1, author = u1.
# Создать топик title = topic2_content, blog = blog1, author = u3, created = 2017 - 01 - 01.
# Лайкнуть topic1 пользователями u1, u2, u3.


def create():
    u1 = User(first_name="u1", last_name='u1')
    u1.save()
    u2 = User(first_name="u2", last_name='u2')
    u2.save()
    u3 = User(first_name="u3", last_name='u3')
    u3.save()

    blog1 = Blog(title="blog1")
    blog1.author = u1
    blog1.save()
    blog2 = Blog(title="blog2")
    blog2.author = u1
    blog2.save()

    blog1.subscribers.add(u1, u2)
    blog1.save()
    blog2.subscribers.add(u2)
    blog2.save()

    topic1 = Topic(title="topic1")
    topic1.blog = blog1
    topic1.author = u1
    topic1.save()

    topic2_content = Topic(title="topic2_content", created="2017-01-01")
    topic2_content.blog = blog1
    topic2_content.author = u3
    topic2_content.save()

    topic1.likes.add(u1, u2, u3)
    topic1.save()


def edit_all():
    for i in User.objects.all():
        i.first_name = 'uu1'
        i.save()


# TODO
# Поменять first_name на uu1 у пользователей, у которых first_name u1 или u2 (функция edit_u1_u2).
def edit_u1_u2():
    for i in User.objects.filter(Q(first_name='u1') | Q(first_name='u2')):
        i.first_name = 'uu1'
        i.save()


#TODO
# удалить пользователя с first_name u1 (функция delete_u1).
# отписать пользователя с first_name u2 от блогов (функция unsubscribe_u2_from_blogs).

def delete_u1():
    User.objects.filter(first_name='u1').delete()


def unsubscribe_u2_from_blogs():
    u2 = User.objects.filter(first_name='u2')
    b2 = Blog.objects.filter(subscribers__first_name='u2')
    for u in u2:
        for b in b2:
            b.subscribers.remove(u)

#TODO
# 4. Найти топики у которых дата создания больше 2018-01-01 (функция get_topic_created_grated).
# 5. Найти топик у которого title заканчивается на content (функция get_topic_title_ended).
# 6. Получить 2х первых пользователей (сортировка в обратном порядке по id) (функция get_user_with_limit).
# 7. Получить количество топиков в каждом блоге, назвать поле topic_count, отсортировать по topic_count по возрастанию (функция get_topic_count).
# 8. Получить среднее количество топиков в блоге (функция get_avg_topic_count).
# 9. Найти блоги, в которых топиков больше одного (функция get_blog_that_have_more_than_one_topic).
# 10. Получить все топики автора с first_name u1 (функция get_topic_by_u1).
# 11. Найти пользователей, у которых нет блогов, отсортировать по возрастанию id (функция get_user_that_dont_have_blog).
# 12. Найти топик, который лайкнули все пользователи (функция get_topic_that_like_all_users).
# 13. Найти топики, у которы нет лайков (функция get_topic_that_dont_have_like)


def get_topic_created_grated():
    return Topic.objects.filter(created__gte='2018-01-01')


def get_topic_title_ended():
    return Topic.objects.filter(title__endswith='content')


def get_user_with_limit():
    return User.objects.all().order_by('-pk')[:2]


def get_topic_count():
    pass


def get_avg_topic_count():
    pass


def get_blog_that_have_more_than_one_topic():
    pass


def get_topic_by_u1():
    pass


def get_user_that_dont_have_blog():
    pass


def get_topic_that_like_all_users():
    pass


def get_topic_that_dont_have_like():
    pass
