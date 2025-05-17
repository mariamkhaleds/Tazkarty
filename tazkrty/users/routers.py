# tazkrty/users/db_routers.py

class UsersRouter:

        route_app_labels = {
            'users',
            'auth',
            'contenttypes',
            'sessions',
            'admin',
            'authtoken',
        }

        def db_for_read(self, model, **hints):
                if model._meta.app_label in self.route_app_labels:
                        return 'users_db' 
                return 'default' 

        def db_for_write(self, model, **hints):
                if model._meta.app_label in self.route_app_labels:
                        return 'users_db' 
                return 'default' 

        def allow_relation(self, obj1, obj2, **hints):
                db1 = obj1._meta.app_label in self.route_app_labels
                db2 = obj2._meta.app_label in self.route_app_labels

                if db1 and db2:
                        return True 
                elif not db1 and not db2:
                        return True 
                else:
                        return False 

        def allow_migrate(self, db, app_label, model_name=None, **hints):

                if app_label in self.route_app_labels:
                        return db == 'users_db' 
                else:
                        return db == 'default' 