# coding = utf-8
import os, sys

# �õ����ļ�����һ��·�����൱��cd..��
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# ��־���D�̣�û�����C��
if os.path.exists('d:'):
    LOG_BASE_DIR = 'D:/'
else:
    LOG_BASE_DIR = 'C:/'

# 1.������һ��ģ��ʱ��import xxx��Ĭ�������python������������
#  ��ǰĿ¼���Ѱ�װ������ģ��͵�����ģ�飬����·�������sysģ���path��
# 2.sys.path����һ���б�
# 3.����ʱ�޸ģ��ű����к�ͻ�ʧЧ
sys.path.append(BASE_DIR)

# �����ļ�
CONFIG_DIR = os.path.join(BASE_DIR, "myConfig", "baseConfig.ini")
# �豸��Ϣ
DESIRED_CAPS = os.path.join(BASE_DIR, "myConfig", "desired_caps")
# ��������Ŀ¼
TESTCASE_DIR = os.path.join(BASE_DIR, "Case")
# �����ͼĿ¼
TEST_ERROR_Image = os.path.join(LOG_BASE_DIR, "logs", "image").replace('\\', '/')
# ����ͼƬ��
TEST_BASE_IMAGE = os.path.join(LOG_BASE_DIR, "logs", "base_img").replace('\\', '/')
# ���Ա���Ŀ¼
TEST_REPORT = os.path.join(LOG_BASE_DIR, "logs", "report").replace('\\', '/')
# ��־Ŀ¼
LOG_DIR = os.path.join(LOG_BASE_DIR, "logs", "pylog").replace('\\', '/')
# ���������ļ�
TEST_DATA = os.path.join(BASE_DIR, "myConfig", "keyword.xls")
# Ԫ�ؿؼ�
TEST_ELEMENT_DIR = os.path.join(BASE_DIR, "myConfig", "LocalElement.ini")
# ����
KEY_PAD = os.path.join(BASE_DIR, "myConfig", "keypad.ini")
# ����ִ����Щ��������
CASELIST_DIR = os.path.join(BASE_DIR, "myConfig", "zouchaCaseList.txt")
