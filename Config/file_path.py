import os.path


class FilePath:

    base_dir = os.path.dirname(os.path.abspath(__file__))

    captcha_dir = os.path.join(base_dir, r'Captcha\captcha.png')


if __name__ == '__main__':

    cs = FilePath()

    c = cs.captcha_dir
    print(c)
