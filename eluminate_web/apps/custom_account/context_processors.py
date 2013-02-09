# Over-ride pinax_theme_bootstrap_account/context_processors.theme so that we can 
#   provide our own settings for these.

from eluminate_web import settings

def theme(request):
    ctx = {
        #"THEME_ACCOUNT_ADMIN_URL": settings.THEME_ACCOUNT_ADMIN_URL,
        "THEME_ACCOUNT_CONTACT_EMAIL": settings.THEME_ACCOUNT_CONTACT_EMAIL,
    }
    return ctx

