# Generated by Django 2.0.7 on 2019-05-13 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_goods_num', models.IntegerField(default=1)),
                ('c_is_select', models.BooleanField(default=True)),
                ('c_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ct', to='goods.Goods')),
                ('c_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ca', to='user.AXFUser')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]