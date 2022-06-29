# This class needs to avoid a circular import of models

import psycopg2


class Request:
    @staticmethod
    def __connect_to_db():
        try:
            connection = psycopg2.connect(
                host="127.0.0.1",
                dbname="ilias",
                user="postgres",
                password="Harlan483",
                port=5432,
            )
            if connection:
                return connection
            else:
                raise Exception

        except Exception as ex:
            print(ex)


    def send_request(self, request, is_need_response):
        connection = Request.__connect_to_db()
        try:
            with connection.cursor() as cursor:
                cursor.execute(request)
                connection.commit()

            if (is_need_response):
                return cursor.fetchall()
            else:
                if (len(cursor.fetchall) != 0):
                    return True
                return False

        except Exception as ex:
            print(ex)
        finally:
            connection.close()