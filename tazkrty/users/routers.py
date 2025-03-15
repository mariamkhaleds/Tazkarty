class AuthRouter:

    # route_app_labels = {'auth', 'contenttypes', 'admin', 'sessions', 'users'}
    route_app_labels = {'auth', 'admin', 'users'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'users':
            return 'users_db'
        return 'default'


    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'users':
            return 'users_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):

        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Critical part: direct migrations to the right database
        if app_label == 'users':
            return db == 'users_db'
        return db == 'default'



    def allow_syncdb(self, db, model):
 
        if db == 'users_db' and model._meta.app_label in self.route_app_labels:
            return True
        elif db == 'default' and model._meta.app_label not in self.route_app_labels:
            return True
        return None