from odps import ODPS
from odps.df import DataFrame


def odsp_t():
    o = ODPS('LTAI4FhwhQLvnJxKSgEZ5QmT', 'aCxrQ6r89wfjmGxAbzSGl9yjdzWoOT',
             project='product_D', endpoint='https://service.odps.aliyun.com/api')
    cron = DataFrame(o.get_table('cron_n'))
    data = cron.head()
    # print((data.locate))
    return data
odsp_t()
