from lab3_example.models import Department, User
from lab3_example.api import DBConn

__all__ = ['fill_db']


def fill_db():
    with DBConn.get_session() as session:
        dep1 = Department(name='каф. МО ЭВМ')
        dep2 = Department(name='каф. ВТ')

        session.add(dep1)
        session.add(dep2)
        session.flush()

        user1 = User(name='Сергей Беляев', department_id=dep1.id)
        user2 = User(name='Дмитрий Клионский', department_id=dep2.id)
        user3 = User(name='Марк Заславский', department_id=dep1.id)

        session.add(user1)
        session.add(user2)
        session.add(user3)
        session.commit()
