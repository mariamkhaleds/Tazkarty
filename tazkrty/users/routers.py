
class AuthRouter:
    route_app_labels = {'auth', 'admin', 'users', 'sessions','delete'}

    def db_for_read(self, model, **hints):
        print(f"Read: {model._meta.app_label} -> {model._meta.db_table} -> {model._meta.app_config.label}")
        if model._meta.app_label in self.route_app_labels:
            print(f"Read: {model._meta.app_label} -> users_db")
            return 'users_db'
        print(f"Read: {model._meta.app_label} -> default")
        return 'default'

    def db_for_write(self, model, **hints):
        print(f"Write: {model._meta.app_label} -> {model._meta.db_table} -> {model._meta.app_config.label}")
        if model._meta.app_label in self.route_app_labels:
            print(f"Write: {model._meta.app_label} -> users_db")
            return 'users_db'
        print(f"Write: {model._meta.app_label} -> default")
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):

        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        print(f"Migrate: {app_label} -> {db == 'users_db'}")
        if app_label in self.route_app_labels:
            return db == 'users_db'
        return db == 'default'