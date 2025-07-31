from sqlalchemy import create_engine

engine = create_engine("ibm_db_sa://yds36824:9EWETqWQQQozva8Y@1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud:32286/bludb?sslcertificate=/etc/ssl/cert.pem&authenticationDatabase=admin&replicaSet=replset")

with engine.connect() as connection:
    result = connection.execute("SELECT * DATE FROM YSD36824.Employee")
    for row in result:
        print(row)

