# Generated by Django 3.2 on 2022-07-15 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actees',
            fields=[
                ('id', models.CharField(max_length=36)),
                ('species', models.CharField(blank=True, max_length=36, null=True)),
                ('parent', models.CharField(blank=True, max_length=36, null=True)),
                ('purgedat', models.DateTimeField(blank=True, db_column='purgedAt', null=True)),
                ('purgedname', models.TextField(blank=True, db_column='purgedName', null=True)),
                ('details', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'actees',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=15, null=True)),
                ('acteeid', models.CharField(db_column='acteeId', max_length=36)),
                ('displayname', models.CharField(db_column='displayName', max_length=64)),
                ('meta', models.JSONField(blank=True, null=True)),
                ('createdat', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='deletedAt', null=True)),
                ('expiresat', models.DateTimeField(blank=True, db_column='expiresAt', null=True)),
            ],
            options={
                'db_table': 'actors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Audits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.TextField()),
                ('acteeid', models.CharField(blank=True, db_column='acteeId', max_length=36, null=True)),
                ('details', models.JSONField(blank=True, null=True)),
                ('loggedat', models.DateTimeField(blank=True, db_column='loggedAt', null=True)),
                ('claimed', models.DateTimeField(blank=True, null=True)),
                ('processed', models.DateTimeField(blank=True, null=True)),
                ('lastfailure', models.DateTimeField(blank=True, db_column='lastFailure', null=True)),
                ('failures', models.IntegerField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'audits',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Blobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sha', models.CharField(max_length=40, unique=True)),
                ('content', models.BinaryField()),
                ('contenttype', models.TextField(blank=True, db_column='contentType', null=True)),
                ('md5', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'blobs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClientAudits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.TextField(blank=True, null=True)),
                ('node', models.TextField(blank=True, null=True)),
                ('start', models.TextField(blank=True, null=True)),
                ('end', models.TextField(blank=True, null=True)),
                ('latitude', models.TextField(blank=True, null=True)),
                ('longitude', models.TextField(blank=True, null=True)),
                ('accuracy', models.TextField(blank=True, null=True)),
                ('old_value', models.TextField(blank=True, db_column='old-value', null=True)),
                ('new_value', models.TextField(blank=True, db_column='new-value', null=True)),
                ('remainder', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'client_audits',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('createdat', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
            ],
            options={
                'db_table': 'comments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('value', models.JSONField(blank=True, null=True)),
                ('setat', models.DateTimeField(blank=True, db_column='setAt', null=True)),
            ],
            options={
                'db_table': 'config',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormDefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xml', models.TextField()),
                ('hash', models.CharField(max_length=32)),
                ('sha', models.CharField(max_length=40)),
                ('sha256', models.CharField(max_length=64)),
                ('version', models.TextField()),
                ('createdat', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('publishedat', models.DateTimeField(blank=True, db_column='publishedAt', null=True)),
                ('drafttoken', models.CharField(blank=True, db_column='draftToken', max_length=64, null=True)),
                ('enketoid', models.CharField(blank=True, db_column='enketoId', max_length=255, null=True)),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'form_defs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormFieldValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.TextField()),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'form_field_values',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xmlformid', models.CharField(db_column='xmlFormId', max_length=64)),
                ('createdat', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='deletedAt', null=True)),
                ('acteeid', models.CharField(db_column='acteeId', max_length=36)),
                ('state', models.TextField(blank=True, null=True)),
                ('enketoid', models.CharField(blank=True, db_column='enketoId', max_length=255, null=True)),
                ('enketoonceid', models.TextField(blank=True, db_column='enketoOnceId', null=True)),
            ],
            options={
                'db_table': 'forms',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Keys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.TextField(unique=True)),
                ('private', models.JSONField(blank=True, null=True)),
                ('managed', models.BooleanField(blank=True, null=True)),
                ('hint', models.TextField(blank=True, null=True)),
                ('createdat', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
            ],
            options={
                'db_table': 'keys',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KnexMigrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('batch', models.IntegerField(blank=True, null=True)),
                ('migration_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'knex_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KnexMigrationsLock',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('is_locked', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'knex_migrations_lock',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('acteeid', models.CharField(db_column='acteeId', max_length=36, unique=True)),
                ('createdat', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='deletedAt', null=True)),
                ('archived', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'projects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('system', models.CharField(blank=True, max_length=8, null=True)),
                ('createdat', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
                ('verbs', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'roles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sessions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64)),
                ('expiresat', models.DateTimeField(db_column='expiresAt')),
                ('createdat', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('csrf', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'sessions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubmissionDefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xml', models.TextField()),
                ('createdat', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('encdataattachmentname', models.CharField(blank=True, db_column='encDataAttachmentName', max_length=255, null=True)),
                ('localkey', models.TextField(blank=True, db_column='localKey', null=True)),
                ('signature', models.TextField(blank=True, null=True)),
                ('current', models.BooleanField(blank=True, null=True)),
                ('instancename', models.TextField(blank=True, db_column='instanceName', null=True)),
                ('instanceid', models.CharField(db_column='instanceId', max_length=64)),
                ('useragent', models.CharField(blank=True, db_column='userAgent', max_length=255, null=True)),
                ('deviceid', models.CharField(blank=True, db_column='deviceId', max_length=255, null=True)),
                ('root', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'submission_defs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instanceid', models.CharField(db_column='instanceId', max_length=64)),
                ('createdat', models.DateTimeField(blank=True, db_column='createdAt', null=True)),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
                ('deletedat', models.DateTimeField(blank=True, db_column='deletedAt', null=True)),
                ('deviceid', models.CharField(blank=True, db_column='deviceId', max_length=255, null=True)),
                ('draft', models.BooleanField()),
                ('reviewstate', models.TextField(blank=True, db_column='reviewState', null=True)),
            ],
            options={
                'db_table': 'submissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CSMFData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('upload_csmf_dataset', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'CSMF Data',
            },
        ),
        migrations.CreateModel(
            name='ICD10Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('icd10_category_name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'ICD10 Category List',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('organization_name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Organization List',
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Role List',
            },
        ),
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('actorid', models.OneToOneField(db_column='actorId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dashboard.actors')),
                ('acteeid', models.CharField(db_column='acteeId', max_length=36)),
            ],
            options={
                'db_table': 'assignments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FieldKeys',
            fields=[
                ('actorid', models.OneToOneField(db_column='actorId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dashboard.actors')),
            ],
            options={
                'db_table': 'field_keys',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormAttachments',
            fields=[
                ('name', models.TextField()),
                ('type', models.TextField(blank=True, null=True)),
                ('formdefid', models.OneToOneField(db_column='formDefId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dashboard.formdefs')),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
            options={
                'db_table': 'form_attachments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormFields',
            fields=[
                ('formdefid', models.OneToOneField(db_column='formDefId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dashboard.formdefs')),
                ('path', models.TextField()),
                ('name', models.TextField()),
                ('type', models.CharField(max_length=32)),
                ('binary', models.BooleanField(blank=True, null=True)),
                ('order', models.IntegerField()),
                ('selectmultiple', models.BooleanField(blank=True, db_column='selectMultiple', null=True)),
            ],
            options={
                'db_table': 'form_fields',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PublicLinks',
            fields=[
                ('actorid', models.OneToOneField(db_column='actorId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dashboard.actors')),
                ('once', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'public_links',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubmissionAttachments',
            fields=[
                ('name', models.TextField()),
                ('submissiondefid', models.OneToOneField(db_column='submissionDefId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='dashboard.submissiondefs')),
                ('index', models.IntegerField(blank=True, null=True)),
                ('isclientaudit', models.BooleanField(blank=True, db_column='isClientAudit', null=True)),
            ],
            options={
                'db_table': 'submission_attachments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ICD10List',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('icd10_code', models.CharField(max_length=50)),
                ('icd10_name', models.CharField(max_length=200)),
                ('icd10_display_name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('icd10_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.icd10category')),
            ],
            options={
                'verbose_name_plural': 'ICD10 List',
            },
        ),
        migrations.CreateModel(
            name='Authorization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dashboard', models.BooleanField(default=False)),
                ('coded_va_data', models.BooleanField(default=False)),
                ('create_graph', models.BooleanField(default=False)),
                ('create_table', models.BooleanField(default=False)),
                ('create_map', models.BooleanField(default=False)),
                ('concordant_vas', models.BooleanField(default=False)),
                ('discordant_vas', models.BooleanField(default=False)),
                ('coding_work', models.BooleanField(default=False)),
                ('update_profile', models.BooleanField(default=False)),
                ('system_user', models.BooleanField(default=False)),
                ('system_role', models.BooleanField(default=False)),
                ('icd_10_category', models.BooleanField(default=False)),
                ('interviewer_data', models.BooleanField(default=False)),
                ('organization', models.BooleanField(default=False)),
                ('upload_csmf', models.BooleanField(default=False)),
                ('icd_10_list', models.BooleanField(default=False)),
                ('settings', models.BooleanField(default=False)),
                ('download_data', models.BooleanField(default=False)),
                ('user_authorization', models.BooleanField(default=False)),
                ('update_access', models.BooleanField(default=False)),
                ('delete_access', models.BooleanField(default=False)),
                ('view_access', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('authorize_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Authorization List',
            },
        ),
    ]
