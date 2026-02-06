# INSTALLED_APPS debe incluir:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Tus apps - ELIGE UNA OPCIÓN:
    
    # OPCIÓN 1: Si las apps están en carpeta apps/
    'users',
    'courses',
    'progress',
    'teacher',
    
    # OPCIÓN 2: Si prefieres prefijo apps.
    # 'apps.users',
                            'a          ss',
    # 'teacher',
]

# Y AUTH_USER_MODEL según corresponda:
# Para Opción 1:
AUTH_USER_MODEL = 'users.User'
# Para Opción 2:
# AUTH_USER_MODEL = 'apps_users.User'
