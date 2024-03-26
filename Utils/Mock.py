import string
from faker import Faker
import random


class Mock:

    @staticmethod
    def rand_str(strs="测试项目"):
        """随机字符串"""
        ran_str = string.digits + string.ascii_letters

        all_str = ''.join(random.sample(ran_str, 5))

        return strs + all_str

    @staticmethod
    def mock_six_data():
        """字符5位"""
        faker = Faker(locale='zh_CN')

        datas = faker.pystr(max_chars=6)

        return datas

    @staticmethod
    def ran_phone():
        """156开头的手机号"""

        head_num = '156'
        # 生成后8位随机数字 choice取序列随机一个元素返回,
        # ‘_’ 是一个常用习惯用法，在循环中表示一个临时变量，通常用于表示在循环中不需要使用到的值。
        suffix = ''.join(random.choice('0123456789') for _ in range(8))
        # 拼接前缀和后缀
        return head_num + suffix


if __name__ == '__main__':

    mock = Mock()
    data = mock.rand_str()
    print(data)
