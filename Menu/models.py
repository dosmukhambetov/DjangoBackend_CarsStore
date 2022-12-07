from django.db import models


class Seller(models.Model):
    """Seller"""
    seller_name = models.CharField('Name', max_length=100)
    seller_surname = models.CharField('Surname', max_length=100)
    seller_photo = models.ImageField('Photo', upload_to='photo/seller')
    seller_age = models.IntegerField('Age')
    seller_description = models.TextField('Description', blank=True)

    def __str__(self):
        return self.seller_name

    class Meta:
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'
        db_table = 'seller'


class AutoCenter(models.Model):
    """AutoCenter"""
    auto_center_name = models.CharField('Name', max_length=100)
    auto_center_description = models.TextField('Description', blank=True)
    auto_center_location = models.TextField('Location')
    auto_center_license = models.CharField('License', max_length=300)
    auto_center_photo = models.ImageField('Photo', upload_to='photo/autocenter')

    def __str__(self):
        return self.auto_center_name

    class Meta:
        verbose_name = 'Auto Center'
        verbose_name_plural = 'Auto Centers'
        db_table = 'autocenter'


class Category(models.Model):
    """Category"""
    category_car = models.CharField('Category', max_length=100)
    category_description = models.TextField('Description', blank=True)
    category_photo = models.ImageField('Photo', upload_to='photo/category', blank=True)

    def __str__(self):
        return self.category_car

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category'


class Car(models.Model):
    """"Car"""
    car_name = models.CharField('Car Name', max_length=100)
    car_description = models.TextField('Description', blank=True)
    car_photo = models.ImageField('Photo', upload_to='photo/cars')
    car_cost = models.IntegerField('Cars Cost')
    car_data = models.DateTimeField('Cars Year')
    autocenter = models.ForeignKey(AutoCenter, null=True, blank=True,
                                   verbose_name='AutoCenters',
                                   on_delete=models.CASCADE,
                                   related_name='cars'
                                   )
    seller = models.ForeignKey(Seller, null=True, blank=True,
                               verbose_name='Sellers',
                               on_delete=models.CASCADE,
                               related_name='cars'
                               )
    category = models.ForeignKey(Category, null=True, blank=True,
                                 verbose_name='Categories',
                                 on_delete=models.CASCADE,
                                 related_name='cars'
                                 )

    def __str__(self):
        return self.car_name

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
        db_table = 'car'


class CarCategory(models.Model):
    """Car and Category"""
    car_id = models.ForeignKey(Car,
                               verbose_name='Car',
                               on_delete=models.CASCADE,
                               related_name='carcategories'
                               )
    category_id = models.ForeignKey(Category,
                                    verbose_name='Categories',
                                    on_delete=models.CASCADE,
                                    related_name='carcategories'
                                    )

    def __str__(self):
        return f"{self.car_id.car_name} - {self.category_id.category_car}"

    class Meta:
        verbose_name = 'Car and Category'
        verbose_name_plural = 'Cars and Categories'
        db_table = 'carcategory'


class CarSeller(models.Model):
    """Car and Seller"""
    car_id = models.ForeignKey(Car,
                               verbose_name='Cars',
                               on_delete=models.CASCADE,
                               related_name='carssellers'
                               )
    seller_id = models.ForeignKey(Seller,
                                  verbose_name='Sellers',
                                  on_delete=models.CASCADE,
                                  related_name='carssellers'
                                  )

    def __str__(self):
        return f"{self.car_id.car_name} - {self.seller_id.seller_name}"

    class Meta:
        verbose_name = 'Car and Seller'
        verbose_name_plural = 'Cars and Sellers'
        db_table = 'carseller'


class ClientContact(models.Model):
    """Contact form"""
    name = models.CharField('Name', max_length=100)
    email = models.CharField('Email', max_length=255)
    subject = models.CharField('Subject', max_length=255, blank=True)
    message = models.TextField('Text', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Client Contact'
        verbose_name_plural = 'Client Contacts'
        db_table = 'client_contact'
