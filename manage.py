from app import create_app, db
from flask_script import Manager,Shell,Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Quality

#create app instance
app = create_app('production')
manager = Manager(app)
manager.add_command('server', Server)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Quality=Quality)

if __name__ == '__main__':
    manager.run()
