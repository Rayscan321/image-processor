# 配置文件
import os


# 项目根目录
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)
                    )
)

# 数据目录
DB_DIR = os.path.join(BASE_DIR, 'db')

if __name__ == '__main__':
    print(BASE_DIR)
    print(DB_DIR)
