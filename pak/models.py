# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdmAccessModule(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    accesscode = models.IntegerField(db_column='AccessCode', blank=True, null=True)  # Field name made lowercase.
    modulecode = models.IntegerField(db_column='ModuleCode', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adm_access_module'


class AdmAccesslevel(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    fulllevel = models.IntegerField(db_column='FullLevel', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adm_accesslevel'


class AdmConfig(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    dbhost = models.CharField(db_column='dbHost', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dbuser = models.CharField(db_column='dbUser', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dbpassword = models.CharField(db_column='dbPassword', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dbdatabase = models.CharField(db_column='dbDatabase', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mailserver = models.CharField(db_column='mailServer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mailfrom = models.CharField(db_column='mailFrom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mailusername = models.CharField(db_column='mailUserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mailpassword = models.CharField(db_column='mailPassword', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mailfromname = models.CharField(db_column='mailFromName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    countshow = models.IntegerField(db_column='CountShow', blank=True, null=True)  # Field name made lowercase.
    fnamesite = models.CharField(db_column='fNameSite', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enamesite = models.CharField(db_column='eNameSite', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adm_config'


class AdmMenu(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    parentcode = models.IntegerField(db_column='ParentCode', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=100, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    modulecode = models.IntegerField(db_column='ModuleCode', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    accesscode = models.IntegerField(db_column='AccessCode', blank=True, null=True)  # Field name made lowercase.
    location = models.IntegerField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    levelno = models.IntegerField(db_column='LevelNo', blank=True, null=True)  # Field name made lowercase.
    orderno = models.IntegerField(db_column='OrderNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adm_menu'


class AdmModule(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=100, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=50, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    help1 = models.TextField(db_column='Help1', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    help2 = models.TextField(db_column='Help2', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adm_module'


class AdmUsers(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    accesscode = models.IntegerField(db_column='AccessCode', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=32, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=50, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    accept = models.IntegerField(db_column='Accept', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adm_users'


class Advertiser(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ordernum = models.IntegerField(db_column='OrderNum', blank=True, null=True)  # Field name made lowercase.
    location = models.IntegerField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    picture = models.TextField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    flashfile = models.CharField(db_column='FlashFile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'advertiser'


class Advertisercategory(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='fName', max_length=200, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    ename = models.CharField(db_column='eName', max_length=200, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'advertisercategory'


class Agent(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='fName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fowner = models.CharField(db_column='fOwner', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fphone = models.CharField(db_column='fPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    faddress = models.CharField(db_column='fAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ename = models.CharField(db_column='eName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    eowner = models.CharField(db_column='eOwner', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ephone = models.CharField(db_column='ePhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eaddress = models.CharField(db_column='eAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'agent'


class Announcement(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    ftitle = models.CharField(db_column='fTitle', max_length=200, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    fsummary = models.TextField(db_column='fSummary', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    fcontent = models.TextField(db_column='fContent', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    etitle = models.CharField(db_column='eTitle', max_length=200, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    esummary = models.TextField(db_column='eSummary', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    econtent = models.TextField(db_column='eContent', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    topnew = models.IntegerField(db_column='TopNew', blank=True, null=True)  # Field name made lowercase.
    picture = models.TextField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'announcement'


class Article(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    categorycode = models.IntegerField(db_column='CategoryCode', blank=True, null=True)  # Field name made lowercase.
    ftitle = models.CharField(db_column='fTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fsummary = models.TextField(db_column='fSummary', blank=True, null=True)  # Field name made lowercase.
    fcontent = models.TextField(db_column='fContent', blank=True, null=True)  # Field name made lowercase.
    etitle = models.CharField(db_column='eTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    esummary = models.TextField(db_column='eSummary', blank=True, null=True)  # Field name made lowercase.
    econtent = models.TextField(db_column='eContent', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    topnew = models.IntegerField(db_column='TopNew', blank=True, null=True)  # Field name made lowercase.
    picture = models.TextField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    ffilename = models.CharField(db_column='fFileName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    efilename = models.CharField(db_column='eFileName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rank = models.FloatField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(db_column='Number', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'article'


class ArticleRank(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    articlecode = models.IntegerField(db_column='articleCode', blank=True, null=True)  # Field name made lowercase.
    sessionid = models.CharField(db_column='SessionId', max_length=32, blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='RegDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'article_rank'


class Articlecategory(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='fName', max_length=200, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    ename = models.CharField(db_column='eName', max_length=200, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'articlecategory'


class Bank(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, db_collation='utf8mb3_persian_ci')  # Field name made lowercase.
    logo = models.TextField(db_column='Logo', blank=True, null=True)  # Field name made lowercase.
    getwaycode = models.IntegerField(db_column='GetwayCode', blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bank'


class Cart(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    usercode = models.IntegerField(db_column='UserCode', blank=True, null=True)  # Field name made lowercase.
    sessionid = models.CharField(db_column='SessionId', max_length=32, blank=True, null=True)  # Field name made lowercase.
    paymentmethodcode = models.IntegerField(db_column='PaymentMethodCode', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    accept = models.IntegerField(db_column='Accept', blank=True, null=True)  # Field name made lowercase.
    paid = models.IntegerField(db_column='Paid', blank=True, null=True)  # Field name made lowercase.
    sent = models.IntegerField(db_column='Sent', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    acceptdate = models.DateTimeField(db_column='AcceptDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cart'


class Certificates(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    ftitle = models.CharField(db_column='fTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    etitle = models.CharField(db_column='eTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    picture = models.TextField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'certificates'


class Chargecart(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    chargecart = models.CharField(db_column='ChargeCart', max_length=100)  # Field name made lowercase.
    serialcart = models.CharField(db_column='SerialCart', max_length=100)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    productcode = models.IntegerField(db_column='ProductCode', blank=True, null=True)  # Field name made lowercase.
    paymentcode = models.IntegerField(db_column='PaymentCode', blank=True, null=True)  # Field name made lowercase.
    active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'chargecart'


class Customer(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=32, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=20)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=250, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='Id', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class Document(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    fcontenttype = models.CharField(db_column='fContentType', max_length=50, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    econtenttype = models.CharField(db_column='eContentType', max_length=50, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    ffilename = models.CharField(db_column='fFileName', max_length=100, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    efilename = models.CharField(db_column='eFileName', max_length=100, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    ftitle = models.CharField(db_column='fTitle', max_length=200, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    flead = models.TextField(db_column='fLead', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    etitle = models.CharField(db_column='eTitle', max_length=200, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    elead = models.TextField(db_column='eLead', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    defaultfile = models.IntegerField(db_column='DefaultFile', blank=True, null=True)  # Field name made lowercase.
    fauthor = models.CharField(db_column='fAuthor', max_length=100, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    eauthor = models.CharField(db_column='eAuthor', max_length=100, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'document'


class Download(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    documentcode = models.IntegerField(db_column='DocumentCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'download'


class Exhibition(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    categorycode = models.IntegerField(db_column='CategoryCode', blank=True, null=True)  # Field name made lowercase.
    ftitle = models.CharField(db_column='fTitle', max_length=300, blank=True, null=True)  # Field name made lowercase.
    etitle = models.CharField(db_column='eTitle', max_length=300, blank=True, null=True)  # Field name made lowercase.
    flocation = models.CharField(db_column='fLocation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    elocation = models.CharField(db_column='eLocation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fdate = models.CharField(db_column='fDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    edate = models.CharField(db_column='eDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fprice = models.CharField(db_column='fPrice', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eprice = models.CharField(db_column='ePrice', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fsample = models.CharField(db_column='fSample', max_length=200, blank=True, null=True)  # Field name made lowercase.
    esample = models.CharField(db_column='eSample', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fexpire = models.CharField(db_column='fExpire', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eexpire = models.CharField(db_column='eExpire', max_length=50, blank=True, null=True)  # Field name made lowercase.
    active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'exhibition'


class Exhibitioncategory(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='fName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ename = models.CharField(db_column='eName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fdescription = models.TextField(db_column='fDescription', blank=True, null=True)  # Field name made lowercase.
    edescription = models.TextField(db_column='eDescription', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exhibitioncategory'


class Faq(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    fquestion = models.TextField(db_column='fQuestion', blank=True, null=True)  # Field name made lowercase.
    equestion = models.TextField(db_column='eQuestion', blank=True, null=True)  # Field name made lowercase.
    fanswer = models.TextField(db_column='fAnswer', blank=True, null=True)  # Field name made lowercase.
    eanswer = models.TextField(db_column='eAnswer', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'faq'


class Filmgallery(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    ftitle = models.CharField(db_column='fTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    etitle = models.CharField(db_column='eTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    atitle = models.CharField(db_column='aTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    picture = models.TextField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    active = models.TextField(db_column='Active')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'filmgallery'


class Getway(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='utf8mb3_persian_ci')  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=50, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    merchantid = models.CharField(db_column='MerchantId', max_length=50, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    terminalid = models.CharField(db_column='TerminalId', max_length=50, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=200)  # Field name made lowercase.
    active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'getway'


class Keyword(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    ftitle = models.TextField(db_column='fTitle', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    fkeywords = models.TextField(db_column='fKeywords', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    fdescription = models.TextField(db_column='fDescription', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    etitle = models.TextField(db_column='eTitle', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    ekeywords = models.TextField(db_column='eKeywords', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    edescription = models.TextField(db_column='eDescription', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'keyword'


class Link(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='fName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ename = models.CharField(db_column='eName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    flink = models.CharField(db_column='fLink', max_length=200, blank=True, null=True)  # Field name made lowercase.
    elink = models.CharField(db_column='eLink', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ordernum = models.IntegerField(db_column='OrderNum', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'link'


class Listdocument(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    documentcode = models.IntegerField(db_column='DocumentCode', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    tablecode = models.IntegerField(db_column='TableCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'listdocument'


class Mentaltext(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    fmentaltext = models.TextField(db_column='fMentaltext', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    ementaltext = models.TextField(db_column='eMentaltext', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mentaltext'


class Menu(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    parentcode = models.IntegerField(db_column='ParentCode', blank=True, null=True)  # Field name made lowercase.
    modulecode = models.IntegerField(db_column='ModuleCode', blank=True, null=True)  # Field name made lowercase.
    fname = models.CharField(db_column='fName', max_length=100, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    ename = models.CharField(db_column='eName', max_length=100, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    location = models.IntegerField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=100, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    pagecode = models.IntegerField(db_column='PageCode', blank=True, null=True)  # Field name made lowercase.
    ordernum = models.IntegerField(db_column='OrderNum', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'menu'


class News(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    ftitle = models.CharField(db_column='fTitle', max_length=200, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    fsummary = models.TextField(db_column='fSummary', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    fcontent = models.TextField(db_column='fContent', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    etitle = models.CharField(db_column='eTitle', max_length=200, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    esummary = models.TextField(db_column='eSummary', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    econtent = models.TextField(db_column='eContent', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    picture = models.TextField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    topnew = models.TextField(db_column='TopNew', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rank = models.FloatField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(db_column='Number', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'news'


class NewsRank(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    newscode = models.IntegerField(db_column='newsCode', blank=True, null=True)  # Field name made lowercase.
    sessionid = models.CharField(db_column='SessionId', max_length=32, blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='RegDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'news_rank'


class Newsletter(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=200)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='RegDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'newsletter'


class Pages(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    ftitle = models.CharField(db_column='fTitle', max_length=200, db_collation='utf8mb3_persian_ci')  # Field name made lowercase.
    fcontent = models.TextField(db_column='fContent', db_collation='utf8mb3_persian_ci')  # Field name made lowercase.
    etitle = models.CharField(db_column='eTitle', max_length=200, db_collation='utf8mb3_persian_ci')  # Field name made lowercase.
    econtent = models.TextField(db_column='eContent', db_collation='utf8mb3_persian_ci')  # Field name made lowercase.
    langcode = models.IntegerField(db_column='LangCode')  # Field name made lowercase.
    pagetype = models.IntegerField(db_column='PageType')  # Field name made lowercase.
    viewer = models.CharField(db_column='Viewer', max_length=100, db_collation='ucs2_persian_ci')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, db_collation='utf8mb3_persian_ci')  # Field name made lowercase.
    formcode = models.IntegerField(db_column='FormCode')  # Field name made lowercase.
    showinpage = models.IntegerField(db_column='ShowInPage')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pages'


class Payment(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    productcode = models.IntegerField(db_column='ProductCode', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.
    paid = models.TextField(db_column='Paid', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    refid = models.CharField(db_column='RefId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bankcode = models.IntegerField(db_column='BankCode', blank=True, null=True)  # Field name made lowercase.
    getwaycode = models.IntegerField(db_column='GetwayCode', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='RegDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'


class Paymentmethod(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    methodname = models.CharField(db_column='MethodName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    processmodule = models.CharField(db_column='ProcessModule', max_length=50)  # Field name made lowercase.
    accountnumber = models.CharField(db_column='AccountNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    branchnumber = models.CharField(db_column='BranchNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    requirefiche = models.TextField(db_column='RequireFiche', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    requirefollownumber = models.TextField(db_column='RequireFollowNumber', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ordernum = models.SmallIntegerField(db_column='OrderNum', blank=True, null=True)  # Field name made lowercase.
    active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    merchantid = models.CharField(db_column='MerchantId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    merchantpassword = models.CharField(db_column='MerchantPassword', max_length=50, blank=True, null=True)  # Field name made lowercase.
    terminalid = models.CharField(db_column='TerminalId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paymentmethod'


class Photogallery(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    parentcode = models.IntegerField(db_column='ParentCode', blank=True, null=True)  # Field name made lowercase.
    fname = models.CharField(db_column='fName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ename = models.CharField(db_column='eName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contenttype = models.IntegerField(db_column='ContentType', blank=True, null=True)  # Field name made lowercase.
    picture = models.TextField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'photogallery'


class Picture(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    productcode = models.IntegerField(db_column='ProductCode')  # Field name made lowercase.
    picture = models.TextField(db_column='Picture')  # Field name made lowercase.
    contenttype = models.CharField(db_column='ContentType', max_length=50, db_collation='utf8mb3_persian_ci')  # Field name made lowercase.
    keyword = models.CharField(db_column='Keyword', max_length=100, db_collation='utf8mb3_persian_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'picture'


class Product(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    categorycode = models.IntegerField(db_column='CategoryCode', blank=True, null=True)  # Field name made lowercase.
    pagecode = models.IntegerField(db_column='PageCode', blank=True, null=True)  # Field name made lowercase.
    brandcode = models.IntegerField(db_column='BrandCode', blank=True, null=True)  # Field name made lowercase.
    fname = models.CharField(db_column='fName', max_length=100, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    ename = models.CharField(db_column='eName', max_length=200, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    fsummary = models.TextField(db_column='fSummary', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    esummary = models.TextField(db_column='eSummary', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    fdescription = models.TextField(db_column='fDescription', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    edescription = models.TextField(db_column='eDescription', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    picture = models.TextField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    ordernum = models.IntegerField(db_column='OrderNum', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    topnew = models.BooleanField(db_column='TopNew', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    newproduct = models.BooleanField(db_column='NewProduct', blank=False, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'product'


class Productcategory(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    parentcode = models.IntegerField(db_column='ParentCode', blank=True, null=True)  # Field name made lowercase.
    fname = models.CharField(db_column='fName', max_length=200, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    ename = models.CharField(db_column='eName', max_length=100, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    fdescription = models.TextField(db_column='fDescription', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    edescription = models.TextField(db_column='eDescription', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    ordernum = models.IntegerField(db_column='OrderNum', blank=True, null=True)  # Field name made lowercase.
    picture = models.TextField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productcategory'


class Projects(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    citycode = models.IntegerField(db_column='CityCode', blank=True, null=True)  # Field name made lowercase.
    fname = models.CharField(db_column='fName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ename = models.CharField(db_column='eName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fsummary = models.TextField(db_column='fSummary', blank=True, null=True)  # Field name made lowercase.
    esummary = models.TextField(db_column='eSummary', blank=True, null=True)  # Field name made lowercase.
    fdescription = models.TextField(db_column='fDescription', blank=True, null=True)  # Field name made lowercase.
    edescription = models.TextField(db_column='eDescription', blank=True, null=True)  # Field name made lowercase.
    picture = models.TextField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'projects'


class Province(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='fName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ename = models.CharField(db_column='eName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'province'


class Provinceagent(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    provincecode = models.IntegerField(db_column='ProvinceCode', blank=True, null=True)  # Field name made lowercase.
    agentcode = models.IntegerField(db_column='AgentCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'provinceagent'


class Servicecategory(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    parentcode = models.IntegerField(db_column='ParentCode', blank=True, null=True)  # Field name made lowercase.
    fname = models.CharField(db_column='fName', max_length=200, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    ename = models.CharField(db_column='eName', max_length=200, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    fdescription = models.TextField(db_column='fDescription', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    edescription = models.TextField(db_column='eDescription', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    ordernum = models.IntegerField(db_column='OrderNum', blank=True, null=True)  # Field name made lowercase.
    levelno = models.IntegerField(db_column='LevelNo', blank=True, null=True)  # Field name made lowercase.
    picture = models.TextField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servicecategory'


class Services(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    categorycode = models.IntegerField(db_column='CategoryCode', blank=True, null=True)  # Field name made lowercase.
    fname = models.CharField(db_column='fName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ename = models.CharField(db_column='eName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fsummary = models.TextField(db_column='fSummary', blank=True, null=True)  # Field name made lowercase.
    esummary = models.TextField(db_column='eSummary', blank=True, null=True)  # Field name made lowercase.
    fdescription = models.TextField(db_column='fDescription', blank=True, null=True)  # Field name made lowercase.
    edescription = models.TextField(db_column='eDescription', blank=True, null=True)  # Field name made lowercase.
    picture = models.TextField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.
    ordernum = models.IntegerField(db_column='OrderNum', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    topnew = models.IntegerField(db_column='TopNew', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'services'


class Transfermethod(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    methodname = models.CharField(db_column='MethodName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    requirepostnumber = models.TextField(db_column='RequirePostNumber', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    requirevehiclenumber = models.TextField(db_column='RequireVehicleNumber', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    ordernum = models.IntegerField(db_column='OrderNum', blank=True, null=True)  # Field name made lowercase.
    active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'transfermethod'


class View(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    langcode = models.IntegerField(db_column='LangCode', blank=True, null=True)  # Field name made lowercase.
    tablecode = models.IntegerField(db_column='TableCode', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=300, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=200, db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='utf8mb3_persian_ci', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='RegDate')  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'view'


class Vote(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    fquestion = models.CharField(db_column='fQuestion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    equestion = models.CharField(db_column='eQuestion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fanswer1 = models.CharField(db_column='fAnswer1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fanswer2 = models.CharField(db_column='fAnswer2', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fanswer3 = models.CharField(db_column='fAnswer3', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fanswer4 = models.CharField(db_column='fAnswer4', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fanswer5 = models.CharField(db_column='fAnswer5', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fanswer6 = models.CharField(db_column='fAnswer6', max_length=250, blank=True, null=True)  # Field name made lowercase.
    eanswer1 = models.CharField(db_column='eAnswer1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    eanswer2 = models.CharField(db_column='eAnswer2', max_length=250, blank=True, null=True)  # Field name made lowercase.
    eanswer3 = models.CharField(db_column='eAnswer3', max_length=250, blank=True, null=True)  # Field name made lowercase.
    eanswer4 = models.CharField(db_column='eAnswer4', max_length=250, blank=True, null=True)  # Field name made lowercase.
    eanswer5 = models.CharField(db_column='eAnswer5', max_length=250, blank=True, null=True)  # Field name made lowercase.
    eanswer6 = models.CharField(db_column='eAnswer6', max_length=250, blank=True, null=True)  # Field name made lowercase.
    number1 = models.IntegerField(db_column='Number1', blank=True, null=True)  # Field name made lowercase.
    number2 = models.IntegerField(db_column='Number2', blank=True, null=True)  # Field name made lowercase.
    number3 = models.IntegerField(db_column='Number3', blank=True, null=True)  # Field name made lowercase.
    number4 = models.IntegerField(db_column='Number4', blank=True, null=True)  # Field name made lowercase.
    number5 = models.IntegerField(db_column='Number5', blank=True, null=True)  # Field name made lowercase.
    number6 = models.IntegerField(db_column='Number6', blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'vote'


class Voterank(models.Model):
    code = models.AutoField(db_column='Code', primary_key=True)  # Field name made lowercase.
    votecode = models.IntegerField(db_column='VoteCode', blank=True, null=True)  # Field name made lowercase.
    sessionid = models.CharField(db_column='SessionId', max_length=32, blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'voterank'
