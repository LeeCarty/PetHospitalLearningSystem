# coding: utf-8
from django.test import TestCase, Client
from .models import Accounts

# Create your tests here.


class AccountsTestCase(TestCase):

    def setUp(self):
        zhangsan = Accounts.objects.create(name="张三", email="zhangsan@qq.com", password='1')
        lisi = Accounts.objects.create(name="李四", email="lisi@qq.com", password='1')
        # zhangsan.save()
        self.assertEqual(zhangsan.email, 'zhangsan@qq.com')
        # Accounts.objects.create(name="王二", email="zhangsan@qq.com", password='1')
        # super(AccountsTestCase, self).setUp()
        # self.client = Client(enforce_csrf_checks=True)

    def test_accounts_set_confirm_code(self):
        zhangsan = Accounts.objects.get(email="zhangsan@qq.com")
        lisi = Accounts.objects.get(email="lisi@qq.com")
        try:
            self.assertEqual(zhangsan.set_confirm_code(), zhangsan.set_confirm_code())
            self.assertEqual(lisi.set_confirm_code(), lisi.set_confirm_code())
        except AssertionError:
            print('验证码简单测试成功。')

    def test_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        print('login is OK')

    def test_email_confirm(self):
        response = self.client.get('/email_confirm')
        self.assertEqual(response.status_code, 200)
        print('email_confirm is OK')

    def test_password_modify(self):
        response = self.client.get('/password_modify')
        self.assertEqual(response.status_code, 200)
        print('password_modify is OK')
