from django.apps import AppConfig

class JuntagricoTranslationConfig(AppConfig):
    name = 'juntagrico_translations'
    verbose_name = "Juntagrico Translation"
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        from . import patches  # noqa: F401
        from django.contrib import admin
        from juntagrico import entity
        from juntagrico_translations import translation

        admin.site.unregister(entity.subtypes.SubscriptionProduct)
        admin.site.register(entity.subtypes.SubscriptionProduct, translation.TranslatedSubscriptionProductAdmin)
        admin.site.unregister(entity.subtypes.SubscriptionCategory)
        admin.site.register(entity.subtypes.SubscriptionCategory, translation.TranslatedSubscriptionCategoryAdmin)
        admin.site.unregister(entity.subtypes.SubscriptionBundle)
        admin.site.register(entity.subtypes.SubscriptionBundle, translation.TranslatedSubscriptionBundleAdmin)
        admin.site.unregister(entity.subtypes.SubscriptionType)
        admin.site.register(entity.subtypes.SubscriptionType, translation.TranslatedSubscriptionTypeAdmin)
        admin.site.unregister(entity.depot.Tour)
        admin.site.register(entity.depot.Tour, translation.TranslatedTourAdmin)
        admin.site.unregister(entity.depot.Depot)
        admin.site.register(entity.depot.Depot, translation.TranslatedDepotAdmin)
        admin.site.unregister(entity.jobs.JobType)
        admin.site.register(entity.jobs.JobType, translation.TranslatedJobTypeAdmin)
        admin.site.unregister(entity.jobs.RecuringJob)
        admin.site.register(entity.jobs.RecuringJob, translation.TranslatedJobAdmin)
        admin.site.unregister(entity.jobs.OneTimeJob)
        admin.site.register(entity.jobs.OneTimeJob, translation.TranslatedOneTimeJobAdmin)
        admin.site.unregister(entity.location.Location)
        admin.site.register(entity.location.Location, translation.TranslatedLocationAdmin)
        admin.site.unregister(entity.jobs.ActivityArea)
        admin.site.register(entity.jobs.ActivityArea, translation.TranslatedAreaAdmin)
