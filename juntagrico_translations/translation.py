from juntagrico.admins.area_admin import AreaAdmin
from juntagrico.admins.delivery_admin import DeliveryAdmin
from juntagrico.admins.inlines.delivery_inline import DeliveryInline
from juntagrico.admins.job_admin import JobAdmin
from juntagrico.admins.job_type_admin import JobTypeAdmin
from juntagrico.admins.location_admin import LocationAdmin
from juntagrico.admins.one_time_job_admin import OneTimeJobAdmin
from juntagrico.entity.delivery import DeliveryItem
from juntagrico.entity.jobs import RecuringJob, JobType, OneTimeJob, ActivityArea
from juntagrico.entity.location import Location
from modeltranslation.translator import register, TranslationOptions
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline, TranslationTabularInline

from juntagrico.admins import subscription_product_admin
from juntagrico.admins.tour_admin import TourAdmin
from juntagrico.admins.subscription_type_admin import SubscriptionBundleAdmin, SubscriptionTypeInline, \
    ProductSizeInline, SubscriptionCategoryAdmin, SubscriptionBundleInline, SubscriptionTypeAdmin
from juntagrico.entity.depot import Tour, Depot
from juntagrico.entity.subtypes import SubscriptionProduct, SubscriptionType, SubscriptionBundle, ProductSize, \
    SubscriptionCategory


@register(SubscriptionProduct)
class SubscriptionProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(ProductSize)
class ProductSizeTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(SubscriptionCategory)
class SubscriptionCategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(SubscriptionBundle)
class SubscriptionBundleTranslationOptions(TranslationOptions):
    fields = ('long_name', 'description',)


@register(SubscriptionType)
class SubscriptionTypeTranslationOptions(TranslationOptions):
    fields = ('long_name', 'description',)


@register(Tour)
class TourTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(Depot)
class DepotTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'access_information')


@register(JobType)
class JobTypeTranslationOptions(TranslationOptions):
    fields = ('displayed_name', 'description')


@register(RecuringJob)
class RecuringJobTranslationOptions(TranslationOptions):
    fields = ('additional_description',)


@register(OneTimeJob)
class OneTimeJobTranslationOptions(TranslationOptions):
    fields = ('displayed_name', 'description')


@register(DeliveryItem)
class DeliveryItemTranslationOptions(TranslationOptions):
    fields = ('name', 'amount', 'comment')


@register(Location)
class LocationTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(ActivityArea)
class ActivityAreaTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


class TranslatedProductSizeInline(subscription_product_admin.ProductSizeInline, TranslationTabularInline):
    pass


class TranslatedSubscriptionBundleInline(SubscriptionBundleInline, TranslationTabularInline):
    pass


class TranslatedSubscriptionCategoryAdmin(SubscriptionCategoryAdmin, TranslationAdmin):
    inlines = [TranslatedSubscriptionBundleInline]


class TranslatedSubscriptionProductAdmin(subscription_product_admin.SubscriptionProductAdmin, TranslationAdmin):
    inlines = [TranslatedProductSizeInline]


class TranslatedSubscriptionTypeInline(SubscriptionTypeInline, TranslationStackedInline):
    pass


class TranslatedSubscriptionBundleAdmin(SubscriptionBundleAdmin, TranslationAdmin):
    inlines = [ProductSizeInline, TranslatedSubscriptionTypeInline]


class TranslatedSubscriptionTypeAdmin(SubscriptionTypeAdmin, TranslationAdmin):
    pass


class TranslatedTourAdmin(TourAdmin, TranslationAdmin):
    pass


class TranslatedJobTypeAdmin(JobTypeAdmin, TranslationAdmin):
    pass


class TranslatedJobAdmin(JobAdmin, TranslationAdmin):
    pass


class TranslatedOneTimeJobAdmin(OneTimeJobAdmin, TranslationAdmin):
    pass


class TranslatedDeliveryInline(DeliveryInline, TranslationTabularInline):
    pass


DeliveryAdmin.inlines = [TranslatedDeliveryInline]


class TranslatedLocationAdmin(LocationAdmin, TranslationAdmin):
    pass


class TranslatedAreaAdmin(AreaAdmin, TranslationAdmin):
    pass
