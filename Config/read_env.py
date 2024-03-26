
import configparser
import os.path

# dirname获取上一级目录。 abspath绝对路径，file当前文件
base_dir = os.path.dirname(os.path.abspath(__file__))

# 获取ini文件路径
env_path = os.path.join(base_dir, 'env.ini')

config_path = configparser.ConfigParser()

# 实例对象，读取env文件
config_path.read(env_path, encoding='utf-8')
pick = config_path.get("pick", 'env')  # 获取配置项[pick] env键，就是test  传给pick变量

url = config_path.get(pick, 'url')  # 再[test]里，获取对应的信息，如环境，账号，密码
account = config_path.get(pick, 'account')
password = config_path.get(pick, 'password')


class EnvironMent:
    """env, account全局变量，类里可直使用"""

    @staticmethod
    def account():

        return account

    @staticmethod
    def password():

        return password

    @staticmethod
    def url():

        return url


if __name__ == '__main__':

    csd = EnvironMent()
    print(csd.url())
