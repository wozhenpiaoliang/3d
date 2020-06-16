import os
import uuid
import zipfile

from django.http import JsonResponse

from user.models import Pcd


def upload_img(dir_files, token):
    for img in dir_files:
        # 这种思路是仅仅保存了文件到服务器，需要单独保存文件路径到数据库

        uuid4 = str(uuid.uuid4())

        new_uuid4 = ''.join(uuid4.split('-'))

        file = open(os.path.join(f'~/sse-images/', f'{new_uuid4}_{img.name}'), 'wb')

        for chunk in img.chunks():
            # 保存文件路径
            # print(chunk)

            pcd = Pcd()
            pcd.pcd_url = rf'~/sse-images/{new_uuid4}_' + img.name

            pcd.pcd_name = img.name

            pcd.pcd_uuid = new_uuid4
            file.write(chunk)
            pcd.save()

        file.close()

    #
    # with open(os.path.join(f'static/pro/{pro_name}_{pro_time}', 'options.txt'), 'w', encoding='UTF-8') as steam:
    #     steam.write(f'{attr_dict}')


from functools import wraps, partial

# 线程池
# def run_in_thread_pool(func):
#     """将函数放入线程池执行的装饰器"""
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         future=EXECUTOR.submit(func, *args, **kwargs)
#         # for index, callback in enumerate(callbacks):
#         #     try:
#         #         kwargs = callbacks_kwargs[index]
#         #     except IndexError:
#         #         kwargs = None
#         #     fn = partial(callback, **kwargs) if kwargs else callback
#         #     future.add_done_callback(fn)
#         # return func(*args,**kwargs)
#         return future.result()
#     return wrapper


# 文件压缩
# def zip_pro(zip_url, dir1, dir2):
#     file_news = zip_url + '.zip'  # 压缩后文件夹的名字
#     z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)  # 参数一：文件夹名
#
#     for dirpath, dirnames, filenames in os.walk(dir1):
#
#         fpath = dirpath.replace(dir1, '')  # 这一句很重要，不replace的话，就从根目录开始复制
#         fpath = fpath and fpath + os.sep or ''  # 这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
#         for filename in filenames:
#             if filename.endswith('.txt'):
#                 pass
#             else:
#                 z.write(os.path.join(dirpath, filename), fpath + filename)
#
#     for dirpath, dirnames, filenames in os.walk(dir2):
#         fpath = dirpath.replace(dir2, '')  # 这一句很重要，不replace的话，就从根目录开始复制
#         fpath = fpath and fpath + os.sep or ''  # 这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
#         for filename in filenames:
#             z.write(os.path.join(dirpath, filename), fpath + filename)
#     z.close()
