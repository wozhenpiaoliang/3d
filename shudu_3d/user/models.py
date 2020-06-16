from django.db import models


# Create your models here.
class TimeBase(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(TimeBase):
    user_id = models.AutoField(db_column='user_id', primary_key=True)

    user_name = models.CharField(unique=True, db_column='user_name', max_length=16)

    user_pwd = models.CharField(db_column='user_paw', max_length=100)
    user_tel = models.CharField(unique=True, db_column='user_tel', max_length=40)
    user_idcard = models.CharField(unique=True, db_column='user_idcard', max_length=80)

    class Meta:
        db_table = 'user'


class Pcd(TimeBase):
    pcb_id = models.AutoField(primary_key=True)
    # 上传的路径是相对于当前的媒体中心，是配置MEDIA_ROOT=os.path.join(BASE_DIR,r'static/upload')
    pcd_url = models.CharField(max_length=128)
    pcd_name = models.CharField(max_length=128,default='xx.pcd')

    pcd_uuid = models.CharField(max_length=128,unique=True)

    # # 默认0未标注
    # state_id = models.IntegerField(default=0)
    # # state_id = models.BooleanField(default=False)
    # read_state = models.IntegerField(default=0)
    # time_img = models.IntegerField(default=0)
    #
    # pro = models.ManyToManyField(to='Project', through='ProjectImg')

    class Meta:
        db_table = 'pcd'
