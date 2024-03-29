# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Dairy(models.Model):
    eid = models.ForeignKey('Entry', models.DO_NOTHING, db_column='EID')  # Field name made lowercase.
    date = models.DateField(primary_key=True)
    email = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='email')

    class Meta:
        managed = False
        db_table = 'dairy'
        unique_together = (('date', 'email', 'eid'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Dream(models.Model):
    eid = models.OneToOneField('InnerK', models.DO_NOTHING, db_column='EID', primary_key=True)  # Field name made lowercase.
    lucidity = models.IntegerField(db_column='Lucidity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dream'


class Emotion(models.Model):
    type = models.CharField(max_length=64)
    subtype = models.CharField(primary_key=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'emotion'


class Entry(models.Model):
    eid = models.AutoField(db_column='EID', primary_key=True)  # Field name made lowercase.
    hour = models.IntegerField(db_column='Hour')  # Field name made lowercase.
    minute = models.IntegerField(db_column='Minute')  # Field name made lowercase.
    text = models.TextField(db_column='Text')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'entry'


class EntryAbout(models.Model):
    eid = models.OneToOneField(Entry, models.DO_NOTHING, db_column='EID', primary_key=True)  # Field name made lowercase.
    pid = models.ForeignKey('Person', models.DO_NOTHING, db_column='PID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'entry_about'
        unique_together = (('eid', 'pid'),)


class EntryEmotion(models.Model):
    eid = models.ForeignKey(Entry, models.DO_NOTHING, db_column='EID')  # Field name made lowercase.
    subtype = models.OneToOneField(Emotion, models.DO_NOTHING, db_column='SubType', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'entry_emotion'
        unique_together = (('subtype', 'eid'),)


class EntryUrl(models.Model):
    eid = models.ForeignKey(Entry, models.DO_NOTHING, db_column='EID')  # Field name made lowercase.
    url = models.CharField(db_column='Url', primary_key=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'entry_url'
        unique_together = (('url', 'eid'),)


class Fitness(models.Model):
    eid = models.OneToOneField(Entry, models.DO_NOTHING, db_column='EID', primary_key=True)  # Field name made lowercase.
    exercise_name = models.CharField(db_column='Exercise_Name', max_length=64)  # Field name made lowercase.
    duration = models.FloatField(db_column='Duration')  # Field name made lowercase.
    calories_burned = models.FloatField(db_column='Calories_Burned', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fitness'
        unique_together = (('eid', 'exercise_name'),)


class InnerK(models.Model):
    eid = models.OneToOneField(Entry, models.DO_NOTHING, db_column='EID', primary_key=True)  # Field name made lowercase.
    timeline = models.CharField(db_column='TimeLine', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inner_k'


class Mantra(models.Model):
    eid = models.OneToOneField('OuterK', models.DO_NOTHING, db_column='EID', primary_key=True)  # Field name made lowercase.
    translation = models.TextField(db_column='Translation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mantra'


class Meditation(models.Model):
    eid = models.OneToOneField(InnerK, models.DO_NOTHING, db_column='EID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=64, blank=True, null=True)  # Field name made lowercase.
    duration = models.FloatField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'meditation'


class OuterK(models.Model):
    eid = models.OneToOneField(Entry, models.DO_NOTHING, db_column='EID', primary_key=True)  # Field name made lowercase.
    book_title = models.CharField(db_column='Book_Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_quote = models.IntegerField(db_column='Is_quote')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'outer_k'


class Person(models.Model):
    pid = models.AutoField(db_column='PID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    group_name = models.CharField(max_length=64)
    email = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='email')

    class Meta:
        managed = False
        db_table = 'person'


class Poem(models.Model):
    eid = models.OneToOneField(OuterK, models.DO_NOTHING, db_column='EID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'poem'


class Travel(models.Model):
    country = models.CharField(db_column='Country', max_length=64)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=64, blank=True, null=True)  # Field name made lowercase.
    plan = models.TextField(db_column='Plan', blank=True, null=True)  # Field name made lowercase.
    email = models.OneToOneField(AuthUser, models.DO_NOTHING, db_column='email', primary_key=True)

    class Meta:
        managed = False
        db_table = 'travel'


class User(models.Model):
    email = models.CharField(primary_key=True, max_length=64)
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'user'
